---
title: "Session7"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/FoundationsOnline/slides/session7.pdf
---

## SESSION 7: VALUING A CONTRACTUAL CLAIM (BONDS)

# The nature of contractual claims

¨ A contractual claim cash flow is set at the time a contract or transaction is initiated, with the promisor committing to deliver that cash flow at the specified time. ¨ The cash flow that is contracted can be a constant cash flow or it can be tied to an observable and specific index or value. ¤ An example of the first would be a conventional fixed rate coupon bond ¤ An example of the second would be a floating rate bond.

# The Effect of Default

¨ Even though a claim is contractually set, there is the possibility that the promisor may default. ¨ If the promisor has no default risk, the claim is said to be a risk free claim. ¤ The only entities that can conceivable by default free are governments that control the printing of currency. ¤ Not all governments are default free. ¨ If there is default risk, you have to adjust for the likelihood of default, when valuing the claim.

# A fixed rate, risk free bond

¨ To value a fixed rate, risk free bond (issued by a government that is default free), you will discount the coupons (which are annuity) and the face value of the bond at the risk free rate. ¨ Thus, if you view the US government as default free, the value of 3% coupon rate, US treasury bond with ten years to maturity, if the US\$ risk free rate today for a 10-year bond is 2% can be written as follows:

Price of the Bond = 
$$30 * \text{PV}(A, 10, 2\%) + 1000/1.02^{10} = \$1089.83$$

¨ This bond is trading at above par (with the face value of \$1000 defined as par) because the market interest rate is lower than the coupon rate.

# The Yield to Maturity and Yield on a Bond

¨ If you have the price for a bond, you can solve for the interest rate that would make the present value of the coupons and face value equal to the price of the bond. That IRR is called the yield to maturity on the bond. Thus, if you had been told that the price of the 10-year, 3% coupon bond was \$1043.76, you could have solved for the interest rate.

1043.76= 30\* PV(A,10,r) + 1000/(1+r)10 *YTM = 2.50%*

¨ The yield on the bond is a related but less involved concept, estimated by dividing the coupon by the price of the bond. In the case of this bond, the yield for the bond is:

Bond Yield = Coupon/Price of Bond = 30/1043.76 = 2.87%

# Bond Convexity

¨ Let's go back to the 3% coupon, 10-year bond that we valued at \$1043.76.

Price of the Bond = 
$$30^* \text{ PV}(A, 10, 2.5\%) + 1000/1.025^{10} = \$1043.76$$

¨ If the market interest rate rises from 2.5% to 3.5%.

Price of the Bond = 
$$30 * \text{PV}(A, 10, 3.5\%) + 1000/1.035^{10} = \$958.41$$

Percentage change in price = **-8.18%**

¨ If the market interest rate falls from 2.5% to 1.5%.

Price of the Bond = 
$$30^* PV(A,10,1.5\%) + 1000/1.015^{10} = \$1138.33$$

Percentage change in price = **+9.06%**

¨ This asymmetric response to interest rate changes is called **convexity**.

# Bond Pricing Proposition 1

¨ The longer the maturity of a bond, the more sensitive it is to changes in interest rates.

![](_page_6_Figure_3.jpeg)

Bond Maturity and Price Change in Percent (for a 1% up and a 1% down movement)

# Bond Pricing Proposition 2

¨ The lower the coupon rate on the bond, the more sensitive it is to changes in interest rates.

![](_page_7_Figure_3.jpeg)

Bond Coupon and Price Change in Percent (for a 1% up and a 1% down movement)

# Default Risk

¨ When a fixed rate bond (or loan) is issued by an entity with default risk, there is a likelihood that you will not get your promised coupon or principal payments. ¨ The risk that you will not be paid your contractually due payments is called default or credit risk. ¨ To compensate for this risk, you (as the lender) have to charge a higher interest rate on the bond, with the addition being called the default spread: ¤ Default-risk adjusted rate = Risk free rate + Default Spread

# Default Risk and Default Spreads

![](_page_9_Figure_2.jpeg)

Default Spreads for 10-year Corporate Bonds: 2015 thru 2017

# Pricing a bond with default risk

¨ To price a bond with default risk, we discount the promised cash flows (coupons and face value) and discount back at a rate that includes the default spread. ¨ Thus, the value of a BBB-rated 3% coupon rate, 10 year corporate bond in January 2017, when the risk free rate was 2.5% and the default spread on the bond was 1.75% would have been:

Price of Bond = 
$$30^* PV(A, 10, 4.25\%) + 1000/1.0425^{10} = \$899.87$$

# Changing Default Risk

¨ If the price of a bond is lower for a firm with more default risk, it should come as no surprise that the prices for corporate bonds issued by firms that slip into distress will drop, even if overall market interest rates don't change. ¨ Bonds with ratings below BBB are considered below investment grade and bonds in the lower ratings classes are classified as "high yield" bonds.

# Pricing Floating Rate Bonds

¨ A floating rate bond where the interest rate is reset to the market interest rate each period should trade at par. ¨ In general, even if the interest rate reset is not perfect, floating rate bonds should trade much closer to par than otherwise similar fixed rate bonds.