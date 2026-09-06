---
title: "Apva"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/apva.pdf
---

# **The Adjusted Present Value: The Combined Impact of Growth and the Tax Shield of Debt on the Cost of Capital and Systematic Risk**

Michael C. Ehrhardt

Phillip R. Daves

Finance Department, SMC 424 University of Tennessee Knoxville, TN 37996-0540

Phone: 423-974-1717 Fax: 423-974-1716 E-mail: ehrhardt@utk.edu

June 15, 1999

We appreciate the helpful comments made by Jim Wansley and participants of the University of Tennessee Workshop Series. Any remaining errors are our responsibility.

# **The Adjusted Present Value: The Combined Impact of Growth and the Tax Shield of Debt on the Cost of Capital and Systematic Risk**

#### **Abstract**

Despite the widespread use of Myers' (1974) Adjusted Present Value (APV) approach, the finance literature does not specify within the context of APV the combined impact of both growth and the tax shield of debt on the cost of capital, the cost of equity, and systematic risk. This paper fills that gap in the literature. Our results demonstrate that the widely used models of Modigliani and Miller (M&M) (1963) and Hamada (1972) are inappropriate for a growing firm and lead to economically significant errors when used to estimate the cost of capital, the cost of equity, and systematic risk.

We explore a general version of Myers' APV in which the firm is allowed to grow and the discount rate for the tax shield can be any value. Special cases of this model are the M&M/Hamada models and the Compressed APV (CAPV) of Kaplan and Ruback (1995). The M&M/Hamada models assume zero growth and discount the tax shield at the cost of debt while the CAPV allows for non-zero growth and discounts the tax shield at the unlevered cost of equity. Despite these different assumptions, we show that the CAPV expressions for the cost of equity and systematic risk for arbitrary growth rates and arbitrary tax rates are identical to the zero-tax, zero growth expressions of M&M/Hamada. In other words, if tax shields are discounted at the unlevered cost of equity, then neither the growth rate nor the tax rate affects the cost of equity and systematic risk.

We show that if tax shields of a growing firm are discounted at a rate less than the unlevered cost of equity, then two unusual results are likely to occur. First, the levered cost of equity can actually be *smaller* than the unlevered cost of equity! Second, the cost of capital decreases as growth increases, implying that high growth firms should have large amounts of debt in their capital structures. These two results are inconsistent with intuition and observation of actual practices, and suggest that the CAPV is the appropriate model with tax shields being discounted at the unlevered cost of equity.

#### **I. Introduction**

The Adjusted Present Value (APV), as developed by Myers (1974), defines the value of a levered firm as the value of an otherwise identical but unlevered firm plus the value of any "side effects" due to leverage. These side effects often include the tax shield of debt, expected bankruptcy costs, and agency costs. The APV provides a powerful framework for analyzing a variety of issues in corporate finance, and is especially useful in applications of corporate valuation; for recent examples, see Kaplan and Ruback (1995, 1996), Luehrman (1997), and Inselbag and Kaufold (1997).

Corporate valuation with APV requires estimates for the following items: (1) expected future free cash flows (defined as net operating profits after taxes less necessary investment in net operating working capital and net plant, property, and equipment); (2) the unlevered cost of equity; (3) the expected future capital structure; (4) the discount rate to be applied to the tax shield; and (5) the steady-state long-term growth rate of free cash flows and debt. Two problems immediately present themselves. First, the unlevered cost of equity is not observable, and so it usually is derived from the levered cost of equity for the firm in question or from the levered cost of equity for similar firms. Second, the appropriate discount rate for the tax shield is not observable; usually a rate greater than or equal to the cost of debt and less than or equal to the unlevered cost of equity is chosen.

Modigliani and Miller (1963) address these two problems by assuming that the growth rate is zero and that the appropriate discount rate for the tax shield is the interest rate on debt. Under these conditions, they show that the relationship between the levered cost of equity and the unlevered cost of equity depends upon the firm's cost of debt, tax rate, and capital structure. Hamada (1972) incorporates the same assumptions and derives the impact that leverage has on systematic risk. To the best of our knowledge, however, the finance literature does not identify the relationship between the levered cost of equity and unlevered cost of equity for a growing firm, especially if the discount rate for tax shields is not equal to either the cost of debt or the cost of unlevered equity. Nor does the finance literature identify the impact that growth and the discount rate for the tax shield have on the cost of capital and systematic risk. This paper fills that gap in the literature.

As we show later in this paper, growth and its interaction with the discount rate for the tax shield have a major impact on systematic risk, the cost of equity, and the cost of capital. For example, using typical values for the tax rate, capital structure, and observed levered beta, even a modest growth rate of 5% causes the widely-used Hamada adjustment to underestimate significantly the unlevered beta, leading to an unlevered cost of equity that is too low by 86 basis points. Alternately, if the appropriate discount rate for the tax shield is the unlevered cost of equity rather than the cost of debt, then applying the M&M-Hamada adjustment to a typical firm results in an estimate of the unlevered cost of equity that is too high by about 35 basis points. These biases in the estimated unlevered cost of equity are large enough to cause economically meaningful errors in the valuation of a firm, even if free cash flows are correctly estimated.

We also show that if the tax shields of a growing firm are discounted at a rate less than the unlevered cost of equity, then two unusual results can occur. First, the levered cost of equity can actually be *smaller* than the unlevered cost of equity! Second, the cost of capital decreases as growth increases, implying that high growth firms should have large amounts of debt in their capital structures. These two results are inconsistent with intuition and observation of actual practices, and suggest that the CAPV is the appropriate model with tax shields being discounted at the unlevered cost of equity.

The remainder of the paper is organized as follows. Section II is a brief literature review. Section III presents the equations that define firm value, the cost of capital, the levered cost of equity, and systematic risk as functions of growth, the discount rate for the tax shield, and capital structure. Section IV demonstrates the impact of growth and the discount rate for the tax shield with a numerical example. Section V is a discussion and a brief summary.

## **II. Literature Review**

The impact of leverage on the value of a firm and its cost of capital and cost of equity has been analyzed extensively in the finance literature, beginning with the seminal works of Modigliani and Miller (M&M) (1958, 1963). Their analysis included corporate taxes but not personal taxes. In addition, they assumed that the growth rate of free cash flow is zero, that the appropriate discount rate for the tax shield of debt is the interest rate on the debt, and that the firm has only debt and equity in its capital structure. Based on these assumptions, they derived the relationship between leverage and the value of the firm, the cost of capital, and the levered

