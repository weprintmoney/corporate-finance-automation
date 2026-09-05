---
title: "Aimr3"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/Seminars/AIMR3.pdf
---

# Valuing Firms inDistress

Aswath Damodaran

http://www.damodaran.com

# The Going Concern Assumption

Traditional valuation techniques are built on the assumption of a goingconcern, I.e., a firm that has continuing operations and there is nosignificant threat to these operations.•In discounted cashflow valuation, this going concern assumption finds itsplace most prominently in the terminal value calculation, which usually isbased upon an infinite life and ever-growingcashflows.•In relative valuation, this going concern assumption often shows upimplicitly because a firm is valued based upon how other firms - most ofwhich are healthy - are priced by the market today.When there is a significant likelihood that a firm will not survive theimmediate future (next few years), traditional valuation models mayyield an over-optimistic estimate of value.

# Why distress matters…

Some firms are clearly exposed to possible distress, though the sourceof thedistress may vary across firms.•For some firms, it is too much debt that creates the potential for failure tomake debt payments and its consequences (bankruptcy, liquidation,reorganization)•For other firms, distress may arise from the inability to meet operatingexpenses.When distress occurs, the firm's life is terminated leading to apotential loss of all cashflows beyond that point in time.•In a DCF valuation, distress can essentially truncate the cashflows wellbefore you reach "nirvana" (terminal value).•A multiple based upon comparable firms may be set higher for firms thathave continuing earnings than for one where there is a significant chancethat these earnings will end (as a consequence of bankruptcy).

#### The Purist DCF Defense: You do not need toconsider distress in valuation

If we assume that there is unrestricted access to capital, no firm that isworth more as a going concern will ever be forced into liquidation.•Response: But access to capital is not unrestricted, especially for firmsthat are viewed as troubled and in depressed financial markets.The firms we value are large market-cap firms that are traded on majorexchanges. The chances of these firms defaulting is minimal…•Response: Enron and Kmart….Firms that default will be able to sell their assets (both in-place andgrowth opportunities) for a fair market value, which should be equal tothe expected operatingcashflows on these assets.•Response: Unlikely, even for assets-in-place, because of the need toliquidate quickly.

#### The Adapted DCF Defense: It is already in thevaluation

The expectedcashflows can be adjusted to reflect the likelihood ofdistress. For firms with a significant likelihood of distress, theexpected cashflows should be much lower.•Response: Easier said than done. Most DCF valuations do not considerthe likelihood in any systematic way. Even if it is done, you are implicitlyassuming that in the event of distress, the distress sale proceeds will beequal to the present value of the expected cash flows.The discount rate (costs of equity and capital) can be adjusted for thelikelihood of distress. In particular, the beta (or betas) used to estimatethe cost of equity can be estimated using the updated debt to equityratio, and the cost of debt can be increased to reflect the current defaultrisk of the firm.•Response: This adjusts for the additional volatility in the cashflows butnot for the truncation of the cashflows.

# Dealing with Distress in DCF Valuation

*Simulations*: You can use probability distributions for the inputs intoDCF valuation, run simulations and allow for the possibility that astring of negative outcomes can push the firm into distress.*Modified DiscountedCashflow Valuation*: You can use probabilitydistributions to estimate expected cashflows that reflect the likelihoodof distress.*Going concern DCF value with adjustment for distress*: You can valuethe distressed firm on the assumption that the firm will be a goingconcern, and then adjust for the probability of distress and itsconsequences.*Adjusted Present Value*: You can value the firm as anunlevered firmand then consider both the benefits (tax) and costs (bankruptcy) ofdebt.

#### I. Monte Carlo Simulations

Preliminary Step: Define the circumstances under which you wouldexpect a firm to be pushed intodistres.Step 1: Choose the variables in the DCF valuation that you wantestimate probability distributions on.Steps 2 & 3: Define the distributions (type and parameters) for each ofthese variables.Step 4: Run a simulation, where you draw one outcome from eachdistribution and compute the value of the firm. If the firm hits the"distress conditions", value it as a distressed firm.Step 5: Repeat step 4 as many times as you can.Step 6: Estimate the expected value across repeated simulations.

#### II. Modified Discounted Cashflow Valuation

If you can come up with probability distributions for thecashflows(across all possible outcomes), you can estimate the expected cashflowin each period. This expected cashflowshould reflect thelikelihood of default. In conjunction with these cashflow estimates,you should estimate the discount rates by•Using bottom-up betas and updated debt to equity ratios (rather thanhistorical or regression betas) to estimate the cost of equity•Using updated measures of the default risk of the firm to estimate the costof debt.If you are unable to estimate the entire distribution, you can at leastestimate the probability of distress in each period and use as theexpected cashflow:

Expected cashflowt= Cash flowt \* (1 - Probability ofdistresst)

#### III. DCF Valuation + Distress Value

A DCF valuation values a firm as a going concern. If there is asignificant likelihood of the firm failing before it reaches stable growthand if the assets will then be sold for a value less than the present valueof the expectedcashflows (a distress sale value), DCF valuations willunderstate the value of the firm.Value of Equity= DCF value of equity (1 - Probability of distress) +Distress sale value of equity (Probability of distress)

