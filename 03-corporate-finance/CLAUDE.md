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
| [03-1-course-overview/CLAUDE.md](03-1-course-overview/CLAUDE.md) | NYU Stern Certificate in Corporate Finance — course outline, syllabus, FAQ, key dates |
| [03-2-course-content/CLAUDE.md](03-2-course-content/CLAUDE.md) | All 36 lesson folders — navigation guide and lesson-index.yaml pointer |
| [03-2-course-content/lesson-index.yaml](03-2-course-content/lesson-index.yaml) | Full lesson map: folder paths, topics, and which file types are present per lesson |
| [03-4-blogs/README.md](03-4-blogs/README.md) | Damodaran "Musings on Markets" archive fetcher — pulls all posts to `posts/` for local text analysis |
| [03-4-blogs/posts/](03-4-blogs/posts/) | Full Damodaran blog archive (~680 posts, 2008–present) |
| [03-3-supplemental-data/market-rates.json](03-3-supplemental-data/market-rates.json) | Live rates from FRED: 10-year Treasury, SOFR, Fed Funds — refreshed weekdays by CI |
| [03-3-supplemental-data/companies/](03-3-supplemental-data/companies/) | Per-ticker JSON from Financial Modeling Prep: income statement, balance sheet, cash flow |
| [03-3-supplemental-data/industry-betas.json](03-3-supplemental-data/industry-betas.json) | Damodaran industry betas — refreshed monthly by CI |
| [03-3-supplemental-data/country-risk.json](03-3-supplemental-data/country-risk.json) | Damodaran country risk premiums — refreshed monthly by CI |

> **Excluded from navigation:** `03-5-damodaran-online/` (website archive — datasets, course materials, papers, tools). The import is corrupted and needs to be re-run before this folder is linked from the index again. Do not navigate agents into it in the meantime.
