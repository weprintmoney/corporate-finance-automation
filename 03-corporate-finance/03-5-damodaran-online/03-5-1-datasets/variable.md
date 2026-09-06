---
title: "Variables used in Data Set"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm
---

Variables used in Data Set

# **Variables used in Datasets**

*For many of the ratios, estimated on a sector basis, we used the cumulated values for the sector. As an example, the PE ratio for the sector is not a simple average of the PE ratios of individual firms in the sector. Instead, it is obtained by dividing the cumulated net income for the sector (obtained by adding up the net income of each firm in the sector) by the cumulated market value of equity of firm in the sector ( obtained by adding up the market values of all of the firms in the sector).*

|  |  |
| --- | --- |
| Variables | Description |
| Accounts Payable /Sales | Estimated by dividing the cumulated accounts payable for the sector by the cumulated sales for the sector. |
| Accounts Receivable/Sales | Estimated by dividing the cumulated accounts receivable for the sector by the cumulated sales for the sector. |
| Alpha | Estimated from the intercept of the monthly return regression of stock returns against market returns, using the last 5 years of data, as follows: (Jensen’s) Alpha = Intercept - Riskfree Rate (1 - Beta)  The number is annualized by compounding over 12 months. |
| Annual Returns | The annual returns on stocks, bonds and bills are estimated by adding the price appreciation during the year to the dividends (or coupons) paid on the security during the year. |
| Beta | *For US firms*: Estimated by regressing weekly returns on stock against NYSE composite, using 5 years of data or listed period (if less than 5 years). If data is available for less than 2 years, the beta is not estimated).  *For all other firms*: Estimated by regressing weekly returns on stock against the local index (generally the most widely followed index in that market - CAC in France, Sensex in India and Bovespa in Brazil), using 5 years of data. I use a composite of the two year regression beta and the five year regression beta, weighting the former 2/3rds and the latter 1/3rds.  Beta = (2/3) 2 year regression beta + (1/3) 5 year regression beta  If the five year regression beta is missing, I replace it with one. I also apply an aggregate check to ensure that the global average across all the companies is close to one. |
| Beta (Market) | See Beta |
| Beta (Total) | See Total Beta |
| Beta (unlevered) | See Unlevered Beta |
| Beta (unlevered and corrected for cash) | See Unlevered Beta corrected for cash |
| Book Debt Ratio | This is the book estimate of the debt ratio, obtained by dividing the cumulated value of debt by the cumulated value of debt plus the cumulated book value of equity for the entire sector. |
| BV of Capital | This is the book value of debt plus the book value of common equity, as reported on the balance sheet. |
| Cap Ex/ Depreciation | Estimated by dividing the capital expenditures by depreciation. For the sector, we estimate the ratio by dividing the cumulated capital expenditures for the sector by the cumulated depreciation and amortization. |
| Capital (Book Value) | This is the book value of debt plus the book value of common equity, as reported on the balance sheet. |
| Capital Expenditures | This is the cumulated capital spending, as reported in the statement of cash flows, for the sector. It generally does not include acquisitions. |
| Cash | Cash and Marketable Securities reported in the balance sheet. |
| Correlation with the market | This is the correlation of stock returns with the market index, using the same time period as the beta estimation (see beta) . |
| Cost of Capital | The weighted average of the cost of equity and after-tax cost of debt, weighted by the market values of equity and debt: Cost of Capital = Cost of Equity (E/(D+E)) + After-tax Cost of Debt (D/(D+E))  For the weights, we use cumulated market values for the entire sector. |
| Cost of Debt (After-tax) | The after-tax cost of debt is: After-tax cost of debt = Pre-tax Cost of debt (1 — tax rate)  The average effective tax rate for the sector is used for this computation. |
| Cost of Debt (Pre-tax) | This is estimated by adding a default spread to the riskfree rate. To estimate the default spread, we use the standard deviation in stock prices over the last 5 years. The higher the standard deviation, the higher the default sprad. |
| Cost of Equity | Estimated using the capital asset pricing model: Cost of Equity = Riskfree Rate + Beta (Risk Premium)  The average beta for the sector is used. We use the long term treasury bond rate as the riskfree rate, and a 5.5% risk premium. You can change these inputs in the excel spreadsheet. |
| D/(D+E) | This is the market value estimate of the debt ratio, obtained by dividing the cumulated value of debt by the cumulated value of debt plus the cumulated market value of equity for the entire sector. We assume that the book value of debt is roughly equal to the market value of debt. |
| D/E Ratio | Estimated using cumulated market value of equity for the sector and cumulated debt for the sector: Debt/Equity Ratio for Sector = Cumulated Debt for Sector/Cumulated Market Value of Equity  Debt is defined as including both short term and long term debt (but not accounts payable or non-interest bearing liabilities), and the book value of debt is used as a proxy for market value of debt. |
| Debt Ratio (Book Value) | This is the book estimate of the debt ratio, obtained by dividing the cumulated value of debt by the cumulated value of debt plus the cumulated book value of equity for the entire sector. |
| Debt Ratio (Market Value) | This is the market value estimate of the debt ratio, obtained by dividing the cumulated value of debt by the cumulated value of debt plus the cumulated market value of equity for the entire sector. We assume that the book value of debt is roughly equal to the market value of debt. |
| Debt/Equity Ratio | Estimated using cumulated market value of equity for the sector and cumulated debt for the sector: Debt/Equity Ratio for Sector = Cumulated Debt for Sector/Cumulated Market Value of Equity  Debt is defined as including both short term and long term debt (but not accounts payable or non-interest bearing liabilities), and the book value of debt is used as a proxy for market value of debt. |
| Default spread | This is the spread added on to the riskfree rate to estimate a pre-tax cost of borrowing. |
| Depreciation | Includes both depreciation and amortization, as reported in the statement of cash flows. For the sector, we use the cumulated value of depreciation and amortization. |
| Dividend Payout | Estimated by dividing the cumulated dividends, for the sector, by the cumulated net income for the sector. |
| Dividend Yield | Dividend per share divided by the current stock price. We have used the current annualized dividend per share (obtained by quadrupling the last quarter’s dividend per share) |
| Earnings Yield | This is the inverse of the price/earning ratio and is computed by dividing the earnings per share by the price per share |
| EBITDA | Estimated by adding depreciation and amortization back to operating income (EBIT) |
| Effective tax rate | This is the effective tax rate, obtained by dividing the taxes paid by the taxable income as reported to the stockholders. We would rather have used marginal tax rates, but these are not reported. |
| Enterprise Value | Market value of equity + Market value of debt - Cash |
| Equity EVA | (Return on Equity - Cost of Equity) (BV of Equity) See descriptions of each of these variables for more detail. We use the cumulated book value of equity for the entire sector. |
| EVA | (Return on Capital - Cost of Capital) (BV of Capital) See descriptions of each of these variables for more detail. |
| Firm Value | Market Value of Equity + Market Value of Debt |
| Fixed Assets/Total Assets | Estimated by dividing the cumulated book value of fixed assets, for the sector, by the cumulated total assets, for the sector. |
| Free Cash Flow to Firm (FCFF) | FCFF = EBIT(1-t) - (Capital Expenditures - Depreciation) - Change in non-cash Working Capital For the sector as a whole, we compute this using cumulated values for each variable |
| Free Cash Flow to Equity (FCFE) | FCFE = Net Income - (Capital Expenditures - Depreciation) - Change in non-cash Working Capital - (Principal repaid - New Debt Issued) For the sector as a whole, we compute this using cumulated values for each variable. |
| Fundamental growth in EPS | Fundamental Growth in EPS =Retention Ratio \* ROE See descriptions of these variables for more detail |
| Historical Growth Rate | Obtained using this year’s earnings per share and earnings per share from 5 years ago: Historical Growth rate = (EPS (today)/EPS(5 years ago))^(1/5)-1  If EPS five years ago or today is negative, this number is not estimated. |
| Implied Equity Premium | Estimated using the current level of index, the expected dividends on stock and the expected growth rate in earnings. The expected growth rate from 1960 to 1985 was estimated using historical growth rates. From 1985 onwards, we use the Zack’s consensus estimate of growth for the stocks in the S&P 500. |
| Insider Holdings % | Number of shares held by insiders (as defined by the SEC to include corporate officers, directors and those holding more than 5% of the outstanding stock) as a percent of total stock outstanding |
| Institutional Holding % | Number of shares held by mutual funds, pension funds and trusts as a percent of total stock outstanding. |
| Interest coverage ratio | Estimated by dividing the after-tax operating income by the interest expense: Interest coverage ratio = EBIT(1-t) / Interest Expense |
| Inventory/ Sales | Estimated by dividing the cumulated inventory for the sector by the cumulated sales for the sector |
| Invested Capital | Book value of equity + Book value of debt - Cash |
| Market Capitalization | Estimated market value of equity, obtained by multiplying the number of shares outstanding by the share price. |
| Market Debt Ratio | This is the market value estimate of the debt ratio, obtained by dividing the cumulated value of debt by the cumulated value of debt plus the cumulated market value of equity for the entire sector. We assume that the book value of debt is roughly equal to the market value of debt. |
| Net Capital Expenditures | Estimated as the difference between capital expenditures and depreciation. For the sector, we use the cumulated values for both variables. |
| Net Margin | Estimated by dividing the net income by the total revenues Net Margin = Net Income / Sales  To estimate the values for the sector, we use the cumulated values of net income and sales for the sector. |
| Non-cash ROE | (Net Income - Interest income from cash) / (Book value of equity - Cash and Marketable securities) |
| Non-Cash Working Capital / Sales | Non-cash Working Capital = Inventory + Other Current Assets + Accounts Receivable -Accounts Payable - Other Current Liabilities  [Current assets excluding cash - Current liabilities excluding interest bearing debt)  For the sector, we use cumulated values for each of the variables. |
| Operating Income | Used interchangeably with EBIT. Accountants will take issue with this... but... |
| Operating Margin (After-tax) | Estimated by dividing the after-tax operating income by the total revenues. This is an after-tax, pre-debt measure of operating profitability: After-tax Operating Margin = EBIT(1-t) / Sales  To estimate the values for the sector, we use the cumulated values of EBIT(1-t) and sales. The tax rate used is the effective tax rate, averaged across the sector. |
| Operating Marign (Pre-tax) | Estimated by dividing the pre-tax operating income by the total revenues. This is a pre-tax measure of operating profitability: Pre-tax Operating Margin = EBIT / Sales |
| Reinvestment Rate | Reinvestment Rate = (Net Capital Expenditures + Change in WC) / EBIT (1-t) For the sector, we use the cumulated values of each of these variables for the sector. |
| Retention Ratio | Estimated as follows: Retention Ratio = 1 - Dividend Payout Ratio |
| ROC (Return on Capital) or (ROIC) Return on Invested Capital | Estimated by dividing the after-tax operating income by the book value of invested capital. We use the cumulated values for both variables, for the sector, to estimate the sector ROC. ROC = EBIT (1-t) / (BV of Debt + BV of Equity-Cash) |
| ROE (Return on Equity) | Estimated by dividing the net income by the book value of equity. We use the cumulated values for both variables, for the sector, to estimate the sector ROE. If book value of equity is negative, this is not estimated. (For non-cash ROE, see Non-cash ROE) |
| R-squared | Estimated from the monthly return regression of stock returns against market returns, using the last 5 years of data. This is the percent of the variation in stock returns, that is explained by market movements. |
| Standard deviation in firm value | The standard deviation in firm value is obtained using the following formula: Variance in firm value = Variance in Equity Value (E/(D+E))2 + Variance in Debt (D/(D+E))2 + 2 (E/(D+E) (D/(D+E) (Std dev in Equity) (Std dev in debt) (Correlation between debt and equity)  Since variance in debt value is tough to obtain, we assume that it is roughly one-third the standard deviation in equity values (based upon the relative volatilities in equity and bond indices) and that the correlation between stock and bond prices is 0.3 (against based upon the correlation between equity and bond indices) |
| Standard deviation in prices (equity) | The standard deviation in monthly stock prices, estimated using 5-years of data. The number is annualized. |
| Tax Rate | This is the effective tax rate, obtained by dividing the taxes paid by the taxable income as reported to the stockholders. We would rather have used marginal tax rates, but these are not reported. |
| Total Beta | Total Beta = Market Beta / Correlation between stock and market  This measure is equivalent to dividing the standard deviation of a stock by the standard deviation of the market. For an undiversified investor, it may be a better measure of risk than the traditional market beta.  It is useful for computing the cost of equity for a private business with an undiversified owner. |
| Unlevered Beta | This is the beta for the sector, unlevered by the market value debt to equity ratio for the sector: Unlevered Beta = Beta / (1 + (1- tax rate) (Debt/Equity Ratio))  See description of debt/equity ratio for more detail. |
| Unlevered Beta adjusted for cash | The unlevered beta that you compute for a firm reflects both its operatiing assets and the cash holdings of the firm. Since the latter should have a beta close to zero, we estimate the beta of just the operating assets by using two numbers - the unlevered beta and the cash as a percent of overall firm value (in market terms).  Unlevered Beta adjusted for cash = Unlevered Beta/ (1 - Cash/ Firm Value)  Thus if the unlevered beta for the entire firm is 1.20 and the firm has a cash balance of 20%, the unlevered beta corrected for cash would be 1.5 = 1.2/(1-.20) |
| Value/EBITDA | Estimated by dividing the market value of debt and equity by the EBITDA Value/EBITDA = (Market Value of Equity + Value of Debt-Cash) / EBITDA  We use the book value of debt as a proxy for the market value, and cumulate the values, across the sector, to estimate the ratio. |
