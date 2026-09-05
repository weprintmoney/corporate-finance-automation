---
title: "Employeeoptions"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/ovhds/dam2ed/employeeoptions.pdf
---

# Employee Options, Restricted Stock and Value

Aswath Damodaran

#### Basic Proposition on Options

 Any options issued by a firm, whether to management or employees or to investors (convertibles and warrants) create claims on the equity of the firm. By creating claims on the equity, they can affect the value of equity per share. Failing to fully take into account this claim on the equity in valuation will result in an overstatement of the value of equity per share.

#### Why do options affect equity value per share?

- It is true that options can increase the number of shares outstanding but dilution per se is not the problem. Options affect equity value because
  - Shares are issued at below the prevailing market price. Options get exercised only when they are in the money.
  - Alternatively, the company can use cashflows that would have been available to equity investors to buy back shares which are then used to meet option exercise. The lower cashflows reduce equity value.

#### In the beginning…

 XYZ company has \$ 100 million in free cashflows to the firm, growing 3% a year in perpetuity and a cost of capital of 8%. It has 100 million shares outstanding and \$ 1 billion in debt. Its value can be written as follows:

Value of firm = 100 / (.08-.03) = 2000

| - | Debt | $= 1000$ |
|---|------|----------|
|---|------|----------|

= Equity = 1000

Value per share = 1000/100 = \$10

#### Now come the options…

- XYZ decides to give 10 million options at the money (with a strike price of \$10) to its CEO. What effect will this have on the value of equity per share?
  - None. The options are not in-the-money.
  - Decrease by 10%, since the number of shares could increase by 10 million
  - Other

# Dealing with Employee Options: The Bludgeon Approach

 The simplest way of dealing with options is to try to adjust the denominator for shares that will become outstanding if the options get exercised. In the example cited, this would imply the following:

Value of firm = 100 / (.08-.03) = 2000

| - | Debt | $= 1000$ |
|---|------|----------|
|---|------|----------|

= Equity = 1000

Number of diluted shares = 110

Value per share = 1000/110 = \$9.09

#### Problem with the diluted approach

 The diluted approach fails to consider that exercising options will bring in cash into the firm. Consequently, they will overestimate the impact of options and understate the value of equity per share. The degree to which the approach will understate value will depend upon how high the exercise price is relative to the market price. In cases where the exercise price is a fraction of the prevailing market price, the diluted approach will give you a reasonable estimate of value per share.

#### The Treasury Stock Approach

 The treasury stock approach adds the proceeds from the exercise of options to the value of the equity before dividing by the diluted number of shares outstanding.

In the example cited, this would imply the following:

Value of firm = 100 / (.08-.03) = 2000

| - | Debt | $= 1000$ |
|---|------|----------|
|---|------|----------|

= Equity = 1000

Number of diluted shares = 110

Proceeds from option exercise 
$$= 10 * 10 = 100$$
 (Exercise price = 10)

| Value per share | $= (1000+ 100)/110 = \$ 10$ |
|-----------------|-----------------------------|
|-----------------|-----------------------------|

#### Problems with the treasury stock approach

 The treasury stock approach fails to consider the time premium on the options. In the example used, we are assuming that an at the money option is essentially worth nothing. The treasury stock approach also has problems with out-of-the-money options. If considered, they can reduce the value of equity per share. If ignored, they are treated as non-existent.

#### Dealing with options the right way…

- Step 1: Value the firm, using discounted cash flow or other valuation models. Step 2:Subtract out the value of the outstanding debt to arrive at the value of equity. Alternatively, skip step 1 and estimate the of equity directly. Step 3:Subtract out the market value (or estimated market value) of other equity claims:
  - Value of Warrants = Market Price per Warrant \* Number of Warrants : Alternatively estimate the value using option pricing model
- Value of Conversion Option = Market Value of Convertible Bonds Value of Straight Debt Portion of Convertible Bonds Step 4:Divide the remaining value of equity by the number of shares outstanding to get value per share.

#### Valuing Employee Options

