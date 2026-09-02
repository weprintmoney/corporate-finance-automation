# Primers

Pre-course primers Damodaran recommends before starting Corporate Finance — accounting, statistics, finance (risk & return), and present value. Each is a full-fidelity markdown conversion of the original NYU Stern source, with formula images transcribed to plain-text math and figures described inline.

## Doc Index

| File | Subject | Why it matters for the course |
|------|---------|-------------------------------|
| `accounting-primer.md` | Accounting | The raw material for valuing a company comes from accounting statements — how to read them and where to find what you need. Income statement, asset/liability measurement, profitability and leverage ratios. |
| `statistics-primer.md` | Statistics | Making sense of large, contradictory data — exactly the problem in valuation. Descriptive stats, correlation, regression mechanics. |
| `risk-and-return-primer.md` | Finance | The tools drawn on extensively in valuation. *Applied Corporate Finance* 3rd ed. ch. 3 — risk measurement, CAPM/APM/multi-factor models, default risk and ratings. |
| `present-value-primer.md` | Finance | Time value of money — discounting/compounding mechanics, the five cash-flow types (simple CF, annuity, growing annuity, perpetuity, growing perpetuity), bond and stock valuation examples. |

## Statistics quick reference

Supplements `statistics-primer.md` (which covers descriptive stats and regression) with distributions and inference.

| Concept | Notes |
|---------|-------|
| Random variable | Discrete vs. continuous |
| Expected value | E[X] = Σ x·P(x) (discrete); ∫ x·f(x) dx (continuous) |
| Variance / SD | Var(X) = E[(X − μ)²]; SD = √Var |
| Covariance / correlation | Cov(X,Y); ρ = Cov(X,Y) / (σₓ σᵧ) |
| Law of large numbers | Sample mean → population mean as n grows |
| Central limit theorem | Sample-mean distribution approaches Normal for large n |

| Distribution | When it shows up |
|--------------|------------------|
| Normal | Returns approximations, error terms, CLT results |
| Binomial | Fixed-trial success counts |
| Poisson | Rare-event counts over an interval |
| Log-normal | Prices (returns are ~Normal, prices are ~log-normal) |
| Student's t | Small-sample means, unknown σ |
| Chi-square | Variance tests, goodness-of-fit |
| F | Ratio of variances, ANOVA, regression significance |

| Test | Use |
|------|-----|
| z-test | Known σ, large n |
| t-test | Unknown σ, small n |
| Paired t-test | Before/after on same units |
| Two-sample t | Compare means across groups |
| Chi-square | Categorical association / goodness-of-fit |
| ANOVA | Compare 3+ group means |

**Interpretation reminder:** p-value = P(data at least as extreme | H₀ true). It is NOT P(H₀ true).

**Regression:** OLS assumptions — linearity, independence, homoscedasticity, normal residuals, no perfect multicollinearity. Read the output: coefficient sign + magnitude, standard error, t-stat, p-value, R², adjusted R², F-stat. In multiple regression each coefficient is the effect of X holding all other X's constant.
