---
title: "Bloombergfull"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/pdfiles/Bloombergfull.pdf
---

1

# **Using the Bloomberg terminal for data**

# Contents of Package

| 1.Getting information on your company         | Pages 2-31  |
|-----------------------------------------------|-------------|
| 2.Getting information on comparable companies | Pages 32-39 |
| 3.Getting macro economic information          | Pages 40    |

### **Instructions for Getting Bloomberg Data**

- ## • Pick Equity
- ## Under Finding Securities, choose Ticker Symbol Look up (TK)
- Enter the name of your company. You will get all of the equity listings that the company has. Choose the one that you are interested in. For instance, if you look up Nestle, you will get Nestle's local listings in Switzerland (Registered and Bearer Stock) as well as all of Nestle's ADR listings around the world. You might have to work through the listings by trial and error until you get the listing that has all of the financial information that you want. (One quick test that seems to work is to try the DES page below. The right listing will have 10-11 pages. All the other listings will have only 2-4 pages)
- • Once you are in equity screen for your company,
- • Go back to the main menu (out of equity). Pick **Corp Bond**.
- ## • Enter the name of your company
- You will get a list of corporate bonds issued by your company, if any.
- **— Chose a long-term bond (preferably without special features) from the list.**
- Choose Description

### **Using Bloomberg to get information on your company**

![](_page_2_Diagram_2.jpeg)

![](_page_2_Diagram_6.jpeg)

HDS (Just Pg 1)

Shadow: Indicates menu choices on Bloomberg

Regular font: Indicates input that you have to provide or change

To get all other information To get ratings information

### **WHERE TO FIND THE DATA**

This is a listing of all of the financial data that you will need to analyze your company and where exactly on the Bloomberg output you will find the data. Once you have identified what you would like to look up, use the item number and go to the specified page number on Bloomberg to look it up.

| Item | Input        |                                 | In Bloomberg     |             | Page Number | Used in this spreadsheet    |
|------|--------------|---------------------------------|------------------|-------------|-------------|-----------------------------|
| 1    | Beta         |                                 | Equity: Beta     | Calculation | 29          | Capstr, Dividend, Valuation |
| 2    | Current EPS  |                                 | Equity:          | Description | 8           | Valuation                   |
| 3    | Payout Ratio |                                 | Equity:          | Description | 10          | Valuation                   |
| 4    | Total Debt   |                                 | Equity:          | Description | 16          | Capstr, Dividend, Valuation |
| 5    | Book Value   | of Equity                       | Equity:          | Description | 16          | CapStr, Valuation           |
| 6    | Number of    | Shares Outstanding              | Equity:          | Description | 8           | CapStr, Valuation           |
| 7    | Effective    | Tax Rate                        | Equity:          | Description | 10          | CapStr, Valuation           |
| 8    |              | Chg in Non-Cash Working Capital | Equity:          | Description | 17          | Valuation                   |
| 9    | Capital      | Expenditures                    | Equity:          | Description | 17          | CapStr, Valuation           |
| 10   | Depreciation |                                 | Equity:          | Description | 17          | CapStr, Valuation           |
| 11   | EPS 5 years  | ago                             | Equity: FA       | (Income)    | 12          | Valuation                   |
| 12   | Analyst      | Projection for Growth           | Equity: Earnings | Estimates   | 27          | Valuation                   |

| 13 | Interest         | Expenses        |                       | Equity:      | Description           | 15 | CapStr, Valuation       |
|----|------------------|-----------------|-----------------------|--------------|-----------------------|----|-------------------------|
| 14 | Net              | Sales/ Revenues |                       | Equity:      | Description           | 15 | Valuation               |
| 15 | Market           | Capitalization  |                       | Equity:      | Description           | 8  | Risk, CapStr, Valuation |
| 16 | EBIT             | (/Operating     | Income)               | Equity:      | Description           | 15 | CapStr                  |
| 17 | Bond Rating      |                 |                       | Corp Bond:   | Description           | 31 | CapStr                  |
| 18 | Past             | 10 years        | Net Income            | Equity:      | FA (Income)           | 25 | Dividends               |
| 19 | Past             | 10 years        | Depreciation          | Equity:      | FA (Cashflow)         | 25 | Dividends               |
| 20 | Past             | 10 years        | Chg in non-cash Work. | Cap. Equity: | FA (Cashflow)         | 26 | Dividends               |
| 21 | Past             | 10 years        | Dividends             | Equity:      | FA (Cashflow)         | 26 | Dividends               |
| 22 | Past             | 10 years        | Equity Buybacks       | Equity FA    | (Cashflow)            | 25 | Dividends               |
| 23 | Past             | 10 years        | Cap Ex                | Equity:      | FA (Cashflow)         | 26 | Dividends               |
| 24 | Average          | Debt            | Ratio 10 years        | Equity FA    | (Leverage)            | 21 | Dividends               |
| 25 | Past             | 10 years        | BV of Equity          | Equity FA    | (Liabilities)         | 24 | Dividends               |
| 26 | Total            | Return on       | Stock                 | Equity:      | FA (Price Ratio)      | 18 | Dividends               |
| 27 | Operating Income |                 | past 10 years         | Equity:      | FA (Income)           | 22 | DebtDesign              |
| 28 | Stock Price      | Volatility      |                       | Equity:      | HVT                   | 28 | Risk, Option pricing    |
| 29 | Value            | of Firm:        | Last 10 years         | Equity:      | FA (Enterprise Value) | 21 | Dividends               |

| 30  | EBITDA                   | for last 10 years        | Equity: | FA (Income) | 21 | Capital Structure          |
|-----|--------------------------|--------------------------|---------|-------------|----|----------------------------|
| 31  | Alpha                    | (Intercept)              | Beta    | Calculation | 29 | Risk                       |
| 32  | R squared                |                          | Beta    | Calculation | 29 | Risk                       |
| 33  | Standard Error           | of Beta                  | Beta    | Calculation | 29 | Risk                       |
| 34a | Stockholders             | of record                | Equity: | HDS         | 8  | Corporate Governance       |
| 34b | Percent                  | of institutional holding | Equity: | DES         | 11 | Corporate Governance       |
| 35  | Debt                     | Distribution/ Maturity   | Equity: | DDIS        | 30 | Debt value, WACC           |
| 36  | Business                 | Breakdown                | Equity: | DES         | 13 | Risk                       |
| 37  | Geographic               | Breakdown                | Equity: | DES         | 14 | Risk, Financing Choices    |
| 38  | Non-cash Working Capital |                          | Equity: | DES         | 16 | Valuation, Dividend policy |
| 39  | Net                      | Debt Issued              | Equity: | DES         | 16 | Valuation, Dividend policy |

*As a general rule, stay away from the computational data provided by Bloomberg, where they try to estimate numbers based upon raw data. For instance, the WACC and Dividend discount model valuations that they provide are not very useful.*

<HELP> for explanation.

dgp Equity HDS

Enter #<GO> to select aggregate portfolio and see detailed information

00272317@154-000

## HOLDINGS SEARCH

CUSIP 25468710

DIS

US

THE WALT DISNEY CO.

Page

1 / 100

| Holder name           | Portfolio Name       | Source | Held    | Outstd | Percent | Latest Filing | Change Date |
|-----------------------|----------------------|--------|---------|--------|---------|---------------|-------------|
| * 1)BARCLAYS GLOBAL   | BARCLAYS BANK PLC    | 13F    | 91,334M | 4.470  | 7.912M  | 09/04         |             |
| * 2)CITIGROUP INCORP  | CITIGROUP INCORPORAT | 13F    | 71,012M | 3.475  | 893,816 | 09/04         |             |
| * 3)STATE STREET      | STATE STREET CORPORA | 13F    | 69,238M | 3.389  | 1,214M  | 09/04         |             |
| * 4)FIDELITY MANAGEM  | FIDELITY MANAGEMENT  | 13F    | 67,611M | 3.309  | 4,988M  | 09/04         |             |
| * 5)SOUTHEASTERN ASST | SOUTHEASTERN ASSET M | 13F    | 52,949M | 2.591  | 3,194M  | 09/04         |             |
| 6)VANGUARD GROUP      | VANGUARD GROUP INC   | 13F    | 43,710M | 2.139  | 979,055 | 12/04         |             |
| 7)ST FARM MU AUTO     | STATE FARM MUTUAL AU | 13F    | 42,234M | 2.067  | 10,300  | 09/04         |             |
| 8)MELLON BANK N A     | MELLON BANK CORP     | 13F    | 39,545M | 1.935  | 2,998M  | 09/04         |             |
| 9)LORD ABBETT & CO    | LORD ABBETT & CO     | 13F    | 37,460M | 1.833  | 286,434 | 12/04         |             |
| 10)MORGAN STANLEY     | MORGAN STANLEY       | 13F    | 31,643M | 1.549  | -1,348M | 09/04         |             |
| 11)NORTHERN TRUST C   | NORTHERN TRUST CORPO | 13F    | 26,061M | 1.275  | -39,493 | 09/04         |             |
| 12)DEUTSCHE BANK AK   | DEUTSCHE BANK AG     | 13F    | 21,990M | 1.076  | 1,570M  | 09/04         |             |
| 13)DISNEY ROY EDWAR   | n/a                  | Form 4 | 17,279M | 0.846  | -7,726  | 08/03         |             |
| 14)JANUS CAPITAL      | JANUS CAPITAL CORPOR | 13F    | 17,156M | 0.840  | -2,077M | 09/04         |             |
| * 15)CAPITAL RSCH MGM | CAPITAL RESEARCH AND | 13F    | 17,142M | 0.839  | 1,907M  | 09/04         |             |
| * 16)TUKMAN CAP MNGMT | TUKMAN CAPITAL MANAG | 13F    | 16,962M | 0.830  | 1,861M  | 09/04         |             |
| 17)T ROWE PRICE       | T ROWE PRICE ASSOCIA | 13F    | 16,810M | 0.823  | -1,367M | 09/04         |             |

Sub-totals for current page:

680,137M 33.286

\* Money market directory info available. Select portfolio, then hit IP<GO>.

Australia 61 2 9777 8600

Brazil 5511 3048 4500

Europe 44 20 7330 7500

Germany 49 69 920410

Hong Kong 852 2977 6000

Japan 81 3 3201 8900

Singapore 65 6212 1000

U.S. 1 212 318 2000

Copyright 2005 Bloomberg L.P.  
1 24-Jan-05 15:13:32

Item 34a:  
Largest  
stockholders  
in company

Mutual fund  
holdings are shown  
as 13F in the US.

Change in  
holding  
since last  
filing date.

**DIS** US \$ 1 **28.01** -.14 M 1s **Equity DES**  
**DELAY 14:53 Vol 4,739,800 Op 28.15 M Hi 28.27 T Lo 27.97 N ValTrd 133.134m**

**DESCRIPTION** Page 1/10  
**DIS US** THE WALT DISNEY CO. **Multimedia**

**CUSIP 254687106**  
 The Walt Disney Company, an entertainment company, conducts operations in media networks, studio entertainment, theme parks and resorts, consumer products, and Internet and direct marketing. The Company produces motion pictures, television programs, and musical recordings, as well as publishes books and magazines. Disney also operates ABC radio and television and theme parks.

| STOCK | DATA                           | USD                | DIVIDENDS | Annual              | USD                |
|-------|--------------------------------|--------------------|-----------|---------------------|--------------------|
| IDPO  | Price                          | 28.01              | 5DVD      | Indicated Gross Yld | .86%               |
|       | 52Wk High                      | 1/19/2005          |           | Dividend Growth     | 5YR                |
|       | 52Wk Low                       | 8/13/2004          |           | Ex-Date             | Type               |
|       | YTD change                     | .21                |           | 12/ 8/04            | Reg. Cash          |
|       | YTD % Change                   | .76%               |           |                     |                    |
| 2FA   | Shares out 12/ 6/2004          | 2043.283M          |           |                     |                    |
|       | Market Cap                     | USD 57232.36M      | 6ERN      | Ann Date            | 1/31/05 (16:01)(C) |
|       | Float                          | 2009.44M Short Int |           | Trailing            | 12mo EPS           |
| 3TRA  | 1 Yr Total Return              | 17.49%             | 7EE       | Est EPS             | 9/2005             |
|       | BETA vs. SPX                   | 1.24               |           | P/E                 | 25.70 LT Growth    |
| 40MON | Options, LEAPs, Stk Marginable |                    |           | Est P/E             | 22.63 Est PEG      |

Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 920410  
 Hong Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S. 1 212 318 2000 Copyright 2005 Bloomberg L.P.  
 1 24-Jan-05 15:14:00

Item 6: No of shares outstanding

Item 15: Market cap in millions. If your stock has multiple classes (voting and non-voting), this will be the market cap of all outstanding shares.

This is the Bloomberg default beta . It is a two-year weekly return adjusted beta.

Item 2: EPS estimates

**DIS US**THE WALT DISNEY CO.500 South Buena Vista Street  
Burbank, CA 91521  
United States

