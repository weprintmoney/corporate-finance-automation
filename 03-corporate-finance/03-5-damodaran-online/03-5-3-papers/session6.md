---
title: "Session6"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/FoundationsOnline/slides/session6.pdf
---

#### SESSION 6: THE TIME VALUE OF MONEY

Aswath Damodaran

# Intuition Behind Present Value

¨ There are three reasons why a dollar tomorrow is worth less than a dollar today ¤ Individuals prefer present consumption to future consumption. To induce people to give up present consumption you have to offer them more in the future. ¤ When there is monetary inflation, the value of currency decreases over time. The greater the inflation, the greater the difference in value between a dollar today and a dollar tomorrow. ¤ If there is any uncertainty (risk) associated with the cash flow in the future, the less that cash flow will be valued. ¨ Other things remaining equal, the value of cash flows in future time periods will decrease as ¤ the preference for current consumption increases. ¤ expected inflation increases. ¤ the uncertainty in the cash flow increases.

# Discounting and Compounding

- The mechanism for factoring in these elements is the discount rate. The discount rate is a rate at which present and future cash flows are traded off. It incorporates
- (3) Uncertainty in the future cash flows (Higher Risk....Higher Discount Rate) A higher discount rate will lead to a lower value for cash flows in the future. The discount rate is also an opportunity cost, since it captures the returns that an individual would have made on the next best opportunity of equivalent risk.

# Present Value Principles

¨ Principle 1: Cash flows at different points in time cannot be compared and aggregated. ¤ All cash flows have to be brought to the same point in time, before comparisons and aggregations are made. ¤ That point of time can be today (present value) or a point in time in the future (future value). ¨ Principle 2: A good investment rule will be based upon not only how much you get in cash flows from an investment but when you get those cash flows.

# Time lines for cash flows

¨ The best way to visualize cash flows is on a time line, where you list out how much you get and when. ¨ In a time line, today is specified as "time 0" and each year is shown as a period.

![](_page_4_Figure_3.jpeg)

*Figure 3.1: A Time Line for Cash Flows: \$ 100 in Cash Flows Received at the End of Each of Next 4 years*

#### Cash Flow Types and Discounting Mechanics

- There are five types of cash flows -
- Most assets represent combinations of these cash flows. Thus, a conventional bond is a combination of an annuity (coupons) and a simple cash flow (face value at maturity). A stock may be a combination of a growing annuity and a growing perpetuity.

# I.Simple Cash Flows

¨ A simple cash flow is a single cash flow in a specified future time period.

Cash Flow: CFt

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Time Period: t

¨ The present value of this cash flow is

PV of Simple Cash Flow = CFt / (1+r)t

¨ The future value of a cash flow is

FV of Simple Cash Flow = CF0 (1+ r)t

#### The Power of Discounting and Compounding

¨ While we casually talk about the power of discounting and compounding, we consistently tend to underestimate that power. ¨ When projecting a growth rate in revenues for a small company, analysts often put in a growth rate reflecting the recent past and stay with that growth rate for 5, 8 or 10 years. The resulting revenues in those years can be huge. ¨ When discounting a future value (say the value of a business at the end of a forecast period of 10 years), it is surprising how much value we lose in the discounting.

# The Frequency of Compounding

¨ The frequency of compounding affects the future and present values of cash flows. The stated interest rate can deviate significantly from the true interest rate – ¤ For instance, a 10% annual interest rate, if there is semiannual compounding, works out to-

Effective Interest Rate = 
$$1.05^2 - 1 = .10125$$
 or 10.25%

| Frequency   | Rate | t   | Formula        | Effective Annual Rate |
|-------------|------|-----|----------------|-----------------------|
| Annual      | 10%  | 1   | r              | 10.00%                |
| Semi-Annual | 10%  | 2   | (1+r/2)2-1     | 10.25%                |
| Monthly     | 10%  | 12  | (1+r/12)12-1   | 10.47%                |
| Daily       | 10%  | 365 | (1+r/365)365-1 | 10.5156%              |
| Continuous  | 10%  |     | expr           |                       |
|             |      |     | -1             | 10.5171%              |

# II. Annuities

¨ An annuity is a constant cash flow that occurs at regular intervals for a fixed period of time. Defining A to be the annuity, the time line looks as follows:

![](_page_9_Figure_2.jpeg)

# Present Value of an Annuity

¨ The present value of an annuity can be calculated by taking each cash flow and discounting it back to the present, and adding up the present values. ¨ Alternatively, there is a short cut that can be used in the calculation

¨ The present value of \$1000 a year for five years can be written as:

$$PV \text{ of an Annuity} = PV(A,r,n) = A \left[ \begin{array}{c} 1 - \frac{1}{(1+r)^n} \\ \hline r \end{array} \right]$$

$$PV \text{ of } \$1000 \text{ each year for next 5 years} = \$1000 \left[ \frac{1 - \frac{1}{(1.10)^5}}{.10} \right] = \$3,791$$

# III. Growing Annuity

- □ A growing annuity is a cash flow growing at a constant rate for a specified period of time. If  $A$  is the current cash flow, and  $g$  is the expected growth rate, the time line for a growing annuity looks as follows –

**Figure 3.8: A Growing Annuity**

![](_page_11_Figure_8.jpeg)

# Present Value of a Growing Annuity

- The present value of a growing annuity can be estimated in all cases, but one - where the growth rate is equal to the discount rate, using the following model:

$$PV \text{ of an Annuity} = PV(A, r, g, n) = A(1 + g) \left[ \frac{1 - \frac{(1+g)^n}{(1+r)^n}}{(r-g)} \right]$$

- In that specific case, the present value is equal to the nominal sums of the annuities over the period, without the growth effect.

# IV. Perpetuity

¨ A perpetuity is a constant cash flow at regular intervals forever. The present value of a perpetuity is-

¨ Forever may be a tough concept for human beings to grasp, but it makes the mathematics much simpler.

$$PV \text{ of Perpetuity} = \frac{A}{r}$$

# V. Growing Perpetuities

¨ A growing perpetuity is a cash flow that is expected to grow at a constant rate forever. The present value of a growing perpetuity is -

where

¤ CF1 is the expected cash flow next year, ¤ g is the constant growth rate and ¤ r is the discount rate.

$$PV \text{ of Growing Perpetuity} = \frac{CF_1}{(r - g)}$$