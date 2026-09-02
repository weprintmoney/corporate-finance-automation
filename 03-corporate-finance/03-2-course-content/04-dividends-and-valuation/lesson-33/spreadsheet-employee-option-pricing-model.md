---
title: "Spreadsheet: Employee Option Pricing Model"
status: active
owner: weprintmoney
created: 2026-09-01
last_updated: 2026-09-01
---

## Warrant Valuation
| 0                                                                                                                                                   |          1 |         2 | 3                          | 4            |       5 |
|:----------------------------------------------------------------------------------------------------------------------------------------------------|-----------:|----------:|:---------------------------|:-------------|--------:|
| Valuing Management Options or Warrants when there is dilution                                                                                       | nan        | nan       | nan                        | nan          |  nan    |
| This program is designed to value options, the exercise of which can create more shares and thus affect the stock price. This is the case           | nan        | nan       | nan                        | nan          |  nan    |
| with warrants and management options. It is also the case with convertible bonds. As a general rule, using an unadjusted                            | nan        | nan       | nan                        | nan          |  nan    |
| option pricing model to value these options will overstate their value.                                                                             | nan        | nan       | nan                        | nan          |  nan    |
| Note: Before you run this program, check under preferences (under tools), and calculations, and ensure that  there is a check against the iteration | nan        | nan       | nan                        | nan          |  nan    |
| box. You will get a circular reasoning warning, but this program needs circular reasoning to compute the option value.                              | nan        | nan       | nan                        | nan          |  nan    |
| Enter the current stock price =                                                                                                                     | nan        | nan       | 10                         | nan          |  nan    |
| Enter the strike price on the option =                                                                                                              | nan        | nan       | 10                         | nan          |  nan    |
| Enter the expiration of the option =                                                                                                                | nan        | nan       | 5                          | nan          |  nan    |
| Enter the standard deviation in stock prices =                                                                                                      | nan        | nan       | 0.4                        | (volatility) |  nan    |
| Enter the annualized dividend yield on stock =                                                                                                      | nan        | nan       | 0                          | nan          |  nan    |
| Enter the treasury bond rate =                                                                                                                      | nan        | nan       | 0.02                       | nan          |  nan    |
| Enter the number of warrants (options) outstanding =                                                                                                | nan        | nan       | 100                        | nan          |  nan    |
| Enter the number of shares outstanding =                                                                                                            | nan        | nan       | 1000                       | nan          |  nan    |
| VALUING WARRANTS WHEN THERE IS DILUTION                                                                                                             | nan        | nan       | nan                        | nan          |  nan    |
| Stock Price=                                                                                                                                        | nan        |  10       | # Warrants issued=         | nan          |  100    |
| Strike Price=                                                                                                                                       | nan        |  10       | # Shares outstanding=      | nan          | 1000    |
| Adjusted S =                                                                                                                                        | nan        |   9.39645 | T.Bond rate=               | nan          |    0.02 |
| Adjusted K=                                                                                                                                         | nan        |  10       | Variance=                  | nan          |    0.16 |
| Expiration (in years) =                                                                                                                             | nan        |   5       | Annualized dividend yield= | nan          |    0    |
| nan                                                                                                                                                 | nan        | nan       | Div. Adj. interest rate=   | nan          |    0.02 |
| d1 =                                                                                                                                                |   0.489416 | nan       | nan                        | nan          |  nan    |
| N (d1) =                                                                                                                                            |   0.687726 | nan       | nan                        | nan          |  nan    |
| d2 =                                                                                                                                                |  -0.405011 | nan       | nan                        | nan          |  nan    |
| N (d2) =                                                                                                                                            |   0.342735 | nan       | nan                        | nan          |  nan    |
| Value of the call =                                                                                                                                 | nan        |   3.361   | nan                        | nan          |  nan    |