cost of equity.<sup>1</sup> Using the M&M assumptions and also assuming that the debt is riskless, Hamada (1972) identified the relationship between leverage and systematic risk. Miller (1977) extended the original M&M analysis by incorporating the impact of personal taxes. Conine (1980, 1980) further extended the analysis by allowing the capital structure to include risky debt and risky preferred stock, and Ehrhardt and Shrieves (1995) extended the Conine analysis by allowing the capital structure to include warrants and convertible securities. In summary, these studies extended the original M&M work along the dimensions of more complicated tax regimes and more complicated capital structures.

A separate line of research focuses on the choice of a discount rate for the interest tax shield. M&M assumed that the risk of the interest tax shield is the same as the risk of the underlying debt, so the tax shield should be discounted at the interest rate on the debt. Other authors, beginning with Miles and Ezzell (1980) and Ezzell and Miles (1983) argued that the tax shield is riskier than the debt itself. If a firm maintains a constant capital structure, then the amount of debt will depend on the value of the firm. Thus, they argued that the tax shield is as risky as the underlying assets, and should be discounted at the unlevered cost of equity.<sup>2</sup> They analyzed the issue in discrete time, and assumed that the tax shield for the first year should be discounted at the cost of debt, but that subsequent tax shields should be discounted at the unlevered cost of equity. Harris and Pringle (1985) argued that all tax shields, including the first, should be discounted at the unlevered cost equity, and they provided an analysis based on this assumption. Taggart (1991) provides a nice synthesis of these results.

Along these same lines, Luehrman (1997) argued that the appropriate discount rate for the tax shield should be between the cost of debt and the cost of unlevered equity. Although Luehrman's argument is reasonable and is likely to be endorsed by practitioners, the existing literature does not actually show how an arbitrary discount rate for the tax shield (i.e., one that is not equal to either the cost of debt or the cost of unlevered equity) affects the value of the firm, the cost of capital, the cost of levered equity, or systematic risk.

 1 M&M did express the value of a firm within the context of a two-stage model, but they showed the relationship between leverage and the cost of capital only under the zero-growth assumption.

<sup>2</sup> Another source of risk is the possibility that earnings before interest and taxes will not be greater than the interest expense. In this case, the tax shield may still be valuable in the current period if the firm can use tax-loss carrybacks. Otherwise the loss must be carried forward. It is also possible that the tax shield will be valuable to an acquiring firm that has tax liabilities. However, these solutions are costly in the sense that there will be a loss due to the time value of money if the tax shield is carried forward and a loss due to transaction costs if the firm is acquired.

To the best of our knowledge, only Lewellen and Emery (1986) have analyzed the case of a firm with non-zero growth. They examine three specific scenarios: (1) the M&M scenario in which the cost of debt is the discount rate for the tax shield; (2) the Harris and Pringle scenario in which the unlevered cost of equity is the discount rate for the tax shield; and (3) the Miles and Ezzell scenario in which the first tax shield is discounted at the cost of debt and subsequent tax shields are discounted at the unlevered cost of equity. For each scenario, they show the value of a levered firm, but not the impact of leverage on the cost of capital, the levered cost of equity, or systematic risk.

In summary, there are some significant gaps in the literature. First, virtually all corporate valuation models assume non-zero growth, but the only analysis in the existing literature for the case of a growing firm focuses on the value of the firm and does not address the impact of growth and leverage on the cost of capital, the cost of levered equity, or systematic risk. Second, all of the existing analyses focus on two special cases with respect to the discount rate for the tax shield: (1) the discount rate is equal to the cost of debt; or (2) the discount rate is equal to the unlevered cost of equity. None of the existing analyses shows the impact that the choice of the discount rate for the tax shield has on the value of the firm, the cost of capital, the cost of levered equity, or systematic risk.

### **III. The Impact of Growth and the Tax Shield Discount Rate**

Only the results of our analysis are shown in the text; full derivations are in the appendix. For expositional clarity we assume only corporate taxes; the results are easily extended to include personal taxes. Because we derive our results in continuous rather than discrete time, we implicitly assume that the appropriate discount rate for the interest tax shield is constant, rather than different in the first period. We believe this is a reasonable approximation, given the prevalence of floating rate debt, the variation of debt balances during the year, and the relatively small contribution to value made by the first tax shield in an infinite stream of tax shields.

### **III.A. Firm Value and the Cost of Capital**

Table 1 defines the value of a levered firm (VL) and its cost of capital (WACC) for four different sets of assumptions. The first row in Table 1 shows the general APV in which the growth rate (g) and the discount rate for the tax shield (kTS) can take on any arbitrary values.

| <p>The second row shows the original APV of Myers, which allows the growth rate to be any value but which restricts the discount rate on the tax shield to be equal to the rate on debt (i). The third row shows the Compressed APV (CAPV), so named by Kaplan and Ruback (1995), in which the growth rate can be any value but which restricts the discount rate on the tax shield to be equal to the unlevered cost of equity (<math>k_{eU}</math>).<sup>3</sup> The fourth row shows the well-known M&amp;M results, in which growth is equal to zero and the discount rate for the tax shield is equal to the cost of debt. For the remainder of our analysis we assume <math>g &lt; k_{TS}</math>; otherwise, the discounted value of the tax shield would be infinitely large. We also assume that the appropriate rate for discounting the tax shield is bounded below by the interest rate on the debt and bounded above by the unlevered cost of equity: <math>i \leq k_{TS} \leq k_{eU}</math>.</p> |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The first column in Table 1 shows the value of a levered firm as the sum of the value of an unlevered firm (VU) and the value of the tax shield (VTS, shown as the second term in the expressions in the first column). Comparing the second and fourth rows, the value of the tax shield in Myers' APV is always greater than the value of the tax shield under M&M. This is not surprising, since the value of a growing tax shield is always larger than the value of a constant tax shield. The value of the tax shield in the CAPV is always lower than that of Myers' APV, because the tax shield is discounted at a higher rate with the CAPV than with Myers' APV. The value of the tax shield for the CAPV may be either higher or lower than the value of the tax shield under M&M, depending on the relative magnitudes of the growth rate and the unlevered cost of capital.

