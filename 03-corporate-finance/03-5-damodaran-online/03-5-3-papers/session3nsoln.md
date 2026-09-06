---
title: "Session3Nsoln"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/invphilcertificate/postclass/session3Nsoln.pdf
---

## *Solutions*

- 1. Assume that you buy a default free government bond with a coupon rate of 2% and a maturity of 20 years, at face value. Assuming that interest rates increase to 3% over the course of the year following your purchase. What will your return on the government bond be for that year?
  - a. 2%. It is default free.
  - b. 3%, since that it is the new interest rate
  - c. More than 3%, since interest rates went up
  - **d. Less than 2%, since interest rates went up**

*Computational bonus: Assuming that coupons are paid annually, compute the annual return on the bond for the year you held it.*

*Explanation: Less than 2%. The rise in interest rates will cause the bond price to drop. New price for the bond (n=19, Coupon rate=2%, r =3%) = PV @ 3% of \$20 in coupons every year for 19 years + PV of \$1000 at the end of 19 years = \$856.76*

*Price change on bond = (856.76-1000)/1000 = -14.33%*

*Return on bond = -14.33% + 2% = -12.33%*

- 2. The duration of a bond measures its interest rate sensitivity, with higher duration reflecting more sensitivity to interest rate changes. Which of the following bonds has the lowest duration?
  - **a. A 10-year, 5% coupon bond**
  - b. A 20-year, 5% coupon bond
  - c. A 10-year, 2% coupon bond
  - d. A 20-year. 2% coupon bond

*Computational bonus: Estimate the duration of the bond with the lowest and highest durations on this list.*

*Explanation: The duration should increase with maturity and should be higher for lower coupon bonds.*

*To estimate the duration of these bonds, you need to assume a market interest rate. With a 4% interest rate:*

*Duration of 10-year, 5% coupon bond (lowest duration) = 8.19 years*

*Duration of 20-year, 2% coupon bond (highest duration) = 15.97 years*

- 3. You are considering investing in a BBB-rated corporate bond with a 10-year maturity, and a 5% coupon rate (with annual coupons). Assuming that the bond rating is appropriate given the default risk of the company, that the risk free rate is 3% and the default spread for BBB rated corporate bonds is 2.5%, which of the following would you expect to see as the price of the bond?
  - a. The bond should trade at face value
  - b. The bond should trade at a premium over face value
  - **c. The bond should trade at a discount on face value**

- d. Impossible to tell without more information

*Computational bonus: Estimate the price of this corporate bond.*

*Explanation: Adding the default spread to the risk free rate yields an interest rate of 5.5% for the bond. Since this is higher than the coupon rate of 5%, the bond has to trade at a discount.* 

*Price of the bond (assuming annual coupons) = PV @5.5% of \$50 a year for 10 years + PV of \$1000 in 10 years at 5.5% = \$962.31*

- 4. Ratings agencies assign bond ratings to companies, with the ratings usually ranging from AAA (Aaa) for the safest companies to D for companies in default. What are the inputs into these ratings?
  - a. The volatility in a company's earnings
  - b. The amount of debt that the company carries
  - c. The interest payments on that debt
  - d. The level of a company's earnings
  - **e. All of the above**

*Explanation: The rating for a company should measure its default risk, which will be a function of all of these variables.*