T:1-818-560-1000F:1-818-560-19302) [www.disney.com](http://www.disney.com)TR AG Company Office# OF EMPLOYEES 129,000 AS OF 09/30/04IMGMT COMPANY MANAGEMENT PROFILES4 GEORGE J MITCHELLCHAIRMAN5 MICHAEL D EISNERCEO6 ROBERT A IGERPRESIDENT/COO7 THOMAS O STAGGSSENIOR EXEC VP/CFO8 PETER E MURPHYSENIOR EXEC VP/CHF STRAT OFCR

| Type             | Common Stock  | PAR USD          | .01 |
|------------------|---------------|------------------|-----|
| PRIMARY EXCHANGE | New York      |                  |     |
| PRIMARY MIC      | XNYS          |                  |     |
| INCORPORATED     | UNITED STATES | ST DE            |     |
| FISCAL YEAR END  | SEPTEMBER     |                  |     |
| SIC Code         | 7812          | PRODUCE VIDEOS   |     |
| NAICS            | 512           | COMMON 009715100 |     |
| SVM Code         | 923592        |                  |     |
| WPK Number       | 855686        |                  |     |
| SEDOL1           | 2270726 US    |                  |     |
| Sicovam          | 929976        |                  |     |
| ISIN             | US2546871060  |                  |     |

| 3WGT MEMBER      | TICKER | WEIGHT  |
|------------------|--------|---------|
| DOW JONES INDUS. | INDU   | 1.990%  |
| S&P 500 INDEX    | SPX    | .526%   |
| S&P 500 MOVIES&E | S5MOVI | 22.839% |
| AMEX MAJOR MKT I | XMI    | 2.965%  |
| S&P 100 INDEX    | OEX    | .976%   |
| NYSE COMPOSITE I | NYA    | .366%   |
| AMEX INSTITUTION | XII    | .858%   |
| MORGAN STAN. CON | CMR    | 3.409%  |
| DOW JONES COMP.  | COMP   | 1.029%  |
| RUSSELL 1000 IND | RIY    | N.A.    |

Auditor PRICEWATERHOUSECOOPERAustralia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 920410  
 Hong Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S. 1 212 318 2000 Copyright 2005 Bloomberg L.P.  
 1 24-Jan-05 15:14:23

**RATIOS**

THE WALT DISNEY CO.

FY END SEP 2004 \* = Trailing 12 month ~ = Last Quarter 04:2004

| ISSUE DATA            | PER SHARE DATA          | CASH FLOW ANALYSIS     |
|-----------------------|-------------------------|------------------------|
| Price USD             | 28.01                   | Cashflow/net inc 1.86  |
| *P/E 25.70            | *Trailing 12m EPS 1.09  | Payout ratio 18.29%    |
| *Div Yld .86%         | Dividends/share .21     | Csh gen/Csh req 2.35   |
| *Price/Book 2.15      | *Book value/share 13.05 | Dvd coverage 5.47      |
| *Price/Sales 1.86     | Sales/share 15.01       | Cash-oper/sales 14.21% |
| Price/Cashflow 13.14  | Cash Flow/Basic sh 2.13 | Eff int. rate 4.99%    |
| Market cap. 57232.361 | Shares out 2043.28      |                        |
| Price/FCF 19.50       | FCF/share 1.44          |                        |

Dividend yield

Item 3: Payout Ratio

| GROWTH POTENTIAL                        | PROFITABILITY            | STRUCTURE              |
|-----------------------------------------|--------------------------|------------------------|
| Dil EPS CO YrChg 63.64%                 | Operating margin 13.16%  | Current ratio .85      |
| Cap Yr change 8.17%                     | Pretax margin 12.16%     | Quick ratio .60        |
| BVPS Yr change 10.44%                   | Return on assets 4.51%   | Debt to assets 25.02%  |
| R & D to sales Return on Com Eqty 9.40% | Return on Com Eqty 7.65% | T debt/Com eqty 51.72% |
| Retention rate 81.71%                   | Return on cap. 7.65%     | A/R turnover 6.99      |
| Sales Yr change 13.64%                  | Asset turnover .59       | Inv. turnover 36.12    |
| Employee Yr chan 15.18%                 | Fin. leverage 2.08       | Gross margin 13.20%    |
| Asset Yr change 7.83%                   | Eff tax rate 32.01%      | EBIT/total inter 6.10  |

Currency: US DOLLAR

Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 920410  
 Hong Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S. 1 212 318 2000 Copyright 2005 Bloomberg L.P.  
 1 24-Jan-05 15:14:44

Item 7: Effective tax rate for most recent year.

Note: Do not trust the return on equity and capital numbers that you see on this page. They are often incorrectly estimated. The same can be said for the multiples and interest coverage ratios. Do your own computations.

## SHAREHOLDER INFORMATION

THE WALT DISNEY CO.

IDACS CORPORATE ACTION CALENDARLATEST PUBLIC OFFERING

| Date of offering | 1/83           |                   |
|------------------|----------------|-------------------|
| Shares offered   | 1.00M          | Split Adj: 48.00M |
| Share Price      | \$ 66.88       | Split Adj: 1.39   |
| Lead Manager     | Morgan Stanley |                   |
| Type             | Common Stock   |                   |

INSIDER TRADINGNet \$ Value Buys and Sells As Of 01/15/05  
(1985 - Present In Dollars)

| Lowest activity     | 12/97 | -372.00MLN |
|---------------------|-------|------------|
| Highest activity    | 08/02 | 10.17MLN   |
| Mean:               |       | -15.95MLN  |
| Most recent 45 days |       | .00        |

INSTITUTIONAL OWNERSHIP

| # of Buyers      | 773     |
|------------------|---------|
| # of Sellers     | 788     |
| # of Holders     | 1,970   |
| Shares Held      | 1.39BLN |
| % Shares Out.    | 68.12   |
| Shares Purchased | 1.75MLN |

Australia 61 2 9777 8600      Brazil 5511 3048 4500      Europe 44 20 7330 7500      Germany 49 69 920410  
 Hong Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S. 1 212 318 2000 Copyright 2005 Bloomberg L.P.  
 1 24-Jan-05 15:16:57

Item 34b: Percent of stock held by institutions and number of institutional investors.

**DIS US THE WALT DISNEY CO.**  
**Net Sales**

![](_page_11_Figure_59.jpeg)

| VR   | Q1-Dec | Q2-Mar | Q3-Jun | Q4-Sep |
|------|--------|--------|--------|--------|
| 2004 | 8549.0 | 7189.0 | 7471.0 | 7543.0 |
| 2003 | 7170.0 | 6500.0 | 6377.0 | 7014.0 |
| 2002 | 7016.0 | 5856.0 | 5795.0 | 6662.0 |
| 2001 | 7403.0 | 6023.0 | 5960.0 | 5786.0 |
| 2000 | 6940.0 | 6307.0 | 6053.0 | 6034.0 |
| 1999 | 6521.0 | 5475.0 | 5489.0 | 5781.0 |
| 1998 | 6339.0 | 5242.0 | 5248.0 | 6147.0 |
| 1997 | 6278.0 | 5481.0 | 5194.0 | 5520.0 |

**EPS**

![](_page_11_Figure_62.jpeg)

| VR   | Q1-Dec | Q2-Mar | Q3-Jun | Q4-Sep |
|------|--------|--------|--------|--------|
| 2004 | .33    | .26    | .31    | .19    |
| 2003 | .09    | .15    | .19    | .17    |
| 2002 | .15    | .13    | .17    | .09    |
| 2001 | .28    | .17    | .23    | .12    |
| 2000 | .23    | .16    | .25    | .20    |
| 1999 | .23    | .13    | .20    | .10    |
| 1998 | .37    | .18    | .20    | .16    |
| 1997 | .32    | .16    | .23    | .20    |

**Total amounts in mil of USD. Per share amounts in USD.**

Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 920410  
 Hong Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S. 1 212 318 2000 Copyright 2005 Bloomberg L.P.  
 1 24-Jan-05 15:17:18

Item 11: EPS from 5 years ago can be obtained by adding up four quarters of EPS.

Quarterly revenue and EPS numbers for past few years.

**PRODUCT SEGMENTATION**

DIS US Walt Disney Co

Page 6 /10  
(in millions of USD)

![](_page_12_Figure_15.jpeg)

| PRODUCT                | 2002     | 2003      | 2004      | AVG 2-YR GROWTH |
|------------------------|----------|-----------|-----------|-----------------|
| 1)MEDIA NETWORKS       | 9,733.00 | 10,941.00 | 11,778.00 | 10.03%          |
| 2)STUDIO ENTERTAINMENT | 6,691.00 | 7,364.00  | 8,713.00  | 14.19%          |
| 3)PARKS AND RESORTS    | 6,465.00 | 6,412.00  | 7,750.00  | 10.02%          |
| 4)CONSUMER PRODUCTS    | 2,440.00 | 2,344.00  | 2,511.00  | 1.60%           |

Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 920410  
 Hong Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S. 1 212 318 2000 Copyright 2005 Bloomberg L.P.  
 1 24-Jan-05 15:17:38

Item 37: Breakdown of revenues by business and growth in each. For more detail, look at the annual report and the 10K for the company.

**GEOGRAPHIC SEGMENTATION**

DIS US Walt Disney Co

Page 7 /10  
(in millions of USD)

![](_page_13_Figure_14.jpeg)

| REGION/CNTRY     | 2002      | 2003      | 2004      | AVG 2-YR GROWTH |
|------------------|-----------|-----------|-----------|-----------------|
| 1) UNITED STATES | 20,770.00 | 22,124.00 | 24,012.00 | 7.53%           |
| 2) EUROPE        | 2,724.00  | 3,171.00  | 4,721.00  | 32.65%          |
| 3) ASIA PACIFIC  | 1,325.00  | 1,331.00  | 1,547.00  | 8.34%           |
| 4) LATIN AMERICA | 510.00    | 435.00    | 472.00    | -3.10%          |

Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 920410  
 Hong Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S. 1 212 318 2000 Copyright 2005 Bloomberg L.P.  
 1 24-Jan-05 15:18:01

Item 38: Breakdown of revenues by geographic area. Again, there should be more detail in the annual report or 10K.

Item 14:  
 Revenues:  
 Last 4  
 years

Hit 1 <GD> for more income statement information (CH2).

**INCOME STATEMENT** (Mil of USD) Page 8 /10  
**DIS US** THE WALT DISNEY CO.

|                        | 9/2001   | 9/2002   | 9/2003   | 9/2004   |
|------------------------|----------|----------|----------|----------|
| Net sales              | 25172.00 | 25329.00 | 27061.00 | 30752.00 |
| Cost of goods sold     | 21573.00 | 22924.00 | 24330.00 | 26692.00 |
| Sell, gen & adm exp    | 767.00   | 21.00    | 18.00    | 12.00    |
| Operating inc(loss)    | 2832.00  | 2384.00  | 2713.00  | 4048.00  |
| Interest expense       |          | 708.00   | 666.00   | 629.00   |
| For exchange L (G)     | .00      | .00      | .00      | .00      |
| Net non-op L (G)       | 1549.00  | -514.00  | -207.00  | -320.00  |
| Income tax expense     | 1059.00  | 853.00   | 789.00   | 1197.00  |
| Income bef X0 items    | 224.00   | 1337.00  | 1465.00  | 2542.00  |
| X0 L(G) pretax         | 278.00   | .00      | 71.00    | .00      |
| Tax effect on X0 items |          | .00      | .00      | .00      |
| Minority interest      | 104.00   | 101.00   | 127.00   | 197.00   |
| Net income (loss)      | -158.00  | 1236.00  | 1267.00  | 2345.00  |
| Tot cash pref. dvd     | .00      | .00      | .00      | .00      |
| Tot cash comm. dvd     | 438.00   | 428.00   | 429.00   | 429.00   |
| Diluted EPS Cont Ops   | .97      | .52      | .66      | 1.08     |
| Diluted EPS bef X0     | .11      | .60      | .65      | 1.12     |
| Diluted EPS            | -.02     | .60      | .62      | 1.12     |
| # Shrs Diluted EPS     | 2100.00  | 2044.00  | 2067.00  | 2106.00  |

Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 920410  
 Hong Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S. 1 212 318 2000 Copyright 2005 Bloomberg L.P.  
 1 24-Jan-05 15:18:19

Item 16:  
 Operating  
 Income/EBIT

Item 13:  
 Interest  
 Expenses

Taxes on  
 taxable  
 income

**BALANCE SHEET**  
DIS US

|                    |  | 9/2003   | 9/2004   |                    |          |          |
|--------------------|--|----------|----------|--------------------|----------|----------|
|                    |  |          |          |                    |          |          |
| Cash & near cash   |  | 1583.00  | 2042.00  | Accounts payable   | 4095.00  | 4531.00  |
| Marketable sec     |  | .00      | .00      | ST borrowings      | 2457.00  | 4093.00  |
| Acct & notes rec   |  | 4238.00  | 4558.00  | Other ST liab      | 2117.00  | 2435.00  |
| Inventories        |  | 703.00   | 775.00   | Cur liabilities    | 8669.00  | 11059.00 |
| Other cur assets   |  | 1790.00  | 1994.00  |                    |          |          |
| Current assets     |  | 8314.00  | 9369.00  | LT borrowings      | 10643.00 | 9395.00  |
|                    |  |          |          | Other LT liab      | 6457.00  | 6569.00  |
| LT inv't & LT rec  |  | 1849.00  | 1292.00  | Noncur liabilities | 17100.00 | 15964.00 |
|                    |  |          |          | Total liabilities  | 25769.00 | 27023.00 |
| Depr fixed assets  |  | 19499.00 | 25168.00 | Preferred equity   | .00      | .00      |
| Non-depr fixed ass |  | 1973.00  | 2979.00  | Minority interest  | 428.00   | 798.00   |
| Accum depreciation |  | 8794.00  | 11665.00 | Share cap & APIC   | 12154.00 | 12447.00 |
| Net fixed assets   |  | 12678.00 | 16482.00 | Retained earnings  | 11637.00 | 13634.00 |
|                    |  |          |          | Shareholder equity | 24219.00 | 26879.00 |
| Other assets       |  | 27147.00 | 26759.00 | Tot liab & equity  | 49988.00 | 53902.00 |
|                    |  |          |          |                    |          |          |
| Total assets       |  | 49988.00 | 53902.00 | ST part of LT debt | 2457.00  | 4093.00  |
|                    |  |          |          | # treasury shares  | 86.70    | 101.60   |
| Shares out         |  | 2013.30  | 1998.40  | Amt treasury stock | 1527.00  | 1862.00  |

Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 920410  
 Hong Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S. 1 212 318 2000 Copyright 2005 Bloomberg L.P.  
 1 24-Jan-05 15:18:36

Item 4:  
 Total Debt  
 = ST  
 Borrowing  
 + LT  
 .

Item 5:  
 Book  
 Value of  
 Equity

Item 38: Non-cash Working capital = Acct & Notes rec + Inventories + Other Current Assets - Accounts Payable - Other ST Liab

Item 10:  
Deprecn &  
Amortization

Hit 1 <GD> for more cash flow information (CH6).

P235 Equity DES

**CASH FLOW SUMMARY**  
DIS US

( Mil of USD ) Page 10/10

Item 8:  
Change in  
non-cash  
VC

Dividend

Stock  
buybacks =  
Dec  
Capital  
Stock

