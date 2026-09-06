---
title: "Tools"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/cf2E/tools.pdf
---

# Present Value

Aswath Damodaran

### Intuition Behind Present Value

- <sup>n</sup> There are three reasons why a dollar tomorrow is worth less than a dollar today
  - Individuals prefer present consumption to future consumption. To induce people to give up present consumption you have to offer them more in the future.
  - When there is monetary inflation, the value of currency decreases over time. The greater the inflation, the greater the difference in value between a dollar today and a dollar tomorrow.
- If there is any uncertainty (risk) associated with the cash flow in the future, the less that cash flow will be valued. <sup>n</sup> Other things remaining equal, the value of cash flows in future time periods will decrease as
  - the preference for current consumption increases.
  - expected inflation increases.
  - the uncertainty in the cash flow increases.

### Discounting and Compounding

- The mechanism for factoring in these elements is the discount rate.
- **Discount Rate:** The discount rate is a rate at which present and future cash flows are traded off. It incorporates -
  - (1) Preference for current consumption (Greater ....Higher Discount Rate)
  - (2) expected inflation (Higher inflation .... Higher Discount Rate)
  - (3) the uncertainty in the future cash flows (Higher Risk....Higher Discount Rate)
- A higher discount rate will lead to a lower value for cash flows in the future.
- The discount rate is also an opportunity cost, since it captures the returns that an individual would have made on the next best opportunity.
  Discounting future cash flows converts them into cash flows in present value dollars. Just a discounting converts future cash flows into present cash flows,
  Compounding converts present cash flows into future cash flows.

### Present Value Principle 1

<sup>n</sup> Cash flows at different points in time cannot be compared and aggregated. All cash flows have to be brought to the same point in time, before comparisons and aggregations are made.

### Cash Flow Types and Discounting Mechanics

- ■ There are five types of cash flows -
  - • simple cash flows,
  - • annuities,
  - • growing annuities
  - • perpetuities and
  - • growing perpetuities

### I.Simple Cash Flows

<sup>n</sup> A simple cash flow is a single cash flow in a specified future time period.

Cash Flow: CF<sup>t</sup>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|

Time Period: t

<sup>n</sup> *The present value of this cash flow is-*

PV of Simple Cash Flow = CF<sup>t</sup> / (1+r)<sup>t</sup>

<sup>n</sup> *The future value of a cash flow is -*

FV of Simple Cash Flow = CF<sup>0</sup> (1+ r)t

# Application 1: The power of compounding - Stocks, Bonds and Bills

<sup>n</sup> Ibbotson and Sinquefield, in a study of returns on stocks and bonds between 1926-92 found that stocks on the average made 12.4%, treasury bonds made 5.2% and treasury bills made 3.6%. <sup>n</sup> The following table provides the future values of \$ 100 invested in each category at the end of a number of holding periods - 1, 5 , 10 , 20, 30 and 40 years.

| Holding Period | Stocks      | T. Bonds | T.Bills  |
|----------------|-------------|----------|----------|
| 1              | \$112.40    | \$105.20 | \$103.60 |
| 5              | \$179.40    | \$128.85 | \$119.34 |
| 10             | \$321.86    | \$166.02 | \$142.43 |
| 20             | \$1,035.92  | \$275.62 | \$202.86 |
| 30             | \$3,334.18  | \$457.59 | \$288.93 |
| 40             | \$10,731.30 | \$759.68 | \$411.52 |

### Concept Check

<sup>n</sup> Most pension plans allow individuals to decide where their pensions funds will be invested - stocks, bonds or money market accounts. <sup>n</sup> Where would you choose to invest your pension funds? <sup>o</sup> Predominantly or all equity <sup>o</sup> Predominantly or all bonds and money market accounts <sup>o</sup> A Mix of Bonds and Stocks <sup>n</sup> Will your allocation change as you get older? <sup>o</sup> Yes <sup>o</sup> No

