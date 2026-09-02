## Input Page
| Inputs for debt computation | Unnamed: 1 | Unnamed: 2 |
| --- | --- | --- |
| Interest bearing Debt & income statement information | NaN | NaN |
| Book value of interest-bearing debt = | 10788 | NaN |
| Interest expense for most recent year = | 606 | NaN |
| Weighted average maturity of debt = | 14.82 | ! If you cannot get it, enter zero. |
| Operating income (Earnings before interest & taxes)= | 6661 | NaN |
| Lease commitments (if any) | NaN | NaN |
| Do you have lease commitments? | Yes | NaN |
| If you do, please enter the commitments below | NaN | NaN |
| Operating lease expense (most recent year) = | 823 | NaN |
| Lease commitment in year 1 = | 800 | NaN |
| Lease commitment in year 2 = | 746 | NaN |
| Lease commitment in year 3 = | 682 | NaN |
| Lease commitment in year 4 = | 637 | NaN |
| Lease commitment in year 5 = | 557 | NaN |
| Lease commitments beyond year 5 = | 4577 | NaN |
| NaN | NaN | NaN |
| Cost of debt inputs | NaN | NaN |
| Do you want to input your pre-tax cost of debt? | No | NaN |
| If yes, please enter the pre-tax cost of debt | 0.03 | (If you have a rating for the company, you can estimate this number by looking at the synthetic ratings page for default spreads) |
| If no, you can compute a synthetic rating | NaN | NaN |
| Enter type of firm | 1 | (Enter 1 if large manufacturing firm, 2 if smaller or riskier firm, 3 if financial service firm) Small < $5 billion |
| NaN | NaN | NaN |
| Macro information | NaN | NaN |
| Riskfree rate = | 0.0193 | (Long term and default free) |
| Country default spread (if any) = | 0 | (If your company is from a non AAA rated country, enter the default spread for country) |

