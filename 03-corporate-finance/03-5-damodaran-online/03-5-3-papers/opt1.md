---
title: "Opt1"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/opt1.pdf
---

# **Literature on Real Options in Venture Capital and R&D**

A Review

# **Executive Summary**

- • Real options as a tool grew out of a pressing need for better investment criteria, as well as advances in the techniques for option pricing.
- • This essay attempts to offer a survey of literature in the field of real options, specifically of the literature that deals with the areas of venture capital and research and development projects.
- • Models are typically closely related to the work of Black & Scholes (1973), with improvements in the specification and modeling of parameters to suit the characteristics of venture and R&D investments. Thus most of the advances in the field are of an incremental nature.
- • The good news is, models are generally quite applicable, and the state of the science of real options valuation tools in this field is encouraging.

# **Table of Contents**

| The Literature on Real Options in Venture Capital and R&D | ................................1                                                |
|-----------------------------------------------------------|----------------------------------------------------------------------------------|
| Lessons from financial options                            | .......................................................................3         |
| Interest Rate Sensitivities                               | ...............................................................................4 |
| Models with Two State Variables                           | ...................................................................6             |

Essay Eight 10-05-2001

Søren Bruun Petersen int+ 45 86 12 88 85 bruun@realoptions.dk

Peter Christopher Bason int+ 45 28 73 19 72 bason@realoptions.dk

#### **Literature on Real Options in Venture Capital and R&D**

While options as a concept has existed for decades, analytic rigor in their pricing has only been possible since the breakthrough results of Black & Scholes (1973). This is also the starting point for the techniques for the valuation of real options. In the essay at hand, an attempt is made towards clarifying the academic lineage of the predominant valuation techniques, and identifying the strands of research that make up the current real options landscape. This is undertaken with a focus on growth options, particularly in relation to venture capital (VC) and research and development (R&D). As it appears, the options embedded in these two settings share many common characteristics. For a broad based review of the literature on real options see Dixit & Pindyck (1994), Trigeorgis (1996) and Lander & Pinches (1998).

# **The Cry for Help**

The early 1980's saw a period of crisis for corporate America, and there was widespread concern that the country's status as the world economic superpower was at risk. At the heart of the problem, it was conjectured, was the way American firms were managed. A common observation was that firms were too focused on short-term financial goals, and thus were underinvesting in productive capital, R&D and knowledge. This attack on time-honed management paradigms was articulated by, among others, Americas leading corporate pessimist, Robert Hayes, under headlines such as "Managing our way to economic decline" and, with a touch of irony, "Managing as if tomorrow mattered" (Hayes & Abernathy 1980, Hayes & Garvin 1982). Hayes and his contemporaries blamed naïve application of Discounted Cash Flow (DCF) analysis for a large share of the problems. A similar observation is made, slightly more eloquently, by Stewart Myers in a discussion of the disparities between financial theory and corporate strategy (Myers 1984), where it is noted that the two issues are typically dealt with by different people in the corporate hierarchies, people who often don't "speak the same language"<sup>1</sup> . Myers argues that finance and strategy are in fact two sides of the same coin and should be

treated as such in the corporate capital budgeting process, and goes on to suggest that many investments should be viewed through option pricing lenses, rather than DCF lenses. The same year, Kester (1984) argues the same case in a more managerially oriented forum, and these two articles are commonly recognized as "ground zero" for real options thinking, although Myers had already in 1977 suggested viewing a firm's growth opportunities as options. Not everyone agreed, though, that the answer to America weakened economic stance vis-à-vis e.g. Japan should be found in enhanced number crunching techniques, as when Michael Porter a decade later (1992) blames, among other factors, the reliance of US managers on simplistic financial metrics for "America's failing capital investment system". His cure is more use of qualitative criteria for evaluating projects and performance.

While managers may have become more skilled in using qualitative management tools, there is little evidence that the quantitative approaches have improved much. In a survey of investment criteria used by American firms, Graham & Harvey (2001) document a widespread use of dubious techniques such as accounting based internal rates of return and more or less random hurdle rates, while e.g. project-specific risk assessments are rare, and real options techniques hardly anywhere to be found. The reason can hardly be that real options as an academic discipline is undeveloped.

