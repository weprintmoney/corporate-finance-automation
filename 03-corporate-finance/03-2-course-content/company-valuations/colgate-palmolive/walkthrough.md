---
title: "Colgate-Palmolive — How this valuation was built"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive — How this valuation was built

## How to read this

This document walks through the valuation of Colgate-Palmolive one step at a time, in the order the course teaches it. Every number in it was either read from a named document or computed by the model from those documents; nothing is typed in from memory. Each step has the same six parts: what we wanted to know, why it matters, what we did, the numbers and where they came from, what we decided, and how sure we are. Terms are explained the first time they appear and will be collected in the glossary at the end.

## The valuation in ten sentences

To be written last, when all 36 steps are done.

## Where the numbers come from

*The company's own reports.* Colgate-Palmolive's annual reports (Form 10-K) for 2025 and 2024, filed with the Securities and Exchange Commission (SEC), the US regulator. The 2025 report, filed on 2026-02-23, is the main one. Also the quarterly report (Form 10-Q) for the three months to 2026-09-30, and the 2026 proxy statement, the document sent to shareholders before the annual meeting, which lists the directors, their pay and who owns the shares. A fifth file holds every annual figure Colgate reported to the SEC in machine-readable form for 2014 through 2025. Files: `sources/filings/`.

*A data service, as a cross-check.* Twenty pages from Capital IQ, a financial database, read through a university account. The filings are the record. Capital IQ is used for what filings do not carry: the credit rating, the breakdown of shareholders by type, analysts' forecasts and a list of similar companies. Files: `sources/capital-iq/`.

*Market data.* The interest rate on 10-year US government bonds on 2026-11-19, from the Federal Reserve Bank of St. Louis's public database (FRED). The extra return investors demand for owning stocks, the table that turns a credit rating into an interest rate, the risk measures for each industry and the risk premiums for each country, all from Professor Damodaran's published datasets. Month-end share prices for Colgate and the S&P 500 index (500 large US companies) from December 2020 to 2026-11-20. Files: `sources/market-data/`.

*Two generated files.* `model-output.md` is produced by the course model from the ledger (`inputs.yaml`, the list of every input with its source). `module-1-cross-checks-output.md` is produced by a short script from the same ledger and source files; it holds the alternatives quoted in steps 1 to 12, so a reader can see how much each choice is worth. A second script produces `modules-2-4-cross-checks-output.md` the same way for steps 13 to 28: the finer debt schedule, the year-by-year cash flow table and the comparisons with other companies. None of the three is edited by hand.

*The professor's spreadsheets.* Three of Professor Damodaran's workbooks were filled in with the same inputs. Their results are in `professor-spreadsheet/results.md` and are used from step 13 on. A fourth workbook, on how sensitive industries are to interest rates, inflation and currencies, supplies the figures in `professor-spreadsheet/macro-sensitivity-output.md`, used in step 23.

## Step 1: What kind of company is Colgate-Palmolive, and how old is it in business terms?

*What we wanted to know.* Which company we are valuing and where it sits in a business life cycle. Companies, like people, move from start-up to fast growth to maturity to decline, and the right behavior changes at each stage.

*Why it matters.* A young company should put its cash into growth. A mature one should hand spare cash back to its owners. If we misjudge the stage, we misjudge how much of the value comes from future growth, and every later forecast is off.

*What we did.* We looked at four things: how fast sales grow, how much profit the company keeps from each dollar of sales, how much it reinvests, and what it does with its cash. Sales growth is this year's sales divided by last year's, minus one. For Colgate, $20,382 million in 2025 divided by $20,101 million in 2024, minus one, is 1.4%. We also had to settle one judgment before anything else: what the company's yearly operating profit really is.

*The numbers and where they came from.* From the 2025 annual report (Form 10-K), filed 2026-02-23. File: `sources/filings/cl-10k-fy2025.txt`. Colgate sells toothpaste, soap, household cleaners and pet food. Net sales were $20,382 million. Operating income, meaning profit before interest and taxes, was reported at $3,306 million. That is after a $919 million write-down: an accounting charge that admits a business bought earlier, the Filorga skin care brand, is worth less than was paid. No cash left the company in 2025 for it. The company spent $2,703 million on advertising, $366 million on research and $564 million on plant and equipment, against $630 million of depreciation, the yearly charge for wearing out what was bought before. It bought one business, an Australian pet food maker, for $293 million. It paid shareholders $1,823 million in dividends and bought back $1,210 million of its own shares, $3,033 million in all. From the twelve-year file (`sources/filings/cl-multi-year-financials-fy2014-fy2025.tsv`): sales grew 3.3% a year from 2016 to 2025; operating income before write-downs grew 0.7% a year; Colgate spent $3,894 million buying businesses from 2018 to 2025 and wrote down $2,211 million over the same years, in 2021 ($571 million), 2022 ($721 million) and 2025 ($919 million). The model (`model-output.md`, sections 5 and 8) shows a return on invested capital of 34.56%, and $9,438 million returned to shareholders over three years against $8,204 million of free cash flow to equity (FCFE: the cash left for shareholders after reinvestment and debt payments).

*What we decided, and what we didn't.* Colgate is a mature company: slow growth, high profit margins, little reinvestment, and all its spare cash paid out. This is a judgment, but every measure points the same way. The second decision is the operating income we build on: $4,225 million, the reported $3,306 million plus the $919 million write-down. The reason is that the write-down is not a cost of running the business this year. We did not also remove the year's restructuring and lawsuit charges, as the company does to reach its own figure of $4,347 million, because Colgate books charges like those most years. And we did not let the write-downs disappear: the $2,211 million written off since 2021 is added back to the capital the company has invested, so that money spent on purchases that failed still counts when we measure returns. The alternative, ignoring the write-downs everywhere, would make management look better than its record.

*How sure we are.* High on the stage; the figures are disclosed. The operating income is a judgment with a clear range: $3,306 million as reported, $4,225 million as used, $4,347 million on the company's own basis. One thing does not fit the label "mature": the purchases. More than half the money spent on them, 57%, has been written down.

## Step 2: Who really controls Colgate-Palmolive?

*What we wanted to know.* Who sits on the board of directors, whose interests they serve, and who holds the power. Corporate governance means the system of who decides what in a company.

*Why it matters.* The course assumes managers work for shareholders. Where they do not, the company can sit on decisions that would raise its value, and a valuation should say whether anyone is in a position to force them.

*What we did.* We read the list of directors, the table of large shareholders and the pay plans, then the rules on what shareholders can do without the board's consent. We asked who could remove a director, who could block a takeover, and what management is paid for.

*The numbers and where they came from.* The 2026 proxy statement, filed 2026-03-25. File: `sources/filings/cl-def14a-2026.txt`. There are 10 nominees for the board. Nine are independent, meaning they have no job or business tie with the company. The tenth, Noel Wallace, is both chief executive and chairman. The independent nominees have served 8.1 years on average. The three largest shareholders are Vanguard with 10.26%, BlackRock with 8.18% and State Street with 5.95%; all three mainly run index funds, which buy every large company and do not pick among them. Directors and executives together own 0.43%. Capital IQ (`sources/capital-iq/public-ownership.tsv`) counts 2,356 institutions holding 87.19% of the shares, and the largest holder it tags as an activist, an investor who buys in to force change, owns 0.05%. Every director stands for election every year. Holders of 15% of the shares can call a special meeting. There is no poison pill (a device that makes a hostile takeover ruinously expensive). If the company were sold and Mr. Wallace then lost his job, he would receive about $45.3 million, which is 0.06% of the $78.5 billion the shares are worth. His 2025 pay was $16,478,196. Of the yearly bonus, 80% depends on sales growth and on earnings per share measured before special charges. The pay committee also restated a cash flow measure from 133.6% to 115.7% by leaving the write-down and a lawsuit charge out of the profit figure. A shareholder proposal to split the chairman's job from the chief executive's is on the 2026 ballot, and the board recommends voting against it.

*What we decided, and what we didn't.* Power sits with management, checked by a board that shareholders could replace in any year but never have reason to organize against. The formal rights are strong. The owners who hold them are index funds, which cannot sell and rarely campaign. The weak point is in what pay measures: the $919 million write-down reduced what shareholders own and did not reduce the bonus measure. We did not conclude the board is captured; nothing in the documents shows that.