- Option pricing models can be used to value employee options with three caveats –
  - Employee options are long term, making the assumptions about constant variance and constant dividend yields much shakier,
  - Employee options result in stock dilution, and
  - Employee options are often exercised before expiration, making it dangerous to use European option pricing models.
  - Employee options cannot be exercised until the employee is vested.
- Employee options are illiquid. These problems can be partially alleviated by using an option pricing model, allowing for shifts in variance and early exercise, and factoring in the dilution effect. The resulting value can be adjusted for the probability that the employee will not be vested.

#### Modifications to Option pricing Model

 Since employee options can be exercised early, a case can be made that the right model to use is the Binomial model, since you can make the exercise contingent on the stock price. (Exercise if the stock price exceeds 150% of exercise value, for example). Using a Black-Scholes model with a shorter maturity (half the stated one) and a dilution adjustment to the stock price yields roughly similar values. Bottom line: The argument that option pricing models do a terrible job at valuing employee options does not hold water. Even the lousiest option pricing model does better than the accounting "exercise value = option value" model.

# Back to the numbers… Inputs for Option valuation

 Stock Price = \$ 10 Strike Price = \$ 10 Maturity = 5 years Standard deviation in stock price = 40% Riskless Rate = 4%

#### Valuing the Options

- Using a dilution-adjusted Black Scholes model, we arrive at the following inputs:
  - N (d1) = 0.7274
  - N (d2) = 0.3861
  - Value per call = \$ 9.43 (0.7274) \$10 exp-(0.04) (5)(0.3861) = \$ 3.70

Dilution adjusted Stock price

#### Value of Equity to Value of Equity per share

 Using the value per call of \$5.42, we can now estimate the value of equity per share after the option grant:

Value of firm = 100 / (.08-.03) = 2000

| - | Debt | $= 1000$ |
|---|------|----------|
|---|------|----------|

= Equity = 1000

- Value of options granted = \$ 37

= Value of Equity in stock = \$963

/ Number of shares outstanding / 100

= Value per share = \$ 9.63

#### To tax adjust or not to tax adjust…

 In the example above, we have assumed that the options do not provide any tax advantages. To the extent that the exercise of the options creates tax advantages, the actual cost of the options will be lower by the tax savings. One simple adjustment is to multiply the value of the options by (1 tax rate) to get an after-tax option cost.

#### Option grants in the future…

- Assume now that this firm intends to continue granting options each year to its top management as part of compensation. These expected option grants will also affect value. The simplest mechanism for bringing in future option grants into the analysis is to do the following:
  - Estimate the value of options granted each year over the last few years as a percent of revenues.
  - Forecast out the value of option grants as a percent of revenues into future years, allowing for the fact that as revenues get larger, option grants as a percent of revenues will become smaller.
  - Consider this line item as part of operating expenses each year. This will reduce the operating margin and cashflow each year.

# When options affect equity value per share the most…

- Option grants affect value more
  - The lower the strike price is set relative to the stock price
  - The longer the term to maturity of the option
- The more volatile the stock price The effect on value will be magnified if companies are allowed to revisit option grants and reset the exercise price if the stock price moves down.

# The Agency problems created by option grants…

**The Volatility Effect**: Options increase in value as volatility increases, while firm value and stock price may decrease. Managers who are compensated primarily with options may have an incentive to take on far more risk than warranted. **The Price Effect**: Managers will avoid any action (even ones that make sense) that reduce the stock price. For example, dividends will be viewed with disfavor since the stock price drops on the ex-dividend day. **The Short-term Effect**: To the extent that options can be exercised quickly and profits cashed in, there can be a temptation to manipulate information for short term price gain (Earnings announcements…)

#### The Accounting Effect…

 The accounting treatment of options has been abysmal and has led to the misuse of options by corporate boards. Accountants have treated the granting of options to be a non-issue and kept the focus on the exercise. Thus, there is no expense recorded at the time of the option grant (though the footnotes reveal the details of the grant). Even when the options are exercised, there is no uniformity in the way that they are are accounted for. Some firms show the difference between the stock price and the exercise price as an expense whereas others reduce the book value of equity.