|                        | 9/2001   | 9/2002   | 9/2003   | 9/2004   |
|------------------------|----------|----------|----------|----------|
| Net income (loss)      | -158.00  | 1236.00  | 1267.00  | 2345.00  |
| Deprec & amort         | 1754.00  | 1042.00  | 1077.00  | 1210.00  |
| Other non-cash adj     | 1696.00  | 35.00    | 293.00   | 866.00   |
| Chg in non-cash wc     | -244.00  | -27.00   | 264.00   | -51.00   |
| Cashflow-operating act | 3048.00  | 2286.00  | 2901.00  | 4370.00  |
| Disp of fixed asst     | .00      | .00      | .00      | .00      |
| Capital expenditures   | -1795.00 | -1086.00 | -1049.00 | -1427.00 |
| Sale LT invest         | .00      | .00      | .00      | .00      |
| Purchase LT invest     | .00      | .00      | .00      | .00      |
| Other investing acts   | -220.00  | -2090.00 | 15.00    | -57.00   |
| Cashflow-investing act | -2015.00 | -3176.00 | -1034.00 | -1484.00 |
| Dividends paid         | -438.00  | -428.00  | -429.00  | -430.00  |
| Inc(dec) ST borrow     | -186.00  | -33.00   | -721.00  | 100.00   |
| Increase: LT borrow    | 3070.00  | 4038.00  | 1635.00  | 176.00   |
| Decrease: LT borrow    | -2807.00 | -2113.00 | -2059.00 | -2479.00 |
| Inc capital stock      | 177.00   | 47.00    | 51.00    | 201.00   |
| Dec capital stock      | -1073.00 | .00      | .00      | -335.00  |
| Other financing acts   | .00      | .00      | .00      | 66.00    |
| Cashflow-financing act | -1257.00 | 1511.00  | -1523.00 | -2701.00 |
| Net changes in cash    | -224.00  | 621.00   | 344.00   | 185.00   |

Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204  
Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S. 1 212 318 2000 Copyright 2005 Bloomberg  
1 24-Jan-05 15:1

Item 11:  
Capital  
expenditures

Item 39: Net  
debt issued =  
Inc(dec) ST  
borrow +  
Increase LT  
borrow -  
Decrease LT  
borrow

Note:

1. 1. The change in non-cash working capital computed by Bloomberg is an approximation since it includes short term interest bearing debt in ST liabilities.
2. 2. Capital expenditures do not include acquisitions. If the acquisitions are funded with cash it may be shown as LT investments. If funded with stock, it will not show up here.
3. 3. If disposal of fixed assets is a consistent number, you can net out against cap ex to reflect replacement of existing assets.

Item 26 Total Return = % Change + Div Yld

