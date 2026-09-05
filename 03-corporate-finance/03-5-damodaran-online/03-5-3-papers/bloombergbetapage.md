---
title: "Bloombergbetapage"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/cfovhds/BloombergBetapage.pdf
---

Find your stock symbol and the local listing. This may not be as easy as it looks when your company has multiple listings.

This is the market index. The default index in Bloomberg will be the local index for the country in which your stock is listed. You can change the index to any index you want (for example): SPX: S&P 500 NFT: MSCI Global equity index SPEURO: S&P 350 Euro stocks

This is your return interval. The default is weekly but you can change it to daily or monthly.

This is the currency in which your returns are computed. It is good to be currency consistent. Leave at Local CCY with the local index but change to US\$ when you change the index to the S&P 500 or MSCI which are \$ based.

<HELP> for explanation, <MENU> for similar functions.

Equity BETA

| XOM US Equity | Relative Index | SPX Index           | Historical Beta |
|---------------|----------------|---------------------|-----------------|
| Data          | Last Price     | Range               | Period          |
| Linear        | Beta +/-       | 02/27/09 - 02/18/11 | Weekly          |
|               | Non-Parametric | Lag 0               | Local CCY       |

![](_page_0_Figure_26.jpeg)

| Item                 | Value  |
|----------------------|--------|
| Y = EXXON MOBIL CORP |        |
| X = S&P 500 INDEX    |        |
| Raw BETA             | 0.791  |
| Adj BETA             | 0.860  |
| ALPHA(Intercept)     | -0.242 |
| R^2(Correlation^2)   | 0.598  |
| R(Correlation)       | 0.773  |
| Std Dev Of Error     | 1.770  |
| Std Error Of ALPHA   | 0.179  |
| Std Error Of BETA    | 0.064  |
| t-Test               | 12.261 |
| Significance         | 0.000  |
| Last T-Value         | 0.813  |
| Last P-Value         | 0.791  |
| Number Of Points     | 103    |

Intercept Bloomberg reports this number already in percent. So, this is -0.242%. To get to Jensen's alpha, subtract out Rf(1-Beta) from this number. Assuming a 1.00% annualized rate, for instance, Exxon's weekly Jensen's alpha will be -0.242% - (1.00%/52) (1- 0.79) = -0.243% (Make sure your riskfree rate matches your return interval)

![](_page_0_Figure_29.jpeg)

Std Error of Beta Adding (subtracting) this number to (from) your regression beta will give you a 67% range. Two standard errors in both directions will give you a 95% range. 0.727-0.855 (67% range) 0.663- 0.929 (95% range)

Regression beta

Adjusted beta = 0.67 (Raw Beta) + 0.33 (1.00)

R^2= R Squared This number is in decimals. Thus, 0.598 is really 59.8%...