*How sure we are.* High on who owns what and what the rules are; all of it is disclosed. Our files do not include how shareholders voted on past proposals, so we cannot say how close any challenge came.

## Step 3: What is Colgate-Palmolive trying to achieve, and has anything held it to account?

*What we wanted to know.* What goals management states, which measures it steers by, and whether markets, lenders or courts have ever forced a correction.

*Why it matters.* A goal is only useful if hitting it makes the company worth more. If sales growth is bought at too high a price, the company can hit its targets while its value stands still, and a forecast that copies the targets will be too high.

*What we did.* We read the stated objectives, then checked them against what happened to profit while sales grew. Then we listed the events that count as outside judgment on the company and looked at what shareholders earned.

*The numbers and where they came from.* The 2025 annual report, Item 1, says the company is "focused on driving organic sales growth; delivering consistent, compounded earnings per share growth; achieving operational efficiencies". Organic sales growth means growth with currency moves and purchased businesses taken out. In 2025 sales rose 1.4%: prices went up 2.1% and the number of units sold fell 0.4%, with currencies taking 0.3%. Operating income before write-downs was 24.0% of sales in 2017 and 20.7% in 2025. From 2016 to 2025 sales grew 3.3% a year and that operating income 0.7% a year. Files: `sources/filings/cl-10k-fy2025.txt` and `sources/filings/cl-multi-year-financials-fy2014-fy2025.tsv`. The events: three write-downs totalling $2,211 million; a lawsuit over pension payments settled for $332 million; and, from Capital IQ (`sources/capital-iq/credit-ratings.tsv`), a downgrade by the rating agency S&P on 2024-04-19 to A+. The proxy statement's performance table says $100 invested in Colgate at the end of 2020 was worth $104.0 at the end of 2025, against $111.8 in a group of similar companies. Our price file shows the S&P 500 returned 96.2% over those five years and Colgate 4.0%. Dividends rose to $2.06 a share in 2025 and the board authorized up to $5 billion of share buybacks. The stock closed at $98.71 on 2026-11-20; analysts' average target is $101.70.

*What we decided, and what we didn't.* Management aims at growth in sales and in earnings per share. Both are real measures, and over nine years they have not tracked value: sales grew more than four times as fast as operating profit. Growth in 2025 came from price alone. There has been no single day of reckoning, no scandal and no activist campaign. The correction has been slow and came from the stock market: five years of almost no return. We did not conclude that growth was bought with advertising, although advertising rose while margins fell; the filing does not say so, and two series moving together is not proof.

*How sure we are.* High on the figures. The reading that the targets have been met in ways that added little value is our interpretation. It matters later, because analysts expect profit margins to rise from here.

## Step 4: Who sets Colgate-Palmolive's share price, and does that investor spread their bets?

*What we wanted to know.* How many kinds of shares exist, who the biggest shareholders are, and who the marginal investor is: the buyer or seller whose trades set the price.

*Why it matters.* The return shareholders require depends on how risky the company looks to the investor who sets its price. An investor who owns hundreds of stocks cares only about risk that moves with the whole market, because the rest averages out. An investor with everything in one stock cares about all of it.

*What we did.* We counted the share classes, read the ownership tables, and asked whether the things that have hurt Colgate were its own troubles or the market's. We also ran a regression, a statistical comparison of Colgate's monthly returns with the market's, to see how much of its movement the market explains.

*The numbers and where they came from.* The proxy statement says there is one class of common stock with one vote a share. The quarterly report's cover shows 794.9 million shares. Institutions hold 87.19% and insiders 0.13% (Capital IQ, 2026-09-30). The annual report says Walmart buys about 11% of what Colgate sells, and that 454 lawsuits over talcum powder are pending. From the price file (`sources/market-data/cl-vs-sp500-monthly-2020-12-to-2026-11.tsv`): in 2022 the S&P 500 lost 18.1% and Colgate lost 5.4%. In the first twenty days of November 2026 the index fell 8.8% and Colgate rose 3.6%. Over sixty months the market explains 6.4% of the movement in Colgate's returns. Colgate's monthly returns swung 1.24 times as widely as the index's.

*What we decided, and what we didn't.* The marginal investor is a diversified institution. That follows from the ownership figures and is not a close call. So the right measure of risk is beta: how far a stock moves when the whole market moves. Colgate's own troubles (write-downs, lawsuits, one large customer) belong in the forecast of cash flows, not in the discount rate. We did not use a method that reads risk from the ratio of share price to book value, the accounting value of the shareholders' stake. Years of buybacks have cut that book value to $54 million, so the ratio says nothing about risk.

*How sure we are.* High. One point to carry forward: Colgate is not a calm stock. About 94% of its ups and downs are its own. A diversified owner does not bear that risk; anyone holding only Colgate would.

## Step 5: What return could an investor earn with no risk at all, in dollars, on the day we value Colgate?

*What we wanted to know.* The risk-free rate: the yearly return on an investment with no chance of default. Every other required return is this rate plus a reward for risk.

*Why it matters.* It is the base of the cost of equity, the return shareholders require. A one-point error here moves every discount rate by about a point.

*What we did.* We chose the currency first, because each currency has its own risk-free rate. Then we took that government's 10-year bond rate and subtracted the default spread, the extra yield investors demand in case the government does not pay. The rule is: risk-free rate equals government bond rate minus default spread. For the US dollar, 5.04% minus 0.22% is 4.82%.

*The numbers and where they came from.* Colgate reports in US dollars. About two-thirds of its sales are made outside the United States, in many currencies (annual report, note 14). The 10-year US Treasury bond yielded 5.04% at the close on 2026-11-19, from the Federal Reserve's public database (file: `sources/market-data/market-rates-2026-11-19.json`). The rating agency Moody's grades the United States Aa1, one step below its top grade, and Professor Damodaran's November figures put the default spread for that grade at 0.22%. At the start of November the Treasury rate was 4.94%, so it rose 0.10 points in three weeks. About 35.9% of Colgate's bonds are in euros.

*What we decided, and what we didn't.* The analysis is in US dollars and the risk-free rate is 4.82%. Dollars, because the company's accounts, the analysts' forecasts and the share price are all in dollars, and cash flows and discount rate must be in the same currency. Foreign sales do not change that: they reach us already converted, so a weak peso or lira shows up as lower reported sales. The alternative, valuing each region in its own currency, needs sales by currency, which the company does not publish. The euro bonds are a financing choice and do not change the currency of the valuation.

*How sure we are.* High. The rate is a market price read from a public source, with one published adjustment.

## Step 6: How much extra return do investors demand for owning stocks instead of risk-free bonds?

*What we wanted to know.* The equity risk premium: the extra yearly return investors expect from stocks as a whole, above the risk-free rate. It is the price of market risk.

*Why it matters.* The cost of equity is the risk-free rate plus the company's beta times this premium. A premium that is too low makes every future dollar look worth more than it is.

*What we did.* There are three ways to estimate it. A survey asks investors. A historical premium averages what stocks earned above bonds in the past. An implied premium works backward from today's share prices and expected cash flows to the return investors must be expecting. We chose the implied premium and compared it with the historical one.

*The numbers and where they came from.* The implied premium is 3.61%, from Professor Damodaran's November 2026 workbook, measured on 2026-11-01 with the S&P 500 at 7,580.07 (file: `sources/market-data/market-rates-2026-11-19.json`). The historical premium for 1928 to 2022 is 6.64% as a simple average, with a standard error (the typical size of the estimate's error) of 2.15%, and 5.06% as a compounded average, from the course's own spreadsheet. On 2026-11-20 the S&P 500 closed at 6,910.39, which is 8.8% lower than on the measurement date. Using the historical figures in place of 3.61% would raise Colgate's cost of capital (the blended return its lenders and shareholders require, built up over steps 5 to 12) from 8.34% to 10.35% or 9.31% (`module-1-cross-checks-output.md`, section 2).

*What we decided, and what we didn't.* We use 3.61%. It looks forward, it reflects what investors were paying for risk this month, and it is the figure the professor's own spreadsheets pair with a risk-free rate measured our way. The historical average lost because its error is too large: an estimate of 6.64% with a 2.15% standard error cannot tell 4% from 9%. No survey figure is in our files. The harder choice is the date. When share prices fall and expected profits have not changed, the implied premium goes up, so the premium on 2026-11-20 was higher than 3.61%. We kept the published figure and say so, because recomputing it needs inputs inside the professor's workbook that we do not have. The alternative was a rough adjustment. If nothing changed but the index level, the premium would be about 3.96% and the cost of capital 8.57%.