Note that I have used the old FA format. The new data is in roughly the same place but you have to print the section off separately. (There are separate print outs for price ratio analysis and stock performance, for example.

| Price    | 28.00 | Current | 12/04 | 12/03 | 12/02 | 12/01 | 12/00 | 12/99 | 12/98 | 12/97 | 12/96 | 12/95 | 3Y     | AvgGr  | 5Y | AvgGr |
|----------|-------|---------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------|--------|----|-------|
| P/E      | HI    | 26.55   | 33.82 | 45.77 | 39.95 | 38.67 | 34.39 | 50.24 | 43.63 | 39.43 | 39.29 | 29.80 | -2.74  | -12.04 |    |       |
|          | LO    | 24.70   | 19.51 | 27.61 | 23.65 | 17.61 | 30.95 | 34.98 | 24.73 | 27.37 | 22.29 | 21.12 | 7.23   | -5.35  |    |       |
|          | CL    | 25.70   | 25.50 | 27.77 | 33.98 | 30.93 | 32.51 | 32.52 | 38.96 | 34.38 | 34.70 | 22.39 | -5.52  | -5.36  |    |       |
| P/Book   | HI    | 2.22    | 2.38  | 2.01  | 2.24  | 3.13  | 4.01  | 4.01  | 4.68  | 3.91  | 5.15  | 5.18  | -7.59  | -10.54 |    |       |
|          | LO    | 2.27    | 1.65  | 1.30  | 1.18  | 1.28  | 2.23  | 2.31  | 2.40  | 2.67  | 2.23  | 4.14  | 7.74   | -3.92  |    |       |
|          | CL    | 2.13    | 2.13  | 1.95  | 1.43  | 1.86  | 2.54  | 2.63  | 3.11  | 3.67  | 2.80  | 4.34  | 7.53   | -3.08  |    |       |
| P/Sales  | HI    | 1.93    | 2.04  | 1.82  | 2.11  | 2.84  | 3.70  | 3.42  | 3.90  | 3.03  | 2.93  | 2.81  | -9.08  | -12.61 |    |       |
|          | LO    | 1.80    | 1.41  | 1.19  | 1.12  | 1.27  | 2.13  | 2.07  | 1.99  | 2.06  | 1.87  | 2.41  | 4.42   | -6.75  |    |       |
|          | CL    | 1.87    | 1.85  | 1.68  | 1.13  | 1.73  | 2.33  | 2.54  | 2.65  | 2.97  | 2.16  | 2.47  | 4.74   | -8.86  |    |       |
| P/CF     | HI    | 13.57   | 17.52 | 20.98 | 26.22 | 22.29 | 28.81 | 15.61 | 15.46 | 10.85 | 10.40 | 12.13 | -6.28  | -2.86  |    |       |
|          | LO    | 12.69   | 9.04  | 12.35 | 11.36 | 8.75  | 10.51 | 8.60  | 8.96  | 7.22  | 6.95  | 8.33  | 3.90   | -1.08  |    |       |
|          | CL    | 13.14   | 13.04 | 14.39 | 13.57 | 21.74 | 12.95 | 11.11 | 12.10 | 10.72 | 8.20  | 8.44  | -13.65 | 6.72   |    |       |
| Div Yld  | HI    | .88     | .98   | 1.38  | 1.49  | 1.18  | .77   | .80   | .81   | .65   | .73   | .65   | -3.37  | 10.59  |    |       |
|          | LO    | .83     | .76   | .90   | .85   | .62   | .50   | .50   | .44   | .51   | .52   | .53   | 8.87   | 13.04  |    |       |
|          | CL    | .86     | .86   | .90   | 1.29  | 1.01  | .73   | .72   | .67   | .51   | .60   | .59   | -2.38  | 8.13   |    |       |
| P/EBITDA | HI    | 11.28   | 12.64 | 13.81 | 13.67 | 12.47 | 16.69 | 11.56 | 11.13 | 8.19  | 8.67  | 8.34  | .75    | -5.77  |    |       |
|          | LO    | 10.54   | 8.37  | 9.57  | 7.84  | 5.93  | 9.61  | 7.29  | 6.45  | 5.23  | 7.16  | 13.90 | .86    |        |    |       |
|          | CL    | 10.91   | 10.83 | 10.38 | 10.52 | 10.50 | 10.61 | 10.00 | 8.97  | 8.09  | 5.50  | 7.31  | 1.09   | .55    |    |       |

|          | Current | 12/04   | 12/03   | 12/02   | 12/01   | 12/00   | 12/99   | 12/98   | 12/97   | 40     | AvGr | 120    | AvGr |
|----------|---------|---------|---------|---------|---------|---------|---------|---------|---------|--------|------|--------|------|
| Price    | OP      | 27.810  | 23.490  | 16.800  | 20.900  | 28.125  | 29.125  | 30.188  | 33.271  | 23.25  | 13.6 | 2.3    |      |
|          | HI      | 28.940  | 28.410  | 23.800  | 25.170  | 34.800  | 43.875  | 38.688  | 42.792  | 33.41  | -4.6 | -4.2   |      |
|          | LO      | 27.051  | 27.400  | 14.830  | 15.400  | 15.500  | 26.000  | 23.375  | 22.500  | 22.12  | 12.6 | 1.7    |      |
|          | CL      | 28.010  | 27.800  | 23.330  | 16.310  | 20.720  | 28.938  | 29.250  | 30.000  | 33.00  | 73.9 | -478.7 |      |
| % Change |         | 2.8     | 19.2    | 43.0    | 21.3    | 28.4    | 21.1    | 2.5     | 9.1     | 41.    | -.7  | -.7    |      |
| Shares   |         | 2043.3  | 1998.4  | 2013.3  | 2041.0  | 2038.0  | 2067.9  | 2069.0  | 2071.0  | 2025.  | NA   |        |      |
| Mkt cap  |         | 57232.4 | 55555.5 | 46970.3 | 33288.7 | 42227.4 | 59839.9 | 60518.3 | 62330.0 | 66825. | 12.7 | 1.5    |      |

**Act Ratios/Growth Potential**

| #s in %          | 9/04    | 9/03  | 9/02   | 9/01   | 9/00   | 9/99   | 9/98   | 9/97  | 9/96   | 9/95   | 9/94  | 3Y AvgGr | 5Y AvgGr |
|------------------|---------|-------|--------|--------|--------|--------|--------|-------|--------|--------|-------|----------|----------|
| Inv. turnover    | 36.12   | 34.76 | 33.51  | 31.42  | 28.92  | 23.26  | 21.64  | 20.13 | 17.36  | 12.96  | 12.67 | 4.76     | 9.45     |
| TL2 Inv turn-day | 10.13   | 10.50 | 10.89  | 11.62  | 12.66  | 15.69  | 16.86  | 18.13 | 21.08  | 28.17  | 28.81 | -4.44    | -8.18    |
| A/R turnover     | 6.99    | 6.53  | 6.85   | 7.25   | 7.52   | 6.55   | 6.27   | 7.24  | 8.03   | 7.76   | 8.01  | -1.05    | 1.63     |
| TL2 A/R turn-day | 52.34   | 55.89 | 53.26  | 50.33  | 48.66  | 55.75  | 58.21  | 50.38 | 45.58  | 47.03  | 45.54 | 1.47     | -.97     |
| Gr fixed asst tu | 1.24    | 1.28  | 1.22   | 1.26   | 1.38   | 1.41   | 1.56   | 1.71  | 1.73   | 1.37   | 1.26  | -.57     | -2.42    |
| Net fixed asst t | 2.11    | 2.13  | 1.97   | 2.00   | 2.15   | 2.16   | 2.38   | 2.65  | 2.64   | 2.02   | 1.82  | 1.93     | -.37     |
| Dil EPS CO YrChg | 63.64   | 26.92 | -46.39 | 34.72  | 10.77  | -28.57 | -7.77  | 20.82 | -5.77  | 27.45  | 65.85 | 20.26    | 84.18    |
| BVPS Yr change   | 10.44   | 2.87  | 3.26   | -4.55  | 14.96  | 8.29   | 9.68   | 7.29  | 88.18  | 20.67  | 11.88 | 141.15   | 74.70    |
| Asset Yr change  | 7.83    | -.11  | 14.52  | -2.95  | 3.09   | 5.56   | 7.48   | 5.11  | 150.76 | 13.87  | 9.15  | NM       | NM       |
| Payout ratio     | 18.29   | 32.06 | 34.63  | 365.00 | 47.17  | .00    | 22.27  | 17.40 | 22.32  | 12.68  | 13.80 | -46.95   | 133.22   |
| Working Capital  | -376.06 | NA    | -96.30 | NA     | NA     | 9.19   | 34.35  | NA    | NA     | NA     | 36.54 | NM       | NM       |
| Tot Cap Exp Grw  | 36.03   | -3.41 | -39.50 | -10.83 | -5.67  | -7.78  | 20.40  | 10.14 | 94.65  | -12.63 | 29.28 | 267.18   | 136.69   |
| Depreciation Chg | 13.13   | 3.72  | 3.44   | 2.60   | NA     | NA     | 9.62   | 9.01  | 43.98  | 14.77  | 12.49 | 97.75    | 97.75    |
| Cashflow/share g | 50.20   | 26.72 | -23.35 | -19.26 | -32.51 | 6.83   | -28.16 | 38.07 | 14.76  | 28.52  | 30.71 | 93.70    | -67.07   |
| FCF/share grw    | 58.44   | 54.11 | -2.12  | -28.45 | -49.35 | 20.59  | -45.95 | 20.47 | -1.34  | 16.94  | 10.54 | 856.98   | 437.79   |

**Profitability**

| #s in %            | 9/04  | 9/03  | 9/02  | 9/01  | 9/00   | 9/99   | 9/98  | 9/97  | 9/96   | 9/95  | 9/94   | 3Y AvgGr | 5Y AvgGr |
|--------------------|-------|-------|-------|-------|--------|--------|-------|-------|--------|-------|--------|----------|----------|
| Gross margin       | 13.20 | 10.09 | 9.50  | 14.30 | 14.78  | 15.87  | 17.47 | 19.19 | 17.79  | 20.19 | 19.55  | 1.17     | -1.33    |
| Sales Yr change    | 13.64 | 6.84  | .62   | -.97  | 8.46   | 2.00   | 2.24  | 19.93 | 54.71  | 20.46 | 17.89  | 420.09   | 294.48   |
| Net inc growth     | 85.08 | 2.51  | NA    | NA    | -29.23 | -29.73 | -5.90 | 61.94 | -12.04 | 24.29 | 270.38 | NM       | NM       |
| Operating margin   | 13.16 | 10.03 | 9.41  | 11.25 | 9.93   | 15.28  | 16.73 | 17.55 | 16.14  | 18.68 | 17.94  | 7.16     | -.05     |
| Pretax margin      | 12.16 | 8.33  | 8.65  | 5.10  | 10.36  | 10.25  | 13.74 | 15.07 | 11.00  | 17.48 | 18.04  | 37.31    | 12.43    |
| Eff tax rate       | 32.01 | 35.00 | 38.95 | 82.54 | 61.00  | 42.20  | 41.40 | 41.95 | 41.10  | 34.80 | 38.77  | -23.83   | 1.68     |
| Profit margin      | 7.63  | 4.68  | 4.88  | -.63  | 3.62   | 5.55   | 8.05  | 8.75  | 6.48   | 11.39 | 11.04  | 312.08   | 156.83   |
| Return on assets   | 4.51  | 2.53  | 2.64  | -.36  | 2.07   | 3.06   | 4.63  | 5.23  | 4.74   | 10.06 | 9.04   | 304.89   | 153.07   |
| Return on Com Eqty | 9.40  | 5.36  | 5.36  | -.68  | 4.08   | 6.44   | 10.09 | 11.78 | 10.68  | 22.70 | 21.07  | 322.92   | 163.12   |
| Return on cap.     | 7.65  | 4.85  | 5.00  | -.16  | 3.07   | 5.44   | 7.45  | 8.34  | 7.86   | 16.55 | 14.93  | NM       | 618.59   |

**ROE Decomposition**

| Percent            | 9/04  | 9/03  | 9/02  | 9/01   | 9/00   | 9/99  | 9/98  | 9/97  | 9/96  | 9/95  | 9/94   | 3Y AvgGr | 5Y AvgGr |
|--------------------|-------|-------|-------|--------|--------|-------|-------|-------|-------|-------|--------|----------|----------|
| Return on Com Eqty | 9.40  | 5.36  | 5.36  | -.68   | 4.08   | 6.44  | 10.09 | 11.78 | 10.68 | 22.70 | 21.07  | 322.92   | 163.12   |
| Tax burden         | 62.72 | 56.21 | 56.44 | -12.31 | 34.94  | 54.10 | 58.60 | 58.05 | 58.90 | 65.20 | 61.23  | 189.82   | 79.76    |
| Interest burden    | 92.37 | 83.08 | 91.86 | 45.30  | 104.28 | 67.12 | 82.15 | 85.86 | 68.15 | 93.57 | 100.55 | 34.80    | 20.64    |
| EBIT margin        | 13.16 | 10.03 | 9.41  | 11.25  | 9.93   | 15.28 | 16.73 | 17.55 | 16.14 | 18.68 | 17.94  | 7.16     | -.05     |
| Asset turnover     | .59   | .54   | .54   | .57    | .57    | .55   | .58   | .60   | .73   | .88   | .82    | 1.59     | 1.56     |
| Fin. leverage      | 2.08  | 2.12  | 2.03  | 1.90   | 1.97   | 2.11  | 2.18  | 2.25  | 2.25  | 2.26  | 2.33   | 3.23     | -.10     |

Copyright 2005 Bloomberg L.P. 24-Jan-05

**Debt Factors**

| #s in %           | 9/04     | 9/03     | 9/02     | 9/01    | 9/00    | 9/99     | 9/98     | 9/97     | 9/96     | 9/95    | 9/94   | 3Y AvgGr | 5Y AvgGr |
|-------------------|----------|----------|----------|---------|---------|----------|----------|----------|----------|---------|--------|----------|----------|
| Debt to assets    | 25.02    | 26.21    | 28.23    | 22.36   | 21.01   | 26.77    | 28.24    | 28.75    | 33.70    | 20.43   | 22.9   | 4.8      | -.10     |
| T debt/Com eqty   | 51.72    | 55.06    | 60.27    | 43.09   | 39.26   | 55.75    | 60.27    | 64.03    | 76.73    | 44.87   | 53.3   | 8.3      | 1.07     |
| LT debt/Com eqty  | 36.02    | 44.74    | 53.18    | 39.43   | 28.88   | 44.23    | 49.32    | 58.84    | 76.73    | 44.87   | 38.2   | -.1      | .27      |
| Total Debt/EBITDA | 2.57     | 3.46     | 4.12     | 2.13    | 2.00    | 1.59     | 1.63     | 1.24     | 1.77     | .73     | .8     | 17.2     | 16.81    |
| Com eqty/assets   | 48.39    | 47.59    | 46.85    | 51.88   | 53.52   | 48.02    | 46.86    | 44.90    | 43.92    | 45.54   | 42.9   | -2.1     | .39      |
| Com eqty/Tot Cap  | 64.61    | 63.75    | 61.68    | 69.07   | 71.06   | 63.53    | 62.40    | 60.96    | 56.59    | 69.03   | 65.2   | -2.0     | .61      |
| Tot debt/Tot cap  | 33.41    | 35.10    | 37.18    | 29.76   | 27.89   | 35.42    | 37.60    | 39.04    | 43.41    | 30.97   | 34.7   | 4.8      | .00      |
| LT debt/Tot cap   | 23.27    | 28.52    | 32.80    | 27.24   | 20.52   | 28.10    | 30.77    | 35.87    | 43.41    | 30.97   | 24.9   | -3.6     | -1.05    |
| CFO/Debt          | .32      | .22      | .16      | .31     | .40     | .48      | .44      | .64      | .37      | 1.18    | .9     | 11.6     | -.66     |
| Net debt          | 11446.00 | 11517.00 | 12891.00 | 9151.00 | 8619.00 | 11279.00 | 11558.00 | 10751.00 | 12064.00 | 1041.50 | 1426.8 | 9.8      | 2.44     |
| Net Debt/Shr Eqty | 42.58    | 47.55    | 53.98    | 39.69   | 35.24   | 52.90    | 59.61    | 62.20    | 75.00    | 15.66   | 25.9   | 4.5      | -1.42    |

**Per Share Data**

|                     | 9/04    | 9/03    | 9/02    | 9/01    | 9/00    | 9/99    | 9/98    | 9/97    | 9/96    | 9/95    | 9/94    | 3Y AvgGr | 5Y AvgGr |
|---------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|----------|----------|
| Cash Flow/Basic shr | 2.13    | 1.42    | 1.12    | 1.46    | 1.81    | 2.68    | 2.51    | 3.50    | 2.53    | 2.21    | 1.72    | 17.86    | .36      |
| FCF/share           | 1.44    | .91     | .59     | .60     | .84     | 1.66    | 1.38    | 2.54    | 1.58    | 1.64    | 1.09    | 6.53     | 6.53     |
| Sales/share         | 15.01   | 13.25   | 12.42   | 12.07   | 12.26   | 11.25   | 11.28   | 11.12   | 10.26   | 7.61    | 6.15    | 6.05     | 6.05     |
| Op income per share | 1.98    | 1.33    | 1.17    | 1.36    | 1.22    | 1.72    | 1.89    | 1.95    | 1.66    | 1.42    | 1.10    | 6.17     | 6.17     |
| Pretax Income per S | 1.82    | 1.10    | 1.07    | .62     | 1.27    | 1.15    | 1.55    | 1.68    | 1.13    | 1.33    | 1.11    | 20.23    | 20.23    |
| Cont inc per share  | 1.24    | .72     | .66     | .11     | .50     | .67     | .91     | .97     | .66     | .87     | .68     | 97.68    | 97.68    |
| Book value/share    | 13.05   | 11.82   | 11.49   | 11.12   | 11.65   | 10.14   | 9.36    | 8.54    | 7.96    | 4.23    | 3.50    | 5.40     | 5.40     |
| Diluted EPS Cont Op | 1.08    | .66     | .52     | .97     | .72     | .65     | .91     | .99     | .82     | .87     | .68     | 17.93    | 17.93    |
| Basic EPS           | 1.14    | .62     | .61     | -.02    | .58     | .63     | .91     | .97     | .66     | .87     | .68     | 624.83   | 624.83   |
| # Shrs Basic EPS    | 2049.00 | 2043.00 | 2040.00 | 2085.00 | 2074.00 | 2083.00 | 2037.00 | 2021.00 | 1827.00 | 1591.20 | 1635.60 | -.32     | -.32     |
| Diluted EPS         | 1.12    | .62     | .60     | -.02    | .57     | .62     | .89     | .95     | .65     | .87     | .68     | 614.48   | 614.48   |
| # Shrs Diluted EPS  | 2106.00 | 2067.00 | 2044.00 | 2100.00 | 2103.00 | 2056.00 | 2079.00 | 2060.00 | 1857.00 | 1591.20 | 1635.60 | .50      | .50      |
| Dil EPS CO YrChg    | 63.64   | 26.92   | -46.39  | 34.72   | 10.77   | -28.57  | -7.77   | 20.82   | -5.77   | 27.45   | 65.85   | 84.18    | 84.18    |
| Cash/Share          | 1.02    | .79     | .61     | .30     | .41     | .20     | .06     | .16     | .14     | 1.23    | .96     | 47.53    | 47.53    |
| Dividends/share     | .21     | .21     | .21     | .21     | .21     | .00     | .20     | .17     | .13     | .11     | .09     | .00      | .00      |

**Employee Data**

| Thousands: (Yrly Only) | 9/04      | 9/03      | 9/02      | 9/01      | 9/00      | 9/99      | 9/98      | 9/97      | 9/96      | 9/95     | 9/94     | 3Y AvgGr | 5Yr Avg |
|------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|----------|---------|
| # OF EMPLOYEES         | 129000.00 | 112000.00 | 112000.00 | 114000.00 | 120000.00 | 120000.00 | 117000.00 | 108000.00 | 100000.00 | 71000.00 | 65000.00 | 3.81     | 1.28    |
| Employee Yr change %   | 15.18     | .00       | -1.75     | -5.00     | .00       | 2.56      | 8.33      | 8.00      | 40.85     | 9.23     | 4.84     | 185.00   | 185.00  |
| Net inc/Employees      | 18.18     | 11.31     | 11.04     | -1.39     | 7.67      | 10.83     | 15.81     | 18.20     | 12.14     | 19.44    | 17.08    | 50.92    | 1.09    |
| Sales/Employees        | 238.39    | 241.62    | 226.15    | 220.81    | 211.82    | 195.29    | 196.38    | 208.08    | 187.39    | 170.59   | 154.69   | 2.48     | 3.86    |
| Assets/Employees       | 417.84    | 446.32    | 446.83    | 383.32    | 375.23    | 363.99    | 353.66    | 356.45    | 366.26    | 205.72   | 197.33   | 2.57     | 2.57    |

Copyright 2005 Bloomberg L.P. 24-Jan-05

Item 24: Average market debt to equity ratio for last 10 years

Item 30: EBITDA for last 10 years

Item 29: Value of firm = Market cap + Total debt + Preferred Equity. If you want enterprise value, subtract out cash.

![](_page_20_Picture_2.jpeg)

| Enterprise Value   |          | Enterprise Value |          |          |          |          |          |          |          |          |          |          |          |
|--------------------|----------|------------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| In Millions        | Current  | 9/04             | 9/03     | 9/02     | 9/01     | 9/00     | 9/99     | 9/98     | 9/97     | 9/96     | 9/95     | 3Y AvgGr | 5Y AvgGr |
| Market cap.        | 57232.36 | 45063.92         | 40608.26 | 30900.74 | 37947.56 | 79097.17 | 53794.00 | 52551.63 | 54421.88 | 42630.50 | 30087.45 | 23.13    | -.24     |
| Preferred equity   |          |                  |          |          |          |          |          |          |          |          |          |          |          |
| Minority interest  | 798.00   | 798.00           | 428.00   | 434.00   | 382.00   | 356.00   | 348.00   |          |          |          |          |          |          |
| Total debt         | 13488.00 | 13488.00         | 13100.00 | 14130.00 | 9769.00  | 9461.00  | 11693.00 | 11685.00 | 11068.00 | 12342.00 | 2984.30  | 28.36    | 21.20    |
| Cash & equivalents | 2042.00  | 2042.00          | 1583.00  | 1239.00  | 618.00   | 842.00   | 414.00   | 127.00   | 317.00   | 278.00   | 1942.80  | 18.92    | 26.13    |
| Enterprise Value   | 69476.36 | 73007.92         | 52553.26 | 44225.74 | 47480.56 | 88072.17 | 65421.00 | 64109.63 | 63172.88 | 54694.50 | 31128.95 | 16.37    | -.77     |
| T12 Sales          | 30752.00 | 30752.00         | 27061.00 | 25329.00 | 25172.00 | 25418.00 | 23435.00 | 22976.00 | 22473.00 | 18739.00 | 12112.10 | 6.83     | 4.03     |
| EV/T12 Sales       | 2.26     | 1.86             | 1.94     | 1.75     | 1.89     | 3.46     | 2.79     | 2.79     | 2.90     | 2.92     | 2.57     | 9.47     | -4.92    |
| T12 EBITDA         | 5258.00  | 5258.00          | 3790.00  | 3426.00  | 4586.00  | 4720.00  | 7359.00  | 7166.00  | 8903.00  | 6968.00  | 4115.10  | 16.45    | 4.24     |
| EV/T12 EBITDA      | 13.21    | 10.90            | 13.87    | 12.91    | 10.35    | 18.66    | 8.89     | 8.95     | 7.32     | 7.85     | 7.56     | 2.42     | -2.52    |
| T12 EBIT           | 4048.00  | 4048.00          | 2713.00  | 2384.00  | 2832.00  | 2525.00  | 3580.00  | 3843.00  | 3945.00  | 3024.00  | 2262.10  | 21.00    | 11.87    |
| EV/T12 EBIT        | 17.16    | 14.16            | 19.37    | 18.55    | 16.77    | 34.88    | 18.27    | 16.68    | 16.52    | 18.09    | 13.76    | -4.2     | -8.51    |
| EV/T12 Net Income  | 29.63    | 24.44            | 41.48    | 35.78    | NA       | 95.73    | 50.32    | 34.65    | 33.15    | 45.05    | 22.56    | -1.31    | 22.83    |
| EV/T12 Cash Flow   | 15.90    | 13.11            | 18.12    | 19.35    | 15.58    | 23.45    | 11.71    | 12.53    | 9.23     | 11.83    | 8.87     | -4.25    | -4.43    |
| EV/T12 FCF         | 23.61    | 19.47            | 28.38    | 36.85    | 37.89    | 50.56    | 18.94    | 22.89    | 12.67    | 18.99    | 11.91    | -11.05   | -12.19   |
| EV/Book Value      | 2.66     | 2.20             | 2.21     | 1.89     | 2.09     | 3.65     | 3.12     | 3.31     | 3.77     | 3.40     | 4.68     | 12.60    | -2.96    |
| EV/Market Cap      | 1.21     | 1.27             | 1.29     | 1.43     | 1.25     | 1.11     | 1.22     | 1.22     | 1.20     | 1.28     | 1.03     | -5.28    | 2.18     |
| Total Debt/EV      | .19      | .24              | .25      | .32      | .21      | .11      | .18      | .18      | .17      | .23      | .10      | -15.03   | 20.35    |

| Quotient           | 9/04     | 9/03    | 9/02  | 9/01   | 9/00    | 9/99    | 9/98    | 9/97    | 9/96     | 9/95    | 9/94    | 3Y      | AvgGr   | 5Y | AvgGr |
|--------------------|----------|---------|-------|--------|---------|---------|---------|---------|----------|---------|---------|---------|---------|----|-------|
| Cash ratio         | .18      | .18     | .16   | .10    | .10     | .05     | .02     | .05     | .04      | .68     | .35     | 25.27   | 32.31   |    |       |
| Current ratio      | .85      | .96     | 1.00  | 1.13   | .92     | 1.26    | 1.25    | 1.22    | .73      | 1.60    | .90     | -9.10   | -6.27   |    |       |
| Tot debt/Tot cap   | 33.41    | 35.10   | 37.18 | 29.76  | 27.89   | 35.42   | 37.60   | 39.04   | 43.41    | 30.97   | 34.78   | 4.84    | .00     |    |       |
| Cash&equv/Cur asst | 21.80    | 19.04   | 15.79 | 8.79   | 10.94   | 4.26    | 1.35    | 4.14    | 6.08     | 42.61   | 39.23   | 38.21   | 50.41   |    |       |
| T12 A/R turn-days  | 52.34    | 55.89   | 53.26 | 50.33  | 48.66   | 55.75   | 58.21   | 50.38   | 45.58    | 47.03   | 45.54   | 1.47    | -.97    |    |       |
| T12 Inv turn-days  | 10.13    | 10.50   | 10.89 | 11.62  | 12.66   | 15.69   | 16.86   | 18.13   | 21.08    | 28.17   | 28.81   | -4.44   | -8.18   |    |       |
| T12 Inv to cash-da | 62.48    | 66.39   | 64.15 | 61.95  | 61.32   | 71.44   | 75.07   | 68.51   | 66.67    | 75.20   | 74.35   | .39     | -2.41   |    |       |
| Op funds/Cur liab  | .37      | .31     | .30   | .46    | .30     | .46     | .51     | .63     | .48      | .80     | .42     | -4.48   | .56     |    |       |
| Op funds/IT debt   | .43      | .25     | .19   | .32    | .36     | .39     | .40     | .39     | .25      | .76     | .86     | 20.90   | .82     |    |       |
| Op funds/Tot debt  | .30      | .21     | .17   | .29    | .27     | .31     | .33     | .36     | .25      | .76     | .61     | 8.62    | 4.31    |    |       |
| Working Capital    | -1690.00 | -355.00 | 30.00 | 810.00 | -707.00 | 2020.00 | 1850.00 | 1377.00 | -1704.00 | 1717.10 | -422.90 | -585.23 | -335.20 |    |       |

| Quotient          | 9/04     | 9/03     | 9/02     | 9/01    | 9/00    | 9/99     | 9/98     | 9/97     | 9/96     | 9/95    | 9/94    | 3Y    | AvgGr | 5Y | AvgGr |
|-------------------|----------|----------|----------|---------|---------|----------|----------|----------|----------|---------|---------|-------|-------|----|-------|
| Assets/Equity     | 2.01     | 2.06     | 2.10     | 1.90    | 1.84    | 2.05     | 2.13     | 2.23     | 2.28     | 2.20    | 2.33    | 2.07  | -.19  |    |       |
| LT debt/Tot cap   | 23.27    | 28.52    | 32.80    | 27.24   | 20.52   | 28.10    | 30.77    | 35.87    | 43.41    | 30.97   | 24.95   | -3.67 | -1.05 |    |       |
| LT debt/Eq mkt va | .30      | .32      | .46      | .26     | .12     | .22      | .22      | .20      | .29      | .10     | .14     | 13.65 | 22.24 |    |       |
| LT debt/Tot cap   | 33.41    | 35.10    | 37.18    | 29.76   | 27.89   | 35.42    | 37.60    | 39.04    | 43.41    | 30.97   | 34.78   | 4.84  | .00   |    |       |
| Debt to assets    | 25.02    | 26.21    | 28.23    | 22.36   | 21.01   | 26.77    | 28.24    | 28.75    | 33.70    | 20.43   | 22.90   | 4.87  | -.10  |    |       |
| Total debt        | 13488.00 | 13100.00 | 14130.00 | 9769.00 | 9461.00 | 11693.00 | 11885.00 | 11068.00 | 12342.00 | 2984.30 | 2936.90 | 13.44 | 4.90  |    |       |
| Shares out        | 1998.40  | 2013.30  | 2041.00  | 2038.00 | 2067.90 | 2069.00  | 2071.00  | 2025.00  | 2022.00  | 1573.20 | 1572.30 | -.65  | -.69  |    |       |

**Fixed Charge Coverage**

| Quotient           | 9/04 | 9/03 | 9/02 | 9/01 | 9/00 | 9/99  | 9/98 | 9/97  | 9/96  | 9/95  | 9/94  | 3Y AvgGr | 5Y AvgGr |
|--------------------|------|------|------|------|------|-------|------|-------|-------|-------|-------|----------|----------|
| EBIT/int expense   | 6.44 | 4.07 | 3.37 | NA   | NA   | 5.85  | 6.18 | 5.69  | 6.31  | 12.69 | 15.04 | 39.48    | 39.48    |
| EBIT/total interes | 6.10 | 3.88 | 3.20 | NA   | NA   | 5.85  | 5.05 | 4.97  | 5.55  | 9.57  | 10.49 | 39.10    | 39.10    |
| EBITDA-cap exp/int | 5.77 | 3.92 | 3.15 | NA   | NA   | 8.54  | 6.38 | 8.80  | 9.58  | 13.62 | 13.88 | 35.91    | 35.91    |
| Total Debt/EBITDA  | 2.57 | 3.46 | 4.12 | 2.13 | 2.00 | 1.59  | 1.63 | 1.24  | 1.77  | .73   | .86   | 17.21    | 16.81    |
| EBITDA/Total Inter | 7.92 | 5.42 | 4.60 | NA   | NA   | 12.02 | 9.42 | 11.23 | 12.79 | 17.41 | 19.85 | 31.90    | 31.90    |
| CFO/Debt           | .32  | .22  | .16  | .31  | .40  | .48   | .44  | .64   | .37   | 1.18  | .96   | 11.68    | -.66     |

**Capital Source Analysis**

| Net Change         | 9/04     | 9/03     | 9/02    | 9/01     | 9/00     | 9/99    | 9/98    | 9/97     | 9/96    | 9/95    | 9/94    | 3Y AvgGr | 5Y AvgGr |
|--------------------|----------|----------|---------|----------|----------|---------|---------|----------|---------|---------|---------|----------|----------|
| ST borrowings      | 1636.00  | 794.00   | 834.00  | -1673.00 | 87.00    | 292.00  | 1226.00 | NA       | NA      | NA      | -425.60 | 83.70    | -368.42  |
| LT borrowings      | -1248.00 | -1824.00 | 3527.00 | 1981.00  | -2319.00 | -284.00 | -609.00 | -2171.00 | 9357.70 | 877.10  | 976.70  | -35.08   | -127.28  |
| Other liabilities  | 1236.00  | 627.00   | 1212.00 | -208.00  | 455.00   | 706.00  | 161.00  | 1946.00  | NA      | 589.60  | 46.30   | 243.85   | 110.06   |
| Inc in liabilities | 1624.00  | -403.00  | 5573.00 | 100.00   | -1777.00 | 714.00  | 778.00  | NA       | NA      | NA      | 597.40  | NM       | NM       |
| % of total         | 41.49    | 707.02   | 87.82   | -7.53    | -131.82  | 31.03   | 27.00   | NA       | NA      | NA      | 55.56   | 625.73   | 251.61   |
| Reinvested earning | 1916.00  | 838.00   | 808.00  | -596.00  | 486.00   | 1300.00 | 1438.00 | 1624.00  | 943.00  | 1205.07 | 957.20  | 122.64   | 16.53    |
| External equity fi | 374.00   | -492.00  | -35.00  | -832.00  | 2639.00  | 287.00  | 665.00  | -425.00  | 8492.20 | -62.57  | -479.40 | -408.50  | -107.50  |
| Increased equity   | 2290.00  | 346.00   | 773.00  | -1428.00 | 3125.00  | 1587.00 | 2103.00 | 1199.00  | 9435.20 | 1142.50 | 477.80  | 220.25   | 122.39   |
| % of total         | 58.51    | -607.02  | 12.18   | 107.53   | 231.82   | 68.97   | 73.00   | NA       | NA      | NA      | 44.44   | NM       | -975.98  |

**Income Statement Summary**

| Millions            | 9/04     | 9/03     | 9/02     | 9/01     | 9/00     | 9/99     | 9/98     | 9/97     | 9/96     | 9/95     | 9/94     | 3Y AvgGr | 5Y AvgGr |
|---------------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| Net sales           | 30752.00 | 27061.00 | 25329.00 | 25172.00 | 25418.00 | 23435.00 | 22976.00 | 22473.00 | 18739.00 | 12112.10 | 10055.10 | 7.03     | 5.72     |
| Cost of goods sold  | 26692.00 | 24330.00 | 22924.00 | 21573.00 | 21660.00 | 19715.00 | 18961.00 | 18161.00 | 15406.00 | 9666.40  | 8089.40  | 7.37     | 6.31     |
| Sell, gen & adm ex  | 12.00    | 18.00    | 21.00    | 767.00   | 1233.00  | 596.00   | 172.00   | 367.00   | 309.00   | 183.60   | 162.20   | -48.29   | -15.16   |
| Operating inc(loss) | 4048.00  | 2713.00  | 2384.00  | 2832.00  | 2525.00  | 3580.00  | 3843.00  | 3945.00  | 3024.00  | 2262.10  | 1803.50  | 15.73    | 5.98     |
| Interest expense    | 629.00   | 666.00   | 708.00   | NA       | NA       | 612.00   | 622.00   | 693.00   | 479.00   | 178.30   | 119.90   | -5.74    | -5.74    |
| Net non-op L (G)    | -320.00  | -207.00  | -514.00  | 1549.00  | -108.00  | 109.00   | 64.00    | -135.00  | 484.00   | -32.90   | -129.90  | -82.50   | 217.54   |
| Income tax expense  | 1197.00  | 789.00   | 853.00   | 1059.00  | 1606.00  | 1014.00  | 1307.00  | 1421.00  | 847.00   | 736.60   | 703.10   | 8.25     | 9.82     |
| Income bef XO item  | 2542.00  | 1465.00  | 1337.00  | 224.00   | 1027.00  | 1389.00  | 1850.00  | 1966.00  | 1214.00  | 1380.10  | 1110.40  | 193.32   | 95.14    |
| XO L(G) pretax      | .00      | 71.00    | .00      | 278.00   | .00      | .00      | .00      | .00      | .00      | .00      | .00      | NM       | NM       |
| Minority interest   | 197.00   | 127.00   | 101.00   | 104.00   | 107.00   | 89.00    | .00      | .00      | .00      | .00      | .00      | 25.99    | 19.08    |
| Net income (loss)   | 2345.00  | 1267.00  | 1236.00  | -158.00  | 920.00   | 1300.00  | 1850.00  | 1966.00  | 1214.00  | 1380.10  | 1110.40  | 323.29   | 164.69   |
| EBIT                | 4048.00  | 2713.00  | 2384.00  | 2832.00  | 2525.00  | 3580.00  | 3843.00  | 3945.00  | 3024.00  | 2262.10  | 1803.50  | 15.73    | 5.98     |
| Pretax income       | 3739.00  | 2254.00  | 2190.00  | 1283.00  | 2633.00  | 2403.00  | 3157.00  | 3387.00  | 2061.00  | 2116.70  | 1813.50  | 46.50    | 19.88    |
| Tot cash pref. dvd  | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | NM       | NM       |
| Tot cash comm. dvd  | 429.00   | 429.00   | 428.00   | 438.00   | 434.00   | .00      | 412.00   | 342.00   | 271.00   | 175.03   | 153.20   | -.68     | -.28     |
| Reinvested earning  | 1916.00  | 838.00   | 808.00   | -596.00  | 486.00   | 1300.00  | 1438.00  | 1624.00  | 943.00   | 1205.07  | 957.20   | 122.64   | 16.53    |
| Depreciation exp.   | 1198.00  | 1059.00  | 1021.00  | 987.00   | 962.00   | NA       | 809.00   | 738.00   | 677.00   | 470.20   | 409.70   | 6.76     | 5.72     |
| R & D expenditures  | NA       | NA       | NA       | NA       | NA       | NA       | NA       | NA       | NA       | NA       | NA       | NM       | NM       |

Copyright 2005 Bloomberg L.P. 24-Jan-05

Item 27:  
Operating  
income  
each year  
for last 10

**Income Statement: Common Size**

| % of Total Revenu   | 9/04   | 9/03   | 9/02   | 9/01   | 9/00   | 9/99   | 9/98   | 9/97   | 9/96   | 9/95   | 9/94   | 3Y AvgGr | 5Y AvgGr |
|---------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|----------|----------|
| Net sales           | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | .00      | .00      |
| Cost of goods sold  | 86.80  | 89.91  | 90.50  | 85.70  | 85.22  | 84.13  | 82.53  | 80.81  | 82.21  | 79.81  | 80.45  | .49      | .67      |
| Sell, gen & adm ex  | .04    | .07    | .08    | 3.05   | 4.85   | 2.54   | .75    | 1.63   | 1.65   | 1.52   | 1.61   | -52.80   | -20.97   |
| Operating inc(loss) | 13.16  | 10.03  | 9.41   | 11.25  | 9.93   | 15.28  | 16.73  | 17.55  | 16.14  | 18.68  | 17.94  | 7.16     | -.05     |
| Interest expense    | 2.05   | 2.46   | 2.80   | NA     | NA     | 2.61   | 2.71   | 3.08   | 2.56   | 1.47   | 1.19   | -14.42   | -14.42   |
| Net non-op L (G)    | -1.04  | -.76   | -2.03  | 6.15   | -.42   | .47    | .28    | -.60   | 2.58   | -.27   | -1.29  | -77.11   | 225.12   |
| Income tax expense  | 3.89   | 2.92   | 3.37   | 4.21   | 6.32   | 4.33   | 5.69   | 6.32   | 4.52   | 6.08   | 6.99   | .04      | 2.55     |
| Income bef XO item  | 8.27   | 5.41   | 5.28   | .89    | 4.04   | 5.93   | 8.05   | 8.75   | 6.48   | 11.39  | 11.04  | 182.81   | 87.72    |
| XO L(G) pretax      | .00    | .26    | .00    | 1.10   | .00    | .00    | .00    | .00    | .00    | .00    | .00    | NM       | NM       |
| Minority interest   | .64    | .47    | .40    | .41    | .42    | .38    | .00    | .00    | .00    | .00    | .00    | 16.90    | 11.94    |
| Net income (loss)   | 7.63   | 4.68   | 4.88   | -.63   | 3.62   | 5.55   | 8.05   | 8.75   | 6.48   | 11.39  | 11.04  | 312.08   | 156.83   |
| EBIT                | 13.16  | 10.03  | 9.41   | 11.25  | 9.93   | 15.28  | 16.73  | 17.55  | 16.14  | 18.68  | 17.94  | 7.16     | -.05     |
| Pretax income       | 12.16  | 8.33   | 8.65   | 5.10   | 10.36  | 10.25  | 13.74  | 15.07  | 11.00  | 17.48  | 18.04  | 37.31    | 3.41     |
| Tot cash pref. dvd  | .00    | .00    | .00    | .00    | .00    | .00    | .00    | .00    | .00    | .00    | NM     | NM       | NM       |
| Tot cash comm. dvd  | 1.40   | 1.59   | 1.69   | 1.74   | 1.71   | .00    | 1.79   | 1.52   | 1.45   | 1.45   | 1.52   | -7.02    | -4.79    |
| Reinvested earning  | 6.23   | 3.10   | 3.19   | -2.37  | 1.91   | 5.55   | 6.26   | 7.23   | 5.03   | 9.95   | 9.52   | 111.00   | 8.73     |
| Depreciation exp.   | 3.90   | 3.91   | 4.03   | 3.92   | 3.78   | NA     | 3.52   | 3.28   | 3.61   | 3.88   | 4.07   | -.19     | .76      |
| R & D expenditures  | NA     | NA     | NA     | NA     | NA     | NA     | NA     | NA     | NA     | NA     | NA     | NM       | NM       |

**Income Statement: Trend Analysis**

| % Change            | 9/04    | 9/03   | 9/02    | 9/01   | 9/00   | 9/99    | 9/98   | 9/97  | 9/96   | 9/95  | 9/94    | 3Y AvgGr | 5Y AvgGr |
|---------------------|---------|--------|---------|--------|--------|---------|--------|-------|--------|-------|---------|----------|----------|
| Net sales           | 13.64   | 6.84   | .62     | -.97   | 8.46   | 2.00    | 2.24   | 19.93 | 54.71  | 20.46 | 17.89   | 420.09   | 294.48   |
| Cost of goods sold  | 9.71    | 6.13   | 6.26    | -.40   | 9.87   | 3.98    | 4.41   | 17.88 | 59.38  | 19.49 | 18.88   | 571.79   | 351.88   |
| Sell, gen & adm ex  | -33.33  | -14.29 | -97.26  | -37.79 | 106.88 | 246.51  | -53.13 | 18.77 | 68.30  | 13.19 | -1.22   | -125.33  | -113.60  |
| Operating inc(loss) | 49.21   | 13.80  | -15.82  | 12.16  | -29.47 | -6.84   | -2.59  | 30.46 | 33.68  | 25.43 | 15.59   | 71.23    | 4.87     |
| Interest expense    | -5.56   | -5.93  | 708.00  | NA     | NM     | -1.61   | -10.25 | 44.68 | 168.65 | 48.71 | -23.97  | -53.59   | NM       |
| Net non-op L (G)    | -54.59  | 59.73  | NM      | NM     | 70.31  | NM      | NM     | NM    | NM     | 74.67 | NM      | -30.46   | NM       |
| Income tax expense  | 51.71   | -7.50  | -19.45  | -34.06 | 58.38  | -22.42  | -8.02  | 67.77 | 14.99  | 4.76  | 74.60   | 228.30   | 177.40   |
| Income bef XO item  | 73.52   | 9.57   | 496.88  | -78.19 | -26.06 | -24.92  | -5.90  | 61.94 | -12.04 | 24.29 | 65.41   | 435.10   | 220.14   |
| XO L(G) pretax      | -100.00 | 71.00  | -100.00 | 278.00 | .00    | .00     | .00    | .00   | .00    | .00   | -100.00 | -68.61   | -68.61   |
| Minority interest   | 55.12   | 25.74  | -2.88   | -2.80  | 20.22  | 89.00   | .00    | .00   | .00    | .00   | .00     | 367.88   | 182.50   |
| Net income (loss)   | 85.08   | 2.51   | NM      | NM     | -29.23 | -29.73  | -5.90  | 61.94 | -12.04 | 24.29 | 270.38  | NM       | NM       |
| EBIT                | 49.21   | 13.80  | -15.82  | 12.16  | -29.47 | -6.84   | -2.59  | 30.46 | 33.68  | 25.43 | 15.59   | 71.23    | 4.87     |
| Pretax income       | 65.88   | 2.92   | 70.69   | -51.27 | 9.57   | -23.88  | -6.79  | 64.34 | -2.63  | 16.72 | 68.85   | 765.48   | 232.30   |
| Tot cash pref. dvd  | .00     | .00    | .00     | .00    | .00    | .00     | .00    | .00   | .00    | .00   | NM      | NM       | NM       |
| Tot cash comm. dvd  | .00     | .23    | -2.28   | .92    | 434.00 | -100.00 | 20.47  | 26.20 | 54.83  | 14.25 | 19.13   | -118.74  | 49.18    |
| Reinvested earning  | 128.64  | 3.71   | NM      | NM     | -62.62 | -9.60   | -11.45 | 72.22 | -21.75 | 25.90 | 459.11  | NM       | NM       |
| Depreciation exp.   | 13.13   | 3.72   | 3.44    | 2.60   | 962.00 | NM      | 9.62   | 9.01  | 43.98  | 14.77 | 12.49   | 97.75    | 58.73    |
| R & D expenditures  | NA      | NA     | NA      | NA     | NA     | NA      | NA     | NA    | NA     | NA    | NA      | NM       | NM       |

Copyright 2005 Bloomberg L.P. 24-Jan-05

**Assets**

| Millions           | 9/04     | 9/03     | 9/02     | 9/01     | 9/00     | 9/99     | 9/98     | 9/97     | 9/96     | 9/95     | 9/94     | 3Y AvGr | 5Y AvGr |
|--------------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|---------|---------|
| Cash & near cash   | 2042.00  | 1583.00  | 1239.00  | 618.00   | 842.00   | 414.00   | 127.00   | 317.00   | 278.00   | 1076.50  | 186.90   | 52.42   | 46.80   |
| Marketable sec     | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | 866.30   | 1323.20  | NM      | NM      |
| Acct & notes rec   | 4558.00  | 4238.00  | 4049.00  | 3343.00  | 3599.00  | 3160.00  | 3999.00  | 3329.00  | 2875.00  | 1792.80  | 1328.40  | 11.11   | 8.02    |
| Inventories        | 775.00   | 703.00   | 697.00   | 671.00   | 702.00   | 796.00   | 899.00   | 853.00   | 951.00   | 824.00   | 668.30   | 4.99    | -.25    |
| Other cur assets   | 1994.00  | 1790.00  | 1864.00  | 2397.00  | 2552.00  | 5357.00  | 4350.00  | 3154.00  | 468.00   | .00      | 342.10   | -4.94   | -14.65  |
| Current assets     | 9369.00  | 8314.00  | 7849.00  | 7029.00  | 7695.00  | 9727.00  | 9375.00  | 7653.00  | 4572.00  | 4559.60  | 3848.90  | 10.09   | .15     |
| Gross fixed assets | 28147.00 | 21472.00 | 20913.00 | 20635.00 | 19202.00 | 17566.00 | 15728.00 | 13808.00 | 12479.00 | 9228.80  | 8441.60  | 11.70   | 10.38   |
| Accum depreciation | 11665.00 | 8794.00  | 8133.00  | 7728.00  | 6892.00  | 6220.00  | 5382.00  | 4857.00  | 4448.00  | 3038.50  | 2627.10  | 15.34   | 13.79   |
| Net fixed assets   | 16482.00 | 12678.00 | 12780.00 | 12907.00 | 12310.00 | 11346.00 | 10346.00 | 8951.00  | 8031.00  | 6190.30  | 5814.50  | 9.41    | 8.31    |
| LT inv't & LT rec  | 1292.00  | 1849.00  | 1810.00  | 2061.00  | 2270.00  | 2434.00  | 1814.00  | 1914.00  | 1009.00  | .00      | .00      | -13.38  | -11.22  |
| Other assets       | 26759.00 | 27147.00 | 27606.00 | 21702.00 | 22752.00 | 20172.00 | 19843.00 | 19979.00 | 23014.00 | 3855.90  | 3162.90  | 8.04    | 6.46    |
| Total assets       | 53902.00 | 49988.00 | 50045.00 | 43699.00 | 45027.00 | 43679.00 | 41378.00 | 38497.00 | 36626.00 | 14605.80 | 12826.30 | 7.41    | 4.47    |

**Assets (Common Size)**

| % of Total:        | 9/04   | 9/03   | 9/02   | 9/01   | 9/00   | 9/99   | 9/98   | 9/97   | 9/96   | 9/95   | 9/94   | 3Y AvGr | 5Y AvGr |
|--------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|---------|---------|
| Cash & near cash   | 3.79   | 3.17   | 2.48   | 1.41   | 1.87   | .95    | .31    | .82    | .76    | 7.37   | 1.46   | 40.87   | 39.10   |
| Marketable sec     | .00    | .00    | .00    | .00    | .00    | .00    | .00    | .00    | .00    | 5.93   | 10.32  | NM      | NM      |
| Acct & notes rec   | 8.46   | 8.48   | 8.09   | 7.65   | 7.99   | 7.23   | 9.66   | 8.65   | 7.85   | 12.27  | 10.36  | 3.43    | 3.30    |
| Inventories        | 1.44   | 1.41   | 1.39   | 1.54   | 1.56   | 1.82   | 2.17   | 2.22   | 2.60   | 5.64   | 5.21   | -2.03   | -4.41   |
| Other cur assets   | 3.70   | 3.58   | 3.72   | 5.49   | 5.67   | 12.26  | 10.51  | 8.19   | 1.28   | .00    | 2.67   | -10.88  | -17.93  |
| Current assets     | 17.38  | 16.63  | 15.68  | 16.09  | 17.09  | 22.27  | 22.66  | 19.88  | 12.48  | 31.22  | 30.01  | 2.69    | -4.22   |
| Gross fixed assets | 52.22  | 42.95  | 41.79  | 47.22  | 42.65  | 40.22  | 38.01  | 35.87  | 34.07  | 63.19  | 65.81  | 4.28    | 5.92    |
| Accum depreciation | 21.64  | 17.59  | 16.25  | 17.68  | 15.31  | 14.24  | 13.01  | 12.62  | 12.14  | 20.80  | 20.48  | 7.72    | 9.24    |
| Net fixed assets   | 30.58  | 25.36  | 25.54  | 29.54  | 27.34  | 25.98  | 25.00  | 23.25  | 21.93  | 42.38  | 45.33  | 2.11    | 3.92    |
| LT inv't & LT rec  | 2.40   | 3.70   | 3.62   | 4.72   | 5.04   | 5.57   | 4.38   | 4.97   | 2.75   | .00    | .00    | -18.75  | -14.44  |
| Other assets       | 49.64  | 54.31  | 55.16  | 49.66  | 50.53  | 46.18  | 47.96  | 51.90  | 62.84  | 26.40  | 24.66  | .31     | 1.73    |
| Total assets       | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | .00     | .00     |

**Asset Utilization**

| Sales to:          | 9/04  | 9/03  | 9/02  | 9/01  | 9/00  | 9/99  | 9/98   | 9/97  | 9/96  | 9/95  | 9/94  | 3Y AvGr | 5Y AvGr |
|--------------------|-------|-------|-------|-------|-------|-------|--------|-------|-------|-------|-------|---------|---------|
| Cash & near cash   | 15.06 | 17.09 | 20.44 | 40.73 | 30.19 | 56.61 | 180.91 | 70.89 | 67.41 | 11.25 | 53.80 | -26.03  | -17.97  |
| Marketable sec     | NA    | NA    | NA    | NA    | NA    | NA    | NA     | NA    | NA    | 13.98 | 7.60  | NM      | NM      |
| Acct & notes rec   | 6.75  | 6.39  | 6.26  | 7.53  | 7.06  | 7.42  | 5.75   | 6.75  | 6.52  | 6.76  | 7.57  | -3.06   | -1.47   |
| Inventories        | 39.68 | 38.49 | 36.34 | 37.51 | 36.21 | 29.44 | 25.56  | 26.35 | 19.70 | 14.70 | 15.05 | 1.96    | 6.49    |
| Other cur assets   | 15.42 | 15.12 | 13.59 | 10.50 | 9.96  | 4.37  | 5.28   | 7.13  | 40.04 | NA    | 29.39 | 14.22   | 35.16   |
| Current assets     | 3.28  | 3.25  | 3.23  | 3.58  | 3.30  | 2.41  | 2.45   | 2.94  | 4.10  | 2.66  | 2.61  | -2.73   | 7.47    |
| Gross fixed assets | 1.09  | 1.26  | 1.21  | 1.22  | 1.32  | 1.33  | 1.46   | 1.63  | 1.50  | 1.31  | 1.19  | -3.32   | -3.72   |
| Accum depreciation | 2.64  | 3.08  | 3.11  | 3.26  | 3.69  | 3.77  | 4.27   | 4.63  | 4.21  | 3.99  | 3.83  | -6.64   | -6.74   |
| Net fixed assets   | 1.87  | 2.13  | 1.98  | 1.95  | 2.06  | 2.07  | 2.22   | 2.51  | 2.33  | 1.96  | 1.73  | -1.09   | -1.77   |
| LT inv't & LT rec  | 23.80 | 14.64 | 13.99 | 12.21 | 11.20 | 9.63  | 12.67  | 11.74 | 18.57 | NA    | 27.26 | 21.43   | 21.43   |
| Other assets       | 1.15  | 1.00  | .92   | 1.16  | 1.12  | 1.16  | 1.16   | 1.12  | .81   | 3.14  | 3.18  | 1.01    | .60     |
| Total assets       | .57   | .54   | .51   | .58   | .56   | .54   | .56    | .58   | .51   | .83   | .78   | .07     | 1.49    |

Copyright 2005 Bloomberg L.P. 24-Jan-05

Items 18-20: Last 10 years of net income, depresciation and changes in non-cash working capital.

### Item 25: Book value of equity each year for last 10 years

Total Debt = ST Borr + LT Borr

|                     | 9/04     | 9/03     | 9/02     | 9/09     | 9/9      | 9/8      | 9/9      | 9/6      | 9/9      | 9/8      | 9/9      | 9/6   |
|---------------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|-------|
| Accounts payable    | 4531.00  | 4095.00  | 3820.00  | 4603.00  | 5161.00  | 3628.00  | 4767.00  | 4748.00  | 4835.00  | 2842.50  | 1771.00  | -2.8  |
| ST borrowing        | 4093.00  | 2457.00  | 1663.00  | 829.00   | 2502.00  | 2415.00  | 2123.00  | 897.00   | NA       | NA       | 829.70   | 31.64 |
| Other ST liab       | 2435.00  | 2117.00  | 2336.00  | 787.00   | 739.00   | 1664.00  | 635.00   | 631.00   | 1441.00  | NA       | 1670.30  | 67.49 |
| Cur liabilities     | 11059.00 | 8669.00  | 7819.00  | 6219.00  | 8402.00  | 7707.00  | 7525.00  | 6276.00  | 6276.00  | 2842.50  | 4271.00  | 21.39 |
| LT borrowings       | 9395.00  | 10643.00 | 12467.00 | 8940.00  | 6959.00  | 9278.00  | 9562.00  | 1071.00  | 12342.00 | 2984.30  | 2107.20  | 4.37  |
| Other LT liab       | 6569.00  | 6457.00  | 5880.00  | 5486.00  | 5210.00  | 5371.00  | 4903.00  | 4765.00  | 1922.00  | 2128.20  | 939.00   | 6.24  |
| Total liabilities   | 27023.00 | 25769.00 | 2616.00  | 2064.00  | 2037.00  | 2235.00  | 2199.00  | 21212.00 | 20540.00 | 7955.00  | 7318.00  | 10.03 |
| Preferred equity    | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00   |
| Minority interest   | 798.00   | 428.00   | 434.00   | 382.00   | 356.00   | 348.00   | .00      | .00      | .00      | .00      | .00      | NM    |
| Total common equity | 26081.00 | 23791.00 | 23445.00 | 24672.00 | 24100.00 | 20975.00 | 19388.00 | 17285.00 | 16086.00 | 6650.80  | 5508.30  | 4.84  |
| Shareholder equity  | 26879.00 | 24219.00 | 23879.00 | 23054.00 | 24356.00 | 21323.00 | 19285.00 | 16086.00 | 6650.80  | 5508.30  | 5.33     | 4.99  |
| Tot liab & equity   | 53902.00 | 49988.00 | 50045.00 | 4369.00  | 4369.00  | 4369.00  | 14378.00 | 3849.00  | 36626.00 | 16505.80 | 12826.30 | 7.41  |

| * of Total:              | 9/04         | 9/03         | 9/02         | 9/01         | 9/00         | 9/99         | 9/98         | 9/97         | 9/96         | 9/95         | 9/94         | 3Yr AvgGr    | 5Y Avg       |
|--------------------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| <b>Accounts payable</b>  | <b>8.41</b>  | <b>8.19</b>  | <b>7.63</b>  | <b>10.53</b> | <b>11.46</b> | <b>8.31</b>  | <b>11.52</b> | <b>12.33</b> | <b>13.20</b> | <b>19.46</b> | <b>13.81</b> | <b>-5.87</b> | <b>2.46</b>  |
| ST borrowings            | 7.59         | 4.92         | 7.32         | 1.90         | 5.56         | 5.53         | 5.13         | 2.33         | NA           | NA           | 6.47         | 59.19        | 22.44        |
| Other ST liab            | 4.52         | 4.24         | 4.67         | 1.80         | 1.64         | 3.81         | 1.53         | 1.64         | 3.93         | NA           | 13.02        | 52.19        | 21.88        |
| Cur liabilities          | 20.52        | 17.34        | 15.62        | 14.23        | 18.66        | 17.64        | 18.19        | 16.30        | 17.14        | 19.46        | 33.31        | 13.03        | 4.22         |
| OT borrowings            | 17.43        | 21.29        | 24.91        | 20.46        | 15.56        | 21.24        | 23.11        | 26.42        | 33.70        | 20.43        | 16.43        | -3.63        | -1.15        |
| Other LT liab            | 12.19        | 12.92        | 11.75        | 12.55        | 11.57        | 12.38        | 11.85        | 12.38        | 5.25         | 14.57        | 7.32         | -.71         | .05          |
| <b>Total liabilities</b> | <b>50.13</b> | <b>51.55</b> | <b>52.28</b> | <b>47.24</b> | <b>45.69</b> | <b>51.18</b> | <b>53.14</b> | <b>55.10</b> | <b>56.08</b> | <b>54.46</b> | <b>57.05</b> | <b>-2.17</b> | <b>-1.16</b> |
| Preferred equity         | .00          | .00          | .00          | .00          | .00          | .00          | .00          | .00          | .00          | .00          | .00          | NM           | NM           |
| Minority interest        | 1.48         | .86          | .87          | .87          | .79          | .80          | .00          | .00          | .00          | .00          | .00          | 23.62        | 16.13        |
| Total common equity      | 48.39        | 47.59        | 46.85        | 51.88        | 53.52        | 48.02        | 46.86        | 44.90        | 43.92        | 45.54        | 42.95        | -2.75        | .33          |
| Shareholder equity       | 49.87        | 48.45        | 47.72        | 52.76        | 54.31        | 48.82        | 46.86        | 44.90        | 43.92        | 45.54        | 42.95        | -1.77        | .68          |
| Tot liab & equity        | 100.00       | 100.00       | 100.00       | 100.00       | 100.00       | 100.00       | 100.00       | 100.00       | 100.00       | 100.00       | 100.00       | -.00         | .00          |

| Millions           | 9/04    | 9/03    | 9/02    | 9/01    | 9/00    | 9/99    | 9/98    | 9/97    | 9/96    | 9/95    | 9/94    | 3Y     | AvgGr  | 5Y | AvgGr |
|--------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|--------|--------|----|-------|
| Net income (loss)  | 2345.00 | 1267.00 | 1236.00 | -158.00 | 920.00  | 1300.00 | 1850.00 | 1966.00 | 1214.00 | 1380.10 | 1110.40 | 323.29 | 164.49 |    |       |
| Deprec & amort     | 1210.00 | 1077.00 | 1042.00 | 1754.00 | 2195.00 | 3779.00 | 3323.00 | 4958.00 | 3944.00 | 1853.00 | 1608.30 | -8.29  | -17.38 |    |       |
| Other non-cash adj | 866.00  | 293.00  | 35.00   | 1696.00 | -544.00 | 146.00  | 881.00  | -34.00  | 84.00   | 6.30    | 742.70  | 278.26 | 154.79 |    |       |
| Chg in non-cash w  | -51.00  | 264.00  | -27.00  | -244.00 | 1184.00 | 363.00  | -939.00 | 174.00  | -617.00 | 270.70  | -654.10 | 289.84 | 195.02 |    |       |
| Cashflow-operating | 4370.00 | 2901.00 | 2286.00 | 3048.00 | 3755.00 | 5588.00 | 5115.00 | 7064.00 | 4625.00 | 3510.10 | 2807.30 | 17.51  | 1.58   |    |       |
| FCF/share          | 1.44    | .91     | .59     | .60     | .84     | 1.66    | 1.38    | 2.54    | 1.58    | 1.64    | 1.09    | 36.81  | 6.53   |    |       |
| Cash Flow/Basic sh | 2.13    | 1.42    | 1.12    | 1.46    | 1.81    | 2.68    | 2.51    | 3.50    | 2.53    | 2.21    | 1.72    | 17.16  | -1.02  |    |       |

| Millions           | 9/04     | 9/03     | 9/02     | 9/01     | 9/00     | 9/99     | 9/98     | 9/97     | 9/96     | 9/95    | 9/94     | 3Y      | AvgGr   | 5Y | AvgGr |
|--------------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|---------|----------|---------|---------|----|-------|
| Dividends paid     | -430.00  | -429.00  | -428.00  | -438.00  | -434.00  | .00      | -412.00  | -342.00  | -271.00  | -180.00 | -153.20  | -.92    | -.92    |    |       |
| Inc(dec) ST borrow | 100.00   | -721.00  | -33.00   | -186.00  | -741.00  | -451.00  | .00      | .00      | .00      | NA      | NA       | -684.41 | -438.49 |    |       |
| Increase: LT borro | 176.00   | 1635.00  | 4038.00  | 3070.00  | 1117.00  | 2306.00  | 1830.00  | 2437.00  | 13560.00 | 786.10  | 1866.40  | -39.07  | 1.21    |    |       |
| Decrease: LT borro | -2479.00 | -2059.00 | -2113.00 | -2807.00 | -2494.00 | -2031.00 | -1212.00 | -4078.00 | -4872.00 | -771.90 | -1315.30 | -15.89  | -16.60  |    |       |
| Increase: stock    | 201.00   | 51.00    | 47.00    | 177.00   | 482.00   | 204.00   | 184.00   | 180.00   | 85.00    | .00     | .00      | 76.39   | 60.44   |    |       |
| Dec capital stock  | -335.00  | .00      | .00      | -1073.00 | -166.00  | -19.00   | -30.00   | -633.00  | -462.00  | -348.70 | -570.70  | NM      | -660.03 |    |       |
| Other financing ac | 66.00    | .00      | .00      | .00      | .00      | .00      | .00      | 1312.00  | .00      | 182.40  | 76.10    | NM      | NM      |    |       |
| Cashflow-financing | -2701.00 | -1523.00 | 1511.00  | -1257.00 | -2236.00 | 9.00     | 360.00   | -1124.00 | 8040.00  | -332.10 | -96.70   | -19.31  | NM      |    |       |
| Net changes in cas | 185.00   | 344.00   | 621.00   | -224.00  | 428.00   | 287.00   | -190.00  | 39.00    | -799.00  | 889.60  | -176.10  | 95.47   | 36.64   |    |       |

| Millions           | 9/04     | 9/03     | 9/02     | 9/01     | 9/00     | 9/9      | 9/98     | 9/97     | 9/94      | 9/95     | 9/94     | 9/95    | 9/94    |
|--------------------|----------|----------|----------|----------|----------|----------|----------|----------|-----------|----------|----------|---------|---------|
| Disp of fixed asst | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00       | NA       | NA       | NM      | NM      |
| Capital expenditur | -1427.00 | -1049.00 | -1086.00 | -1795.00 | -2013.00 | -2134.00 | -2314.00 | -1922.00 | -1745.00  | -896.50  | -1026.10 | -26.31  | -19.09  |
| Sale LT invest     | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00       | .00      | .00      | NM      | NM      |
| Purchase LT invest | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00      | .00       | .00      | .00      | NM      | NM      |
| Other investing ac | -57.00   | 15.00    | -2090.00 | -220.00  | 922.00   | -3176.00 | -3351.00 | -3979.00 | -11719.00 | -1391.90 | -1860.60 | -409.76 | -244.82 |
| Cashflow-investing | -1484.00 | -1034.00 | -3176.00 | -2015.00 | -1091.00 | -5310.00 | -5665.00 | -5901.00 | -13464.00 | -2288.40 | -2886.70 | -56.19  | -66.55  |

Items 21-23: Last 10 years of dividends paid, stock buybacks (dec in capital stock), stock issues (inc in capital stock) and capital expenditures

These are from Zacks. You can also try I/B/E/S from the EE menu. The number est is the number of analysts making estimates and the average is a %. (14.12% annually for next 5 years)

<HELP> for explanation.

P235 Equity EE

**EARNINGS ESTIMATES**

DIS US Walt Disney Co

Page 1 / 5

Last Update:  
01/21/05

WALL STREET ESTIMATES

|                    | MEAN  | HIGH  | LOW  | NUMBER EST | MEAN CHG LAST MNTH (\$) |
|--------------------|-------|-------|------|------------|-------------------------|
| FISC YR END 0509   | 1.23  | 1.33  | 1.12 | 22         | 0.00                    |
| FISC YR END 0609   | 1.41  | 1.50  | 1.28 | 13         | 0.01                    |
| QUARTER END 0412   | 0.30  | 0.35  | 0.26 | 15         | 0.00                    |
| QUARTER END 0503   | 0.31  | 0.34  | 0.29 | 15         | 0.00                    |
| NEXT 5 YR GRTH (%) | 14.12 | 21.00 | 9.00 | 13         | 0.13                    |

Item 12:  
Expected growth in EPS: Next 5 years

ALL ESTIMATES ARE FOR DILUTED EPS FROM CONTINUING OPERATIONS

The default in Bloomberg is daily data. It is better to use weekly data and the 100 week estimate of standard deviation.

Std deviation in stock price

<HELP> for explanation.

P235 Equity History

## HISTORICAL PRICE VOLATILITY

DIS US Equity

Period Weekly

Currency USD

THE WALT DISNEY CO.

| Date                    | Prices | N-DAY VOLATILITY             |       |       |       | OPTIONS            |       |
|-------------------------|--------|------------------------------|-------|-------|-------|--------------------|-------|
|                         |        | of Historical Closing Prices |       |       |       | Implied Volatility |       |
|                         |        | Market                       | Trade |       |       |                    |       |
|                         |        | N= 10 Week                   | 30    | 50    | 100   | Calls              | Puts  |
| 1/21/05                 | 28.15  | 13.22                        | 22.29 | 21.43 | 27.78 | 26.66              | 27.24 |
| 1/14/05                 | 28.30  | 13.21                        | 22.25 | 25.88 | 27.77 | 25.46              | 24.36 |
| 1/7/05                  | 27.17  | 9.93                         | 21.68 | 25.79 | 27.67 | 25.09              | 24.45 |
| 12/31/04                | 27.80  | 11.64                        | 21.40 | 25.65 | 27.62 | 22.63              | 21.73 |
| 12/24/04                | 27.59  | 11.92                        | 21.61 | 25.91 | 28.13 | 23.31              | 22.44 |
| 12/17/04                | 27.37  | 13.38                        | 21.77 | 25.90 | 28.16 | 23.52              | 21.99 |
| 12/10/04                | 27.63  | 12.44                        | 22.00 | 26.33 | 28.33 | 21.84              | 22.85 |
| 12/3/04                 | 27.37  | 19.33                        | 22.33 | 26.34 | 28.36 | 22.63              | 23.81 |
| 11/26/04                | 27.12  | 21.06                        | 22.67 | 26.33 | 28.51 | 22.62              | 22.98 |
| 11/19/04                | 26.66  | 21.34                        | 23.01 | 26.34 | 29.03 | 23.36              | 23.69 |
| 11/12/04                | 26.80  | 20.71                        | 24.98 | 26.98 | 29.12 | 26.09              | 27.38 |
| 11/5/04                 | 26.43  | 21.16                        | 24.99 | 27.85 | 29.12 | 25.08              | 27.55 |
| 52 Annualization factor |        |                              |       |       |       |                    |       |

Australia 61 2 9 7 7 7 8 6 0 0  
 Hong Kong 852 29 7 7 6 0 0 0 Japan 81 3 3 2 0 1 8 9 0 0 Singapore 65 6 2 1 2 1 0 0 0 U.S. 1 2 1 2 3 1 8 2 0 0 0 Copyright 2005 Bloomberg L.P.  
 1 24-Jan-05 15:21:55

Note: Bloomberg's default beta calculation always uses two years of weekly returns and the local market index. You can (and probably should) change both. I would change weekly to monthly, two years to five years.and narrow indices to broader ones.

<HELP> for explanation.

P235 Equity BETA

## HISTORICAL BETA

Number of points may be insufficient for an accurate beta.

DIS US Equity

THE WALT DISNEY CO.

Relative Index SPX

S&P 500 INDEX

\*Identifies latest observation

Period Monthly  
Range 1/31/00 To 12/31/04  
Market Trade

Item 1:  
Regression  
beta

Item 31:  
Regression  
Intercept

Item 32: R  
squared of  
regression

| ADJ BETA          | 1.17 |
|-------------------|------|
| RAW BETA          | 1.26 |
| Alpha(Intercept)  | 0.11 |
| R2 (Correlation)  | 0.44 |
| Std Dev of Error  | 6.69 |
| Std Error of Beta | 0.19 |
| Number of Points  | 59   |

$$\text{ADJ BETA} = (0.67) * \text{RAW BETA} + (0.33) * 1.0$$

Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 920410  
Hong Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S. 1 212 318 2000 Copyright 2005 Bloomberg L.P.  
1 24-Jan-05 15:12:57

Item 33:  
Std Error  
of Beta

![](_page_28_Figure_58.jpeg)

DDIS

P235 Equity DDIS

25 <GD> to view breakdown of bond types

**DEBT DISTRIBUTION**

Search by:

Debt Type **1** Bonds  
 Issuer **Walt Disney Co**  
 Include **2** Current issuer and subs  
 Or Ticker **1** Ticker Type **1** Corp

Filter by:

Curr of issue **1** Maturity **A** All  
 Country of issue **1** Coupon **A** All  
 Date Range **1/2005 to 12/2093**  
 Sec Type **A** All

![](_page_29_Figure_21.jpeg)

| By Maturity               |                     |          |    |     | Yearly     |     |
|---------------------------|---------------------|----------|----|-----|------------|-----|
| Yr                        | Amt                 | MM       | Yr | Amt | MM         |     |
| 2005                      | 811                 | 2017     |    |     | 300        |     |
| 2006                      | 2160                | 2018     |    |     |            |     |
| 2007                      | 662                 | 2019     |    |     |            |     |
| 2008                      | 425                 | 2020     |    |     |            |     |
| 2009                      | 592                 | 201      |    |     | 190        |     |
| 2010                      | 502                 | 202      |    |     | 25         |     |
| 2011                      | 252                 | 03       |    |     | 1322       |     |
| 2012                      | 125                 | 02       |    |     |            |     |
| 2013                      |                     |          |    |     |            |     |
| 2014                      | 450                 | 02       |    |     |            |     |
| 2015                      |                     |          |    |     | 2027       |     |
| 2016                      |                     |          |    |     | >2028      | 850 |
| <b>Total</b>              | <b>8,581,259.36</b> | <b>M</b> |    |     | <b>USD</b> |     |
| <b>Total # of Issues:</b> |                     |          |    |     | <b>23</b>  |     |

AvDisplays\_issued\_amounts of all bond loans disclosed to Bloomberg

<PGFWD> to see issues

Australia 61 2 9277 8600 Brazil 5511 3048 4500 Europe 44 20 2330 2500  
 Hong Kong 852 2977 6000 Japan 81 3 3201 8900 Singapore 65 6212 1000 U.S.

Item 35:  
 Maturity distribution for debt.

Germany 49 69 920410  
 Copyright 2005 Bloomberg L.P.  
 3 21-Jan-05 11:55:21

SECURITY DESCRIPTIONDISNEY (WALT) CO DISS % 12/15/17 105.968/105.968 (5.23/5.23) TRAC

| ISSUER INFORMATION                  |                                        | IDENTIFIERS  |                        |
|-------------------------------------|----------------------------------------|--------------|------------------------|
| Name WALT DISNEY COMPANY            | Common                                 | 016020613    | 1) Additional Sec Info |
| Type Multimedia                     | ISIN                                   | US25468PCB04 | 2) Identifiers         |
| Market of Issue GLOBAL              | CUSIP                                  | 25468PCB0    | 3) Ratings             |
| SECURITY INFORMATION                | RATINGS                                |              | 4) Fees/Restrictions   |
| Country US Currency USD             | Moody's Baa1                           |              | 5) Prospectus          |
| Collateral Type NOTES               | S&P BBB+                               |              | 6) Sec. Specific News  |
| Calc Typ( 1)STREET CONVENTION       | Fitch BBB+                             |              | 7) Involved Parties    |
| <b>Maturity 12/15/2017</b> Series B |                                        |              | 8) Custom Notes        |
| NORMAL                              |                                        |              | 9) Issuer Information  |
| <b>Coupon 5 % FIXED</b>             |                                        |              | 10) ALLO               |
| S/A 30/360                          | USD 300,000.00 (M)                     |              | 11) Pricing Sources    |
| Announcement Dt 12/16/02            | Amt Outstanding                        |              | 12) Related Securities |
| Int. Accrual Dt 12/19/02            | USD 300,000.00 (M)                     |              | 13) Issuer Web Page    |
| 1st Settle Date 12/19/02            | Min Piece/Increment 1,000.00/ 1,000.00 |              | 14) Par Cds Spreads    |
| 1st Coupon Date 6/15/03             | Par Amount 1,000.00                    |              | 15) TRACE Trade Recap  |
| Iss Pr 99.1170                      |                                        |              | 16) Capital Changes    |
| SPR @ ISS 180.00 vs T 4 11/15/12    | <b>BOOK RUNNER/EXCHANGE</b>            |              |                        |
| HAVE PROSPECTUS DTC                 | GS,CITI                                |              | 65) Old DES            |
|                                     | TRACE                                  |              | 66) Send as Attachment |

