---
title: "Alternatives to Regression Betas"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2009/02/alterntive-to-regression-betas.html
published: 2009-02-15
updated_source: 2009-02-15
fetched: 2026-08-27
---

# Alternatives to Regression Betas

_Source: [https://aswathdamodaran.blogspot.com/2009/02/alterntive-to-regression-betas.html](https://aswathdamodaran.blogspot.com/2009/02/alterntive-to-regression-betas.html) — published 2009-02-15_

In my prior post, I explain why I am averse to regression betas - the high standard errors of the estimates, the backward-looking nature of the estimates and the loss of intuitive feel for risk. In this post, I would like to look at alternatives that are offered to regression betas, with an eye towards making better estimates:

1. Relative standard deviations: The beta is a function of the standard deviation of the stock, the standard deviation of the market and the correlation of the stock with the market:
Beta = (Correlation between stock and market) (Std dev of stock)/Std dev of mkt
The primary culprit behind the high standard error of betas is the shifting correlation number. Hence, there are some who suggest using an alternative measure of relative risk:
Relative Std dev = (Std dev of stock)/Average std dev across all stocks

Note that the denominator has to the average standard deviation across all stocks, not the standard deviation for the market, since you want the relative risk number to average out to one across all stocks (and it will not if you use the standard deviation of the market).
Pros: This number, like beta, should average out to one across stocks and should have lower standard error; even in a period like the last quarter, the standard deviations rose across the board and the relative standard deviation was fairly stable.
Cons: You are looking at total risk (not just market risk), which may not be appropriate for a diversified investor. You are also still backward looking and dependent on stock prices.

2. Option based approaches: A few years ago, there was a hue an a cry, arising from a paper published in the Harvard Business Review, which claimed to have come up with a forward looking estimate for risk. In the approach, the implied standard deviation of stocks is backed out of traded options issued by the company and compared to the standard deviation of bonds issued by the same company.
Cost of equity = Cost of debt *(Imp std dev of equity/ Std dev of bonds)
Pros: Forward looking, becauase you use option prices to back out standard deviation.
Cons: Works only for companies that have traded options and bonds... and it mixes up total risk and market risk. Does not strike me as a general approach that will work with most companies.

3. Accounting betas: Rather than regressing stock returns against market returns, we could regress changes in accounting earnings at a company against changes in accounting earnings for the entire market, and the slope would be the accounting beta.
Pros: Not dependent upon stock prices and can be estimated even for private businesses. For those who do not trust markets, accounting earnings offer a more stable alternative (assuming that you trust accountants).
Cons: Accounting earnings are often smoothed out and lag true earnings. Furthermore, the number of observations in your regression is restricted. With quarterly statements, you will have 20 observations over 5 years and the resulting standard error will be huge.

4. Bottom-up Betas: In this approach, we start with the businesses that a firm operates in, estimate the betas of these businesses (by looking at the average regression betas of publicly traded firms in each of the businesses) and clean up for differences in financial leverage.
Pros: The average across many regression betas will be more precise than any individual company's regression beta. It can be computed based upon the current or even a future business mix of a company and for private businesses.
Cons: You do need to find publicly traded companies that operate predominantly or only in each individual business and you the average regression beta does reflect the past. For instance, the average beta across all banks over the last 5 years may understate the true beta for banks for the future.

I am a firm believer in the last approach. Since there are lots of mechanical details that can trip you up, I do have a link on my site where I examine these:
[http://www.stern.nyu.edu/~adamodar/New_Home_Page/TenQs/TenQsBottomupBetas.htm](http://www.stern.nyu.edu/%7Eadamodar/New_Home_Page/TenQs/TenQsBottomupBetas.htm)
More in my next post!