# **Black-Scholes to the Rescue**

As indicated above, the notion of viewing investment opportunities and managerial flexibility as options is a by-product of the research in pricing of financial options, as well as a pressing need for new perspectives on corporate capital budgeting. Thus it is clear that the value of real options thinking is both as a strategic tool and as a valuation technique. While the latter is the primary focus of this paper, a good starting point on the more high-level issues is found in Faulkner (1996), but he also notes that "there is a tendency to use the term »options« in a casual way to justify investments in a variety of projects without any substantive evaluation", and goes on to emphasize that the numerical analysis is a necessary complement to the intuition. An excellent attempt to

<sup>1</sup> This point is emphasized by Szakonyi (1994a, b), and very powerfully by Merck CFO Judy Lewent in a much-cited Harvard Business Review interview by Nichols (1994).

bridge the gap between the strategy-oriented discussions and the quantitative models is McGrath & MacMillian (2000), who present a framework for translating the verbal intuition into approximations of option values.

#### *Models*

The most obvious point of departure for those wishing to value growth options is to use the Black-Scholes (1973) option pricing model (BS-OPM) with the familiar five input variables. The literature is filled to the brim with applications of the clean-cut version of the model, and for illustrative purposes and a few real settings this is fine. There is a growing body of evidence, however, that the assumptions underlying the standard BS-OPM are either too simplistic, or downright false when it comes to pricing options on many real assets. Additionally, the estimation of several of the input parameters that are needed in the BS-OPM is a less than trivial exercise. These problems, individually or combined, form the motivation and basis for most of the valuation models for real options developed. In the following, a number of these models are presented.

### *Lessons from financial options*

Before turning to models developed specifically for real options, a few results from the financial options literature are worth noting.

Merton and others (e.g. Merton 1973, 1976 and Cox & Ross 1973) developed a range of "special cases" of the Black & Scholes' model shortly after its publication in 1973. One of the interesting cases is when the price process for the underlying asset is discontinuous. While it can be argued that all asset prices should be treated as discontinuous because they can only be observed at sample intervals, the price process for most real projects will appear to be very discontinuous, because the market value parameter generally will be sampled infrequently. Merton (1976) presents an elegant model that deals with this.

Another feature of real projects is that they often consist of a succession of discretionary investment opportunities. Thus part of the payoff from investing in a real option consists of further options. This is commonly known as compound options, and the issue was first dealt with by Geske (1977, 1979). When a VC or R&D project consists of several rounds of financing, they should be thought of as compound options. When the length of each financing round can be extended, Longstaff's (1990) model for pricing options with extendible maturities can be applied.

Finally, an approach that is both simple and intuitive for both real and financial options applications is the binomial/lattice approach first suggested by Cox et al (1979).

#### *Distributional Assumptions and Parameter Estimation*

Angelis (2000) formulates a model that makes two departures from the BS-OPM. The work is essentially an extension of Morris et al (1991). First, she recognizes that value estimates of R&D projects may be difficult to come by, and suggests using predictions of revenue and cost. These estimates are likely to be at hand, and are also more intuitive to work with for managers. The second issue concerns the distribution the (future) value of R&D projects when undertaking options based analysis. She conjectures that a more accurate description of the distribution of these revenue and cost predictions may be a normal, and not a lognormal distribution as the BS-OPM prescribes. These two considerations for the basis of a model that can easily be applied to R&D projects.

While Angelis addresses important points in the model, it is a rather ad hoc approach. In example, using the normal distribution allows negative cost and revenue values since this distribution is symmetric and defined for -8 < x < 8. If ease of implementation and intuitive appeal is important, practitioners might find the model useful.

# *Interest Rate Sensitivities*

