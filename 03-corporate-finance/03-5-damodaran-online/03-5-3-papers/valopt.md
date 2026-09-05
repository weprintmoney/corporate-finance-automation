---
title: "Valopt"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/valopt.pdf
---

## 6. EQUITY TO EMPLOYEES: EFFECT ON VALUE

- ▪ In recent years, firms have turned to **giving employees (and especially top managers) equity option or restricted stock packages** as part of compensation. If they are options, they usually are long term and on volatile stocks. If restricted stock, the restrictions are usually on trading.
- ▪ These equity compensation packages are clearly valuable and the question becomes how best to deal with them in valuation.
- ▪ Two key issues with employee options:
  1. 1. How do options or restricted stock **granted in the past** affect equity value per share today?
  2. 2. How do **expected grants of either, in the future**, affect equity value today?

# THE EASIER PROBLEM: RESTRICTED STOCK GRANTS

- ■ When employee compensation takes the form of restricted stock grants, the solution is relatively simple.
  - ■ To account for restricted stock grants in the past, make sure that you count the restricted stock that have already been granted **in shares outstanding today**. That will reduce your value per share.
  - ■ To account for expected stock grants in the future, estimate the value of these grants as a percent of revenue and forecast that as expense **as part of compensation expenses**. That will reduce future income and cash flows.
- ■ This process has been made easier by accounting rules that have changed to require that stock based compensation be expensed in the year that they are granted. Thus, extrapolating past margins already incorporates stock based compensation.

# THE BIGGER CHALLENGE: EMPLOYEE OPTIONS

- ▪ It is true that options can increase the number of shares outstanding but dilution per se is not the problem.
- ▪ Options affect equity value at exercise because
  - ▪ Shares are **issued at below the prevailing market price**. Options get exercised only when they are in the money.
  - ▪ Alternatively, the company can use cashflows that would have been available to equity investors to **buy back shares which are then used to meet option exercise**. The lower cashflows reduce equity value.
- ▪ Options affect equity value before exercise because we have to build in the expectation that there is a probability of and a cost to exercise.

# A SIMPLE EXAMPLE...

- ■ XYZ company has \$ 100 million in free cashflows to the firm, growing 3% a year in perpetuity and a cost of capital of 8%. It has 100 million shares outstanding and \$ 1 billion in debt. Its value can be written as follows:

$$\text{Value of firm} = 100 / (.08 - .03) = 2000$$

$$\text{Debt} = 1000$$

$$= \text{Equity} = 1000$$

$$\text{Value per share} = 1000/100 = \$10$$

- ■ XYZ decides to give 10 million options at the money (with a strike price of \$10) to its CEO. What effect will this have on the value of equity per share?
  - a. None. The options are not in-the-money.
  - b. Decrease by 10%, since the number of shares could increase by 10 million
  - c. Decrease by less than 10%. The options will bring in cash into the firm but they have time value.

# I. THE DILUTED SHARE COUNT APPROACH

- The simplest way of dealing with options is to try to adjust the denominator for shares that will become outstanding if the options get exercised. In the example cited, this would imply the following:

$$\text{Value of firm} = 100 / (.08 - .03) = 2000$$

$$\text{Debt} = 1000$$

$$= \text{Equity} = 1000$$

$$\text{Number of diluted shares} = 110$$

$$\text{Value per share} = 1000/110 = \$9.09$$

- The diluted approach **fails to consider that exercising options will bring in cash into the firm**. Consequently, they will overestimate the impact of options and understate the value of equity per share.

## II. THE TREASURY STOCK APPROACH

- ■ The treasury stock approach adds the proceeds from the exercise of options to the value of the equity before dividing by the diluted number of shares outstanding.
- ■ In the example cited, this would imply the following:
  - Value of firm =  $100 / (.08 - .03)$  = 2000
  - Debt = 1000
  - = Equity = 1000
  - Number of diluted shares = 110
  - Proceeds from option exercise =  $10 * 10 = 100$
  - Value per share =  $(1000 + 100) / 110 = \$ 10$
- ■ The treasury stock approach **fails to consider the time premium on the options**. The treasury stock approach also has problems with out-of-the-money options. If considered, they can increase the value of equity per share. If ignored, they are treated as non-existent.

# III. OPTION VALUE DRAG