#### The times, they are changing….

 In 2005, the accounting rules governing options will change dramatically. Firms will be required to value options when granted and show them as expenses when granted (though they will be allowed to amortize the expenses over the life of the option) They will be allowed to revisit these expenses and adjust them for subsequent non-exercise of the options. This will lead to restatement of accounting earnings. Any changes in the option characteristics will lead to a reassessment of the option expense and an adjustment in the year of the change.

#### Leading to predictable moaning and groaning..

- The managers of technology firms, who happen to be the prime beneficiaries of these options, have greeted these rule changes with the predictable complaints which include:
  - These options cannot be valued precisely until they are exercised. Forcing firms to value options and expense them will just result in in imprecise earnings.
  - Firms will have to go back and restate earnings when options are exercised or expire.
  - Firms may be unwilling to use options as liberally as they have in the past because they will affect earnings.

#### Some predictions about firm behavior…

- If the accounting changes go through, we can anticipate the following:
  - A decline in equity options as a way of compensating employees even in technology firms and a concurrent increase in the use of conventional stock.
  - A greater awareness of the option contract details (maturity and strike price) on the part of boards of directors, who now will be held accountable for the cost of the options.
  - At least initially, we can expect to see firms report earnings before option expensing and after option expensing to allow investors to compare them to prior periods

#### And market reaction…

 A key test of whether markets are already incorporating the effect of options into the stock price will occur when all firms expense options. If markets are blind to the option overhang, you can expect the stock prices of companies that grant options to drop when options are expensed. The more likely scenario is that the market is already incorporating options into the market value but is not discriminating very well across companies. Consequently, companies that use options disproportionately, relative to their peer groups, should see stock prices decline.

#### Options in Relative Valuation…

 Most valuations on the Street are relative valuations, where companies are compared on the basis of a multiple of earnings, book value or revenues. While it may seem that you are avoiding the options problem in relative valuation, you are not. In fact, when you compare PE ratios or EV/EVITDA multiples across companies, you are making implicit assumptions about options at these companies. In many cases, you are assuming that the option overhang is the same at all of the companies in your comparable list.

#### Bringing options into the picture

 You can use diluted shares in computing earnings per share and hope that this captures options outstanding. You can look at options outstanding as a percent of outstanding stock and use it as a qualitative variable. Firms with more options outstanding should trade at lower earnings multiples. You can compute the value of options outstanding and computing the earnings multiple using the aggregate value of equity(market cap + options outstanding)….

#### Restricted Stock

- In the aftermath of the change in accounting treatment of options, many firms have switched to the practice of giving employees stock with restrictions on trading. These restricted stock are easier to deal with than employee options. The only issue is the discount to be applied to the stock because of the trading restrictions.
  - The illiquidity discount applied to private firms should provide an indicator. Generally, the illiquidity discount has ranged from 10-20%/

#### The Valuation Impact

- Restricted Stock already issued: Value the aggregate equity in the company. To get the value per share:
  - Conservatively: Assume no illiquidity discount and divide by the total number of shares (including restricted stock) outstanding.
- More realistically: Assume an illiquidity discount (as a %) on the value and solve for the value per share of the stock. For instance, if the value of equity is \$ 100 million and there are 8 million regular shares and 2 million restricted shares outstanding and the illiquidity discount is 10%. Value per share = 100/ (8 + (1 - 0.1) 2) = \$10.20 Expected future issues: Estimate the value of restricted stock grants as a percent of revenues and build into operating expenses.

#### Employee Equity: Closing Thoughts

 It is a good idea to give employees an equity stake in the firms that they work in. However, be clear that this equity stake is being funded by the existing stockholders of the firm and is like any other employee expense. There is a cost to making employees into stockholders by giving them stock. They may have too much invested in the firm and become more risk averse as a consequence. On the other side of the ledger, options are not equivalent to common stock. They increase in value with volatility and can encourage risky, short-term behavior in managers.