While not presenting a new valuation framework per se, Hevert et al (1998) analyze the effect of interest rate risk on the value of growth options, and find that the consequences of inflation induced changes in interest rates are different for real growth options compared to financial options, or assets in place for that matter. The value of growth options is generally less sensitive to interest rate changes compared to assets in place. And, while the value of a financial call option increases with rising interest rates, real growth option values generally decrease with rising interest rates. This result, as well as the mode of analysis, is very important for managers concerned with creating and supervising a portfolio of growth options.

# *Competition and Market Imperfection*

Nalin Kulatilaka and Enrico Perotti, each boasting an excellent track record in developing real options thinking, present a model that takes a stab at another two assumptions in the traditional BS-OPM framework (Kulatiliaka & Perotti 1998). These assumptions concern the ownership of the investment opportunity that the option is written on, and the structure of the market for investment opportunities. In the world of financial options, the holder of an option has the exclusive right to exercise that option, and exercise by one firm does not affect the exercise decision by other firms. The firm has, in other words, monopoly over the opportunity, and the market is perfectly competitive, since exercise by one firm will not affect the price of the underlying asset. Not always so in real options analysis. When a firm is undertaking, in example, an R&D investment, it is in effect purchasing an option on possible commercialization or further development. But a competing firm can make similar investments and thus exercise by one firm will affect the market value of the option for other firms – possibly drive it to zero.

Kulatilaka and Perotti's framework explicitly deals with these issues, and while in traditional options analysis (that is, BS-OPM) uncertainty is given as the exogenous variance variable, the proper approach in many situations is to endogenize market structure into the valuation and decision model.

Efforts similar to these are presented by Reiss (1998) where real option valuation under competition is considered, and

# *Jump models*

While challenging the assumptions of the BS-OPM yields very interesting results, it often turns out the largest obstacle to using options analysis is the satisfactory estimation of certain input parameters. Especially the volatility parameter presents a challenge when few, if any, observations regarding the value of the underlying asset are at hand. It could be conjectured that a more accurate representation is a jump process, and this also makes for a more intuitive treatment of volatility. Changes in price are likely to be caused by technical discoveries and the arrival of information that affects the particular project (e.g. competitor entry), and these occurrences often happen at intervals.

Pennings & Lint (1997) formulate such a model with the value of the underlying asset governed by stochastic jumps, plus a deterministic drift component, and have successfully applied it to R&D projects at electronics multinational Philips. This is further discussed in Lint & Pennings (1998). A very similar model is presented by Willner (1995), where the effect of jumps decreases with time. Which model is more appropriate depends on the specifics of the situation.

#### *Models with Two State Variables*

In the world of financial options, the exercise price is usually specified when the contract is entered into. For VC and R&D projects, this translates into knowing with certainty the cost of commercializing the project. Very often, this is not possible. In fact, the only way to uncover the true cost of exercise is to actually undertake the project, and thus uncertainty is resolved through investment. Fischer (1978) pioneers the work on exercise cost uncertainty within the realm of financial options, and Pindyck (1993) considers this problem in relation to real options. Here, the setting is the construction of power plants, and Pindyck splits cost uncertainty into a technical dimension that relates to the true innovation effort needed to realize a project, and input cost uncertainty relating to the future prices of the resources needed. Schwartz & Moon (2000a) apply this thinking to R&D projects, and Ottoo (1998) similarly exemplifies with an R&D example where, additionally, competitive factors are considered. Treating both the value of the underlying asset and the exercise price as stochastic adds considerable realism to the modeling environment, but the complexity of the solution procedure increases correspondingly when working in continuous time. The resulting p.d.e.'s do not have closed-form solutions, and one must resort to rather byzantine numerical methods.

A shortcut to modeling real options with two state variables would be to use a three-dimensional lattice approach. This method is documented by Boyle (1988) where the focus is on financial options, but applications to real settings remain to be seen. It is likely that this could yield quite manageable and still accurate valuations.

# *DCF and Modern Capital Budgeting Methods*

The traditional approaches to valuation (e.g. DCF and multiples) and their shortcomings are well documented (see also Essay Three in this series), there is a place for them in the analysis of VC and R&D projects. While this may seem "suspiciously retro" (Desmet et al 2000, Koller 2001), the notion that "cash is king" certainly has merit, and looking at projects as they could turn out when all options are exercised can yield valuable information. The considerations involved in the projection of cash flows forces managers to think beyond the exercise horizon. In any case, the value of the underlying asset in a real options model will often be the result of a cash-based analysis. Schwartz & Moon (2000b, c) develop a multiples-based model that relies on options thinking and