## Synthetic rating
| Inputs for synthetic rating estimation | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 | Unnamed: 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Please read the special cases worksheet (see below) before you use this spreadsheet. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Before you use this spreadsheet, make sure that the iteration box (under calculation options in excel) is checked. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Enter the type of firm = | NaN | 1 | (Enter 1 if large manufacturing firm, 2 if smaller or riskier firm, 3 if financial service firm) | NaN | NaN | NaN | NaN | Small: <$5 billion |
| Do you have any operating lease or rental commitments? | NaN | NaN | NaN | NaN | Yes | NaN | NaN | NaN |
| Enter current Earnings before interest and taxes (EBIT) = | NaN | NaN | NaN | NaN | 6661 | (Add back only long term interest expense for financial firms) | NaN | NaN |
| Enter current interest expenses = | NaN | NaN | NaN | NaN | 606 | (Use only long term interest expense for financial firms) | NaN | NaN |
| Enter current long term government bond rate = | NaN | NaN | NaN | NaN | 0.0193 | NaN | NaN | NaN |
| Output | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Interest  coverage ratio = | NaN | NaN | 8.889077 | NaN | NaN | NaN | NaN | NaN |
| Estimated Bond Rating = | NaN | NaN | AAA | NaN | Note: If you get REF! All over the place, set the operating lease commitment question in cell F5 | NaN | NaN | NaN |
| Estimated Default Spread = | NaN | NaN | 0.004 | NaN | to No, and then reset it to Yes. It should work. | NaN | NaN | NaN |
| Estimated Cost of Debt = | NaN | NaN | 0.0233 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| If you want to update the spreads listed below, please visit http://www.bondsonline.com | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| For large manufacturing firms | NaN | NaN | NaN | NaN | For financial service firms (default spreads are slighty different) | NaN | NaN | NaN |
| If interest coverage ratio is | NaN | NaN | NaN | NaN | If long term interest coverage ratio is | NaN | NaN | NaN |
| > | ≤ to | Rating is | Spread is | NaN | greater than | ≤ to | Rating is | Spread is |
| -100000 | 0.199999 | D | 0.12 | NaN | -100000 | 0.049999 | D | 0.12 |
| 0.2 | 0.649999 | C | 0.105 | NaN | 0.05 | 0.099999 | C | 0.105 |
| 0.65 | 0.799999 | CC | 0.095 | NaN | 0.1 | 0.199999 | CC | 0.095 |
| 0.8 | 1.249999 | CCC | 0.0875 | NaN | 0.2 | 0.299999 | CCC | 0.0875 |
| 1.25 | 1.499999 | B- | 0.0725 | NaN | 0.3 | 0.399999 | B- | 0.0725 |
| 1.5 | 1.749999 | B | 0.065 | NaN | 0.4 | 0.499999 | B | 0.065 |
| 1.75 | 1.999999 | B+ | 0.055 | NaN | 0.5 | 0.599999 | B+ | 0.055 |
| 2 | 2.25 | BB | 0.04 | NaN | 0.6 | 0.749999 | BB | 0.04 |
| 2.25 | 2.49999 | BB+ | 0.03 | NaN | 0.75 | 0.899999 | BB+ | 0.03 |
| 2.5 | 2.999999 | BBB | 0.02 | NaN | 0.9 | 1.199999 | BBB | 0.02 |
| 3 | 4.249999 | A- | 0.013 | NaN | 1.2 | 1.49999 | A- | 0.013 |
| 4.25 | 5.499999 | A | 0.01 | NaN | 1.5 | 1.99999 | A | 0.01 |
| 5.5 | 6.499999 | A+ | 0.0085 | NaN | 2 | 2.49999 | A+ | 0.0085 |
| 6.5 | 8.499999 | AA | 0.007 | NaN | 2.5 | 2.99999 | AA | 0.007 |
| 8.5 | 100000 | AAA | 0.004 | NaN | 3 | 100000 | AAA | 0.004 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| For smaller and riskier firms | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| If interest coverage ratio is | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| greater than | ≤ to | Rating is | Spread is | NaN | NaN | NaN | NaN | NaN |
| -100000 | 0.499999 | D | 0.12 | NaN | NaN | NaN | NaN | NaN |
| 0.5 | 0.799999 | C | 0.105 | NaN | NaN | NaN | NaN | NaN |
| 0.8 | 1.249999 | CC | 0.095 | NaN | NaN | NaN | NaN | NaN |
| 1.25 | 1.499999 | CCC | 0.0875 | NaN | NaN | NaN | NaN | NaN |
| 1.5 | 1.999999 | B- | 0.0725 | NaN | NaN | NaN | NaN | NaN |
| 2 | 2.499999 | B | 0.065 | NaN | NaN | NaN | NaN | NaN |
| 2.5 | 2.999999 | B+ | 0.055 | NaN | NaN | NaN | NaN | NaN |
| 3 | 3.499999 | BB | 0.04 | NaN | NaN | NaN | NaN | NaN |
| 3.5 | 4.0 | BB+ | 0.03 | NaN | NaN | NaN | NaN | NaN |
| 4 | 4.499999 | BBB | 0.02 | NaN | NaN | NaN | NaN | NaN |
| 4.5 | 5.999999 | A- | 0.013 | NaN | NaN | NaN | NaN | NaN |
| 6 | 7.499999 | A | 0.01 | NaN | NaN | NaN | NaN | NaN |
| 7.5 | 9.499999 | A+ | 0.0085 | NaN | NaN | NaN | NaN | NaN |
| 9.5 | 12.499999 | AA | 0.007 | NaN | NaN | NaN | NaN | NaN |
| 12.5 | 100000 | AAA | 0.004 | NaN | NaN | NaN | NaN | NaN |

