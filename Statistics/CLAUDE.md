# Statistics

Probability, distributions, inference, and regression — the quantitative backbone for finance work.

## Core Concepts

| Concept | Notes |
|---------|-------|
| Random variable | Discrete vs. continuous |
| Expected value | E[X] = Σ x·P(x) (discrete); ∫ x·f(x) dx (continuous) |
| Variance / SD | Var(X) = E[(X − μ)²]; SD = √Var |
| Covariance / correlation | Cov(X,Y); ρ = Cov(X,Y) / (σₓ σᵧ) |
| Law of large numbers | Sample mean → population mean as n grows |
| Central limit theorem | Sample-mean distribution approaches Normal for large n |

## Distributions

| Distribution | When it shows up |
|--------------|------------------|
| Normal | Returns approximations, error terms, CLT results |
| Binomial | Fixed-trial success counts |
| Poisson | Rare-event counts over an interval |
| Log-normal | Prices (returns are ~Normal, prices are ~log-normal) |
| Student's t | Small-sample means, unknown σ |
| Chi-square | Variance tests, goodness-of-fit |
| F | Ratio of variances, ANOVA, regression significance |

## Inference

| Test | Use |
|------|-----|
| z-test | Known σ, large n |
| t-test | Unknown σ, small n |
| Paired t-test | Before/after on same units |
| Two-sample t | Compare means across groups |
| Chi-square | Categorical association / goodness-of-fit |
| ANOVA | Compare 3+ group means |

**Interpretation reminder:** p-value = P(data at least as extreme | H₀ true). It is NOT P(H₀ true).

## Regression

- **OLS assumptions:** linearity, independence, homoscedasticity, normal residuals, no perfect multicollinearity.
- **Read the output:** coefficient sign + magnitude, standard error, t-stat, p-value, R², adjusted R², F-stat.
- **Multiple regression:** each coefficient is the effect of X holding all other X's constant.

## Doc Index

| File | Description |
|------|-------------|
| _(empty)_ | |