The second column shows the cost of capital. Rather than express the cost of capital as an explicit function of the levels of the current market values of debt (D0) and equity (E0), we follow the convention in the existing literature and express the cost of capital as a function of the percentage of debt: wD = D0/(D0+E0). However, care must be taken to apply these relationships only for valid values of wD. Surprisingly, not all values of wD that are less than 100% are valid. As the dollar-value of debt in a firm increases, the size of the debt tax shield also increases. This additional value accrues to the equity holders, and hence both D0 and E0 in the expression wD = D0/(D0+E0) increase as D0 increases. Using the expression for firm value as shown in the first

 3 The regular APV discounts separately the free cash flow and the tax shield. To find free cash flow, it is necessary to find the net operating profit after taxes (NOPAT) and the investment in capital. In the CAPV, there is no need to identify separately NOPAT and the tax shield, since both are discounted at the unlevered cost of equity. Instead, the cash flow is defined as net income less the investment in capital, and it is discounted at the unlevered cost of equity.

column and first row of Table 1, the appendix demonstrates that there is an upper limit on  $w_D$  as debt goes to infinity:

$$w_D \leq \frac{k_{TS} - g}{iT}. \quad (1)$$

This constraint is not binding (i.e., less than 100%) for the M&M model in which  $g$  is zero,  $k_{TS}$  is equal to  $i$ , and  $T$  is less than one. However, for other reasonable values of  $g$  and  $k_{TS}$ , this constraint does become binding. For consistency with the previous literature, we will continue to use  $w_D$  in the expressions for rates of return and also for systematic risk, but with the implicit assumption that  $w_D$  is chosen such that it does not violate the constraint in equation (1).

The Appendix shows that for the general APV the partial derivative of the cost of capital with respect to growth, holding  $w_D$  constant, is strictly negative for  $k_{TS} < k_{eU}$ , which is also the case for Myers' APV. In contrast, this partial derivative is zero when  $k_{TS} = k_{eU}$ , which is the case for the CAPV. In other words, the cost of capital is a decreasing function of the growth rate for both the general APV and Myers' APV, but the CAPV expression for the cost of capital is independent of growth. Even though growth has a large impact on the CAPV value of the firm, as shown in Table 1, growth does not affect the CAPV cost of capital.

The intuition behind these contrasting results can be seen by examining the expression for the value of a firm in the first column of Table 1. Letting  $FCF_0$  denote the free cash flow at time zero, the value of the levered firm is:

$$V_L = V_U + V_{TS} = \frac{FCF_0}{(k_{eU} - g)} + \left( \frac{iTD_0}{k_{TS} - g} \right). \quad (2)$$

The cost of capital satisfies

$$\frac{FCF_0}{WACC - g} = V_U + V_{TS} \quad (2a)$$

so that

$$WACC = \frac{FCF_0}{V_U + V_{TS}} + g. \quad (2b)$$