# The Frequency of Compounding

- <sup>n</sup> The frequency of compounding affects the future and present values of cash flows. The stated interest rate can deviate significantly from the true interest rate –
  - For instance, a 10% annual interest rate, if there is semiannual compounding, works out to-

Effective Interest Rate = 
$$1.05^2 - 1 = .10125$$
 or  $10.25\%$ 

| Frequency   | Rate | t   | Formula          | Effective Annual Rate |
|-------------|------|-----|------------------|-----------------------|
| Annual      | 10%  | 1   | r                | 10.00%                |
| Semi-Annual | 10%  | 2   | (1+r/2) 2        |                       |
|             |      |     | -1               | 10.25%                |
| Monthly     | 10%  | 12  | (1+r/12) 12 -1   | 10.47%                |
| Daily       | 10%  | 365 | (1+r/365) 365 -1 | 10.5156%              |
| Continuous  | 10%  |     | exp r            |                       |
|             |      |     | -1               | 10.5171%              |

## II. Annuities

- An annuity is a constant cash flow that occurs at regular intervals for a fixed period of time. Defining  $A$  to be the annuity,

![](_page_9_Diagram_7.jpeg)

# Present Value of an Annuity

- ■ The present value of an annuity can be calculated by taking each cash flow and discounting it back to the present, and adding up the present values. Alternatively, there is a short cut that can be used in the calculation [ $A = \text{Annuity}$ ;  $r = \text{Discount Rate}$ ;  $n = \text{Number of years}$ ]

$$PV_{\text{of an Annuity}} = PV(A, r_n) = A \left[ \frac{1 - \frac{1}{(1+r)^n}}{r} \right]$$

## Example: PV of an Annuity

- ■ The present value of an annuity of \$1,000 for the next five years, assuming a discount rate of 10% is -

$$PV \text{ of } \$1000 \text{ each year for next 5 years} = \$1000 \left[ \frac{1 - \frac{1}{(1.10)^5}}{.10} \right] = \$3,791$$

- ■ The notation that will be used in the rest of these lecture notes for the present value of an annuity will be  $PV(A,r,n)$ .

## Annuity, given Present Value

- ■ The reverse of this problem, is when the present value is known and the annuity is to be estimated -  $A(PV, r, n)$ .

$$Annuity \text{ given Present Value} = A(PV, r, n) = PV \left[ \frac{r}{1 - \frac{1}{(1+r)^n}} \right]$$

# Future Value of an Annuity

---

- ■ The future value of an end-of-the-period annuity can also be calculated as follows-

$$\text{FV of an Annuity} = \text{FV}(\text{Ar}, n) = \text{A} \left[ \frac{(1 + r^n) - 1}{r} \right]$$

# An Example

- ■ Thus, the future value of \$1,000 each year for the next five years, at the end of the fifth year is (assuming a 10% discount rate) -

$$FV \text{ of } \$1,000 \text{ each year for next 5 years} = \$1000 \left[ \frac{(1.10)^5 - 1}{.10} \right] = \$6,105$$

- ■ The notation that will be used for the future value of an annuity will be  $FV(A,r,n)$ .

# Annuity, given Future Value

---

- ■ if you are given the future value and you are looking for an annuity -  $A(FV,r,n)$  in terms of notation -

$$\text{Annuity given Future Value} = A(FV,r,n) = FV \left[ \frac{r}{(1+r)^n - 1} \right]$$

### Application 2: Saving for College Tuition

- <sup>n</sup> Assume that you want to send your newborn child to a private college (when he gets to be 18 years old). The tuition costs are \$ 16000/year now and that these costs are expected to rise 5% a year for the next 18 years. Assume that you can invest, after taxes, at 8%.
  - Expected tuition cost/year 18 years from now = 16000\*(1.05)18 = \$38,506