# Step 1: Value the firm as a going concern

You can value a firm as a going concern, by looking at the expectedcashflows it will have if it follows the path back to financial health.The costs of equity and capital will also reflect this path. In particular,as the firm becomes healthier, the debt ratio (which is high at the timeof the distress) will converge to more normal levels. This, in turn, willlead to lower costs of equity and debt.Most discounted cashflowvaluations, in my view, are implicitly goingconcern valuations.

![](_page_10_Diagram_0.jpeg)

# Step 2: Estimate the probability of distress

We need to estimate a cumulative probability of distress over thelifetimeof theDCF analysis - often 10 years.There are three ways in which we can estimate the probability ofdistress:•Use the bond rating to estimate the cumulative probability of distress over10 years•Estimate the probability of distress with a probit•Estimate the probability of distress by looking at market value of bonds.

#### a. Bond Rating as indicator of probability ofdistress

| Rating | Cumulative probability of distress |                 |
|--------|------------------------------------|-----------------|
|        | <i>5 years</i>                     | <i>10 years</i> |
| AAA    | 0.03%                              | 0.03%           |
| AA     | 0.18%                              | 0.25%           |
| A+     | 0.19%                              | 0.40%           |
| A      | 0.20%                              | 0.56%           |
| A-     | 1.35%                              | 2.42%           |
| BBB    | 2.50%                              | 4.27%           |
| BB     | 9.27%                              | 16.89%          |
| B+     | 16.15%                             | 24.82%          |
| B      | 24.04%                             | 32.75%          |
| B-     | 31.10%                             | 42.12%          |
| CCC    | 39.15%                             | 51.38%          |
| CC     | 48.22%                             | 60.40%          |
| C+     | 59.36%                             | 69.41%          |
| C      | 69.65%                             | 77.44%          |
| C-     | 80.00%                             | 87.16%          |

# b. Bond Price to estimate probability of distress

Global Crossinghasa 12% couponbond with 8 years to maturity tradingat \$653.Toestimate the probabilityofdefault(witha treasurybondrateof5%used astheriskfree rate):

- nSolving for theprobabilityofbankruptcy,weget
  - With a 10-year bond, it is a process of trial and error to estimate this value. Thesolver function in excel accomplishes the same in far less time.

$$\Box_{\text{Distress}} = \text{Annual probability of default} = 13.53\%$$

nTo estimatethe cumulative probability ofdistress over 10 years:Cumulativeprobabilityofsurviving 10 years=(1 -.1353)10 =23.37%Cumulativeprobabilityofdistressover10years=1.2337=.7663or76.63%

$$653 = \prod_{t=1}^{t=8} \frac{120(1 \prod_{Distress})^t}{(1.05)^t} + \frac{1000(1 \prod_{Distress})^8}{(1.05)^N}$$

# c. Using Statistical Techniques

Thefactthat hundredsof firms gobankrupt everyyear providesus witha richdatabase that can be minedto answer bothwhy bankruptcy occurs and how topredict thelikelihood offuturebankruptcy.Inaprobit,webeginwiththesamedatathatwasusedinlineardiscriminantanalysis,a sampleoffirmsthatsurviveda specificperiodandfirmsthatdidnot. We developanindicator variable, that takesonavalueof zeroor one,asfollows:

Distress Dummy = 0forany firmthat survived theperiod= 1forany firmthat wentbankruptduring the period

nWe thenconsider informationthat would have been availableat thebeginningoftheperiod.Forinstance,wecouldlookatthedebttocapitalratiosandoperatingmarginsofallofthefirmsinthesampleatthestartoftheperiod.Finally,using the dummyvariableas our dependent variableand thefinancialratios (debt to capital and operatingmargin) as independent variables, welookfor a relationship:

Distress Dummy = a + b (Debt to Capital) + c (Operating Margin)

# Step 3: Estimating Distress Sale Value

If a firm can claim the present value of its expected future cashflowsfrom assets in place and growth assets as the distress sale proceeds,there is really no reason why we would need to consider distressseparately.The distress sale value of equity can be estimated•as a percent of book value (and this value will be lower if theeconomy is doing badly and there are other firms in the samebusiness also in distress).•As a percent of the DCF value, estimated as a going concern

# Step 4: Valuing Global Crossing with Distress

Probability of distress•Cumulative probability of distress = 76.63%Distress sale value of equity•Book value of capital = \$14,531 million•Distress sale value = 25% of book value = .25\*14531 = \$3,633 million•Book value of debt = \$7,647 million•Distress sale value of equity = \$ 0Distress adjusted value of equity•Value of Global Crossing = \$3.22 (1-.7663) + \$0.00 (.7663) = \$ 0.75

# IV. Adjusted Present Value Model

In the adjusted present value approach, the value of the firm is writtenas the sum of the value of the firm without debt (the unlevered firm)and the effect of debt on firm value

Firm Value =UnleveredFirm Value + (Tax Benefits of Debt -Expected Bankruptcy Cost from the Debt)

