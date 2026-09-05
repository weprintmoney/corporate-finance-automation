---
title: "Corrections"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/val3ed/corrections.pdf
---

parent company. To do this, you would first need to estimate the market value of equity in LatinWorks, which is a private company. We will use the estimate of equity value that we obtained in Illustration 16.6: Value of equity in LatinWorks = 370.25 million

$$\text{EV/EBITDA}_{\text{no holdings}} = \frac{(1,529 - .51 \times 459 - .15 \times 370.25) + (500 - 150)}{500 - 180} = \frac{4.97}{5.70}$$

This will yield an EV/EBITDA for just the parent company. The alternative is to adjust just the denominator to make it consistent with the numerator. In other words, the EBITDA should include only 51% of the majority active holding's EBITDA and should add in the 15% of the EBITDA in the minority holdings:

$$\text{EV/EBITDA}_{\text{holdings}} = \frac{1,529 + 500 - 150}{500 - .49 \times 180 + .15 \times 120} = \frac{4.97 \times 150}{4.27 \times 45}$$

In the third approach, you estimate the EV-to-EBITDA multiple for the consolidated firm, correcting for just the minority holding. To accomplish this, you need to add the estimated value of the equity in the subsidiary that you have consolidated (since the market value of equity of the parent company reflects only the 51% of the subsidiary that you own) to the numerator and subtract the estimated value of equity in the minority holding in Latin Works from that value. The denominator can be left untouched since it already includes 100% of the EBITDA from the consolidated subsidiary; the same argument applies to the cash and debt items in Segovia:

$$\text{EV/EBITDA}_{\text{Consolidated}} = \frac{1529 + 0.49 \times 459 + 500 - 150}{500} = \frac{4.27 \times 45}{4.21}$$

Note that 49% of the market value of equity in Seville is added back to the numerator, to stay consistent with equity value being measured in market terms. In practice, though, many analysts would have used the minority interests on Segovia's balance sheet, which is the book value measure of the 49% of Seville, to get to enterprise value. While this may be convenient, it does introduce an inconsistency into the estimate.

Since the approaches yield very different values, you may wonder which one is correct. Since the only reason we compute the multiple is to compare it to values computed for similar companies, the answer depends on that comparison. If each of the three companies is in a different sector, it is best to use the first approach and get EV/EBITDA multiples for each company separately and compare that company to other companies in its sector. If you can find consolidated companies that look just like Segovia, in terms of both minority and majority holdings, you can use the second approach. If Segovia and Seville are both in the same sector, you can use the third approach, since you can compare the consolidated value to the values that other companies in the sector trade at.

### Description

Figure 18.13 summarizes the enterprise value to EBITDA multiples for U.S. firms in January 2011. As with the price-earnings ratio, you have a heavily skewed distribution. The average EV/EBITDA multiple across U.S. firms in January 2011 was 54.8, while the median value is closer to 10. To illustrate that these distributional characteristics are not unique to the United States, we compare the distributions of EV/EBITDA multiples globally in Figure 18.14. The European, emerging market, and Japanese firms all have skewed distributions, with positive outliers pushing the average well above the median.

### Analysis

To analyze the determinants of enterprise value to EBITDA multiples, we will revert back to a free cash flow to the firm valuation model that we developed in

*Regressing price to sales ratio against net margins, we get:*

*PS* = *0.304* + *0.126(Net margin)*

*Plugging in Whole Food's net margin into the regression, we get:*

*PS* = *0.304* + *0.126(.273)* = *0.34*

*Whole Food looks significantly over valued in May 2011.*

*In hindsight, these regressions would have suggesting selling short on Whole Foods in January 2007, buying the stock again in January 2009 and reverting back to selling short in January 2010. The first two actions would have generated significant profits, but the last one would have been a money loser since the stock became even more overvalued between 2010 and 2011.*

**Market Regressions** If you can control for differences across firms using a regression, you can extend this approach to look at much broader cross sections of firms. Here, the cross-sectional data is used to estimate the price-to-sales ratio as a function of fundamental variables—profit margin, dividend payout, beta, and growth rate in earnings.

This approach can be extended to cover the entire market. In the first edition of this book, regressions of price-sales ratios on fundamentals—dividend payout ratio, growth rate in earnings, profit margin, and beta—were run for each year from 1987 to 1991.

| Year |    |              | Regression      |              | R-Squared     |
|------|----|--------------|-----------------|--------------|---------------|
| 1987 | PS | = 0.7894     | + .0008 Payout  | −            | 0.2734 Beta   |
|      |    | + 0.5022 EGR | +               | 6.46 Margin  | 0.4434        |
| 1988 | PS | = 0.1660     | + .0006 Payout  | −            | 0.0692 Beta   |
|      |    | + 0.5504 EGR | +               | 10.31 Margin | 0.7856        |
| 1989 | PS | = 0.4911     | + .0393 Payout  | −            | 0.0282 Beta   |
|      |    | + 0.2836 EGR | +               | 10.25 Margin | 0.4601        |
| 1990 | PS | = 0.0826     | + .0105 Payout  | −            | 0.1073 Beta   |
|      |    | + 0.5449 EGR | +               | 10.36 Margin | 0.8885        |
| 1991 | PS | = 0.5189     | + 0.2749 Payout |              | − 0.2485 Beta |
|      |    | + 0.4948 EGR | +               | 8.17 Margin  | 0.4853        |

- where PS = Price-sales ratio at the end of the year
- Payout = Payout ratio = Dividends/Earnings at the end of the year
- Beta = Beta of the stock
- Margin = Profit margin for the year = Net income/Sales for the year (in %)
- EGR = Earnings growth rate over the previous five years

These regressions were updated in May 2011 for both price-to-sales and EV/Sales ratios for companies listed and traded in the United States:

PS =−0.413 + 7.27 Expected growthEPS + 0.16 Payout + 0.42 Beta + 14.44 Net margin (2.99) (14.10) (1.02) (5.86) (35.90) R-squared = 49%

FIGURE 33.2 Decision Tree for Drug Development

![](_page_2_Diagram_3.jpeg)

![](_page_2_Diagram_6.jpeg)

FIGURE 33.3 Present Value of Cash Flows at End Nodes: Drug Development Tree

*AU: The equations in 33.3 do they need some parens to indicate the order of operations? They seem confusing as is.*