*How sure we are.* Moderate, and less sure than usual for this input. We know the direction of the error: our cost of capital is, if anything, too low, by up to about a fifth of a point. Each 0.25 points added to the premium adds about 0.17 points to the cost of capital.

## Step 7: Does where Colgate sells change the price of risk?

*What we wanted to know.* How much of Colgate's business is in riskier countries and what extra premium that adds. A company's risk comes from where it does business, not where its head office is.

*Why it matters.* For Colgate this is the largest single adjustment in the cost of capital. Ignoring it would treat sales in Argentina and Nigeria as if they were sales in Ohio.

*What we did.* We split sales into three groups, gave each an equity risk premium, and weighted the premiums by sales. The formula is: weighted premium equals the sum of each group's share of sales times its premium. With Colgate's numbers: 33.33% times 3.61%, plus 45% times 7.05%, plus 21.67% times 4.65%, is 5.38%.

*The numbers and where they came from.* The 2025 annual report, note 14, says approximately two-thirds of sales come from outside the United States and approximately 45% from emerging markets, meaning Latin America, Asia outside Japan, Africa and Eurasia, and Central Europe. That leaves 21.67% for other developed markets. Sales by region in 2025: Latin America $4,776 million, Asia Pacific $2,814 million, Africa/Eurasia $1,172 million. Professor Damodaran's January 2026 regional table (file: `sources/market-data/country-risk-regions-2026-01-01.md`) gives a country risk premium, the extra return for a region above a safe market, of 4.39% for Latin America, 1.49% for Asia, 4.26% for Africa and the Middle East and 1.04% for Western Europe. Weighting the first three by Colgate's sales gives 3.44% for its emerging markets, so 3.61% plus 3.44% is 7.05%. For other developed markets, 3.61% plus 1.04% is 4.65%. The two United States sales figures in note 14 add to $6,658 million, 32.67% of sales.

*What we decided, and what we didn't.* The weighted premium is 5.38%, against 3.61% if we had looked only at the head office. Without the adjustment the cost of capital would be 7.17%, not 8.34%. We measured exposure by sales because toothpaste and pet food are sold, and mostly made, where the customer lives, and sales are the only figure the company reports by region. We used Professor Damodaran's method of scaling each country's bond risk up by about 1.55, because shares are riskier than bonds; with unscaled figures the premium would be 4.75%. Both choices follow the course.

*How sure we are.* Moderate. The split rests on the company's rounded statements, and the emerging-market premium on regional averages, because Colgate does not publish sales by country. If emerging markets were 40% or 50% of sales, not 45%, the premium would be 5.21% or 5.55%. One question is left open for review: the professor's tables now add 0.22% for the United States itself, and depending on how that is read the premium would be 5.23% or 5.45%. We kept 5.38%, which lies between.

## Step 8: Can Colgate's own share-price history tell us how risky it is?

*What we wanted to know.* Colgate's regression beta: the slope found by comparing the stock's monthly returns with the market's. A beta of 1 means the stock moves with the market; below 1, less.

*Why it matters.* Beta multiplies the equity risk premium. For Colgate the choice of beta moves the cost of capital more than any other input, by about two points.