- PV of four years of tuition costs at \$38,506/year = \$38,506 \* PV(A ,8%,4 years)= \$127,537 <sup>n</sup> If you need to set aside a lump sum now, the amount you would need to set aside would be -
- Amount one needs to set apart now = \$127,357/(1.08)18 = \$31,916 <sup>n</sup> If set aside as an annuity each year, starting one year from now -
  - If set apart as an annuity = \$127,537 \* A(FV,8%,18 years) = \$3,405

### Application 3: How much is an MBA worth?

<sup>n</sup> Assume that you were earning \$40,000/year before entering program and that tuition costs are \$16000/year. Expected salary is \$ 54,000/year after graduation. You can invest money at 8%.

*For simplicity, assume that the first payment of \$16,000 has to be made at the start of the program and the second payment one year later.*

- PV Of Cost Of MBA = \$16,000+16,000/1.08 + 40000 \* PV(A,8%,2 years) = \$102,145

<sup>n</sup> *Assume that you will work 30 years after graduation, and that the salary differential (\$14000 = \$54000-\$40000) will continue through this period.*

- PV of Benefits Before Taxes = \$14,000 \* PV(A,8%,30 years) = \$157,609
- This has to be discounted back two years \$157,609/1.08<sup>2</sup> = \$135,124
- The present value of getting an MBA is = \$135,124 \$102,145 = \$32,979

### Some Follow-up Questions

- 1. How much would your salary increment have to be for you to break even on your MBA?
- 2. Keeping the increment constant, how many years would you have to work to break even?

# Application 4: Savings from Refinancing Your Mortgage

<sup>n</sup> Assume that you have a thirty-year mortgage for \$200,000 that carries an interest rate of 9.00%. The mortgage was taken three years ago. Since then, assume that interest rates have come down to 7.50%, and that you are thinking of refinancing. The cost of refinancing is expected to be 2.50% of the loan. (This cost includes the points on the loan.) Assume also that you can invest your funds at 6%.

Monthly payment based upon 9% mortgage rate (0.75% monthly rate) = \$200,000 \* A(PV,0.75%,360 months) = \$1,609

Monthly payment based upon 7.50% mortgage rate (0.625% monthly rate) = \$200,000 \* A(PV,0.625%,360 months) = \$1,398

<sup>n</sup> Monthly Savings from refinancing = \$1,609 - \$1,398 = \$211

### Refinancing: The Trade Off

<sup>n</sup> *If you plan to remain in this house indefinitely,*

Present Value of Savings (at 6% annually; 0.5% a month)

= \$211 \* PV(A,0.5%,324 months)

= \$33,815

- The savings will last for 27 years the remaining life of the existing mortgage.
- You will need to make payments for three additional years as a consequence of the refinancing -

Present Value of Additional Mortgage payments - years 28,29 and 30

= \$1,398 \* PV(A,0.5%,36 months)/1.06<sup>27</sup>

= \$9,532

<sup>n</sup> Refinancing Cost = 2.5% of \$200,000 = \$5,000 <sup>n</sup> Total Refinancing Cost = \$9,532 + \$5,000 = \$14,532 <sup>n</sup> Net Effect = \$ 33,815 - \$ 9,532 - \$ 14,532 = \$9,751: Refinance

### Follow-up Questions

- 1. How many years would you have to live in this house for you break even on this refinancing?
- 2. We've ignored taxes in this analysis. How would it impact your decision?

### Application 5: Valuing a Straight Bond

<sup>n</sup> You are trying to value a straight bond with a fifteen year maturity and a 10.75% coupon rate. The current interest rate on bonds of this risk level is 8.5%.

PV of cash flows on bond = 107.50\* PV(A,8.5%,15 years) + 1000/1.08515 = \$ 1186.85

<sup>n</sup> If interest rates rise to 10%,

PV of cash flows on bond = 107.50\* PV(A,10%,15 years)+ 1000/1.1015 = \$1,057.05

Percentage change in price = -10.94%