ISS'D UNDER MTN PROGRAM. SR. UNSEC'D. SHORT 1ST CPN.Item 17: Bond Ratings from S&P, Moody's and Fitch for corporate bonds issued by firm.

## **DATA ON COMPARABLE COMPANIES**

### **I. Getting data on related companies**

- ## • Pick Equity
- ## Choose 1. Finding Securities
- ## Choose Ticker Symbol Look up (TK)
- ## Enter the name of your company
- ## Once you are in equity screen for your company, enter
- **Relative Value** (RV): You can modify the data that is printed out. In particular, you can change the display to include only those items that you want for all of your comparable firms by going into the “Edit” function and changing the display.
- **Peer Verification (PV):** Your company's numbers will be printed out next to the average of the sector and the entire market.

Bloomberg will pick the comparable companies and you will have little flexibility. If you prefer to pick your own comparables, try the alternate approach (QSRC, two pages forward).

Print job sent to printer.

| Template List |  | Edit |  | Options |  | Output Results To |  | Relative Value (RV) |  |
|---------------|--|------|--|---------|--|-------------------|--|---------------------|--|
|---------------|--|------|--|---------|--|-------------------|--|---------------------|--|

| Earning Report Dates (Sector: Millimedia) 39 Securities Found |                  |            |        |               |              |             |              |               |  |
|---------------------------------------------------------------|------------------|------------|--------|---------------|--------------|-------------|--------------|---------------|--|
|                                                               | Short            | Volatility | Raw    | Current       | Dividends    | IBES 5      | Cash&Near    | Trailing      |  |
| Ticker                                                        | Name             | 250 Day    | Beta   | Market Cap    | Paid         | Year Growth | Cash Items   | 12M EBITDA    |  |
| Averages:                                                     |                  | 88.49      | 1.40   | 7665236875.00 | -36826800.00 | 19.05       | 290735200.00 | 1426933888.89 |  |
| DIS                                                           | DISNEY (WALT) CO | 25.055     | 1.364  | 57,232.36MLN  | -430.00MLN   | 5.157       | 2,042.00MLN  | 5,258.00MLN   |  |
| 1) RUNM                                                       | RAVEN MOON ENTER | 125.762    | 1.212  | 0.79MLN       |              | N.A.        |              |               |  |
| 2) YSTM                                                       | YOUTHSTREAM MED  | 129.477    | .868   | 12.95MLN      | 0.00MLN      | N.A.        | 0.68MLN      | N.A.          |  |
| 3) MTRM                                                       | METROMEDIA INTL  | 129.523    | 12.728 | 54.54MLN      | -6.97MLN     | N.A.        | 30.25MLN     | N.A.          |  |
| 4) MDP                                                        | MEREDITH CORP    | 15.000     | .796   | 2,570.55MLN   | -21.61MLN    | 8.336       | 58.72MLN     | 281.96MLN     |  |
| 5) MHP                                                        | MCGRAW-HILL COS  | 15.470     | .793   | 17,316.98MLN  | -206.54MLN   | 12.974      | 695.59MLN    | 1,647.15MLN   |  |
| 6) SSP                                                        | EW SCRIPPS-CL A  | 16.081     | .714   | 7,868.09MLN   | -50.46MLN    | 14.754      | 18.23MLN     | 498.19MLN     |  |
| 7) MEG                                                        | MEDIA GENERAL-A  | 18.999     | .794   | 1,497.41MLN   | -17.80MLN    | 3.474       | 10.58MLN     | 200.78MLN     |  |
| 8) TWX                                                        | TIME WARNER INC  | 19.404     | .792   | 84,737.18MLN  | 0.00MLN      | 4.912       | 3,040.00MLN  | 12,339.00MLN  |  |
| 9) VIA                                                        | VIACOM INC-A     | 20.301     | 1.379  | 64,552.57MLN  | -104.60MLN   | 66.012      | 850.70MLN    | 4,772.60MLN   |  |
| 10) BLC                                                       | BELO CORP-A      | 21.058     | 1.113  | 2,671.58MLN   | -38.61MLN    | 21.643      | 31.93MLN     | 405.20MLN     |  |
| 11) JRN                                                       | JOURNAL COMMUN-A | 23.556     | N.A.   | 1,275.63MLN   | -44.08MLN    | N.A.        | 8.44MLN      | 171.78MLN     |  |
| 12) QBID                                                      | TRIANGLE MULTI-M | 255.098    | -.464  | 32.40MLN      |              | N.A.        |              |               |  |
| 13) CEGP                                                      | CNTV ENTERTAINME | 288.600    | .873   | 0.74MLN       | 0.00MLN      | N.A.        | 1.30MLN      | -0.64MLN      |  |
| 14) EVC                                                       | ENTRAVISION CO-A | 33.282     | 1.393  | 923.81MLN     | 0.00MLN      | N.A.        | 19.81MLN     | 74.26MLN      |  |
| 15) ISPO                                                      | IDEA SPORTS ENTE | 354.269    | -.487  | 10.79MLN      |              | N.A.        |              |               |  |
| 16) GMST                                                      | GEMSTAR-TV GUIDE | 49.084     | 1.644  | 2,488.07MLN   | 0.00MLN      | 66.617      | 257.36MLN    | -7.77MLN      |  |
| 17) MSO                                                       | MARTHA STEW-CL A | 67.485     | .261   | 1,426.01MLN   | 0.00MLN      | -13.414     | 165.57MLN    | -38.80MLN     |  |
| 18) PRVT                                                      | PRIVATE MEDIA GP | 67.719     | .823   | 227.62MLN     | 0.00MLN      | N.A.        | 1.08MLN      | N.A.          |  |
| 19) TMEG                                                      | TRIMEDIA ENTERTA | 94.509     | N.A.   | 10.44MLN      | N.A.         | N.A.        | N.A.         | N.A.          |  |