*What we did.* We compared sixty monthly returns on Colgate, with dividends, to the S&P 500 with dividends, from November 2021 to October 2026. We read four results: the beta, its standard error, the R-squared (the share of the stock's movement that the market explains) and the intercept, which shows whether the stock did better or worse than its beta predicts.

*The numbers and where they came from.* All from the price file (`sources/market-data/cl-vs-sp500-monthly-2020-12-to-2026-11.tsv`), computed by `module-1-cross-checks.py`. Beta 0.315. Standard error 0.158, so the range of two standard errors either side runs from 0.00 to 0.63. R-squared 0.064. Intercept 0.39% a month. Capital IQ shows a five-year beta of 0.31. Splitting the window in half gives 0.35 for the first thirty months and 0.25 for the last thirty. With a beta of 0.315 the cost of equity would be 6.51% and the cost of capital 6.31%. Colgate's cost of borrowing is 5.74% (step 12).

*What we decided, and what we didn't.* We report the regression beta and do not use it. Three reasons. The range is too wide: the data cannot rule out a beta of zero. The result describes one five-year stretch. And it fails a plain check: a cost of equity of 6.51% is only 0.77 points above what Colgate pays its lenders, yet shareholders are paid last and carry more risk. The alternative was to use 0.315, which would lower the cost of capital from 8.34% to 6.31%. The data is clean, with no merger or break in the series, so the low figure is not a data fault. Jensen's alpha, the intercept adjusted for the risk-free rate, comes to about 0.17% a month using today's short-term rate of 3.88% for the whole period; that is an estimate, because monthly short-term rates for the window are not in our files.

*How sure we are.* Sure that 0.315 is what the last sixty months show; the figure matches Capital IQ. Not willing to build on it. Step 10 explains the gap between this figure and the one we use.

## Step 9: From what Colgate sells and how it is run, should its risk be high or low?

*What we wanted to know.* What beta the business itself suggests, from three things: whether customers can do without the product, how much of the cost base is fixed, and how much the company has borrowed.

*Why it matters.* A beta taken from statistics should make sense as a description of the business. If the story and the number disagree, one of them is wrong.

*What we did.* We looked at the product mix, the cost structure and the debt. For debt there is a formula: levered beta (the beta of the shares) equals unlevered beta (the beta of the business with no debt) times one plus the after-tax ratio of debt to equity. With Colgate's numbers: 0.6796 times (1 plus 0.75 times 0.1030) is 0.7321.

*The numbers and where they came from.* The 2025 annual report, note 1: oral care is 44% of sales, personal care 17%, home care 16% and pet nutrition 23%. Gross profit, sales less the cost of making the products, is 60.1% of sales. Advertising is 13.3% of sales. In the 24 months of the last sixty in which the index fell, it lost 3.28% on average and Colgate lost 0.80%. Debt is $8,084.0 million and the shares are worth $78,466.6 million, a ratio of 0.1030; the tax rate is 25% (`model-output.md`, section 1). The 110 US household products companies in Professor Damodaran's January 2026 data have an average unlevered beta of 0.7411; the whole market's is 0.7557 (file: `sources/market-data/industry-betas-2026-01-05.json`).

*What we decided, and what we didn't.* Everything points to below-average risk. People keep buying toothpaste, soap and pet food in a recession. The biggest overhead, advertising, is a choice that can be cut in a bad year. Borrowing is light: it adds 0.0525 to the beta, 7.2% of the total. We did not put a separate number on fixed costs; they are part of the business beta and cannot be split out from the published figures.

*How sure we are.* Good on the direction, moderate on the size. The story says Colgate should sit a little below its industry's average, because that average includes many small makers of cosmetics and specialty goods. It does not support a figure as low as 0.315.

## Step 10: What is the right beta for Colgate's two businesses?

*What we wanted to know.* The bottom-up beta: a beta built from the average of many companies in the same businesses, not from Colgate's own share price.

*Why it matters.* This is the beta that goes into the cost of capital. Used across decades of cash flows, the difference between 0.315 and 0.73 is the largest judgment in this part of the valuation.

*What we did.* We split Colgate into its two reported businesses, gave each the unlevered beta of its industry, and weighted by sales: 77.37% times 0.7411, plus 22.63% times 0.4694, is 0.6796. With Colgate's debt added (step 9) the beta of the shares is 0.7321. Then we asked why this is more than twice the regression's 0.315.

*The numbers and where they came from.* The 2025 annual report: Oral, Personal and Home Care had sales of $15,769 million and Hill's Pet Nutrition $4,613 million. Professor Damodaran's January 2026 industry data: Household Products, 110 companies, unlevered beta 0.7411; Food Processing, 78 companies, 0.4694. From the regression (step 8): the gap between 0.7321 and 0.315 is 0.42, or 2.6 standard errors. Colgate's returns were 1.24 times as volatile as the index's, and their correlation with it, a measure of how closely two things move together, was 0.25. In the 36 months the index rose it gained 3.94% on average and Colgate gained 1.74%. Over five years to December 2025 the index returned 96.2% and Colgate 4.0%.

*What we decided, and what we didn't.* We use the bottom-up beta, 0.6796 unlevered and 0.7321 with debt. For Hill's we use the food industry's figure. Pet food is packaged food, made and sold like other packaged food, and the listed owners of large pet food brands are food companies; the professor's table has no pet food industry of its own. The alternative was to give the whole company the household products figure, which would raise the cost of capital from 8.34% to 8.67%.

The gap from the regression needs explaining, because 2.6 standard errors is more than chance. Our reading is this. The regression did not find that Colgate is a safe stock; it found that Colgate's swings, which were larger than the market's, had little to do with the market's. A beta is roughly volatility times correlation, and here the correlation was 0.25. That is a fact about these five years as much as about Colgate: the market nearly doubled while Colgate went sideways. The price file cannot tell us what drove the market, so we do not name causes. A cost of capital has to hold for decades, and one unusual stretch is a poor guide to that. The bottom-up figure has its own error, in the other direction: it averages 110 companies, most of them smaller and selling less essential goods than Colgate, so it probably overstates Colgate's risk.

*How sure we are.* Moderate. We are confident 0.315 is too low to use and that 0.73 is, if anything, a little high. An honest range for the beta of the shares is 0.63, the top of the regression's range, to 0.80, the all-household-products figure. That puts the cost of capital between 7.84% and 8.67%, around the 8.34% we use. Each business also deserves its own rate: about 8.67% for household and personal products and 7.24% for pet food.

## Step 11: Does the beta need adjusting for who owns Colgate?

*What we wanted to know.* The final beta of the shares at Colgate's level of debt, and whether to use total beta instead: a larger figure that counts all of a company's risk, for an owner who holds nothing else.

*Why it matters.* For an owner with everything in one company, the market beta understates the risk they carry, and the required return would be much higher.

*What we did.* We took the beta from step 10 and computed the cost of equity. The formula is: cost of equity equals risk-free rate plus beta times equity risk premium. With Colgate's numbers: 4.82% plus 0.7321 times 5.38% is 8.76%. Then, as an illustration only, we computed the total beta.

*The numbers and where they came from.* Risk-free rate 4.82% (step 5), weighted premium 5.38% (step 7), beta 0.7321 (step 10); the result is in `model-output.md`, section 1. Institutions hold about 87% of the shares (step 4). Total beta is the stock's volatility divided by the market's, 1.24, and the cost of equity at that beta would be 11.50% (`module-1-cross-checks-output.md`, section 2).

*What we decided, and what we didn't.* The cost of equity is 8.76%, using the market beta. This is arithmetic once the beta is chosen. We did not use total beta, because the investors who set Colgate's price are diversified. The gap between 8.76% and 11.50% is what it would cost to hold Colgate as an only asset; nobody who sets the price does. We also did not widen the comparison group to companies outside the United States: 110 and 78 US companies are enough, and no global industry figure is in our files.

*How sure we are.* As sure as we are of the beta in step 10; this step adds no new judgment.

## Step 12: How much does Colgate really owe, and what does it pay to borrow?

*What we wanted to know.* The company's total debt and the interest rate it would pay to borrow today.

*Why it matters.* Debt sets the weights in the cost of capital and is subtracted from the company's value to find what the shares are worth. The interest rate is the cost of the borrowed part.

*What we did.* The course's test: a commitment is debt if the payments are fixed, they are tax-deductible, and missing them can cost the owners control. We tested each item that looked like debt, and valued the debt at what it is worth in the market today, not at the amount on the balance sheet. For the interest rate there are two routes. An agency rating, a grade from a firm such as S&P, comes first if one exists. The other is a synthetic rating: operating income divided by interest expense, called interest coverage, matched to a table of grades. Each grade carries a spread, the extra interest a borrower of that grade pays above the government bond rate. For Colgate: 5.04% plus 0.70% is 5.74%.

*The numbers and where they came from.* The 2025 annual report, notes 6, 7, 10, 13 and 15. The balance sheet carries debt of $7,988 million. Its fair value, what the market would pay for it, is $7,518 million, which is $470 million or 5.9% less, because most of it was borrowed at lower rates than today's: the average coupon is 2.9%. Lease liabilities, the value of rent the company is committed to pay, are $566 million. Pension and retiree plans are short of what they have promised by $1,283 million. Contracts to buy materials and services total $637 million. Interest expense was $267 million. From Capital IQ: S&P rates Colgate A+ with a stable outlook. From Professor Damodaran's January 2026 table (file: `sources/market-data/ratings-spreads-2026-01-01.json`): an A+ borrower pays a spread of 0.70% and an AAA borrower, the top grade, 0.40%. From the model (`model-output.md`, section 2): operating income of $4,225 million covers interest 15.82 times, which the table grades AAA, giving 5.44%.

*What we decided, and what we didn't.* Total debt is $8,084 million: $7,518 million of borrowings at market value plus $566 million of leases. We left out the pension shortfall, which the course does not count as debt at this step; it will be considered when we move from the value of the business to the value of the shares. We left out the $637 million of purchase contracts by judgment: they pay for goods the company will use, and missing one is a contract dispute, not a default. Counting them would raise debt by 7.9% to $8,721 million.

For the interest rate we use the actual rating, 5.74%, and not the synthetic 5.44%. The course's rule is to use a real rating when there is one. Here the agency also sees what one ratio cannot. The coverage figure is flattered by old, cheap debt: at today's rate the interest bill would be about $464 million and coverage 9.11 times. Colgate pays out everything it earns and has almost no accounting equity left. And S&P's last recorded move was downward. S&P's own reasons are not in our files, so that explanation is our inference. After tax, at 25%, the cost of debt is 4.30%.

Putting the pieces together: the shares are 90.66% of the company's value and cost 8.76%; debt is 9.34% and costs 4.30% after tax. The cost of capital is 8.34%.

*How sure we are.* High on the debt and its cost; the fair value and the rating are disclosed. The choice between the two ratings changes the cost of capital only from 8.34% to 8.32%, because debt is so small a part of the total. The real uncertainty in the 8.34% is elsewhere: the beta (7.84% to 8.67%, step 10) and the date of the equity risk premium (up to 8.57%, step 6).

## Step 13: How much of Colgate is paid for with borrowed money, and what does the whole mix cost?

*What we wanted to know.* The shares of Colgate's funding that come from lenders and from shareholders, and the blended cost of the two. We also wanted a separate rate for each of its two businesses.

*Why it matters.* The blended rate, the cost of capital, is the bar every investment has to clear and the rate used later to value the company. Wrong weights give a wrong bar.

*What we did.* We weighted debt and shares by what they are worth in the market today, not by the amounts on the balance sheet (book value). The formula is: cost of capital = share of equity × cost of equity + share of debt × after-tax cost of debt. With Colgate's numbers: 90.66% × 8.76% + 9.34% × 4.30% = 8.34%. Then we ran the same formula with balance-sheet weights to see how much the choice matters. For the two businesses, we gave each its own beta (the measure of risk from step 10) and, as a judgment, the same share of debt as the company.

*The numbers and where they came from.* Debt of $8,084 million (step 12) and shares worth $78,466.6 million (794.9 million shares at $98.71) make a company worth $86,550.6 million; the file is `model-output.md`, section 1. On the balance sheet in the 2025 annual report, debt with leases is $8,554 million and shareholders' equity is $54 million. Industry debt levels are from Professor Damodaran's January 2026 data: 15.36% for household products and 30.43% for food processing. The calculations beyond the model are in `modules-2-4-cross-checks-output.md`, section 1.

*What we decided, and what we didn't.* Debt is 9.34% of Colgate and equity 90.66%; the cost of capital is 8.34%. This is arithmetic once the inputs from steps 5 to 12 are set. We did not use balance-sheet weights. On those, debt would be 99.37% of the total and the cost of capital 4.33%, about four points too low. Years of buying back shares have shrunk the accounting equity to almost nothing, while the market values the shares at about 1,453 times that figure. Leases barely matter: without them debt would be 8.74% of the company. For the two businesses the rates are 8.67% for oral, personal and home care and 7.24% for pet food. We also tried splitting the debt the way each industry borrows, scaled to Colgate's total; the rates came out at 8.69% and 7.17%, almost the same, so we kept the simpler split.

*How sure we are.* High on the weights; both are market values read from documents. The two business rates rest on the step 10 judgment that pet food is as risky as food processing.

## Step 14: Does Colgate earn more on its investments than they cost?

*What we wanted to know.* The return Colgate earns on the money invested in its business, and whether that return beats the 8.34% cost of capital (step 13).

*Why it matters.* A company creates value only when its investments earn more than the money costs. This comparison also decides, later, how much future growth is worth.

*What we did.* Return on invested capital is after-tax operating income divided by invested capital, the money put into the business by lenders and shareholders and not sitting in cash. With Colgate's numbers: $3,168.8 million ÷ $9,169 million = 34.56%. Two judgment calls sit inside that. Operating income leaves out the $919 million write-down of 2025, because no cash was spent in 2025. But we added that write-down, and the two before it, back to invested capital, because the money was spent and lost. We also traced operating income to cash: after-tax operating income of $3,168.8 million, plus depreciation of $630 million, less plant spending of $564 million, plus $344 million released from working capital (the cash tied up in stock and unpaid bills), gives $3,578.8 million of free cash flow.

*The numbers and where they came from.* Operating income of $4,225 million before the write-down, taxed at 25%: the 2025 annual report. Invested capital of $9,169 million: accounting equity of $365 million, plus debt of $7,988 million, less cash of $1,395 million, plus write-downs of $571 million (2021), $721 million (2022) and $919 million (2025), $2,211 million in all, from the twelve-year data file. The results are in `model-output.md`, section 8, and the alternatives in `modules-2-4-cross-checks-output.md`, section 2.

*What we decided, and what we didn't.* Colgate earns 34.56% against a cost of 8.34%, a gap of 26.22 points. We did not use the higher figure that results from letting written-off money drop out of the count, 45.54%; that would reward failed purchases. We did not use reported operating income either, which gives 27.04%. We did not use return on equity, profit divided by accounting equity: with equity of $54 million it comes out at 3,948%, which says nothing about the business. Invested capital would have to be 4.1 times larger before the return fell to the cost of capital, so no adjustment reverses the conclusion.

*How sure we are.* High that returns far exceed the cost; every definition says so, from 27.04% to 52.40%. Less sure of the level. One caution matters later: 34.56% is what the existing brands earn. New money has done worse. Colgate spent $3,894 million buying businesses from 2018 to 2025, and the write-downs over those years come to 57% of that.

## Step 15: What does a typical Colgate investment look like, and how fast can the company grow forever?

*What we wanted to know.* The pattern of cash a typical project produces, which past costs to ignore when judging a new one, and the highest growth rate we may assume lasts forever.

*Why it matters.* Most of the value of a long-lived business sits in the years beyond any forecast. The growth rate assumed for those years moves the answer more than almost any other input.

*What we did.* We sorted Colgate's spending into three kinds: support for existing brands, plants, and purchases of other businesses. For the growth ceiling we used the course's rule: no company can grow faster than the economy forever, and the risk-free rate, 4.82% (step 5), stands in for the economy's long-run growth.

*The numbers and where they came from.* The 2025 annual report: advertising $2,703 million, research $366 million, plant spending $564 million, cash from operations $4,198 million. The twelve-year data file: sales grew 3.3% a year from 2016 to 2025. Capital IQ: analysts expect sales to grow 2.33% in 2027 and 3.46% in 2028, and earnings per share to grow 5.45% a year.

*What we decided, and what we didn't.* A typical project is small beside the company, paid for from the year's cash, and lasts a long time: a little spending up front, heavy advertising at launch, then years of steady cash. Purchases of businesses are the exception: the whole price is paid on day one. Money already lost is a sunk cost, meaning it is spent and cannot be recovered, so it stays out of any decision about what to do next. That applies to the $2,211 million of write-downs. For growth forever we use 3%, a judgment. The ceiling of 4.82% lost because Colgate has grown about 3% a year for a decade. We did not use the analysts' 5.45%: that is a few years of earnings per share, lifted by share buybacks, not a rate that can last forever.

*How sure we are.* Moderate. Colgate does not publish cash flows project by project, so the description is our reading of its filings. The 3% is a judgment between about 2% and 4.82%.

## Step 16: Do Colgate's foreign businesses need a different rate, and should it protect itself against currency swings?

*What we wanted to know.* What currency to value the foreign businesses in, what return to demand from them, and whether the hedging Colgate does, meaning contracts that offset a risk, is worth its cost.

*Why it matters.* About two-thirds of Colgate's sales are outside the United States. A single rate for everything would be too high for the safest markets and too low for the riskiest.

*What we did.* We kept everything in US dollars, as Colgate reports. For each region we added that region's country risk premium (step 7) to the 3.61% premium for a mature market (step 6) and recomputed the cost of capital. For Latin America: 3.61% + 4.39% = 8.00%, which gives a cost of capital of 10.56%. We then listed what Colgate hedges and applied the course's test: hedge only if shareholders cannot spread the risk more cheaply themselves.

*The numbers and where they came from.* Regional premiums from Professor Damodaran's January 2026 table (file: `sources/market-data/country-risk-regions-2026-01-01.md`). Hedges from the 2025 annual report, note 7: currency contracts of $3,535 million, foreign-currency borrowing of $3,942 million set against investments abroad, and commodity contracts of $16 million. The report also says a one-point rise in interest rates would add $7 million to interest. Regional rates are in `modules-2-4-cross-checks-output.md`, section 3.

*What we decided, and what we didn't.* A dollar valuation throughout. The household products business should clear 7.38% in North America, 8.14% in Europe, 8.46% in Asia Pacific, 10.47% in Africa and Eurasia and 10.56% in Latin America. Pet food, sold mostly in the United States, should clear about 6.43%. This is arithmetic on earlier steps. On hedging, a judgment: Colgate's practice is about right. Its owners are large funds holding 87% of the shares, already spread across currencies. Colgate hedges where it is cheap, with contracts of 12 months or less and by borrowing in foreign currencies, and otherwise raises prices. We did not redo the valuation in a foreign currency. Done consistently it gives the same answer, and inflation forecasts by country are not in our files.

*How sure we are.* High on what is hedged; it is disclosed. Moderate on the regional rates, which use regional averages. The cost of the hedging is not disclosed, so "worth it" is a judgment from its small size.

## Step 17: Weighing the good and bad of debt, does Colgate have too much or too little?

*What we wanted to know.* What kinds of financing Colgate uses, and whether, from the general pros and cons of borrowing, it looks over- or under-borrowed. No formula yet; that comes in step 18.

*Why it matters.* Debt is cheaper than equity because interest is deducted before tax. Too little wastes that saving. Too much risks ruin.

*What we did.* We listed Colgate's financing, then went through the course's five factors: the tax saving, the discipline debt puts on managers, the cost of bankruptcy, conflicts between lenders and owners, and the value of keeping room to borrow later. We also tracked the debt share over six years.

*The numbers and where they came from.* The 2025 annual report: notes of $7,767 million at an average interest rate of 2.9%; short-term borrowing, called commercial paper, of $147 million at year end but $1,611 million on an average day; unused bank credit of $3,641 million; no bonds that convert into shares. Tax rate 25%. The proxy statement: directors and executives own 0.43% of the shares. From `modules-2-4-cross-checks-output.md`, section 5: debt was 10.14% of the company's value at the end of 2020, 12.40% in 2022 and 11.90% in 2025.

*What we decided, and what we didn't.* Colgate uses plain debt and plain shares, nothing in between, which suits a company with steady cash. On the five factors: the tax saving is real and little used. Today's debt saves $66.8 million of tax a year, worth $2,021 million if it continues forever. Discipline would help: managers own little and wrote down 57% of what they spent on purchases. Bankruptcy is remote: operating income covers interest 15.82 times, and since 2016 it has never fallen more than 7.4% in a year. Lenders already lend on good terms. And Colgate needs little room in reserve. All five point one way: too little debt. This is a judgment, but not a close one. It is not a legacy of any owner; no family or buyout firm is involved.

*How sure we are.* High on the direction. This step cannot say how much more debt. Two facts argue for care: Colgate's main assets are brands, which cannot be sold piece by piece, and about 45% of sales come from emerging markets.

## Step 18: What level of debt would make Colgate's money cheapest?

*What we wanted to know.* The debt level at which the cost of capital is lowest. The course calls it the optimal debt ratio.

*Why it matters.* A lower cost of capital makes the same business worth more. But past a point, more debt raises the cost of everything.

*What we did.* We recomputed the cost of capital at each debt level from 0% to 70% of the company's value. More debt makes the shares riskier, so the cost of equity rises. More debt also means more interest, lower interest coverage, a lower credit rating and a higher borrowing rate. At 30% debt, in our model: cost of equity 9.65%, borrowing rate 6.15%, cost of capital 8.14%. We did this twice: in Professor Damodaran's spreadsheet for this purpose, and in the course model.

*The numbers and where they came from.* Operating income $4,225 million, company value $86,550.6 million, beta before debt 0.6796, tax rate 25%, and the January 2026 table of ratings and borrowing rates. The model's results are in `model-output.md`, section 3; a finer version, one percentage point at a time, is in `modules-2-4-cross-checks-output.md`, section 6. The spreadsheet's results are in `professor-spreadsheet/results.md`.

*What we decided, and what we didn't.* Both tools say 30%, against 9.34% today. Reaching it would take $17,881 million of new debt, for $25,965 million in all. The spreadsheet puts the cost of capital there at 8.09% with a rating of A−; the model says 8.14% and BBB, one grade lower. We found why. The spreadsheet leaves the $267 million of interest on today's debt unchanged and charges the new rate only on new debt: $1,327 million of interest, covered 3.18 times. The model charges the new rate on all of it: $1,597 million, covered 2.65 times. The spreadsheet describes the first years; the model, where things settle. We use the model's more cautious figures for detail.

The shape matters more than the lowest point. From no debt to 30%, the cost of capital falls only from 8.48% to 8.14%. Just past 30% it turns up sharply: at 31% the rating falls below investment grade, the line under which many lenders will not lend, and at 40% the cost of capital is 10.56%. The model shows 26% and 30% tied at 8.14%.

*How sure we are.* High that the best level is well above 9.34%. Not sure it is 30% and not 25%: the curve is nearly flat there. And 30% takes no account of a warning sign: at today's debt the table grades Colgate AAA, while S&P grades it A+, two steps lower.

## Step 19: What is more debt worth to shareholders, and how far should Colgate really go?

*What we wanted to know.* The gain in value from moving to the best debt level, and the level we would recommend once real-world limits are counted.

*Why it matters.* The gain tells us whether the change is worth the trouble. The limits tell us how much of it is safe to take.

*What we did.* The yearly saving is the fall in the cost of capital times the company's value. Its worth is that saving divided by the cost of capital less growth. With Colgate's numbers in the model: (8.32% − 8.14%) × $86,550.6 million = $157.5 million a year; $157.5 million ÷ (8.14% − 3%) = $3,064.4 million, or $3.86 a share. Then we tested what happens if operating income falls after the borrowing is done.

*The numbers and where they came from.* The model: `model-output.md`, sections 3 and 4. The professor's spreadsheet (`professor-spreadsheet/results.md`): value per share rising from $98.71 to $106.01, a gain of $7.30. Stress tests and debt compared with EBITDA (operating income before depreciation, $4,855 million): `modules-2-4-cross-checks-output.md`, section 6. History of operating income: `professor-spreadsheet/macro-sensitivity-output.md`.

*What we decided, and what we didn't.* The full move to 30% is worth between $3.86 and $7.30 a share. The spreadsheet's figure is higher because it keeps old cheap interest and grows the saving at 4.27% a year, not 3%. We treat $3.86 as the central figure. No new value is created in the business; the gain is tax not paid, and it goes to shareholders.

We recommend 20%, not 30%. This is a judgment. At 30%, a 10% fall in operating income would take the rating to BB, below investment grade; a 20% fall, to B. Falls of that size have happened: 7.4% in 2022 and 21.6% in 2015. At 20% debt the rating stays A− even with income 20% lower. Debt at 30% would be 5.35 times EBITDA; at 20% it is 3.57 times, against 1.67 today. And real rating agencies have been two steps stricter than the table. Stopping at 20% costs little: the cost of capital is 8.22%, not 8.14%, and the gain is $1,798.5 million, or $2.26 a share, 56.9% of what 30% offers. It needs $9,226 million of new debt, for $17,310 million in all. The alternative, about 25%, captures 91.8% of the gain but falls to BB+ if income drops 20%.

*How sure we are.* High that Colgate should borrow more. Moderate on 20%; it depends on how much a strong rating in a bad year is worth, which is partly preference. Colgate's loan conditions are not disclosed in detail, so we could not test them.

## Step 20: Is there anything about Colgate's business that should change the debt answer?

*What we wanted to know.* Whether Colgate's earnings swing with the economy, whether a weaker credit rating would itself hurt the business, and what explains why its best debt level is 30% and not higher.

*Why it matters.* The method in step 18 assumes operating income stays the same whatever the debt. If borrowing scares off customers or suppliers, the true best level is lower.

*What we did.* We checked ten years of operating income for swings. We asked who would behave differently if Colgate's rating fell. And we set Colgate against the four things that drive how much debt a company can carry: its tax rate, its earnings relative to its value, the risk of its business, and the price of debt relative to equity.

*The numbers and where they came from.* Operating income before write-downs, 2016 to 2025: between $3,554 million and $4,268 million (`professor-spreadsheet/macro-sensitivity-output.md`). Walmart is about 11% of sales (2025 annual report). Operating income is 4.88% of the company's value and EBITDA 5.61% (`modules-2-4-cross-checks-output.md`, section 5). Figures for ten similar companies are from Capital IQ and use its definitions; the list of comparison companies is not final.

*What we decided, and what we didn't.* Colgate is not cyclical; no adjustment for swings is needed beyond the stress test in step 19. A weaker rating would cost it little in sales: nobody checks a credit rating before buying toothpaste. It could cost something with suppliers and in short-term borrowing: working capital released $344 million of cash in 2025, most of it from bills not yet paid, and suppliers to a weaker company ask to be paid sooner. S&P's downgrade in 2024 did no visible harm: operating income rose from $3,984 million to $4,268 million. So we made no deduction, and we count this as one more reason to stop short of 30%. On the four drivers, three favor debt. The fourth holds it down: investors pay a high price for Colgate's earnings, so 30% of its value is a great deal of debt for those earnings to carry. Among the ten Capital IQ companies the richly priced ones borrow least, as Colgate does: its net debt is 7.2% of value against a middle figure of 17.6%. The questions about family groups and private ownership do not apply; Colgate is neither.

*How sure we are.* High that Colgate is not cyclical. Moderate on the cost of a weaker rating: Colgate has never been near trouble, so there is little evidence either way.

## Step 21: Does a second method, and the industry, agree about the debt?

*What we wanted to know.* Whether a different way of finding the best debt level gives the same answer as step 18, and how Colgate's debt compares with its industry's.

*Why it matters.* Two methods that agree deserve more trust. If they disagree, one is hiding a weak assumption.

*What we did.* The second method is called adjusted present value. The formula is: value = value with no debt + tax saving from debt − expected cost of bankruptcy. The tax saving is the tax rate times the debt. The expected cost is the chance of default at each credit rating times the loss if it happens. With Colgate's numbers at 30% debt: $84,538.5 million + $6,491.3 million − $956.1 million = $90,073.6 million. The chance of default comes from a table by Professor Altman of NYU, used in the lecture; a BBB rating has defaulted 7.54% of the time over ten years. The loss in bankruptcy is a judgment: we used 15% of the company's value.

*The numbers and where they came from.* The model, `model-output.md`, section 9, and `modules-2-4-cross-checks-output.md`, section 6b for other bankruptcy costs. The lecture slides give direct bankruptcy costs as 5% to 10% of value. Industry debt levels are from Professor Damodaran's January 2026 data, and company comparisons from Capital IQ.

*What we decided, and what we didn't.* The second method also says 30%, with a gain of $3,596.7 million, or $4.52 a share. We chose 15% for the bankruptcy loss because shoppers keep buying staples from a company in trouble and the brands would keep their worth under a new owner. We tested other values: at 10% the best level is 34%, and at 25% or 40% it is 26%. So the answer stays between 26% and 34% whatever we assume. The industry is lower: 15.36% for household products, 30.43% for food processing, and 18.77% when weighted by Colgate's mix. All three views say Colgate's 9.34% is too low. Our recommended 20% (step 19) sits close to the industry figure. By this method, moving to 20% is worth $2,072.0 million.

*How sure we are.* High on the direction: three approaches agree. But the two calculated methods share the same ratings table, so they are not independent, and Colgate's closest equals (Procter & Gamble, Kimberly-Clark, Church & Dwight) borrow as little as it does. The 15% is reasoned, not observed.

## Step 22: Should Colgate change its debt quickly, slowly, or not at all?

*What we wanted to know.* Whether anything forces Colgate to act, whether it has good uses for borrowed money, and the best route from 9.34% debt to the 20% we recommend (step 19).

*Why it matters.* A right target reached the wrong way can destroy more value than it adds, for instance by borrowing to buy businesses that then fail.

*What we did.* We followed the course's three questions. Is the company under- or over-borrowed? Is it under threat, from a buyer if it has too little debt or from bankruptcy if it has too much? Does it have good projects? Under-borrowed companies under threat should act fast; those with good projects should borrow to invest; the rest should borrow gradually and hand the money to shareholders.

*The numbers and where they came from.* Shares worth $78.5 billion (step 13). The 2026 proxy statement and Capital IQ: no takeover defenses of the usual kinds, and the largest activist investor owns 0.05%. The price file: over five years to December 2025 Colgate's shares returned 4.0% and the S&P 500 index 96.2%. The 2025 annual report: a buyback program of up to $5 billion approved in March 2025; $1,210 million of shares bought in 2025; $3,033 million returned to shareholders in all.

*What we decided, and what we didn't.* Colgate is under-borrowed. It is not under threat of being bought: it is too large, and a buyer could not load it with debt (step 18). An activist campaign is possible, given the weak share returns, but none is visible. Its existing business earns 34.56% (step 14), but it has few new places to put money: plant spending runs below depreciation, and its purchases were followed by write-downs equal to 57% of what was spent. So we recommend borrowing gradually and buying back shares: $9,226 million over five years, about $1,845 million a year, 61% of what Colgate already returns each year. We would leave the regular dividend alone. We rejected a single large borrowing, because nothing forces speed and a slow pace lets Colgate stop if rating agencies react badly. We rejected investing the money, because of the record on purchases. Doing nothing leaves between $2.26 and $3.86 a share with the tax authorities.

*How sure we are.* Moderate. The route is a recommendation, not a calculation. It is worth 2% to 4% of the share price: worth having, not urgent. A large purchase, a lasting fall in income, or a harsh response from S&P would each change it.

## Step 23: What kind of debt suits Colgate, and is that what it has?

*What we wanted to know.* The best design for Colgate's debt (how long, fixed or floating interest, which currencies) and how its actual debt compares.

*Why it matters.* Debt whose payments rise and fall with the business is safer, so a company can carry more of it. Debt that moves the wrong way adds risk for no reward.

*What we did.* We reasoned from the business first, then checked against numbers. Professor Damodaran's spreadsheet for this gives, by industry, how sensitive companies' values and incomes are to interest rates, the economy, inflation and the dollar. We also ran the same tests on Colgate's own history. Duration is the measure for interest rates: roughly, how many years of cash flow the value rests on.

*The numbers and where they came from.* `professor-spreadsheet/macro-sensitivity-output.md`. Industry figures, weighted by Colgate's two businesses: duration 4.78 years, sensitivity to the economy 0.96. They are old, from 1987 to 1997, and pet food is not listed, so a neighboring industry stands in. Colgate's own results (9 to 11 yearly observations) are not statistically significant: none is as large as 1.3 times its own margin of error. Actual debt, from 21 rated notes totaling $6,869 million on Capital IQ: average time to repayment 9.6 years, 90.5% at fixed rates, 64.1% in dollars and 35.9% in euros. Sales by region are from the 2025 annual report.

*What we decided, and what we didn't.* Because the numbers are weak, the reasoning carries the conclusion, as the professor's project checklist advises. Colgate's brands last for generations and its cash arrives steadily, so its debt should be plain, fixed-rate and medium to long. It can raise prices (up 2.1% in 2025), but over ten years sales grew 3.3% a year and operating income 0.7%, so profit has not kept up with inflation; that argues against floating-rate debt. Two-thirds of sales are abroad, so most debt should not be in dollars. Colgate's actual debt matches on type, rate and length. It misses on currency: the United States is 32.67% of sales but dollars are 64.1% of the notes, and no note is in an emerging-market currency, though about 45% of sales come from there. Colgate does set $3,942 million of foreign-currency borrowing against its foreign businesses, which narrows the gap by an amount we cannot measure. The fix is to issue the new debt from step 22 outside the dollar. We would not replace the existing notes: they cost 2.9%, well below today's rates.

*How sure we are.* Moderate, lower than most steps. The industry data is about thirty years old and Colgate's own tests show nothing reliable. The conclusions rest on what the business is.

## Step 24: How much has Colgate paid its shareholders over five years?

*What we wanted to know.* The dividends (cash a company pays its shareholders) Colgate paid each year from 2021 to 2025, and how they compare with its profit and its share price.

*Why it matters.* The next steps ask whether Colgate pays too much or too little. The record comes first. Companies rarely cut dividends, so the history shows what shareholders have come to expect.

*What we did.* Two measures. The payout ratio is dividends divided by net income, the share of profit paid out. For 2025: $1,823 million ÷ $2,132 million = 85.51%. The dividend yield is the dividend per share divided by the share price. Today: $2.08 ÷ $98.71 = 2.11%. We also counted buybacks, where a company returns cash by buying its own shares.

*The numbers and where they came from.* The twelve-year data file from the SEC: dividends of $1,679 million, $1,691 million, $1,749 million, $1,789 million and $1,823 million for 2021 to 2025, and buybacks of $1,320 million, $1,308 million, $1,128 million, $1,739 million and $1,210 million. Dividends per share, from Capital IQ and the 2025 annual report: $1.79 rising to $2.06. The table is in `modules-2-4-cross-checks-output.md`, section 9.

*What we decided, and what we didn't.* Colgate paid $8,731 million in dividends over five years and bought back $6,705 million of shares, $15,436 million in all, about $3 billion every year. The dividend is regular and rises a little each year, 3.6% a year per share. The payout ratio was 77.46% over the five years, and between 61.92% and 94.73% in single years. The swings come from profit, not the dividend: 2022 and 2025 are write-down years. Before the 2025 write-down, that year's payout was 62.3%. Counting buybacks, Colgate returned 136.9% of its net income. That is possible without borrowing because write-downs cut profit but not cash. All of this is arithmetic. One reading note: the annual report shows $2.48 a share declared in 2024 and $2.08 in 2025 only because five dividends were declared in 2024 and four in 2025; the amount paid per share rose.

*How sure we are.* High. Every figure is disclosed. The yearly yields, 2.10% to 2.61%, use December prices, not the price on each payment date.

## Step 25: Should Colgate be paying dividends at all, and why does it?

*What we wanted to know.* The benefits and costs to Colgate of paying dividends, and whether it should pay high, low or none.

*Why it matters.* A dividend is a promise that is painful to break. Paying the wrong amount, or in the wrong form, costs shareholders either tax or flexibility.

*What we did.* We looked at who owns Colgate and how they are taxed, because tax is the main cost of a dividend. Then we went through the course's list of reasons companies pay dividends and marked which apply.

*The numbers and where they came from.* Capital IQ: institutions hold 87.19% of the shares. Professor Damodaran's January 2026 industry table: the average for household products companies is 42.96% (file: `professor-spreadsheet/originals/divfund.xls`). The 2025 annual report: Colgate's own statement that it returns cash "through dividends and ongoing share repurchases", and that its bank loan conditions are met.

*What we decided, and what we didn't.* Colgate should pay a high share of its earnings, and it does. This is a judgment resting on four facts. The business cannot use the cash: it spends less on plant than its plant wears out (step 14). Its owners are mostly funds that pay little tax on dividends, so the usual tax cost is small. Its shareholders have come to expect a dividend that rises every year. And management's main alternative use for cash, buying businesses, has a poor record (step 14). The costs attach to the fixed dividend, not to returning cash as such. So the form matters: keep the regular dividend about where it is, near 60% of earnings before write-downs, and send the rest out through buybacks, which carry no promise. That is the mix Colgate runs. Lenders do not restrict it, and no controlling owner needs the income. We did not run the course's test of how the share price behaves on the day a dividend is paid: it needs daily prices, and our file is monthly.

*How sure we are.* High on the direction. The missing price test would show the owners' tax position more directly; we expect it to agree, but that is an expectation, not a finding.

## Step 26: Did Colgate pay out more than it could afford?

*What we wanted to know.* How the cash Colgate returned to shareholders compares with its free cash flow to equity (FCFE), the cash left for shareholders after reinvestment and debt payments.

*Why it matters.* A company that returns more than its FCFE year after year must borrow or run down cash, and cannot go on. One that returns much less is building a pile of cash that managers may waste.

*What we did.* The formula is: FCFE = net income + depreciation and non-cash write-downs − plant spending and purchases of businesses − increase in working capital + new debt less repayments. For 2025: $2,132 million + $1,549 million − $857 million + $344 million − $456 million = $2,712 million. We used Professor Damodaran's spreadsheet for this, for 2018 to 2025, and built the same table year by year. Then we made one correction the formula misses.

*The numbers and where they came from.* The inputs are in `professor-spreadsheet/inputs.md` and the spreadsheet's results in `professor-spreadsheet/results.md`; the year-by-year table is in `modules-2-4-cross-checks-output.md`, section 10. Cash received when employees exercise share options is from the SEC data file: $3,662 million over 2018 to 2025 and $1,961 million over 2021 to 2025.

*What we decided, and what we didn't.* Over 2021 to 2025 Colgate returned $15,436 million against FCFE of $12,838 million, 120.24%. Over eight years it returned $24,211 million against $18,819 million, $5,392 million more. Taken alone, that says Colgate overpaid. We do not conclude that, because the formula leaves out the cash employees pay Colgate when they exercise options. Much of the buyback is Colgate buying shares to hand to those employees, so counting the buyback and not the cash received overstates what shareholders got. After that correction the eight-year gap is $1,730 million, 7% of what was returned, and the five-year gap is $637 million, 4.1%. Colgate returned roughly what it generated. The rest left no mark: cash on hand was $1,535 million at the end of 2017 and $1,288 million at the end of 2025, and debt has stayed between 10% and 12% of the company's value. Colgate borrowed in 2019 and 2022, the years it bought businesses, not to pay dividends.

*How sure we are.* High on cash returned and option receipts; both are disclosed. Moderate on FCFE, which depends on whether purchases of businesses count as reinvestment. On every version, the corrected figure is between about 100% and 107% of FCFE. We did not trace the last $1,730 million line by line.

## Step 27: Can Colgate's managers be trusted with shareholders' cash, and should the payout change?

*What we wanted to know.* Whether Colgate should return more, less or the same, given how good its investments are.

*Why it matters.* A company with good projects can be allowed to keep cash. One with poor projects should be pressed to hand it over.

*What we did.* The course uses a grid with two questions. Does the company return less or more than its FCFE? Are its projects good or poor? We placed Colgate on it. For the second question the course offers two tests: return on capital against the cost of capital, and the share's return against the return investors required.

*The numbers and where they came from.* FCFE comparison: step 26. Return on capital 34.56% against 8.34%: `model-output.md`, section 8. From the professor's dividend spreadsheet (`professor-spreadsheet/results.md`): Colgate's shares fell short of their required return in four of the five years from 2021 to 2025, by between 3.03 and 25.08 points. From the price file: 4.0% total return over five years against 96.2% for the S&P 500.

*What we decided, and what we didn't.* Colgate returns about what it generates and its existing business earns far more than its cost, so it sits in the part of the grid that calls for no change. That placement is a judgment, because the two tests disagree. The business earns excellent returns; the shares have done poorly. Both are true: the high returns come from brands built long ago and already in the share price, while the last five years brought slow growth and write-downs. On trust: Colgate holds little cash, $1,395 million or 1.61% of its value, so the question hardly arises. If it did build cash, the record on purchases says shareholders should object. It should not scale back: the excess over FCFE is 4.1% over five years (step 26) and was not paid for with debt. Over eight years the business covered dividends 1.31 times before any borrowing. The buyback is the flexible part and should stay that way. The borrowing recommended in step 22 would lift cash returned above FCFE for about five years; that is a planned change in financing, not a payout the business must sustain.

*How sure we are.* High that no change in dividend policy is needed. The poor share returns are a warning about growth and purchases, not about the dividend.

## Step 28: How does Colgate's payout compare with similar companies?

*What we wanted to know.* Whether Colgate pays out more or less than companies like it.

*Why it matters.* It is a cross-check on steps 25 to 27. A company far from its industry needs a reason.

*What we did.* We compared Colgate with industry averages on four measures. We also used a formula from the lecture slides, fitted across US companies in January 2014, that predicts payout from risk, growth and debt: payout = 0.649 − 0.296 × beta − 0.800 × expected growth + 0.300 × debt share. With Colgate's beta of 0.7321, expected growth of 5.45% and debt share of 9.34%, it predicts 41.67%. A matching formula for the dividend yield predicts 2.12%.

*The numbers and where they came from.* Professor Damodaran's industry tables: January 2026 for payout and yield (file: `professor-spreadsheet/originals/divfund.xls`), and a table dated January 2024 from the lesson materials for buybacks and FCFE. Colgate's figures are from steps 24 and 26. The side-by-side table is in `modules-2-4-cross-checks-output.md`, section 11. Company-by-company figures for similar companies are not in our files, and the comparison list is not final.

*What we decided, and what we didn't.* Colgate is typical of its industry. Its dividend payout was 77.46% over five years against 67.25% for household products. Its yield is 2.11% against 2.94%. Counting buybacks it returned 136.9% of net income against the industry's 153.90%, and, after option receipts, 105.0% of FCFE against 88.21%. All are far above the average US company, which pays out 34.83% and yields 1.10%. Against the formula, Colgate's yield is almost exactly as predicted. Its payout is well above the predicted 41.67%. We give that gap little weight, a judgment: the formula is twelve years old, covers companies of every age, and uses a growth figure that buybacks flatter. So by this test Colgate returns about the right amount, which agrees with steps 26 and 27.

*How sure we are.* Moderate for this step taken alone: the benchmarks are averages, two years apart, and no final list of similar companies exists yet. High for the conclusion of steps 24 to 28 together: Colgate pays a high, steady dividend, adds flexible buybacks, returns roughly what it generates, and needs no change in policy. The valuation itself is settled in steps 29 to 35.

## Corrections made along the way

None yet. Three points were raised for review during steps 1 to 12 and left unchanged: how the United States' own country risk premium is treated (step 7); a rating label in the ledger that implies a Moody's rating we have not sourced (step 12); and a ledger note that gives the lawsuit charge as $65 million where the charge inside operating profit is $99 million (step 1). None changes a number used above.

No ledger value was changed during steps 13 to 28. One input was added on 2026-11-21: the cost of bankruptcy, 15% of the company's value, a judgment needed for step 21. Two further points were raised for review and left unchanged: the professor's debt spreadsheet and the course model agree on a best debt level of 30% but grade it differently (A− and BBB), for the reason given in step 18; and the dividend spreadsheet, read alone, overstates what shareholders were paid, which step 26 corrects for cash received from employee share options.

## Glossary

To be completed with the summary. Terms defined so far, in the step where each first appears: activist (2), beta (4), book value (4), bottom-up beta (10), correlation (10), corporate governance (2), cost of capital (6), cost of equity (5), country risk premium (7), default spread (5), depreciation (1), equity risk premium (6), free cash flow to equity (1), gross profit (9), implied premium (6), independent director (2), index fund (2), interest coverage (12), Jensen's alpha (8), levered and unlevered beta (9), marginal investor (4), operating income (1), organic sales growth (3), poison pill (2), R-squared (8), regression (4), risk-free rate (5), spread (12), standard error (6), synthetic rating (12), total beta (11), write-down (1). Added in steps 13 to 28: adjusted present value (21), buyback (24), commercial paper (17), dividend (24), dividend yield (24), duration (23), EBITDA (19), free cash flow (14), hedging (16), invested capital (14), investment grade (18), optimal debt ratio (18), payout ratio (24), return on equity (14), return on invested capital (14), sunk cost (15), working capital (14).