## Operating Leases
| Operating lease inputs | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 |
| --- | --- | --- | --- | --- | --- |
| Operating lease expense in current year = | NaN | NaN | NaN | 823 | NaN |
| Operating Lease Commitments (From footnote to financials) | NaN | NaN | NaN | NaN | NaN |
| Year | Commitment | ! Year 1 is next year, …. | NaN | NaN | NaN |
| 1 | 800 | NaN | NaN | NaN | NaN |
| 2 | 746 | NaN | NaN | NaN | NaN |
| 3 | 682 | NaN | NaN | NaN | NaN |
| 4 | 637 | NaN | NaN | NaN | NaN |
| 5 | 557 | NaN | NaN | NaN | NaN |
| 6 and beyond | 4577 | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN |
| Pre-tax Cost of Debt = | NaN | 0.0233 | ! If you do not have a cost of debt, use the attached ratings estimator | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN |
| From the current financial statements, enter the following | NaN | NaN | NaN | NaN | NaN |
| Reported Operating Income (EBIT) = | NaN | NaN | 6661 | ! This is the EBIT reported in the current income statement | NaN |
| Reported Debt = | NaN | NaN | 0 | ! This is the interest-bearing debt reported on the balance sheet | NaN |
| Reported Interest Expenses = | NaN | NaN | 606 | NaN | NaN |
| Output | NaN | NaN | NaN | NaN | NaN |
| Number of years embedded in yr 6 estimate = | NaN | NaN | 7 | ! I use the average lease expense over the first five years | NaN |
| NaN | NaN | NaN | NaN | to estimate the number of years of expenses in yr 6 | NaN |
| Converting Operating Leases into debt | NaN | NaN | NaN | NaN | NaN |
| Year | Commitment | Present Value | NaN | NaN | NaN |
| 1 | 800 | 781.784423 | NaN | NaN | NaN |
| 2 | 746 | 712.414712 | NaN | NaN | NaN |
| 3 | 682 | 636.466357 | NaN | NaN | NaN |
| 4 | 637 | 580.934991 | NaN | NaN | NaN |
| 5 | 557 | 496.409775 | NaN | NaN | NaN |
| 6 and beyond | 653.857143 | 3724.044265 | ! Commitment beyond year 6 converted into an annuity for ten years | NaN | NaN |
| Debt Value of leases = | NaN | 6932.054522 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN |
| Restated Financials | NaN | NaN | NaN | NaN | NaN |
| Operating Income with Operating leases reclassified as debt = | NaN | NaN | NaN | NaN | 6822.516870 |
| Debt with Operating leases reclassified as debt = | NaN | NaN | NaN | NaN | 6932.054522 |
| NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN |
| Full Operating lease adjustment | NaN | NaN | NaN | NaN | NaN |
| Reported Operating income = | NaN | NaN | 6661 | NaN | NaN |
| + Current year's operating lease expense = | NaN | NaN | 823 | NaN | NaN |
| - Depreciation on leased asset = | NaN | NaN | 577.67121 | NaN | NaN |
| Adjusted Operating Income | NaN | NaN | 6906.32879 | NaN | NaN |

## MV of Debt
| Unnamed: 0 | Inputs | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 |
| --- | --- | --- | --- | --- |
| Book value of debt | 10788.000000 | NaN | NaN | NaN |
| Interest expense | 606.000000 | NaN | NaN | NaN |
| Average maturity | 14.820000 | NaN | NaN | NaN |
| Pre-tax cost of debt | 0.023300 | NaN | NaN | NaN |
| NaN | NaN | NaN | Book interest rate = | 0.056174 |
| Estimated market value of debt | 15189.580949 | NaN | NaN | NaN |

## Weighted maturity of debt
| Due in | Number of years | Amount due | Weight |
| --- | --- | --- | --- |
| 2013 | 1.000000 | 1309 | 0.121429 |
| 2016 | 4.000000 | 3069 | 0.284694 |
| 2020 | 8.000000 | 499 | 0.046289 |
| 2021 | 9.000000 | 998 | 0.092579 |
| 2036 | 24.000000 | 2961 | 0.274675 |
| 2040 | 28.000000 | 499 | 0.046289 |
| 2041 | 29.000000 | 996 | 0.092393 |
| 2055 | 43.000000 | 449 | 0.041651 |
| Total | 14.822449 | 10780 | 1.000000 |

## Input choices
| Yes | 1 |
| --- | --- |
| No | 2 |
| NaN | 3 |

## Sheet8
|
|  |

## Sheet9
|
|  |

## Sheet10
|
|  |

## Sheet11
|
|  |

## Sheet12
|
|  |

## Sheet13
|
|  |

## Sheet14
|
|  |

## Sheet15
|
|  |

## Sheet16
|
|  |