### **II. Using Bloomberg to get Sector Data or to Screen Stocks**

- Start with this screen by typing “ESRC”. You will begin with this screen. If you want to screen based on market cap, PE or growth, you can do it here. (For example, I have screened for stocks with market cap> 30 million)

![](_page_33_Figure_2.jpeg)

- • Restrict your search to just common stocks to avoid multiple listings for the same company:

![](_page_34_Figure_9.jpeg)

- • Pick the country or countries you want to screen for

![](_page_35_Figure_67.jpeg)

- And make sure that you pick the exchanges to go with those countries. Looking for French stocks on the Indonesian exchange will give you no listings.....

![](_page_36_Figure_65.jpeg)

- • Pick the industry group you want to analyze or collect data from

![](_page_37_Figure_26.jpeg)

- • Go into the Edit function and choose the items you want displayed in your output.

Warning: This is not the friendliest interface in the world. You will often find yourself building elaborate criteria for 20 minutes and then losing them all because you hit the menu button twice instead of once. I would suggest saving the criteria under Save Set as you go along and assigning the criteria set a name. I would also suggest adding the company name to your data set - the default is only the ticker symbols, which are tough to expand, and keeping your data sets manageable.

# Getting Historical Macroeconomic Information

![](_page_39_Diagram_6.jpeg)