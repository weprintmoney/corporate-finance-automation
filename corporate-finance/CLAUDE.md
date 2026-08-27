# Corporate Finance

How firms value cash flows, choose projects, and finance themselves.

## Core Concepts

| Concept | Notes |
|---------|-------|
| Time value of money | A dollar today > a dollar tomorrow |
| Risk / return | Investors require compensation for risk |
| Efficient markets | Prices reflect available information (weak / semi-strong / strong) |
| Capital structure | Mix of debt and equity used to finance the firm |

## TVM Formulas

| Quantity | Formula |
|----------|---------|
| Future Value | FV = PV · (1 + r)ⁿ |
| Present Value | PV = FV / (1 + r)ⁿ |
| Annuity PV | PV = C · [1 − (1+r)⁻ⁿ] / r |
| Growing Perpetuity | PV = C / (r − g) |
| Effective Annual Rate | EAR = (1 + APR/m)ᵐ − 1 |

## Capital Budgeting

| Rule | Decision |
|------|----------|
| **NPV** | Accept if NPV > 0. Best rule — accounts for scale and TVM. |
| **IRR** | Accept if IRR > cost of capital. Fails with non-conventional cash flows. |
| **Payback** | Simple screen, ignores TVM and post-payback flows. |
| **Profitability Index** | PV of future flows / initial investment. Rank projects under capital rationing. |

## Cost of Capital (WACC)

WACC = (E/V) · rₑ + (D/V) · r_d · (1 − t)

- **rₑ** via CAPM: rₑ = r_f + β · (r_m − r_f)
- Use market values of debt and equity, not book values
- Adjust β for leverage differences (unlever, relever)

## Valuation

| Method | When |
|--------|------|
| DCF (FCFF or FCFE) | Standard — model explicit cash flows + terminal value |
| Comparables | Multiples (EV/EBITDA, P/E) sanity-check DCF |
| Precedent transactions | M&A pricing benchmark |
| Dividend Discount Model | Mature, stable dividend payers |

## Doc Index

| File | Description |
|------|-------------|
| [course-overview/CLAUDE.md](course-overview/CLAUDE.md) | NYU Stern Certificate in Corporate Finance — course outline, syllabus, FAQ, key dates |