•The unleveredfirm value can be estimated by discounting the freecashflows to the firm at the unlevered cost of equity•The tax benefit of debt reflects the present value of the expected taxbenefits. In its simplest form,

Tax Benefit = Tax rate \* Debt

•The expected bankruptcy cost can be estimated as the difference betweenthe unlevered firm value and the distress sale value:

Expected Bankruptcy Costs = (Unlevered firm value - Distress Sale Value)\*Probability of Distress

#### Relative Valuation: Where is the distressfactored in?

RevenueandEBITDAmultiplesareusedmoreoftentovaluedistressedfirmsthanhealthyfirms.Thereasonsarepragmatic.Multiplesuchaspriceearningsorpricetobookvalueoftencannoteven becomputedfor adistressedfirm.Analystswhoareawareofthepossibilityofdistressoftenconsiderthemsubjectivelyatthepointwhenthecomparethemultipleforthefirm they are analyzing tothe industry average.Forexample, assumethattheaveragetelecommfirmtrades at2times revenues.Youmayadjustthismultipledownto1.25timesrevenuesforadistressedtelecomm firm.

#### Ways of dealing with distress in RelativeValuation

You can choose only distressed firms as comparable firms, if you arecalled upon to value one.•Response: Unless there are a large number of distressed firms in yoursector, this will not work.Adjust the multiple for distress, using some objective criteria.•Response: Coming up with objective criteria that work well may bedifficult to do.Consider the possibility of distress explicitly•Distress-adjusted value = Relative value based upon healthy firms (1 -Probability of distress) + Distress sale proceeds (Probability of distress)

## I. Choose Comparables

| <i>Company Name</i>            | <i>Value to Book Capital</i> | <i>EBIT</i> | <i>Market Debt to Capital Ratio</i> |
|--------------------------------|------------------------------|-------------|-------------------------------------|
| SAVVIS Communications Corp     | 0.80                         | -83.67      | 75.20%                              |
| Talk America Holdings Inc      | 0.74                         | -38.39      | 76.56%                              |
| Choice One Comm. Inc           | 0.92                         | -154.36     | 76.58%                              |
| FiberNet Telecom Group Inc     | 1.10                         | -19.32      | 77.74%                              |
| Level 3 Communic.              | 0.78                         | -761.01     | 78.89%                              |
| Global Light Telecom.          | 0.98                         | -32.21      | 79.84%                              |
| Korea Thrunet Co. Ltd CI A     | 1.06                         | -114.28     | 80.15%                              |
| Williams Communications Grp    | 0.98                         | -264.23     | 80.18%                              |
| RCN Corp.                      | 1.09                         | -332.00     | 88.72%                              |
| GT Group Telecom Inc CI B      | 0.59                         | -79.11      | 88.83%                              |
| Metromedia Fiber 'A'           | 0.59                         | -150.13     | 91.30%                              |
| Global Crossing Ltd.           | 0.50                         | -15.16      | 92.75%                              |
| Focal Communications Corp      | 0.98                         | -11.12      | 94.12%                              |
| Adelphia Business Solutions    | 1.05                         | -108.56     | 95.74%                              |
| Allied Riser Communications    | 0.42                         | -127.01     | 95.85%                              |
| CoreComm Ltd                   | 0.94                         | -134.07     | 96.04%                              |
| Bell Canada Intl               | 0.84                         | -51.69      | 96.42%                              |
| Globix Corp.                   | 1.06                         | -59.35      | 96.94%                              |
| United Pan Europe Communicatio | 1.01                         | -240.61     | 97.27%                              |
| Average                        | 0.87                         |             |                                     |

# II. Adjust the Multiple

In theillustration above, you can categorizethefirms on thebasis ofan observable measure of default risk. For instance, if you divide alltelecomm firms on the basis of bond ratings, you find the following -

*Bond RatingValue to Book Capital Ratio*

| A |     |
|---|-----|
| 1 | .70 |
| 1 | .61 |
| 1 | .18 |
| 1 | .06 |
| 0 | .88 |
| 0 | .61 |

You can adjust the average value to book capital ratio for the bondrating.

## III. Multiple Valuation + Distress Value

You could apply the average value to book capital ratio of alltelecomm firms to value Global Crossing as a going concern.•Going concern value = Average for telecomm firms \* BV of capital forGlobal CrossingOnce you have the going concern value, you could use the sameapproach you used in the DCF approach to adjust for distress salevalue.

#### Other Considerations in Valuing Distressedfirms

With distressed firms, everything is in flux - the operating margins,cash balance and debt to name three. It is important that you updateyour valuation to reflect the most recent information that you have onthe firm.The equity in a distressed firm can take on the characteristics of anoption and it may therefore trade at a premium on the DCF value.

# Closing Thoughts

Distress is not restricted to a few small firms. Even large firms areexposed to default and bankruptcy risk.When firms are pushed into bankruptcy, the proceeds received on adistress sale are usually much lower than the value of the firm as agoing concern.Conventional valuation models understate the impact of distress onvalue, by either ignoring the likelihood of distress or by using ad hoc(or subjective) adjustments for distress.Valuation models - both DCF and relative - have to be adapted toincorporate the effect of distress.