<sup>n</sup> If interest rate fall to 7%,

PV of cash flows on bond = 107.50\* PV(A,7%,15 years)+ 1000/1.0715 = \$1,341.55

Percentage change in price = +13.03%

<sup>n</sup> This asymmetric response to interest rate changes is called **convexity**.

# Application 6: Contrasting Short Term and Long Term Bonds

![](_page_23_Figure_1.jpeg)

### Bond Pricing Proposition 1

<sup>n</sup> The longer the maturity of a bond, the more sensitive it is to changes in interest rates.

# Application 7: Contrasting Low-coupon and High-coupon Bonds

![](_page_25_Figure_1.jpeg)

### Bond Pricing Proposition 2

<sup>n</sup> The lower the coupon rate on the bond, the more sensitive it is to changes in interest rates.

### III. Growing Annuity

- ■ A growing annuity is a cash flow growing at a constant rate for a specified period of time. If  $A$  is the current cash flow, and  $g$  is the expected growth rate, the time line for a growing annuity looks as follows –

**Figure 3.8: A Growing Annuity**

![](_page_27_Figure_9.jpeg)

# Present Value of a Growing Annuity

- The present value of a growing annuity can be estimated in all cases, but one - where the growth rate is equal to the discount rate, using the following model:

$$PV_{\text{of an Annuity}} = PV(A, r_n) = A \left[ \frac{1 - \frac{1}{(1+r)^n}}{r} \right]$$

- In that specific case, the present value is equal to the nominal sums of the annuities over the period, without the growth effect.

## Appendix 8: The Value of a Gold Mine

- ■ Consider the example of a gold mine, where you have the rights to the mine for the next 20 years, over which period you plan to extract 5,000 ounces of gold every year. The price per ounce is \$300 currently, but it is expected to increase 3% a year. The appropriate discount rate is 10%. The present value of the gold that will be extracted from this mine can be estimated as follows –

$$PV \text{ of extracted gold} = \$300 * 5000 * (1.03) \left[ \frac{1 - \frac{(1.03)^{20}}{(1.10)^{20}}}{.10 - .03} \right] = \$16,145,980$$

# PV of Extracted Gold as a Function of Expected Growth Rate

![](_page_30_Figure_1.jpeg)

# PV of Extracted Gold as a Function of Expected Growth Rate

![](_page_31_Figure_1.jpeg)

### Concept Check

<sup>n</sup> If both the growth rate and the discount rate go up by 1%, will the present value of the gold to be extracted from this mine increase or decrease?

## IV. Perpetuity

---

- ■ A perpetuity is a constant cash flow at regular intervals forever. The present value of a perpetuity is-

$$PV \text{ of Perpetuity} = \frac{A}{r}$$

### Application 9: Valuing a Console Bond

<sup>n</sup> A console bond is a bond that has no maturity and pays a fixed coupon. Assume that you have a 6% coupon console bond. The value of this bond, if the interest rate is 9%, is as follows -

Value of Console Bond = \$60 / .09 = \$667

### V. Growing Perpetuities

<sup>n</sup> A growing perpetuity is a cash flow that is expected to grow at a constant rate forever. The present value of a growing perpetuity is -

where

- CF1is the expected cash flow next year,
- g is the constant growth rate and
- r is the discount rate.

$$PV \text{ of Growing Perpetuity} = \frac{CF_1}{(r-g)}$$

# Application: Valuing a Stock with Growing Dividends

<sup>n</sup> Southwestern Bell paid dividends per share of \$2.73 in 1992. Its earnings and dividends have grown at 6% a year between 1988 and 1992, and are expected to grow at the same rate in the long term. The rate of return required by investors on stocks of equivalent risk is 12.23%.

Current Dividends per share = \$2.73

Expected Growth Rate in Earnings and Dividends = 6%

Discount Rate = 12.23%

Value of Stock = \$2.73 \*1.06 / (.1223 -.06) = \$46.45