use a novel approach to the budgeting procedure that deals with uncertainty about future outcomes in an explicit manner.

#### *Discussions*

The literature is filled to the brim with rather ordinary discussions of options thinking, and many use standard oil drilling rights examples that neglect important points in relation to more complex VC and R&D problems (e.g. Boer 2000). However, clarifying the strategic importance in a simple framework is generally easier (Mitchell & Hamilton 1988, Mitchell 1990 and Newton & Pearson 1994 are some of the better) and it still holds true that one of the most valuable aspects of real options thinking is a revised approach to investment under uncertainty (Vasudevan 2001).

## **References**

Angelis, Diana I. (2000): Capturing the Option Value of R&D, *Research•Technology Management*, July-August, pp. 31-34

Black, Fischer and Scholes, Myron (1973): Theory of Rational Option Pricing, Journal of Political Economy,

Boer, F. Peter (2000): Valuation of Technology Using "Real Options", *Research•Technology Management*, July-August, pp. 26-30

Boyle, Phelim P. (1988): A Lattice Framework for Option Pricing with Two State Variables, *Journal of Financial and Quantitative Analysis* 23, no. 1, March, pp. 1- 12

Cox, John C. and Ross, Stephen A. (1976): The Valuation of Options for Alternative Stochastic Processes, *Journal of Financial Economics* 3, pp. 145-166

Cox, John C.; Ross, Stephen A. and Rubinstein, Mark (1979): Option Pricing: A Simplified Approach, *Journal of Financial Economics*, 7, 27-39

Desmet, Driek; Francis, Tracy; Hu, Alice; Koller, Timothy M. and Riedel, George A. (2000): Valuing dot-coms, *The McKinsey Quarterly*, no. 3, pp. 148-157

Dixit, Avinash K. and Pindyck, Robert S. (1994): *Investment Under Uncertainty*, Princeton University Press, Princeton NJ

Faulkner, Terrence W. (1996): Applying 'Options Thinking' to R&D Valuation, *Research•Technology Management*, May-June, pp. 50-56

Fischer, Stanley (1978): Call Option Pricing When the Exercise Price is Uncertain, and the Valuation of Index Bonds, *Journal of Finance* 23, March, pp. 169-176

Geske, Robert. (1977): The Valuation of Corporate Liabilities as Compound Options, *Journal of Financial and Quantitative Analysis*, November, pp. 541 - 552

Geske, Robert. (1979): The Valuation of Compound Options, *Journal of Financial Economics* 7, 63-81

Graham, John R. and Harvey, Campbell R. (2001): The Theory and Practice of Corporate Finance: Evidence from the Field, *Journal of Financial Economics* 61

Hayes, Robert H. and Garvin, David A. (1982): Managing as if Tomorrow Mattered, *Harvard Business Review*, May-June, pp. 71-79

Hayes, Robert H. and Abernaty, William J. (1980): Managing our Way to Economic Decline, *Harvard Business Review*, July-August, pp. 67-77

Hevert, Kathleen T.; McLaughlin, Robyn M. and Taggart, Robert A. (1998): Interest Rates, Inflation and the Value of Growth Options, *The Quarterly Review of Economics and Finance*, vol. 38, Special Issue, pp. 599-613

Kester, W: Carl (1984): Today's Options for Tomorrow's Growth, *Harvard Business Review*, March-April, pp. 153-160

Koller, Timothy M. (2001): Valuing dot-coms after the fall, *The McKinsey Quarterly*, no. 2

Kulatilaka, Nalin and Perotti, Enrico C. (1998): *Strategic Growth Options*, Management Science, vol. 44, no. 8, August, pp. 1021-1031

Lander, Diane M. and Pinches, George E. (1998): Challenges to the Practical Implementation of Modeling and Valuing Real Options, *The Quarterly Review of Economics and Finance*, vol. 38, Special Issue, pp. 537-567