- ▪ Step 1: **Value the firm**, using discounted cash flow or other valuation models.
- ▪ Step 2: Subtract out the **value of the outstanding debt** to arrive at the value of equity. Alternatively, skip step 1 and estimate the of equity directly.
- ▪ Step 3: Subtract out the **market value (or estimated market value) of other equity claims**:
  - ▪  $\text{Value of Warrants} = \text{Market Price per Warrant} \times \text{Number of Warrants}$   
    : Alternatively estimate the value using option pricing model
  - ▪  $\text{Value of Conversion Option} = \text{Market Value of Convertible Bonds} - \text{Value of Straight Debt Portion of Convertible Bonds}$
  - ▪  $\text{Value of employee Options}$ : Value using the average exercise price and maturity.
- ▪ Step 4: Divide the remaining value of equity by the **number of shares outstanding** to get value per share.

# VALUING EQUITY OPTIONS ISSUED BY FIRMS... THE DILUTION PROBLEM

- ▪ Option pricing models can be used to value employee options with four caveats –
  - ▪ Employee options are **long term**, making the assumptions about constant variance and constant dividend yields much shakier,
  - ▪ Employee options **result in stock dilution**, and
  - ▪ Employee options are **often exercised before expiration**, making it dangerous to use European option pricing models.
  - ▪ Employee options cannot be exercised until the employee is vested.
- ▪ These problems can be partially alleviated by using an option pricing model, allowing for shifts in variance and **early exercise**, and **factoring in the dilution effect**. The resulting value can be adjusted for the **probability that the employee will not be vested**.

# VALUING EMPLOYEE OPTIONS

- ▪ To value employee options, you need the following inputs into the option valuation model:
  - ▪ Stock Price = \$ 10, Adjusted for dilution = \$9.58
  - ▪ Strike Price = \$ 10
  - ▪ Maturity = 10 years (Can reduce to reflect early exercise)
  - ▪ Standard deviation in stock price = 40%
  - ▪ Riskless Rate = 4%
- ▪ Using a dilution-adjusted Black Scholes model, we arrive at the following inputs:
  - ▪  $N(d1) = 0.8199$
  - ▪  $N(d2) = 0.3624$
  - ▪ Value per call =  $\$ 9.58 (0.8199) - \$10 e^{-(0.04) (10)(0.3624)} = \$5.42$

# VALUE OF EQUITY TO VALUE OF EQUITY PER SHARE

- ▪ Using the value per call of \$5.42, we can now estimate the value of equity per share after the option grant:
  - ▪ Value of firm =  $100 / (.08 - .03)$  = 2000
  - ▪ Debt = 1000
  - ▪ = Equity = 1000
  - ▪ Value of options granted = \$ 54.2
  - ▪ = Value of Equity in stock = \$945.8
  - ▪ / Number of shares outstanding / 100
  - ▪ = Value per share = \$ 9.46
- ▪ Note that this approach yields a higher value than the diluted share count approach (which ignores exercise proceeds) and a lower value than the treasury stock approach (which ignores the time premium on the options)

# OPTION GRANTS IN THE FUTURE...

- ▪ Assume now that this firm intends to continue granting options each year to its top management as part of compensation. These expected option grants will also affect value.
- ▪ The simplest mechanism for bringing in future option grants into the analysis is to do the following:
  - ▪ Estimate the value of options granted each year over the last few years as a percent of revenues.
  - ▪ Forecast out the value of option grants as a percent of revenues into future years, allowing for the fact that as revenues get larger, option grants as a percent of revenues will become smaller.
  - ▪ Consider this line item as part of operating expenses each year. This will reduce the operating margin and cashflow each year.
- ▪ To the extent that accountants have been treating option grants as expenses in the year that they are granted already, you are effectively forecasting their continuance, when you keep those margins.

# AND DON'T PLAY THE ADJUSTED EARNINGS GAME

- ■ Over the last decade, just as accountants have come to their senses and treated stock-based compensation as an operating expense, companies and analysts have tried to reverse this move by adding back these expenses to arrive at “adjusted” EBITDA and earnings numbers.
- ■ The rationale that they provide is that options are non-cash expenses, and that they should be added back, just as we do depreciation.
- ■ The truth is that options are not non-cash expenses, but in-kind expenses, where equity in the firm is being paid out to employees. Consequently, you should not be adding them back.