The first term in equation (2b) is the "free cash flow yield," and the cost of capital is the sum of this "free cash flow yield" and the growth rate. Inspection of equation (2) shows that an increase in g causes VU and VTS to increase, which decreases the free cash flow yield in equation (2b). If kTS = keU, as in the CAPV, then an increase in growth, but holding wD fixed, causes V<sup>U</sup> and VTS to increase by enough so that the decline in the free cash flow yield in equation (2b) is just sufficient to offset the increase in g, leaving WACC constant. When kTS < keU (which is the case for the general APV and Myers' APV) the partial derivative of the present value of the tax shield with respect to growth is larger than when kTS = keU. Thus when kTS < keU, an increase in growth causes a larger increase in VTS, leading to a decline in the free cash flow yield in equation (2b) that is greater than the increase in g. The net effect is a decrease in the cost of capital with increasing growth for the general APV and Myers' APV.

The costs of capital in Table 1 can be ranked in the following descending order:

#### *WACC for CAPV > WACC for M&M > WACC for Myers' APV.*

Given the same tax rate, unlevered cost of equity, cost of debt, and capital structure, the CAPV leads to the highest cost of capital. This is not surprising, since tax shields are discounted at the highest rate in the CAPV. If the appropriate discount rate for the tax shield is the unlevered cost of equity, then the CAPV is the appropriate model and the application of the M&M equation for the cost of capital results in a downward biased estimate of the cost of capital, irrespective of growth. On the other hand, if the firm is growing and the appropriate discount rate is the cost of debt, then Myers' APV is the appropriate model and the M&M equation gives an upward biased estimate of the cost of capital. In other words, the M&M expression for the cost of capital almost certainly is biased, given that most firms are expected to grow. In fact, it is unbiased only if the following condition is true:

$$\left(\frac{k_{eU}-g}{k_{TS}-g}\right)\left(\frac{i}{k_{eU}}\right)=1 . \quad (3)$$

The following example illustrates these points. Consider an unlevered firm with an unlevered cost of equity of 10.6% and an expected constant growth rate of 5.0%. It has a corporate tax rate of 34% and is planning on recapitalizing so that its capital structure will have 35% debt at an interest rate of 8.0%. Table 2 shows the resulting costs of capital under the four different sets of assumptions. Myers' APV assumes that the firm will grow at 5.0% and that the tax shield should be discounted at the cost of debt. This results in a cost of capital of 8.82%.

Suppose instead that the M&M equations were used, in which growth is ignored and the tax shield is also discounted at the cost of debt. This results in a cost of capital of 9.34%, which is 52 basis points higher than the cost of capital from Myers' APV. In other words, even if the correct discount rate for the tax shield is the cost of debt, ignoring growth leads to a cost of capital that is biased upwards by 52 basis points.

On the other hand, if the tax shield should be discounted at the unlevered cost of equity, as in the CAPV, then the cost of capital is 9.65%. In this case, the M&M expression results in a downward bias of 31 basis points, irrespective of growth. The difference between the estimates of Myer's APV and the CAPV is 83 basis points. This range is certainly sufficient to induce significant valuation errors if the wrong set of assumptions is used in obtaining the cost of capital.

As an intermediate case, suppose, that the tax shield should be discounted at a rate somewhere between the cost of debt and the unlevered cost of equity, such as 9.3%. As the row for the general case in Table 2 shows, the expected cost of capital is 9.36%. Interestingly, this is very close to the M&M cost of capital of 9.34%. The reason for the rough correspondance of these estimates is that the M&M model's errors are offsetting for these parameter choices: (1) the M&M model assumes a growth rate of zero when the actual growth rate is 5.0%, which biases its cost of capital estimate upwards; and (2) the M&M model assumes an 8.0% discount rate for the tax shield when it should be 9.3%, which biases its cost of capital estimate downwards. As Table 2 shows, two wrongs almost make a right for this example. For these parameters the value of equation (3) is 0.98. If equation (3) had been exactly equal to 1.0, then M&M would be unbiased relative to the general case.

.

#### **III.B. The Cost of Equity and Systematic Risk**

Table 3 shows the relationships for the levered cost of equity ( $k_{el}$ ) and systematic risk of equity ( $\beta_{el}$ ) under the four different sets of assumptions. Not surprisingly, many of the results for the cost of capital also apply to the levered cost of equity and systematic risk. For example, the levered cost of equity and the levered beta can be ranked in the same order as the cost of capital:

*keL for CAPV > keL for M&M > keL for Myers' APV;*

*$$\beta_{el}$$
 for  $CAPV > \beta_{el}$  for  $M$ & $M$ /Hamada >  $\beta_{el}$  for Myers'  $APV$ .*

As with the cost of capital, the levered cost of equity and systematic risk are explicit functions of the growth rate in the general case and Myers' APV, but they are not functions of growth for the CAPV. Also, the M&M/Hamada expressions for the levered cost of equity and systematic risk will be biased unless equation (3) holds.

In addition to reinforcing some of the results from Table 1, Table 3 provides some new insights. First, notice that the CAPV expressions for the levered cost of equity and systematic risk are the same as the original 1958 results of M&M in which they ignored taxes. This is somewhat surprising, since Table 1 shows the large impact that the tax rate has on the value of the firm and the cost of capital in the CAPV case. Despite this, the tax rate does not affect the CAPV cost of equity or systematic risk. The reason for this can be seen by comparing a definitional expression for the cost of capital to that of the general case in the first row of Table 1:

Definition: 
$$\text{WACC} = (1\text{-w}_{\text{D}})\text{k}_{\text{L}} + \text{w}_{\text{D}}(1\text{-T}) = (1\text{-w}_{\text{D}})\text{k}_{\text{L}} + \text{w}_{\text{D}} - \text{w}_{\text{D}}\text{T}$$

versus

Table 1: 
$$\text{WACC} = k_{\text{eU}} - \left( \frac{k_{\text{eU}} - g}{k_{\text{TS}} - g} \right) i \text{T} \ w_{\text{D}} \ .$$

In the definitional expression, the cost of capital is expressed as the weighted average of the levered cost of equity and the pre-tax cost of debt, reduced by an amount equal to the periodic tax savings on the debt. In the expression from Table 1, the cost of capital is the unlevered cost of equity, reduced by an amount to account for the present value of all of the future debt tax shields. In the CAPV, the reduction to account for the present value of the future debt tax shields happens to be exactly equal to the reduction in the generic expression due to the periodic tax savings on the debt because the tax shield is discounted at keU. If kTS < keU, the two reductions do not cancel, and the resulting levered cost of equity is a function of g, kTS, and T.

A second insight comes from close examination of the equation in row 2 of Table 3 for the levered cost of equity under the Myers' APV assumptions. It is straightforward to show that if g is sufficiently large:

| $i(1-T) - g < 0,$ | (4) |
|-------------------|-----|
|-------------------|-----|

then *the levered cost of equity is less than the unlevered cost of equity!* In other words, the tax shield of interest adds so much value to the firm relative to the value of the firm's other cash flows that the levered cost of equity goes down. Notice that equation (4) is likely to be true for reasonable values of i, T, and g. For example, suppose i=8%, T=34%, and g=5.5%. The value of equation (4) is –0.2%. If the unlevered cost of equity is 10.6% and WD is 35%, then application of the Myers' APV from the second row of Table 2 shows that the levered cost of equity is 10.48%, which is higher than the unlevered cost of equity. In contrast, inspection of the CAPV relationship for the levered cost of equity in the third row of Table 2 shows that the CAPV levered cost of equity must always be greater than the unlevered cost of equity, given that the unlevered cost of equity is greater than the cost of debt. The reason for these markedly different results is that under the CAPV the tax shields are discounted at the same rate as the free cash flows; different values of g cannot change the relative magnitudes of VU and VTS. However, if kTS < keU, then larger growth rates increase the magnitude of VTS relative to VU, driving keL below keU for sufficiently large g.

#### **IV. The Magnitude of Typical Estimation Errors**

There are two common applications of the expressions shown in Tables 1 and 3. The first application is the use of the APV approach in estimating the value of a firm. In this application, an estimate of the unlevered cost of equity is required, which usually is derived from an observable cost of equity. This observed cost of equity usually is the levered cost of equity for the firm in question or that of a similar firm. The second common application is the estimation of the cost of equity that results from a change in capitalization. The unlevered cost of equity is derived from the observed levered cost of equity given the current capital structure, and the new levered cost of equity is estimated based on the new capital structure. This same approach often is used when estimating the cost of equity for a non-traded company. The following sections show typical estimation errors when incorrect assumptions are employed. As the examples indicate, these estimation errors are large enough to be economically meaningful.

#### **IV.A. Errors when Estimating the Unlevered Cost of Equity**

Consider a typical firm whose observed (i.e., levered) beta is equal to 1.0. The risk-free rate is 5.5% and the market risk premium is 6.5%. Using the CAPM, these imply a levered cost of equity of 12.0%. The firm is financed with risky debt and equity, and has a target capital structure of 35% debt. The interest rate on the debt is 8%, which implies a debt beta of 0.38. The tax rate is 34%, and the expected annual growth rate is 5%. Table 4 shows the estimates of the unlevered equity beta and unlevered cost of equity that would be obtained using Myers' APV, the CAPV, and M&M. The beta estimates range from a low of 0.78 for the CAPV to a high of 0.97 for Myers' APV, while the unlevered costs of equity range from 10.60% to 11.81%. The range in estimates for the unlevered cost of equity is 121 basis points, which is large enough to cause economically meaningful errors in the resulting valuation.

If the cost of debt is the appropriate rate for discounting the tax shield, then either Myers' APV or the M&M model should be used. Since the firm in this example is growing, the unlevered cost of equity of 11.81% from Myers' APV should be used. If instead the well-known M&M/Hamada model is used, then the (incorrect) estimate of the unlevered cost of equity is 10.95%. For the typical firm in this example, incorrectly ignoring growth results in an estimated unlevered cost of equity that is 86 basis points lower than the true unlevered cost of equity.

Suppose an analyst correctly includes growth, but uses the wrong discount rate for the tax shield. In particular, suppose that the unlevered cost of equity is the appropriate discount rate for the tax shield. The CAPV should be used, resulting in an unlevered cost of equity of 10.60%. If the analyst incorrectly uses the Myers' APV, the estimated unlevered cost of equity is 11.81%. This is an error of 121 basis points, which will lead to large errors when estimating the value of the company.

### **IV.B. Errors when Estimating Levered Cost of Equity in a Recapitalization or Non-Traded Company**

A second application of the equations in Tables 1 and 3 involves changes in capital structure. Suppose an analyst wishes to estimate the new cost of equity that will result from a recapitalization, or the cost of equity for a non-traded company or a division within a traded company. In the case of a recapitalization, the analyst begins with the observed beta for the firm in question. In the case of estimating the cost of equity for a non-traded company, the analyst begins with the observed beta for a similar publicly traded company. In both cases, the first step is to find the unlevered cost of equity implied by the observed beta and the current capital structure. In a recapitalization, the second step is to "re-lever" the cost of equity, using the capital structure that is expected after the change in capital structure. In estimating of the cost of equity for a non-traded company, the second step is to "re-lever" the unlevered cost of equity using the capital structure of the non-traded company.

Suppose the analyst chooses the wrong model when unlevering the cost of equity, and chooses the same model when re-levering the cost of equity. How much difference will this make in the resulting cost of equity? In other words, do two wrongs make a right? We begin with the same typical firm whose unlevering is shown in Table 4. Suppose the old capital structure had 35% debt at a rate of 8%. The new capital structure has 55% debt at a rate of 8.3%, and growth is 5%. Table 5 shows the results of the re-levering.

Myers' APV and the M&M/Hamada model share the same assumption about the discount rate for the tax shield (kTS = i) but make different assumptions about the growth rate. Suppose the assumed discount rate for the tax shield is appropriate, but that the M&M-Hamada model is used instead of the correct Myers' APV model. The M&M-Hamada model results in an estimated levered cost of equity of 13.09% which is 66 basis points higher than the true 12.43%, of the Myers' APV model.

On the other hand, suppose the analyst includes the correct growth rate, but is uncertain whether the discount rate for the tax shield should be the cost of debt or the cost of unlevered equity. Table 5 shows that the levered cost of equity from the Myers' APV is 12.43%, while the unlevered cost of equity from the CAPV is 13.41%, a difference of 98 basis points.

As this example shows, accurate results cannot be obtained simply by picking a model and using it consistently; i.e., using the same model to unlever and re-lever. Ignoring growth leads to large errors in the estimated cost of equity. Furthermore, the choice of the appropriate discount rate for the tax shield leads to large differences in the estimated cost of levered equity.

## **V. Summary and Discussion**

An estimate of the unlevered cost of equity is necessary for many applications of corporate valuation. However, the widely used M&M/Hamada formula is based on two assumptions that may not be true. First, the M&M formula assumes that the firm will not grow. This assumption is almost certainly violated in practice, since almost all firms are expected to grow. Applying the M&M/Hamada formula to a growing firm leads to large errors in the estimates of the unlevered beta and unlevered cost of equity. As we show, even modest growth of 5% causes the M&M/Hamada estimate of the levered cost of equity to be 86 basis points too low relative to Myers' APV, even though both models discount the tax shield at the same rate.

A second issue is the choice of discount rate for the tax shield. The M&M and Myers' APV models assume that the discount rate for the tax shield should be the cost of debt. However, there are sound arguments for using a larger rate, perhaps even as high as the unlevered cost of equity. We provide specific formulas for the general APV case in which the discount rate can be any value.

If the appropriate discount rate should be the unlevered cost of equity, the M&M/Hamada adjustment produces an unlevered beta that is higher than the true beta. For a typical company, this causes the M&M formula to estimate an unlevered cost of equity that is 35 basis points too high relative to the true unlevered cost of equity.

A typical use for these models is to unlever a firm's cost of equity and then re-lever it with a different capital structure. We show that if the incorrect model is first used to unlever a firm's cost of equity, and then to re-lever it, large estimation errors still result. In other words, consistent use of the same model doesn't prevent large estimation errors; i.e., two wrongs don't make a right.

This implies that despite its widespread use by practitioners, researchers, and textbook writers, it is almost always inappropriate to use the M&M/Hamada model, since virtually all firms are expected to grow. Using this model inappropriately leads to errors in the estimated costs of equity that are large enough to be economically significant. Given that growth should be incorporated explicitly into the model, the only remaining decision is the choice of discount rate for the tax shield. Should the discount rate for the tax shield equal the cost of debt, the unlevered cost of equity, or some value in between?

Unfortunately, there are no empirical tests to provide an answer to this question, and two major econometric problems will confound future research in this area. First, the unlevered beta and unlevered cost of equity for a firm are unobservable. Second, there are large measurement errors in the other required variables. If empirical tests are unable to provide definitive answers, then guidance for the choice of a discount rate for the tax shield must be sought elsewhere.

We show that using the cost of debt as the discount rate for the tax shield can lead to a levered cost of equity that is less than the unlevered cost of equity. Since this contradicts both intuition and casual observations of levered firms, we believe that a rate higher than the cost of debt should be used. In fact, for sufficiently large growth rates, the levered cost of equity can be less than the unlevered cost of equity when any rate less than the unlevered cost of equity is used to discount the tax shield. This effect diminishes as the discount rate for the tax shield approaches the unlevered cost of equity, which suggests to us that discount rate for the tax shield ought to be closer to the unlevered cost of equity than to the cost of debt.

We also show that if a rate less than the unlevered cost of equity is used to discount the tax shield, then the partial derivative of the cost of capital with respect to growth is negative, and it becomes more negative for higher degrees of leverage. Taken alone, this would imply that a high growth firm could substantially reduce its cost of capital, and hence increase its value, if it had a high degree of leverage. But this is inconsistent with the observed capital structures of high growth firms, which typically have low levels of debt. Although there are other explanations for this phenomenon, such as agency costs and asymmetric information, this suggests once again that a relatively high rate, perhaps even the unlevered cost of equity itself, should be used to discount the tax shield of debt.

| <b>Table 1: Leverage, Value, and the Cost of Capital</b>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                       |                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <b>Value of the Firm</b>                              | <b>Cost of Capital</b>                                               |
| <b>General APV</b>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | $V_L = V_U + \left( \frac{iTD_0}{k_{TS} - g} \right)$ | $WACC = k_{eU} - \left( \frac{k_{eU} - g}{k_{TS} - g} \right) iTW_D$ |
| <b>Myers' APV</b><br>$k_{TS} = i$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | $V_L = V_U + \left( \frac{iTD_0}{i - g} \right)$      | $WACC = k_{eU} - \left( \frac{k_{eU} - g}{i - g} \right) iTW_D$      |
| <b>Compressed APV</b><br>$k_{TS} = k_{eU}$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | $V_L = V_U + \left( \frac{iTD_0}{k_{eU} - g} \right)$ | $WACC = k_{eU} - iTW_D$                                              |
| <b>M&amp;M</b><br>$k_{TS} = i$<br>$g = 0$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | $V_L = V_U + TD_0$                                    | $WACC = k_{eU} - iTW_D$                                              |
| <p>Note: <math>V_L</math> denotes the value of a levered firm; <math>V_U</math> denotes the value of an otherwise identical but unlevered firm; <math>D_0</math> denotes debt at time zero; <math>k_{TS}</math> denotes the appropriate discount rate for the tax shield; <math>i</math> denotes the interest rate on debt; <math>WACC</math> denotes cost of capital (i.e., weighted average cost of capital); <math>T</math> denotes the corporate tax rate; <math>g</math> denotes the growth rate of free cash flows and debt; and <math>w_D</math> denotes the percent of the firm that is financed with debt.</p> |                                                       |                                                                      |

**Table 2: The Combined Impact of Growth and the Tax Shield Discount Rate on the Cost of Capital**

|                | Growth | Tax Shield Discount Rate | Cost of Capital |
|----------------|--------|--------------------------|-----------------|
| General APV    | 5.0%   | 9.3%                     | 9.36%           |
| Myers' APV     | 5.0%   | 8.0%                     | 8.82%           |
| Compressed APV | 5.0%   | 10.6%                    | 9.65%           |
| M&M            | 0.0%   | 8.0%                     | 9.34%           |

Notes: The target capital structure has 35% debt. The unlevered cost of equity is 10.6%, the tax rate is 34%, and the interest rate on debt is 8.0%

**Table 3: Leverage, the Cost of Equity, and Systematic Risk**

|                                                  | Levered Cost of Equity                                                                                                                                     | Systematic Risk                                                                                                                                                     |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <b>General APV</b>                               | $k_{eL} = k_{eU} +$<br>$\left[ k_{eU} \left( 1 - \frac{iT}{k_{TS} - g} \right) - i \left( 1 - \frac{k_{TS} T}{k_{TS} - g} \right) \right] \frac{w_D}{w_E}$ | $\beta_L = \beta_U \left( 1 + \frac{w_D}{w_E} \right) - \beta_D \frac{w_D}{w_E}$<br>$- (\beta_U - \beta_{TS}) \left( \frac{iT}{k_{TS} - g} \right) \frac{w_D}{w_E}$ |
| <b>Myers' APV</b><br>$k_{TS} = i$                | $k_{eL} = k_{eU} +$<br>$(k_{eu} - i) \left( 1 - \left( \frac{i}{i - g} \right) T \right) \frac{w_D}{w_E}$                                                  | $\beta_L = \beta_U \left( 1 + \left( 1 - \frac{iT}{i - g} \right) \frac{w_D}{w_E} \right) -$<br>$\beta_D \left( 1 - \frac{iT}{i - g} \right) \frac{w_D}{w_E}$       |
| <b>Compressed APV</b><br>$k_{TS} = k_{eU}$       | $k_{eL} = k_{eU} + (k_{eu} - i) \frac{w_D}{w_E}$                                                                                                           | $\beta_L = \beta_U \left( 1 + \frac{w_D}{w_E} \right) - \beta_D \frac{w_D}{w_E}$                                                                                    |
| <b>M&amp;M/Hamada</b><br>$k_{TS} = i$<br>$g = 0$ | $k_{eL} = k_{eU} + (k_{eu} - i)(1 - T) \frac{w_D}{w_E}$                                                                                                    | $\beta_L = \beta_U \left( 1 + (1 - T) \frac{w_D}{w_E} \right) -$<br>$\beta_D (1 - T) \frac{w_D}{w_E}$                                                               |

Note:  $k_{eU}$  denotes the cost of equity of an unlevered firm;  $k_{eL}$  denotes the cost of equity of a levered firm;  $k_{TS}$  denotes the appropriate discount rate for the tax shield;  $i$  denotes the interest rate on debt;  $T$  denotes the corporate tax rate;  $g$  denotes the growth rate of free cash flows and debt;  $\beta_U$  denotes systematic risk of an unlevered firm;  $\beta_L$  denotes systematic risk of equity in a levered firm;  $\beta_D$  denotes systematic risk of debt;  $\beta_{TS}$  denotes systematic risk of the tax shield;  $w_D$  denotes the percent of the firm that is financed with debt; and  $w_E$  denotes the percent of the firm that is financed with equity.

**Table 4: Unlevering Beta and the Cost of Equity for a Typical Firm**

|                | Unlevered Equity Beta | Unlevered Cost of Equity |
|----------------|-----------------------|--------------------------|
| Myers' APV     | 0.97                  | 11.81%                   |
| Compressed APV | 0.78                  | 10.60%                   |
| M&M            | 0.84                  | 10.95%                   |

Notes: The current target capital structure is 35% debt and the tax rate is 34%. The levered beta is 1.0 and the levered cost of equity is 12%. The interest rate on debt is 8.0%, implying a debt beta of 0.38. The expected growth rate is 5%.

**Table 5: Re-levering Systematic Risk and the Cost of Equity to Reflect a Different Capital Structure**

|                | Unlevered Cost of Equity | Results of unlevering at the old capital structure. Unlevered Beta | Levered Cost of Equity | Results of re-levering at the new capital structure Levered Beta |
|----------------|--------------------------|--------------------------------------------------------------------|------------------------|------------------------------------------------------------------|
| Myers' APV     | 11.81%                   | 0.97                                                               | 12.43%                 | 1.07                                                             |
| Compressed APV | 10.60%                   | 0.78                                                               | 13.41%                 | 1.22                                                             |
| M&M            | 10.95%                   | 0.84                                                               | 13.09%                 | 1.17                                                             |

Notes: The unlevered beta and unlevered costs of equity are from Table 4. The new target capital structure is comprised of 55% debt (at an interest rate of 8.3%) and 45% equity. All other parameters are the same as in Table 4.

## **Appendix**

VL denotes the value of a levered firm at time 0, VU denotes the value of an otherwise identical but unlevered firm at time 0, FCFt denotes free cash flow at time t, and let keU denote the cost of equity of an unlevered firm. Free cash flow is the amount of cash available for distribution to all investors, after the firm has paid all costs and made all capital investments necessary to support the growth in sales. In particular, we define free cash flow as net operating profit after taxes (NOPAT) less investment in capital, where capital is defined as the sum of net operating working capital (NOWC) and net plant, property, & equipment (PPE). NOWC is the difference between the operating current assets, such as inventory and receivables, and the operating current liabilities, such as payables and accruals. See Copeland, Koller, and Murrin (1990) or Brigham, Gapenski, and Ehrhardt (1999) for a more detailed explanation of the calculation of free cash flow.

The value of an unlevered firm is the present value of the expected free cash flows discounted at the unlevered cost of equity:

$$V_U = \int_0^\infty FCF_t e^{-k_{eu} t} dt . \quad (A1)$$

The value of a levered firm is the sum of the present value of its free cash flows, the present value of the expected interest deduction tax shields, the present value of expected bankruptcy costs, and the present value of any expected agency costs or benefits due to debt. Let TSt denote the expected tax shield at time t, BCt denote the expected bankruptcy costs at time t, and ACt denote the expected agency costs or benefits at time t. Also, let kTS, kBC, and kAC denote the appropriate discount rates for the debt tax shield, expected bankruptcy costs, and expected agency costs. In the most general case, these discount rates may themselves be functions of other state variables, including time, free cash flows, tax shields, bankruptcy costs, and agency costs. The value of a levered firm can then be written as:

$$V_L = V_U + \int_0^\infty TS_t e^{-k_{TS} t} dt + \int_0^\infty BC_t e^{-k_{BC} t} dt + \int_0^\infty AC_t e^{-k_{AC} t} dt . \quad (A2)$$

In general, free cash flow is determined by NOPAT and capital expenditures, which may themselves be complex functions of other state variables and time. For example, free cash flows may be adversely affected by high probabilities of bankruptcy, as suppliers tighten credit

standards. To simplify matters, we assume that there is a stable proportional relationship between sales (St denotes sales at time t) and NOPAT. NOPAT can be written as:

NOPATt = ATOPM St, (A3)

where ATOPM is the after tax operating profit margin. Similarly, assuming that capital is proportional to sales yields:

Capitalt = CRR St, (A4)

where CRR is the capital requirement ratio (i.e., the ratio of capital to sales). Under these assumptions, the rate of capital expenditures is equal to the CRR multiplied by the rate of growth in sales.

For the case of constant growth in sales,

$$S_t = S_0 e^{gt}$$
, (A5)

where g is the growth rate in sales. These relationships allow free cash flow to be expressed in terms of sales in an intuitive fashion:

FCFt = (ATOPM – CRR g) St. (A6)

Under these assumptions and the additional assumption that the growth rate is less than the unlevered cost of equity (i.e., g < keU), the value of an unlevered firm is:

$$V_U = \int_0^\infty FCF_t e^{-k_{eU} t} dt = \int_0^\infty (ATOPM - CRR g) S_t e^{-k_{eU} t} dt = \frac{(ATOPM - CRR g) S_0}{k_{eU} - g}. \quad (A7)$$

Ignoring expected bankruptcy costs and agency costs, the value of a levered firm is equal to the value of an unlevered firm plus the present value of the interest payment tax shields. Let i denote the interest rate on debt, Dtdenote the amount of debt at time t, and wD denote the proportion of the firm's market value that is financed with debt. For a constant growth firm with a constant capital structure, the assumptions above imply that,

| $D_t = D_0 e^{gt}$ | (A8) |
|--------------------|------|
|--------------------|------|

where D0 is the initial amount of debt. Notice that D0 can also be expressed as wD VL.

Under the assumption that growth, interest rates, and the tax rate are all constant, and that the growth rate is less than the discount rate for the tax shield (i.e., g < kTS), the value of the tax shield is:

$$V_{TS} = \int_0^\infty i T D_0 e^{gt} e^{-k_{TS} t} dt = \left( \frac{i}{k_{TS} - g} \right) T D_0. \quad (A9)$$

$$V_L = V_U + \left( \frac{i}{k_{TS} - g} \right) T D_0 \quad (A10)$$

Equation (A10) is shown in the text as the first row of the first column in Table 1. The remainder of the first column of Table 1 can easily be found by specifying specific values of  $k_{TS}$  and  $g$  and simplifying Equation (A10).

Equation (A10) has implications for the range of possible values of  $w_D$  given a growing tax shield. Using the definition  $w_D = D_0/V_L$ , substituting Equation (A10) and rearranging, gives an expression for  $w_D$ :

$$w_D = \frac{(k_{TS} - g)}{\left[ \left[ \frac{V_U(k_{TS} - g)}{D_0} \right] + iT \right]} \quad (A11)$$

As more and more debt is used, the value of tax shield, and hence the value of the equity, increases along with the debt, preventing  $w_D$  from increasing further. Examination of Equation (A11) shows that in the limit as  $D_0$  goes to infinity,  $w_D$  is constrained from above by  $(k_{TS} - g)/iT$ . Noting this constraint and substituting  $V_L w_D$  for  $D_0$  into Equation (A10) and rearranging, the value of a levered firm can be expressed as a function of  $w_D$  instead of  $D_0$ :

$$V_L = \frac{V_U}{1 - \left( \frac{i}{k_{TS} - g} \right) T w_D}. \quad (A12)$$

Equation (A12) is only meaningful if  $iT w_D / (k_{TS} - g) < 1$ . For combinations of low  $k_{TS}$ , high growth rate, high tax rate, high debt interest rate and high debt level, the value of the debt tax shield exceeds the value of the entire levered firm, and the constraint derived from Equation (A11) is violated.

By definition, the value of a levered firm is the present value of the free cash flows discounted at the weighted average cost of capital (WACC). Under our assumptions this is:

$$V_L = \frac{(ATOPM - CRR g) S_0}{WACC - g}. \quad (A13)$$

Substituting Equations (A7) and (A12) into (A13) and rearranging gives the following expression for the cost of capital for a levered firm:

$$WACC = k_{eU} - \left( \frac{k_{eU} - g}{k_{TS} - g} \right) i T w_D. \quad (A14)$$

Equation (A14) is shown in the second column and first row of Table 1 in the body of the text. The remainder of the second column of Table 1 can easily be found by specifying specific values of kTS and g and simplifying Equation (A14).

As Equation (A14) shows, unless keU=kTS, the cost of capital is an explicit function of growth. The partial derivative of Equation (14) with respect to g is:

$$\frac{\partial \text{WACC}}{\partial g} = -iT w_D \left( \frac{k_{eU} - k_{TS}}{(k_{TS} - g)^2} \right). \quad (\text{A15})$$

Since the unlevered cost of equity is defined to be greater than or equal to the discount rate on the tax shield, this partial derivative is always non-positive.

Also by definition, WACC is:

WACC k (1 w ) i(1 T) w . eL <sup>D</sup> -+-= <sup>D</sup> (A16)

Setting Equations (A14) and (A16) equal and rearranging gives an expression for the levered cost of equity for a constant growth firm and arbitrary discount rate for the debt tax shield:

$$\mathbf{k}_{el} = \mathbf{k}_{eu} + \left[ \mathbf{k}_{eu} \left( 1 - \frac{iT}{\mathbf{k}_{TS} - \mathbf{g}} \right) - i \left( 1 - \frac{\mathbf{k}_{TS} T}{\mathbf{k}_{TS} - \mathbf{g}} \right) \right] \frac{\mathbf{w}_D}{\mathbf{w}_E}. \quad (A17)$$

Equation (A17) is shown in the first column and first row of Table 3 in the body of the text. The remainder of the first column of Table 3 can easily be found by specifying specific values of kTS and g and simplifying Equation (A17).

The value of a levered firm can be expressed:

| $V_L = E_0 + D_0 = V_U + V_{TS}$ | (A18) |
|----------------------------------|-------|
|----------------------------------|-------|

Where E0 denotes the current market value of equity and VTS denotes the current value of the tax shield of interest payments.

The systematic risk of a firm is the weighted average of the systematic risks of the components of value. Let  $\beta_U$  denote the systematic risk of an unlevered firm,  $\beta_L$  denote the systematic risk of equity in a levered firm,  $\beta_D$  denote the systematic risk of debt, and  $\beta_{TS}$  denote the systematic risk of the tax shield. Using Equation (18), systematic risk can be expressed as:

$$\beta_U V_U + \beta_{TS} V_{TS} = \beta_L E_0 + \beta_D D_0. \quad (A19)$$

Rewriting Equation (A18) in terms of VU and substituting for VU in Equation (A19) yields:

| $\beta_U (E_0 + D_0 - V_{TS}) + \beta_{TS} V_{TS} = \beta_L E_0 + \beta_D D_0$ | (A20) |
|--------------------------------------------------------------------------------|-------|
|                                                                                |       |

Solving for  $\beta_L$ , substituting Equation (9) for the value of the tax shield, and rearranging provides and expression for the systematic risk of a levered firm.

$$\beta_L = \beta_U \left( 1 + \frac{w_D}{w_E} \right) - \beta_D \frac{w_D}{w_E} - (\beta_U - \beta_{TS}) \left( \frac{iT}{k_{TS} - g} \right) \frac{w_D}{w_E} \quad (A21)$$

Equation (A21) is shown in the second column and first row of Table 3 in the body of the text. The remainder of the second column of Table 3 can easily be found by specifying specific values of  $k_{TS}$  and  $g$  and simplifying Equation (A21).

#### **References**

Brigham, E.F., L.C. Gapenski, and M.C. Ehrhardt, 1999, *Financial Management: Theory and Practice*, 9th Edition, The Dryden Press, Fort Worth. Conine, T.E., Jr., 1980, "Corporate Debt and Corporate Taxes: An Extension," *Journal of Finance*, (September), 1033-1037. Conine, T.E., Jr., 1980, "Debt Capacity and the Capital Budgeting Decision: A Comment," *Financial Management*, (Spring), 20-22 Copeland, T., T. Koller, and J. Murrin, 1990, *Valuation: Measuring and Managing the Value of Companies*, John Wiley & Sons, New York. Ehrhardt, M.C., and R.E. Shrieves, 1995, "The Impact of Warrants and Convertible Securities on the Systematic Risk of Common Equity," *The Financial Review*, (Vol. 30, No. 4, November), 843-856. Ezzell, J., and J. Miles, 1983, "Capital Project Analysis and the Debt Transaction Plan," *Journal of Financial Research*, (Vol. 6, Spring), 25-31. Hamada, R.S., 1972, "The Effect of the Firm's Capital Structure on the Systematic Risk of Common Stocks," *Journal of Finance*, (May), 435-452. Harris, R.S., and Pringle, J.J., 1985, "Risk-Adjusted Discount Rates—Extensions from the Average-Risk Case," *Journal of Financial Research*, (Fall), 237-244. Inselbag, I., and H. Kaufold, 1997, "Two DCF Approaches for Valuing Companies Under Alternative Financing Strategies (And How to Choose Between Them)," *Journal of Applied Corporate Finance*, (Vol. 10, No. 1, Spring), 114-122. Kaplan, S.N. and R.S. Ruback, 1995, "The Valuation of Cash Flow Forecasts: An Empirical Analysis," *Journal of Finance*, (Vol. 50, No. 4, September), 1059-1093. Kaplan, S.N. and R.S. Ruback, 1996, "The Market Pricing of Cash Flow Forecasts: Discounted Cash Flow vs. the Method of "Comparables"," *Journal of Applied Corporate Finance*, (Vol. 8, No. 4, Winter), 45-60. Lewellen, W.G., and D.R. Emery, 1986, "Corporate Debt Management and the Value of the Firm," *Journal of Financial and Quantitative Analysis*, (Vol. 21, No. 4, December), 415- 426.

Luehrman, T.A., 1997, "Using APV: A Better Tool for Valuing Operations," *Harvard Business Review*, (May-June), 145-154. Miles, J., and J. Ezzell, 1980, "The Weighted Average Cost of Capital, Perfect Capital Markets, and Project Life: Clarification," *Journal of Financial and Quantitative Analysis*, (Vol. 15, September), 719-730. Miller, M., 1977, "Debt and Taxes," *Journal of Finance*, (May), 261-275. Modigliani, F., and M. Miller, 1958, "The Cost of Capital, Corporation Finance, and the Theory of Investment," *American Economic Review*, (June), 261-297. Modigliani, F., and M. Miller, 1963, "Corporate Income Taxes and the Cost of Capital: A Correction," *American Economic Review*, (Vol. 53, June), 433-443. Myers, S., 1974, "Interactions in Corporate Financing and Investment Decisions—Implications for Capital Budgeting," *Journal of Finance*, (Vol. 29, March), 1-25. Taggart, R.A., 1991, "Consistent Valuation and Cost of Capital Expressions with Corporate and Personal Taxes," *Financial Management*, (Autumn), 8-20.