Lint, Onno and Pennings, Enrico (1998): R&D as an Option on Market Introduction, R&D Management 28, no. 4, pp. 279-287

Longstaff, Francis. A. (1990): Pricing Options with Extendible Maturities: Analysis and Applications, *Journal of Finance*, 45(3), pp. 935-957

McGrath, Rita Gunther and MacMillan, Ian C. (2000): Assessing Technology Projects Using Real Options Reasoning, *Research•Technology Management*, July-August, pp. 35-49

Merton, Robert C. (1973): Theory of Rational Option Pricing, *Bell Journal of Economics and Management Science* 4, 141-183

Merton, Robert C. (1976): Option Pricing When Underlying Stock Returns are Discontinuous, *Journal of Financial Economics*, no. 3, pp. 125-144

Mitchell, Graham R. and Hamilton, William F. (1988): Managing R&D as a Strategic Option, *Research•Technology Management*, May-June, pp. 15-22

Mitchell, Graham R. (1990): Alternative Frameworks for Technology Strategy, *European Journal of Operational Research*, 47, 2, pp- 153-161

Morris, Peter A.; Teisberg, Elizabeth Olmstead and Kolbe, A. Lawrence (1991): When Choosing R&D Projects, go with Long Shots, *Research•Technology Management*, January-February, pp. 35-40

Myers, Stewart C. (1977): Determinants of Corporate Borrowing, *Journal of Financial Economics* 5, pp. 147-175

Myers, Stewart C. (1984): Finance Theory and Financial Strategy, *INTERFACES* 14, January-February, pp. 126-137

Newton, D. P. and Pearson, A. W (1994): Application of Option Pricing Theory to R&D, *R&D Management* 24, pp. 83-89

Nichols, Nancy A. (1994): Scientific Management at Merck, *Harvard Business Review*, January-February, pp. 88-99

Ottoo, Richard E. (1998): Valuation of Internal Growth Opportunities: The Case of a Biotechnology Company, *The Quarterly Review of Economics and Finance*, vol. 38, Special Issue, pp. 615-633

Pennings, Enrico and Lint, Onno (1997): The Option Value of Advanced R&D, *European Journal of Operational Research* 103, pp. 83-94

Pindyck, Robert S. (1993): Investments of Uncertain Cost, *Journal of Financial Economics* 34, pp. 53-76

Porter, Michael E. (1992): Capital Disadvantage: America's Failing Capital Investment System, Harvard Business Review 72, September-October pp. 65-83

Reiss, Ariane (1998): Investment in Innovations and Competition: An Option Pricing Approach, *The Quarterly Review of Economics and Finance*, vol. 38, Special Issue, pp. 635-650

Roberts, Kevin and Weitzman, Martin L. (1981): Funding Criteria for Research, Development and Exploration Projects, *Econometrica* 49, 5, pp. 1261-1288

Schwartz, E. and M. Moon (2000a): Evaluating Research and Development Investments, in Brennan, M. and L. Trigeorgis (eds.), *Project Flexibility, Agency, and Product Market Competition: New Developments in the Theory and Application of Real Options Analysis*, Oxford University Press

Schwartz, E.Szakonyi, Robert (1994a): Measuring R&D Effectiveness  
*Research•Technology Management*, March-April, pp. 27-32

Szakonyi, Robert (1994b): Measuring R&D Effectiveness II, *Research•Technology Management*, May-June, pp. 44-55

Trigeorgis, Leons (1996): *Real Options – Managerial Flexibility and Strategy in Resource Allocation*, The MIT Press, Cambridge, Mass.

Vasudevan, Ash (2001): Shaping the Future with a Portfolio of Real Options, *CommerceNet papers available at <http://www.commerce.net>*, posted March 9

Willner, Ram (1995): Valuing Start-up Venture Growth Options, in Trigeorgis, L. (ed.) *Real Options in Capital Investment – Models, Strategies and Applications*, Praeger, Westport, Conn., pp. 221-239