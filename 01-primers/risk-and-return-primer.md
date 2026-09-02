---
title: Finance Primer — Risk and Return Models
status: active
owner: weprintmoney
created: 2026-09-01
last_updated: 2026-09-01
---

# Finance Primer — Risk and Return Models

> Source: [Aswath Damodaran, Applied Corporate Finance 3rd ed., Chapter 3 (PDF)](https://pages.stern.nyu.edu/~adamodar/pdfiles/acf3E/ch3.pdf) — converted to markdown 2026-09-01.

> **Note on format:** The source chapter is copyrighted (Wiley), so this document is a comprehensive study summary in original wording, not a verbatim transcription. It follows the chapter's full section structure and preserves every equation, all figure/table content (described or condensed), the numbered Illustrations, the "In Practice" boxes, the concept-check questions, and the end-of-chapter problem topics.

---

## Chapter 3: The Basics of Risk — Overview

The chapter opens with the observation that risk is usually framed purely as a negative (dictionary definitions treat it as exposure to danger), but the Chinese term for risk (危机) combines the characters for "danger" and "opportunity." That duality is the core tradeoff of finance: higher potential rewards come bundled with higher risk. The central test in finance is whether an investor is *appropriately compensated* for the risk taken.

**Chapter purpose:** lay the foundation for analyzing risk in corporate finance, present alternative models for measuring risk, and show how those risk measures convert into acceptable hurdle rates.

---

## Motivation and Perspective in Analyzing Risk

Why do we need a risk-and-return model at all? Because a good model both **measures the risk** in any investment and **maps that risk measure into an expected return**, which becomes the hurdle rate for project analysis.

Key perspective questions:

- **Whose risk?** Risk looks different to managers (whose human and financial capital is concentrated in the firm) than to stockholders (who typically hold the stock as one piece of a larger portfolio).
- **The marginal investor.** Since firms have thousands of investors with different views, the chapter argues risk should be measured from the perspective of the **marginal investor** — the investor most likely to be trading the stock at any given time. Because the objective of corporate finance is maximizing firm value and stock price, the viewpoint that matters is the one that actually sets prices.
- **Equity vs. debt.** Equity investors (who share upside and downside) view risk more sanguinely than lenders (limited upside, large downside). The first part of the chapter covers equity risk; the latter part covers risk from the lender's perspective (default risk).

**Characteristics of a good risk and return model** (five criteria):

1. Produces a risk measure that applies universally across all assets, not just one asset class.
2. Clearly delineates which risks are rewarded and which are not, with a rationale for the distinction.
3. Produces standardized risk measures, so an investor can tell whether an asset is above- or below-average risk.
4. Translates risk into an expected rate of return the investor should demand as compensation.
5. Works not only for explaining past returns but for predicting future expected returns.

Every risk-and-return model is flawed; the point is not to let the perfect be the enemy of a good or adequate model.

---

## Equity Risk and Expected Returns

The analysis proceeds in three steps: (1) define risk in terms of the distribution of actual returns around an expected return; (2) distinguish risk specific to an investment from risk that affects a broad cross-section of investments — only the latter (**market risk**) is rewarded when the marginal investor is diversified; (3) examine alternative models for measuring market risk and the expected returns that go with it.

### I. Measuring Risk

Investors buy assets expecting a return over their holding period; the actual return can differ from the expected return — that gap is where risk lives.

> **Definition — Variance in Returns:** a measure of the squared difference between actual returns and expected returns on an investment.

- A 1-year Treasury bill (or any default-free 1-year bond) bought with a 5% expected return delivers exactly 5% — actual always equals expected. This is a riskless investment, at least in nominal terms.

*[Figure 3.1: Returns on a Riskfree Investment — a probability distribution that is a single vertical spike at the expected return with probability = 1. Takeaway: no dispersion means no risk.]*

- By contrast, an investment in a stock like Disney with an expected 1-year return of 30% will almost never deliver exactly 30% — the actual could be far higher or lower.

*[Figure 3.2: Probability Distribution for Risky Investment — a spread-out, positively skewed bell-like curve of possible returns centered near the expected return. Takeaway: risky assets have a distribution of outcomes, not a point.]*

Beyond the expected return, three moments of the distribution matter:

1. **Variance / standard deviation** — the spread of actual returns around the expected return; more deviation = more variance.
2. **Skewness** — the bias toward large positive vs. large negative returns (Figure 3.2's distribution is positively skewed).
3. **Kurtosis** — the fatness of the tails; fatter tails = higher kurtosis, capturing the tendency of prices to "jump" in either direction.

In the special case of the **normal distribution**, returns are symmetric (no skewness, kurtosis defined as zero), so investments can be judged on just two dimensions: expected return (the reward) and variance (the risk).

*[Figure 3.3: Return Distribution Comparisons — two symmetric distributions with the same expected return: a tall narrow "low variance investment" curve and a flatter, wider "high variance investment" curve. Takeaway: with equal expected returns, investors prefer lower variance; with equal variance, they prefer higher expected return.]*

When distributions are neither symmetric nor normal, investors may still choose on mean and variance alone if their utility functions permit it, but more plausibly they trade off the good (higher expected return, more positive skewness) against the bad (higher variance and kurtosis). Of the models in this chapter, the CAPM explicitly requires choices to be made only on expected returns and variances — it ignores skewness and kurtosis, though it is unclear how much those extra moments drive expected returns.

*(Footnote concept: a utility function summarizes investor preferences as "utility" of wealth; the quadratic utility function is the special case that compresses everything into mean and variance, justifying the mean-variance framework.)*

**Practical caveat:** return moments are almost always estimated from *past* returns, which assumes historical distributions are good predictors of future ones. When an asset's characteristics have changed significantly, historical estimates may be poor risk measures.

> **Concept check 3.1 — Do you live in a mean-variance world?** Two investments share a 15% expected return and 25% standard deviation, but A has a tiny chance of quadrupling your money while B tops out at +60%. Would you (a) be indifferent, (b) prefer A for the lottery-like upside, or (c) prefer B as safer? (Tests whether you truly care only about mean and variance, or also about skewness.)

> **Boxed aside — Risk Assessment: A Behavioral Perspective**
> The mean-variance framework compresses risk into one number (a standard deviation), which imposes discipline but may miss the messier human relationship with risk. Behavioral finance identifies three departures:
>
> - **Loss aversion:** experiments show people are hurt far more by a loss than helped by an equivalent gain, and tend to measure losses in dollars rather than percentages — investors are loss averse rather than risk averse. Even a small chance of a large wealth loss makes an investment feel risky regardless of its standard deviation.
> - **Familiarity bias:** people perceive less risk in familiar investments (e.g., long-established domestic companies vs. emerging-market firms), which helps explain "home bias" — overweighting domestic assets. More generally, perceived risk rises with how hard something is to understand.
> - **Emotional factors:** risk has an emotional component quantitative measures miss — gains feed happiness/optimism, losses feed worry/anxiety, and mood shifts can turn "safe" assets risky in investors' eyes.
>
> Attempts to build composite risk measures incorporating these factors have not converged on a consensus, but they may explain why quantitative risk measures for a firm often diverge from qualitative risk assessments of the same firm.

#### Illustration 3.1: Calculating standard deviation from historical returns — Disney

Monthly returns on Disney stock were computed for January 2004–December 2008 using price changes plus dividends:

```
Returnₜ = (Priceₜ − Priceₜ₋₁ + Dividendsₜ) / Priceₜ₋₁
```

*[Figure 3.4: Returns on Disney 2004–2008 — a line chart of monthly returns oscillating roughly between −16% and +12%. Best month: October 2004 (+11.82%); worst month: October 2008 (−15.58%).]*

Key results:

| Statistic (monthly, Jan 2004–Dec 2008) | Value |
|---|---|
| Average monthly return (59 months) | 0.18% |
| Standard deviation of monthly returns | 5.59% |
| Variance of monthly returns | 31.25%² |
| Start price (Jan 2004) → end price (Dec 2008) | $23.68 → $22.69 |
| Annual dividend | $0.24 (2004) rising to $0.35 (2008) |

Annualizing:

```
Annualized standard deviation = 5.59% × √12 = 19.36%
Annualized variance = 31.25% × 12 = 374.98%²
```

*(Footnote: variance is in percent-squared units — a 9.96% standard deviation is 0.0996 in decimals, but the corresponding 99.15%² variance is 0.009915 in decimal terms.)*

Important limitation: a standard deviation in isolation says little — you can only judge whether Disney is relatively risky by comparing against other companies' standard deviations. *(Web dataset referenced: `optvar.xls` — average standard deviations of equity values by U.S. industry group.)*

> **Concept check 3.2 — Upside and downside risk.** Two investments both show 35% standard deviation over five years, but one returned −10% and the other +40% over the period. Are they equally risky? Why doesn't finance distinguish "upside risk" from "downside risk"?

> **In Practice: Estimating only downside risk**
> Variance counts deviations both below the average return (downside) and above it (upside), yet investors mostly experience the downside as "risk." The **semi-variance** counts only downside deviations — deviations from the average are computed only in periods where the actual return fell below the expected return:
>
> ```
> Semi-variance = Σₜ₌₁ⁿ (Rₜ − Average Return)² / n
> where n = number of periods with actual return < average return
> ```
>
> Under a normal distribution, semi-variance equals variance; for asymmetric distributions they differ. A stock that earns small positive returns most periods but suffers occasional large negative returns will have a semi-variance much higher than its variance.

### II. Rewarded and Unrewarded Risk

Deviations of actual from expected returns arise for many reasons, which sort into two buckets: **firm-specific risks** (specific to one or a few investments) and **market risks** (affecting most or all investments).

#### The Components of Risk

When a firm makes an investment, the return is affected by several forces, mostly outside its control. Some risk gets eliminated by the firm across multiple investments; more gets eliminated by investors holding diversified portfolios. Five sources, running from most firm-specific to most market-wide:

1. **Project-specific risk** — a single project's cash flows can beat or miss expectations due to estimation error or project-specific factors. Firms taking many similar projects diversify much of it away in the ordinary course of business. Example: Disney faces estimation error on each movie's costs and revenues, but releases many movies per year. *(Footnote example: Treasure Planet (2002) cost $140M and produced a $98M write-off; months later Finding Nemo became one of 2003's biggest hits.)*
   > *Definition — Project risk: risk affecting only the project under consideration, arising from project-specific factors or estimation error.*
2. **Competitive risk** — competitors' actual actions differ from what was built into project forecasts, affecting cash flows positively or negatively. Harder for the firm to diversify (it hits multiple projects); Disney can't diversify away Universal Studios' moves, but Disney's stockholders can, by also holding competitor stocks. *(Footnote: firms could in theory buy competitors, but antitrust law and yet-unannounced entrants limit this.)*
   > *Definition — Competitive risk: the unanticipated effect (positive or negative) of competitor actions on a project's cash flows.*
3. **Industry-specific risk** — factors hitting the earnings and cash flows of a whole industry, of three types: **technology risk** (technology evolving differently than expected), **legal risk** (changing laws and regulation), and **commodity risk** (price changes in commodities/services the industry disproportionately uses or produces). Disney's broadcasting unit (ABC) faces all three: internet blurring TV entertainment lines (technology), changing broadcast law (legal), and program production costs (commodity). Firms can only escape it by diversifying across industries; stockholders escape it by holding cross-industry portfolios.
   > *Definition — Industry-specific risk: unanticipated effects on project cash flows of industry-wide shifts in technology, law, or commodity prices.*
4. **International risk** — arises when revenues or costs sit outside the domestic market; cash flows move with unexpected exchange-rate movements and political developments (e.g., Disney's Hong Kong theme park). Firms partially diversify it by operating across countries (McDonald's) or borrowing in local currency; investors mitigate it by diversifying globally.
   > *Definition — International risk: added cash-flow uncertainty from unanticipated exchange-rate changes and political risk in foreign markets.*
5. **Market risk** — macroeconomic forces affecting essentially all companies and projects: interest-rate changes (hitting value both through discount rates and through cash flows), the term structure, investor risk aversion, inflation, and economic growth. Neither firms nor investors can diversify it away, since all risky investments carry some exposure.
   > *Definition — Market risk: unanticipated changes in project cash flows created by changes in interest rates, inflation, and the economy, affecting all firms to differing degrees.*

> **Concept check 3.3 — Risk is in the eyes of the beholder.** True or false: a privately owned firm will generally end up with a higher discount rate for a project than an otherwise identical publicly traded firm with diversified investors. Does this rationalize private firms being acquired by public ones? (Answer direction: true — undiversified owners must be compensated for total risk.)

#### Why Diversification Reduces or Eliminates Firm-Specific Risk

Two mechanisms:

- **Position sizing:** each holding in a diversified portfolio is a small fraction of the whole, so any shock affecting only that investment barely moves the portfolio.
- **Averaging out:** firm-specific news is positive for some holdings and negative for others in any period, so in large portfolios these effects average to roughly zero.

Market-wide risk, by contrast, persists in even the largest portfolios — e.g., a rate increase lowers the value of most assets simultaneously.

*[Figure 3.5: A Break Down of Risk — a spectrum from "Firm-specific" (actions affecting one firm) to "Market" (affecting all investments): projects doing better/worse than expected → competition stronger/weaker than anticipated → whole sector affected → exchange rate and political risk → interest rates, inflation, economy news. Below the spectrum: how the firm can reduce each (many projects; acquiring competitors; diversifying across sectors; diversifying across countries; cannot affect market risk) and how investors can mitigate each (diversifying across domestic stocks; diversifying globally; diversifying across asset classes).]*

**The statistics of diversification (two-asset portfolio).** Asset A has expected return μ_A and variance σ²_A; asset B has μ_B and σ²_B; their return correlation is ρ_AB. With portfolio weight w_A in A:

```
μ_portfolio = w_A μ_A + (1 − w_A) μ_B

σ²_portfolio = w_A² σ²_A + (1 − w_A)² σ²_B + 2 w_A w_B ρ_AB σ_A σ_B
```

The last term is often written via the covariance:

```
σ_AB = ρ_AB σ_A σ_B
```

The diversification benefit depends on the correlation coefficient: the higher the correlation between the two assets, the smaller the gain from combining them. *(Correlation ranges from −1 — lock-step opposite movement — to +1 — perfectly synchronized movement.)*

> **Boxed aside — Under Diversification: A Behavioral Perspective**
> The case for diversification is airtight in a mean-variance world, yet most investors don't diversify. Blume, Crockett and Friend (1974) found 34% of individual investors held a single dividend-paying stock, 55% held one to ten, and only 11% held more than ten. Goetzmann and Kumar, studying 60,000 discount-brokerage investors (1991–96), found little improvement — 25% held one stock, 50% held two or three — and that transaction costs can't explain it. Behavioral explanations:
>
> - **The gambling instinct:** investors build layered "pyramid" portfolios — a bottom layer for downside protection and a top layer of a few lottery-ticket-like positions for upside (Shefrin and Statman, 2000).
> - **Overconfidence:** investors who overweight specific industries or characteristics (e.g., volatility) hold narrower portfolios, consistent with overconfidence in their ability to pick winners.
> - **Narrow framing and estimation biases:** looking at portfolio pieces in isolation, or overestimating how correlated individual stocks are with each other, leads to holding fewer names.
>
> Bottom line: many individual (and some institutional) investors ignore diversification, and their risk perspective differs from that of diversified investors in the same companies.

#### Illustration 3.2: Variance of a portfolio — Disney and Aracruz ADR

Using the same Jan 2004–Dec 2008 window (Aracruz is a Brazilian stock traded in the U.S. as an ADR — dollar-denominated depositary shares tracking the local listing plus exchange-rate effects):

| | Disney | Aracruz ADR |
|---|---|---|
| Average monthly return | 0.18% | −0.74% |
| Standard deviation (monthly) | 5.59% | 14.87% |

With hindsight Disney dominated — higher return, lower volatility. Two nuances: Aracruz actually averaged +2.47%/month from Jan 2004 to Apr 2008, then collapsed from an all-time high of $90.74 to $8.39 between May and December 2008; and the ADR returns embed both the Brazilian-real stock performance and the $/BR exchange rate, whose late-2008 plunge amplified the fall.

Correlation between the two over 60 months: **ρ = 0.1807**. For a portfolio 90% Disney / 10% Aracruz:

```
σ²_portfolio = w_Dis² σ²_Dis + (1 − w_Dis)² σ²_Ara + 2 w_Dis w_Ara ρ_Dis,Ara σ_Dis σ_Ara
            = (0.9)²(0.0559)² + (0.1)²(0.1487)² + 2(0.9)(0.1)(0.1807)(0.0559)(0.1487)
            = 0.003023

σ_portfolio = √0.003023 = 0.0550 = 5.50%
```

The 90/10 portfolio is **less risky than either stock alone** (5.50% < 5.59% < 14.87%).

*[Figure 3.6: Standard deviation of the Disney/Aracruz portfolio as a function of the proportion in Disney — a curve that dips slightly below Disney's own 5.59% around 90% Disney, then rises steadily toward Aracruz's 14.87% as the Aracruz share goes to 100%. Takeaway: even a small allocation to a lowly-correlated asset can reduce total portfolio risk.]*

The Aracruz episode also illustrates the firm-specific vs. market split: management's speculative currency-derivative bets (losses over $2 billion when the real weakened in 2008) were firm-specific risk; the global market collapse in late 2008 that accelerated the fall was market risk.

#### Identifying the Marginal Investor

The marginal investor — the one most likely trading at the margin — has the most influence on pricing. It may be an institution (which vary by tax status, domestic vs. international reach, and investment philosophy), an individual (varying widely in diversification and objectives), or an insider/founder. A practical diagnostic based on the breakdown of holdings among individuals, institutions, and insiders:

| Ownership pattern | Likely marginal investor |
|---|---|
| Small institutional holdings, substantial wealthy-individual holdings | An individual with a significant equity stake — assess how diversified that individual is; if undiversified, treat the firm like a private firm and price in *all* risk |
| Small institutional and small insider holdings | Dispersed small individual investors, possibly only partially diversified (e.g., U.S. phone/utility stocks historically held by dividend-seeking individuals concentrated in high-dividend sectors) |
| Significant institutional holdings, small insider holdings | Almost always a diversified institutional investor; refine by examining the top 15–20 holders' tax status, growth-vs-value objective, and domestic-vs-international reach |
| Significant institutional *and* large insider holdings | Usually still the institutional investor — founders (e.g., Gates at Microsoft, Dell at Dell) rarely trade and their wealth rides on prices institutions set — though the leading stockholder influences decisions |

Why it matters: marginal investors set prices, so their risk assessment governs. If they are diversified institutions, managers should consider only non-diversifiable risk in investment decisions; if they are undiversified individuals, the firm should consider total risk.

#### Illustration 3.3: Identifying the marginal investor — Disney, Aracruz, Tata Chemicals, Deutsche Bank

Insider positions: the Disney family's stake had dwindled below 1%, but the Pixar acquisition made Steve Jobs the largest single holder (~7%); Aracruz's voting shares were held by the Votorantim Group (84%) and Brazil's BNDES, with non-voting shares dispersed; the Tata family controls a significant stake in Tata Chemicals via other Tata group companies; Deutsche Bank had no significant insiders. Insiders are nevertheless *not* the marginal investors: their holdings are static, both because insider-trading rules restrict trading (especially at Disney) and because selling would erode control (Tata, Aracruz).

**Table 3.1 — Ownership breakdown (source: Value Line, Morningstar, Bloomberg):**

| Holder type | Disney | Deutsche Bank | Aracruz (non-voting) | Tata Chemicals |
|---|---|---|---|---|
| Institutions | 72% | 76% | 32% | 47% |
| Individuals | 21% | 23% | 60% | 24% |
| Insiders | 7% | 1% | 8% | 29% |

**Table 3.2 — Ten largest stockholders (end 2008, % of stock, source: Bloomberg), condensed:**

- **Disney:** Steve Jobs (7.43%) followed by nine institutions — Fidelity (4.86%), State Street (3.97%), Barclays (3.79%), Vanguard (3.07%), Southeastern Asset (2.40%), State Farm Mutual (2.27%), AXA (2.13%), Wellington (1.87%), Massachusetts Financial (1.57%).
- **Deutsche Bank:** Deutsche Post (8.05%), Allianz (6.81%), AXA (4.64%), Credit Suisse (3.55%), Deutsche Bank (3.52%), Barclays (3.02%), Blackrock (2.35%), UBS (1.65%), Deka (1.52%), Dekabank (1.44%) — the top two reflecting German cross-holding governance; about half the institutions non-German.
- **Aracruz preferred:** all small institutional stakes under 1% — BB DTVM (0.89%), Barclays (0.34%), Banco Itau (0.32%), Banco Barclays (0.19%), Vanguard (0.18%), UBS Strategy (0.17%), Banco Itau (0.17%), Dimensional (0.10%), Banco Bradesco (0.09%), Landesbank (0.08%).
- **Tata Chemicals:** Tata Sons (14.26%), Life Insurance Co (11.71%), Tata Investment (6.8%), Tata Tea (6.54%), New India Assurance (2.58%), Hindustan Lever (2.14%), General Insurance (2.12%), United India Insurance (1.13%), National Insurance (1.01%), Templeton Funds (1.01%) — four of the top ten are other Tata companies whose stakes rarely trade; ~12% of stock held by foreign institutions.

**Conclusions:** For Disney (nine of top ten are institutions) and Deutsche Bank, it's safe to assume the marginal investor is institutional and diversified — so only non-diversifiable risk should count in investment decisions. Aracruz's voting stock is closely held and thinly traded, but its price is tightly linked to the widely dispersed preferred shares, so self-interest pushes controlling shareholders to treat preferred-share investors as marginal. Tata Chemicals is similar despite heavy insider influence — the remaining large holders are institutions. So the diversified-marginal-investor assumption holds, most strongly at Disney and Deutsche Bank.

#### Why is the marginal investor assumed to be diversified?

Risk-and-return models go beyond "investors can diversify" to assert the price-setting marginal investor *is* diversified. The logic: an undiversified investor perceives more risk in any asset than a diversified one (who ignores firm-specific risk). Given identical cash-flow expectations, the diversified investor will pay more — so over time assets end up held by diversified investors. The argument is strongest for liquid, small-unit assets like stocks; it is weaker for large illiquid assets (real estate is still mostly held by undiversified owners — which is why REITs and mortgage-backed securities were invented, to let investors hold real estate and stay diversified). Note also that diversification doesn't preclude chasing excess returns: an investor who believes low-PE stocks beat the market can hold low-PE stocks *across many sectors*.

> **Concept check 3.4 — Management quality and risk.** True or false: a well-managed firm is less risky than a badly managed one. (Directionally: management quality affects expected cash flows, not necessarily exposure to market risk.)

> **In Practice: Who should diversify — the firm or its investors?**
> Either can mitigate each risk type; the tiebreaker is cost. A firm should act to reduce a risk only when it can do so more cheaply than its investors can. For publicly traded firms, investors almost always diversify more cheaply: to shed sector risk, a firm must acquire other firms at premium prices or pour capital into businesses it doesn't understand, while an investor just broadens the portfolio or buys a mutual fund. So public firms should diversify away risk only when the cost is minimal or the risk reduction is a side effect of an action taken for other reasons (e.g., Disney's project risk falls essentially for free just by making many movies). Private businesses are the harder case: owners with most of their wealth locked in the business can either pull money out and invest elsewhere or diversify the business itself — which is partly why many Latin American and Asian family businesses grew into conglomerates.

### III. Measuring Market Risk

The models in use agree on the first two steps — risk comes from the distribution of actual returns around expectations, and should be measured from the perspective of a well-diversified marginal investor — but diverge on how to measure the non-diversifiable (market) component. Four families: CAPM, arbitrage pricing model (APM), multi-factor models, and proxy models.

#### A. The Capital Asset Pricing Model (CAPM)

The oldest and still the standard model in most real-world analyses; much-criticized but a useful starting point.

**1. Assumptions.** In reality investors stop diversifying well short of the full market — even large mutual funds may hold only 10–20 stocks — for two reasons: marginal diversification benefits shrink as the portfolio grows (the 21st asset removes far less firm-specific risk than the 5th) while transaction and monitoring costs continue; and many investors believe they can find undervalued assets and refuse to hold assets they view as fairly or over-priced. The CAPM assumes away both frictions: **no transaction costs, all assets traded, infinitely divisible investments, and no private information** (so no one can systematically find under- or over-valued assets). With nothing stopping diversification, the logical end point is holding *every traded risky asset* in proportion to market value — the **market portfolio**. *(Footnote: deviating from market-value weights costs diversification benefits with no offsetting gain when mispricing can't be found.)*

> *Definition — Riskless asset: an asset whose actual return always equals its expected return.*

**2. Implications for investors.** If everyone holds the same market portfolio, risk preferences are expressed through **allocation**: risk-averse investors put more (even all) wealth in the riskless asset; risk-seekers put everything in the market portfolio; those wanting still more risk **borrow at the riskless rate and lever the market portfolio**. This requires two extra assumptions — a riskless asset exists, and investors can lend and borrow at the riskless rate (variants of CAPM relax these while preserving the core conclusions).

> **Concept check 3.5 — Efficient risk taking.** Under CAPM, the most efficient way to take a lot of risk is: (a) a well-balanced portfolio of the riskiest stocks, (b) risky stocks that are also undervalued, or (c) borrow money and buy a well-diversified portfolio. (CAPM answer: c.)

**3. Measuring the market risk of an individual asset.** The risk any asset adds to an investor's portfolio is what matters. When everyone holds the market portfolio, an asset's risk is the risk it adds to the market portfolio — statistically, its **covariance with the market portfolio**. Assets that move more with the market add more risk; movements uncorrelated with the market wash out. Covariance isn't standardized (knowing Disney's covariance with the market is "55%" says nothing by itself), so it is scaled by the market's variance to get **beta**:

```
βᵢ = Covariance of asset i with Market Portfolio / Variance of the Market Portfolio
   = Cov(Rᵢ, Rₘ) / σ²ₘ
```

Since the market's covariance with itself is its variance, the market portfolio (and the average asset) has β = 1; riskier-than-average assets have β > 1; safer assets β < 1; the riskless asset β = 0.

> *Definition — Beta: in the CAPM, a standardized measure of the risk an investment adds to the market portfolio.*

**4. Getting expected returns.** Because every investor holds a mix of the riskless asset and the market portfolio, expected return is **linear in beta**:

```
E(Rᵢ) = R_f + βᵢ × [E(Rₘ) − R_f]
      = Risk-free rate + Beta of asset i × (Risk premium on market portfolio)
```

where E(Rᵢ) = expected return on asset i, R_f = risk-free rate, E(Rₘ) = expected return on the market portfolio, βᵢ = beta of asset i.

Three inputs:

- **Riskless rate:** the return known with certainty over the analysis horizon — so the right rate depends on whether the horizon is 1, 5, or 10 years.
- **Risk premium:** the premium investors demand for the market portfolio (all risky assets as a class) over the riskless asset — not specific to any one asset.
- **Beta:** the only firm-specific input — under the CAPM, the *only* reason two investments have different expected returns is different betas.

Summary: all market risk is captured in one beta, measured against a market portfolio that in theory includes every traded asset held at market-value weights.

> **Concept check 3.6 — What do negative betas mean?** If an asset has β < 0, which is true: (a) expected return below the riskless rate, (b) it insures your diversified portfolio against some market risk, (c) holding it makes sense only if you're well diversified, (d) all of the above. (Answer: d.)

> **In Practice: Index funds and market portfolios**
> Critics call the "everyone holds the market portfolio" conclusion unrealistic — and it's true that not all assets trade, transaction costs exist, some trade on inside information, and many hold undiversified portfolios. But index funds get you surprisingly close: an index fund replicates an index by holding its stocks at index weights. The earliest and largest is the Vanguard 500 (S&P 500), and funds now exist for U.S. small caps, European, Latin American and Asian equities, plus bonds and commodities. A market-value-weighted mix of index funds approximates the market portfolio; the one asset class that stays hard to replicate is real estate.

#### B. The Arbitrage Pricing Model (APM)

The CAPM's restrictive assumptions and dependence on the market portfolio drew long-standing skepticism; in the late 1970s Ross developed the more general arbitrage pricing model *(Ross, 1976, Journal of Economic Theory)*.

> *Definition — Arbitrage: an investment requiring no capital and bearing no risk that still delivers a sure profit.*

**1. Assumptions.** Two investments with identical risk exposure must be priced to earn the same expected return — otherwise investors buy the higher-return portfolio and sell the lower one until returns converge. Like the CAPM, the APM splits risk into firm-specific and market-wide components; actual returns can be written:

```
R = E(R) + m + ε
```

where m is the market-wide component of unanticipated risk and ε is the firm-specific component.

**2. Sources of market-wide risk.** Where the CAPM collapses all market risk into the market portfolio, the APM allows **multiple sources** (unanticipated changes in GNP, inflation, interest rates, ...), each with its own sensitivity ("factor beta"):

```
R = E(R) + m + ε
  = E(R) + (β₁F₁ + β₂F₂ + ... + βₙFₙ) + ε
```

where βⱼ = sensitivity of the investment to unanticipated changes in factor j, and Fⱼ = unanticipated change in factor j.

**3. Effects of diversification.** In a portfolio the firm-specific components (ε) diversify away, leaving portfolio returns as two weighted averages — of expected returns and of factor betas:

```
R_p = (w₁R₁ + w₂R₂ + ... + wₙRₙ)
    + (w₁β₁,₁ + w₂β₁,₂ + ... + wₙβ₁,ₙ) F₁
    + (w₁β₂,₁ + w₂β₂,₂ + ... + wₙβ₂,ₙ) F₂ + ...
```

where wⱼ = portfolio weight on asset j, Rⱼ = expected return on asset j, βᵢ,ⱼ = beta on factor i for asset j.

**4. Expected returns and betas.** Portfolio betas are weighted averages of asset betas; combined with no-arbitrage, expected returns must be **linear in the factor betas**. Worked logic (single factor): portfolio A has β = 2.0 and E(R) = 20%; portfolio B has β = 1.0 and E(R) = 12%; portfolio C has β = 1.5 and E(R) = 14%. A 50/50 mix of A and B has β = 1.5 and E(R) = 16% — dominating C. Buying the A+B combination and selling C yields riskless profit with no net investment, so C's price must fall until its expected return reaches 16%. Extending to multiple factors:

```
E(R) = R_f + β₁[E(R₁) − R_f] + β₂[E(R₂) − R_f] + ... + βₙ[E(Rₙ) − R_f]
```

where R_f = expected return on a zero-beta portfolio and E(Rⱼ) = expected return on a portfolio with a beta of 1 on factor j and 0 on all others. The bracketed terms are the factor risk premiums.

The **CAPM is the special case** of the APM with a single economic factor — the market portfolio:

```
E(R) = R_f + βₘ (E(Rₘ) − R_f)
```

**5. The APM in practice.** Factor betas and premiums are estimated from historical data by **factor analysis**, which searches for return patterns common to broad groups of stocks and outputs (1) the number of common factors and (2) each investment's beta on each factor plus each factor's realized premium. Crucially, factor analysis does **not identify the factors in economic terms** — market risk is measured against multiple *unspecified* macroeconomic factors.

#### C. Multi-Factor Models

The APM's unidentified factors are a statistical strength but an intuitive weakness. Multi-factor models replace them with **specified macroeconomic factors** — chosen empirically by matching the time series of the statistical factors against macroeconomic series. A 1980s study *(Chen, Roll and Ross, 1986, Journal of Business)* found the statistical factors correlate strongly with: industrial production, changes in the corporate-bond default premium, shifts in the term structure, unanticipated inflation, and changes in the real rate of return. The resulting expected-return equation:

```
E(R) = R_f + β_GNP [E(R_GNP) − R_f] + β_I [E(R_I) − R_f] + ... + β_δ [E(R_δ) − R_f]
```

where β_GNP = beta relative to industrial-production changes, E(R_GNP) = expected return on a portfolio with beta 1 on that factor and 0 on all others, and analogously for inflation and the other factors.

> *Definition — Unanticipated inflation: the difference between actual and expected inflation.*

The cost of specifying factors is misidentification risk: the relevant economic factors and their premiums shift over time (oil prices drove returns in the 1970s but not in most other periods), and using wrong or missing factors produces inferior cost-of-equity estimates. Like the APM, these models assume market risk is best captured by multiple macro factors and betas on each — but unlike the APM they name the factors.

#### D. Proxy Models

All previous models start from economic reasoning about market risk. Proxy models work backwards from the data: they look for **firm characteristics** correlated with high past returns over long horizons and treat those characteristics as proxies for market risk.

> *Definition — Book-to-market ratio: book value of equity divided by market value of equity.*

The landmark study is **Fama and French (1992, Journal of Finance)**: over 1963–1990, actual returns were strongly related to market capitalization and price-to-book ratios — small-cap and low price-to-book firms earned higher returns — while beta explained little. Their NYSE monthly-return regression:

```
Rₜ = 1.77% − 0.11 ln(MV) + 0.35 ln(BV/MV)
```

where MV = market value of equity and BV/MV = book-to-market ratio. Plugging a firm's values in yields an expected monthly return — e.g., MV = $100 million and BV/MV = 0.5:

```
Rₜ = 1.77% − 0.11 ln(100) + 0.35 ln(0.5) = 1.02% per month
```

As firm-level data grew richer, proxy models added variables — notably **price momentum** (recent price appreciation predicts higher subsequent returns). In summary: proxy models measure market risk with firm characteristics rather than macro betas *(footnote: confusingly, researchers now often call these "multi factor models" too)*.

### A Comparative Analysis of Risk and Return Models

All the models share two ingredients — only market-wide risk is rewarded, and expected return is derived from a measure of that risk.

*[Figure 3.7: Competing Models for Risk and Return in Finance — a three-step schematic. Step 1 (defining risk): risk is the variance of actual returns around expected return, shown as three distributions — riskless (spike), low-risk (narrow), high-risk (wide). Step 2 (rewarded vs. unrewarded): firm-specific risk diversifies away (small position sizes; averaging out) while market risk cannot; since the marginal investor is diversified, only market risk is priced. Step 3 (measuring market risk), four columns: CAPM — with no private information and no transaction costs, everyone holds the market portfolio, so market risk = risk added to the market portfolio, estimated as beta vs. the market (regression); APM — with no arbitrage opportunities, market risk = exposures to unspecified market factors, estimated as factor betas (factor analysis); Multi-factor — market risk must come from macro forces, measured as betas vs. specified macroeconomic factors (regression); Proxy — in an efficient market, long-run return differences must reflect market-risk differences, so find correlated proxy variables (regression on proxies).]*

Tradeoffs and evidence:

- **CAPM:** most assumptions, simplest model — one risk factor to estimate. It underperforms richer models when a firm's risk loads on factors poorly represented in the market index — e.g., oil companies have low CAPM betas because their risk is oil-price risk; a multi-factor model with a commodity factor gives a better (higher) cost of equity. *(Footnote: Weston and Copeland (1992) estimated 1989 oil-company cost of equity at 14.4% via CAPM vs. 19.1% via APM.)*
- **APM's intuitive block:** unidentified factors make betas hard to interpret and hard to project through firm changes or restructurings.
- **Does the CAPM work?** Early tests found betas and returns positively related, though variance also explained returns — attributed to testing limitations. **Roll (1977)** argued the CAPM is untestable: the true market portfolio (every traded asset) is unobservable, so every test is a joint test of the model *and* the chosen market proxy — any rejection may indict the proxy, not the model; there is thus no way to ever prove the CAPM works.
- **Fama–French (1963–1990):** little relationship between beta and annual returns; size and book-to-market were better risk proxies. Contested on two fronts: **Amihud, Christensen and Mendelson** re-ran the same data with different statistical tests and found betas *did* explain returns; **Chan and Lakonishok (1993)** used a longer 1926–1991 series and found the positive beta-return relation broke down only after 1982 — plausibly due to indexing lifting large low-beta S&P 500 stocks — and that betas still work in extreme markets: the highest-beta decile did far worse than the market in its ten worst months between 1926 and 1991.

*[Figure 3.8: Returns and Betas — Ten Worst Months between 1926 and 1991 — grouped bar chart (e.g., Mar 1988, Oct 1987, May 1940, May 1932, Apr 1932, Sep 1937, Feb 1933, Oct 1932, Mar 1980, Nov 1973) showing high-beta stocks falling much further than the whole market, which in turn fell further than low-beta stocks, in every one of the ten months. Takeaway: beta is a useful guide to risk in extreme market conditions.]*

- **Explaining vs. predicting:** APM and multi-factor models explain *past* returns better because they use more factors. But projecting *future* expected returns requires estimating every factor beta and premium — all volatile — and estimation error can wipe out the theoretical improvement over CAPM. Proxy/regression models are even more exposed: the proxies that work in one period (e.g., size) may not work in the next. This is why multi-factor models are more accepted in portfolio performance evaluation (backward-looking) than in corporate finance (forward-looking).
- **Bottom line:** the CAPM's survival as the default reflects its intuitive appeal and the failure of more complex models to deliver materially better *expected* returns. The recommended stance: use the CAPM judiciously, without over-reliance on historical data, informed by the accumulated evidence from its challengers. *(Footnote: Barra, a leading beta service, adjusts betas for fundamentals such as size and dividend yield, drawing on the regression-proxy literature.)*

> **In Practice: Implied costs of equity and capital**
> Given the assumption controversies and estimation error in all these models, some analysts back the cost of equity **out of the market price** for publicly traded companies. If the market price is right and you're willing to assume future growth, a perpetual-growth dividend model can be inverted. Example — stock at $50, expected dividend next year $2.50, dividends growing 4% forever:
>
> ```
> Stock price = Expected dividends next year / (Cost of equity − Expected growth rate)
> $50 = $2.50 / (r − 0.04)   →   r = 9%
> ```
>
> The approach extends to the whole firm and the cost of capital. It is model-free, but the answer is only as good as the growth/cash-flow estimates (over-optimistic growth ⇒ understated cost of equity) and it presumes the market price is right.

---

## The Risk in Borrowing: Default Risk and the Cost of Debt

Lenders face the possibility that a borrower defaults on interest and principal — **default risk** — and higher-default-risk borrowers should pay higher rates. Unlike equity models (which price *market* risk into *expected* returns), default-risk models measure the effect of **firm-specific** default risk on **promised** returns. Diversification cannot excuse ignoring firm-specific risk here, because bonds have asymmetric payoffs: the best case is simply receiving the promised coupons — there is no upside participation if the company thrives — while every other scenario delivers less than promised. So the expected return on a corporate bond reflects the issuing firm's specific default risk.

### The Determinants of Default Risk

Default risk depends on the firm's capacity to generate operating cash flows relative to its financial obligations (interest and principal — legally committed payments, unlike discretionary dividends or capex), and on the liquidity of its assets. Three propositions:

1. Firms generating **high cash flows relative to obligations** have lower default risk.
2. **More stable cash flows** (predictable businesses) mean lower default risk than cyclical/volatile businesses at the same debt level.
3. **More liquid assets**, for a given cash-flow/obligation profile, mean lower default risk (easier to liquidate in a crisis).

Historically, default risk has been assessed with financial ratios measuring cash-flow coverage, controlled for industry effects to capture cash-flow variability and asset liquidity.

### Default Risk and Interest Rates

When banks dominated lending, each bank did its own default assessment (and still does for most lenders). The corporate bond market created demand for **third-party assessments** — few individual bondholders could do the analysis themselves — giving rise to ratings agencies (Standard & Poor's, Moody's) that convert judgments from public and private information into published **bond ratings**, a shorthand default-risk measure.

#### The Ratings Process

Ratings usually begin when a company planning a bond issue requests one — ratings aren't legally required, but unrated issuers struggle to find buyers. Rated companies concentrate in the U.S. (deepest corporate bond market); Europe still leans on bank lending except for the largest firms. The agency gathers public data (financial statements) and company-provided information, decides a rating, and lets the company appeal with additional information before release.

*[Figure 3.9: The Ratings Process (S&P) — flowchart: issuer requests rating → S&P assigns an analytical team → analysts research S&P library, internal files, databases → issuer meeting/facility tour → final analytical review and rating-committee presentation → committee discussion and vote → issuer notified → optional appeal with additional information (committee re-votes) → rating released.]*

Ratings are letter grades: S&P's AAA / Moody's Aaa is the top grade (lowest default risk), descending to D (in default, S&P).

**Ratings scale (condensed from the chapter's Index of Bond Ratings table):**

| S&P | Moody's | Meaning |
|---|---|---|
| AAA | Aaa | Highest grade; capacity to repay extremely strong / best quality, minimal risk |
| AA | Aa | Strong capacity; differs from top grade only slightly / high quality but thinner margin of protection |
| A | A | Strong capacity but susceptible to adverse changes in circumstances and economic conditions / favorable attributes but some future-risk susceptibility |
| BBB | Baa | Adequate capacity, but adverse conditions more likely to impair it / neither highly protected nor poorly secured |
| BB, B, CCC, CC | Ba, B | Predominantly speculative (BB least, CC most) / speculative risk; B generally lacks desirable investment traits |
| D | Caa, Ca, C | In default or payments in arrears / poor standing to highly speculative, often in default |

> **In Practice: Investment grade and junk bonds**
> BBB (S&P) / Baa (Moody's) and above = **investment grade**; below BBB = **junk / high-yield**. The line is arbitrary but consequential for two reasons: many portfolios are barred from sub-investment-grade bonds, making the investment-grade market wider and deeper; and sub-investment-grade firms face tougher, costlier fundraising — until the early 1980s they often couldn't issue new bonds at all *(footnote: Michael Milken and Drexel Burnham created the original-issue junk bond market, largely to finance hostile takeovers)* — plus knock-on costs like tighter supplier credit and debt covenants.

#### Determinants of Bond Ratings

Ratings rest mainly on public information, especially financial ratios measuring debt-service capacity and cash-flow stability (with some private information and agency judgment mixed in).

**Table 3.2 — Key financial ratios used to measure default risk:**

| Ratio | Definition |
|---|---|
| Pretax interest coverage | (Pretax income from continuing operations + interest expense) / gross interest |
| EBITDA interest coverage | EBITDA / gross interest |
| Funds from operations / total debt | (Net income from continuing operations + depreciation) / total debt |
| Free operating cash flow / total debt | (Funds from operations − capex − change in working capital) / total debt |
| Pretax return on permanent capital | (Pretax income from continuing operations + interest expense) / (average beginning- and end-of-year long- and short-term debt, minority interest and shareholders' equity) |
| Operating income / sales | (Sales − COGS before depreciation − selling − administrative − R&D expenses) / sales |
| Long-term debt / capital | Long-term debt / (long-term debt + equity) |
| Total debt / capitalization | Total debt / (total debt + equity) |

**Table 3.3 — Median ratios by S&P rating, manufacturing firms, 2006–2008:**

| | AAA | AA | A | BBB | BB | B | CCC |
|---|---|---|---|---|---|---|---|
| EBIT interest coverage (×) | 17.5 | 10.8 | 6.8 | 3.9 | 2.3 | 1.0 | 0.2 |
| EBITDA interest coverage (×) | 21.8 | 14.6 | 9.6 | 6.1 | 3.8 | 2.0 | 1.4 |
| Funds flow / total debt (%) | 105.8 | 55.8 | 46.1 | 30.5 | 19.2 | 9.4 | 5.8 |
| Free operating cash flow / total debt (%) | 55.4 | 24.6 | 15.6 | 6.6 | 1.9 | −4.5 | −14.0 |
| Return on capital (%) | 28.2 | 22.9 | 19.9 | 14.0 | 11.7 | 7.2 | 0.5 |
| Operating income / sales (%) | 29.2 | 21.3 | 18.3 | 15.3 | 15.4 | 11.2 | 13.6 |
| Long-term debt / capital (%) | 15.2 | 26.4 | 32.5 | 41.0 | 55.8 | 70.7 | 80.3 |
| Total debt / capital (%) | 26.9 | 35.6 | 40.1 | 47.4 | 61.3 | 74.6 | 89.4 |
| Number of firms | 10 | 34 | 150 | 234 | 276 | 240 | 23 |

(Coverage ratios are in times-interest-earned; the rest are percentages.) Unsurprisingly, profitable firms with high cash flows relative to debt payments and low debt ratios rate higher. Individual exceptions exist because agencies apply subjective judgment — e.g., a firm with weak current ratios but expected dramatic improvement may get a better rating than the numbers imply — but for most firms, ratios give a reasonable basis for guessing the rating. *(Web dataset referenced: key financial ratios by rating class for the U.S., most recent period.)*

#### Bond Ratings and Interest Rates

A corporate bond's rate should reflect its default risk; if ratings measure that risk well, higher-rated bonds should carry lower rates. The gap between a defaultable bond's rate and a default-free government bond's rate is the **default spread**, which varies by maturity and over time with economic conditions.

**Table 3.4 — Default spreads by rating class, January 2009 (10-year bonds, S&P ratings, T-bond rate 3.5%; source: bondsonline.com):**

| Rating | Default spread | Interest rate on bond |
|---|---|---|
| AAA | 1.25% | 4.75% |
| AA | 1.75% | 5.25% |
| A+ | 2.25% | 5.75% |
| A | 2.50% | 6.00% |
| A− | 3.00% | 6.50% |
| BBB | 3.50% | 7.00% |
| BB | 4.25% | 7.75% |
| B+ | 5.00% | 8.50% |
| B | 6.00% | 9.50% |
| B− | 7.25% | 10.75% |
| CCC | 8.50% | 12.00% |
| CC | 10.00% | 13.50% |
| C | 12.00% | 15.50% |
| D | 15.00% | 18.50% |

Spreads also vary by maturity within a rating: for higher-rated bonds spreads generally widen at longer maturities, while for low-rated bonds spreads can *narrow* with maturity (near-term default risk exceeds long-term). Historically, spreads in every rating class widen in recessions and narrow in booms.

*[Figure 3.10: Default Spreads on Ratings Classes — grouped bars of spread-over-treasury by rating (Aaa/AAA down through Caa/CCC+) at four dates: 1-Jan-08, 12-Sep-08, 12-Nov-08, 1-Jan-09. Spreads widen dramatically through 2008 across all classes, with low-grade spreads blowing out from ~7% to ~16%. Takeaway: default spreads must be re-estimated regularly, especially when the economy shifts between growth regimes.]*

Final point: everything said about ratings and rates applies more generally to default risk and rates — ratings are a convenience; absent them, lenders would still have to assess default risk and set their own default spreads. *(Web dataset referenced: `ratings.xls` — default spreads by rating class, most recent period.)*

> **In Practice: Ratings changes and interest rates**
> Agencies change ratings at their discretion, usually triggered by changes in operating health, new security issues, or new borrowing — downgrades follow deteriorating performance or heavy new debt; upgrades follow better earnings or new equity. But agencies deliberate (often via credit-watch lists) while markets react instantly, so bond prices typically fall *before* downgrades and rise *before* upgrades; studies show much of the price reaction to deteriorating credit precedes the ratings action. Ratings changes still carry some information (markets react, modestly). Arguably the agencies' biggest service is providing a default-risk measure that is *comparable across hundreds of firms*, letting bond investors categorize potential investments simply.

---

## Conclusion

- Risk in finance is measured by deviations of actual returns from expected returns. Two broad types: **equity risk** (investments with expected but not promised cash flows) and **default risk** (investments with promised cash flows).
- For equity risk, variance of actual around expected returns is the base measure; it splits into **firm-specific risk** (affects one or a few investments; diversifiable) and **market risk** (affects many; not diversifiable). Assuming the marginal investor is well diversified, only market risk matters for equity pricing.
- The models differ on measuring market risk: **CAPM** uses a single market beta — how much risk an investment adds to a portfolio of all traded assets; **APM** and **multi-factor models** allow multiple market-risk sources with a beta per source; **proxy/regression models** use firm characteristics (like size) historically correlated with high returns. In all cases the risk measure yields an expected return on equity — the **cost of equity**.
- For default risk, the measure is the likelihood promised cash flows aren't delivered; riskier borrowers pay a **default premium** over the riskless rate. For most U.S. companies, ratings agencies supply the measure via bond ratings, which largely determine borrowing rates; even unrated borrowers pay spreads reflecting lender assessments. These default-risk-adjusted rates are the **cost of debt**.

---

## Problems and Questions (end of chapter)

Sixteen problems; topics condensed:

1. **Microsoft 1989–1998 prices** (no dividends; $1.20 rising to $69.34): compute average annual return, standard deviation and variance; discuss whether historical risk measures should persist.
2. **Unicom (regulated Illinois utility) 1989–1998 prices and dividends**: same three tasks as #1 — contrast with a high-growth stock.
3. **Scientific Atlanta vs. AT&T annual returns 1989–1998**: average and standard deviation for each; covariance and correlation between them; variance of an equal-weighted portfolio.
4. **Gold vs. stocks** (gold: 8% mean, 25% σ; stocks: 20% mean, 22% σ; ρ = −0.4): which to pick standalone; how to answer a friend citing gold's big payoffs; mean/variance of a 50-50 portfolio; the effect if a gold cartel varies production countercyclically to U.S. stocks.
5. **Coca-Cola (25%, 36%) and Texas Utilities (12%, 22%), ρ = 0.28**: mean and σ of a 60/40 portfolio; the minimum-variance portfolio; repeat after international diversification changes Coke to σ = 45%, ρ = 0.20.
6. **Times Mirror (14%, 25%) and Unilever (18%, 40%), 50/50**: portfolio variance as a function of correlation from −1 to +1 in 0.2 steps.
7. **Three assets (Sony 11%/23%, Tesoro 9%/27%, Storage Tech 16%/50%)** with a given correlation matrix (ρ_Sony,Tesoro = −0.15, ρ_Sony,ST = 0.20, ρ_Tesoro,ST = −0.25): variance of an equally weighted three-asset portfolio.
8. **Markowitz portfolio over 1,250 assets**: how many expected returns and variances, and how many covariances, must be estimated.
9. **Average variance 50, average covariance 10**: expected portfolio variance at 5, 10, 20, 50, 100 securities; how many holdings before portfolio risk is within 10% of the minimum.
10. **$1M in Vanguard 500 (12%, 25%), shifting $200K to 5% T-bills**: new portfolio expected return and standard deviation.
11. **CAPM allocations** (market: 15% return, 30% σ; riskless: 5%): the market/riskless split for target σ of 0%, 15%, 30%, 45%, and for a target return of 12%.
12. **Scientific Atlanta vs. market portfolio returns 1989–1998**: covariance with the market, both variances, and beta.
13. **United Airlines** (β = 1.50, σ = 66%; market σ = 22%): correlation with the market; the fraction of UA's risk that is market risk.
14. **APM with five factor betas/premiums for Bethlehem Steel** (betas 1.2/0.6/1.5/2.2/0.5; premiums 2.5%/1.5%/1.0%/0.8%/1.2%): most-exposed factor and whether APM can identify it economically; expected return at R_f = 5%; CAPM comparison (β = 1.1, market premium 5%); why the two differ.
15. **Multi-factor model for Emerson Electric** (interest-rate level β = 0.5 / 1.8%; term structure β = 1.4 / 0.6%; inflation β = 1.2 / 1.5%; GNP growth β = 1.8 / 4.2%; R_f = 6%): expected return.
16. **Fama–French regression** `Rₜ = 0.0177 − 0.11 ln(MV) + 0.35 ln(BV/MV)` (MV, BV in hundreds of millions; monthly returns): expected annual return for Lucent (MV $240B, BV $13.5B); CAPM comparison (β = 1.55, R_f = 6%, premium 5.5%); why the approaches differ.

## Live Case Study: Stockholder Analysis

**Objective:** determine who the average and marginal investors in your chosen company are — relevant because risk-and-return models assume a diversified marginal investor.

**Key questions:** Who is the average investor (individual vs. pension fund, taxable vs. tax-exempt, small vs. large, domestic vs. foreign)? Who is the marginal investor?

**Framework:**

1. *Who holds the stock?* — number of stockholders; percent held by institutions; foreign listings and non-domestic ownership share.
2. *Insider holdings* — who the insiders are (anyone over 5% counts, beyond managers/directors); their role in running the company; percent held by insiders and by employees (including pension plans); recent insider buying/selling.

**Data sources:** insider and institutional ownership are in SEC filings (used to build largest-holder rankings); insider trades are SEC-recorded with a few weeks' lag. Online data reference: http://www.stern.nyu.edu/~adamodar/cfin2E/project/data.htm

---

## Quick-Reference Formula Sheet

| # | Formula | Context |
|---|---|---|
| 1 | `Returnₜ = (Priceₜ − Priceₜ₋₁ + Dividendsₜ) / Priceₜ₋₁` | Holding-period return |
| 2 | `Annualized σ = monthly σ × √12`; `Annualized variance = monthly variance × 12` | Annualizing |
| 3 | `Semi-variance = Σ (Rₜ − R̄)² / n` over below-average periods only | Downside risk |
| 4 | `μ_p = w_A μ_A + (1 − w_A) μ_B` | Two-asset portfolio return |
| 5 | `σ²_p = w_A² σ²_A + (1 − w_A)² σ²_B + 2 w_A w_B ρ_AB σ_A σ_B` | Two-asset portfolio variance |
| 6 | `σ_AB = ρ_AB σ_A σ_B` | Covariance ↔ correlation |
| 7 | `βᵢ = Cov(Rᵢ, Rₘ) / σ²ₘ` | Beta |
| 8 | `E(Rᵢ) = R_f + βᵢ [E(Rₘ) − R_f]` | CAPM |
| 9 | `R = E(R) + m + ε` | Return decomposition (APM) |
| 10 | `R = E(R) + (β₁F₁ + ... + βₙFₙ) + ε` | APM factor form |
| 11 | `E(R) = R_f + Σⱼ βⱼ [E(Rⱼ) − R_f]` | APM expected return |
| 12 | `E(R) = R_f + βₘ (E(Rₘ) − R_f)` | CAPM as 1-factor APM |
| 13 | `E(R) = R_f + β_GNP[E(R_GNP) − R_f] + β_I[E(R_I) − R_f] + ...` | Multi-factor model |
| 14 | `Rₜ = 1.77% − 0.11 ln(MV) + 0.35 ln(BV/MV)` | Fama–French proxy regression |
| 15 | `Price = Div₁ / (r − g)` ⇒ solve for r | Implied cost of equity |
