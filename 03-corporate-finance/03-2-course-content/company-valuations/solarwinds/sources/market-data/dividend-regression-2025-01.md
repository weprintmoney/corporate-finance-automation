---
title: "SolarWinds (SWI) — Damodaran US dividend payout regression, January 2025"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# US dividend payout regression, January 2025

Source: Aswath Damodaran, "Dividend Regressions: January 2025", https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/divreg25.htm, section "US Regression: Dividend Payout". The regression output is published as two images, `Budimage/PayoutUSPart1.jpeg` and `Budimage/PayoutUSPart2.jpeg`; the figures below were transcribed from them on 2026-11-03. The January 2025 edition is used because it is the one in force on the 2025-02-05 analysis date. The January 2026 edition is at `divreg26.htm`.

## Definitions (from the page)

- Dividend payout ratio = dividends / net income
- Beta: regression or bottom-up beta
- Return on equity: net income / book value of equity

## Model summary

| Item | Value |
|---|---|
| Sample | United States, 1,532 firms (total df 1,531) |
| Method | Weighted least squares, weighted by market cap (US $) |
| Dependent variable | Payout ratio |
| R | 0.162 |
| R squared | 0.026 |
| Adjusted R squared | 0.025 |
| F | 20.577 (significance < 0.001) |

## Coefficients

| Variable | Coefficient (B) | Std. error | t | Significance |
|---|---|---|---|---|
| Constant | 0.990 | 0.097 | 10.186 | < 0.001 |
| Beta | −0.478 | 0.089 | −5.356 | < 0.001 |
| Return on equity | −0.115 | 0.054 | −2.118 | 0.034 |

**Equation:** payout = 0.990 − 0.478 × beta − 0.115 × return on equity

## Applied to SolarWinds

Beta 1.6714 (levered bottom-up beta, model-output.md §1; the delisted ticker has no regression beta) and return on equity 7.99% (model-output.md §8):

0.990 − 0.478 × 1.6714 − 0.115 × 0.0799 = 0.990 − 0.7989 − 0.0092 = 0.182, a predicted payout of 18.2%.

The regression explains 2.6% of the variation in payout across US companies, so the prediction is a rough marker. The lesson 28 slides' January 2014 regression (payout = 0.649 − 0.296 × beta − 0.800 × growth + 0.300 × debt-to-capital, R squared 19.6%) gives 18.8% for the same company.
