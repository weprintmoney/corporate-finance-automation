---
title: "SolarWinds (SWI) — fcffsimpleginzu.xlsx inputs"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# fcffsimpleginzu.xlsx (Feb 2026 edition, pages.stern.nyu.edu/~adamodar/pc/) — SolarWinds inputs, valuation date 2025-02-05

All amounts $M. Source for each value: [../inputs.yaml](../inputs.yaml) (FY2024 10-K; merger information statement plan) unless noted.

## Input sheet

| Cell | Label | Value | Why |
|---|---|---|---|
| B3 | Date of valuation | 2025-02-05 | last undisturbed trading day |
| B4 | Company | SolarWinds Corporation | |
| B7 | Country | United States | |
| B8 / B9 | Industry (US / Global) | Software (System & Application) | one segment |
| B11 / C11 / D11 | Revenues LTM / last 10K / years since | 796.9 / 796.9 / 0 | FY2024 10-K is the LTM (D11=0 only breaks a display cell, E25) |
| B12 / C12 | EBIT | 208.4 / 208.4 | GAAP operating income |
| B13 / C13 | Interest expense | 112.4 / 112.4 | |
| B14 / C14 | Book equity | 1400.7 / 1400.7 | |
| B15 / C15 | Book debt | 1285.0 / 1285.0 | term loan face 1235.7 + leases 49.4 (what the report deducts) |
| B16 | Capitalize R&D? | No | his default; report's DCF expenses R&D |
| B17 | Operating leases? | No | leases already in B15 under ASC 842 |
| B18 | Cash | 259.3 | |
| B19 | Cross holdings | 0 | |
| B20 | Minority interests | 0 | |
| B21 | Shares outstanding | 183.8 | 171.6 basic + 12.214 RSUs/PSUs treated as shares (zero-strike units break the option sheet's LN); equals the report's $185M deduction |
| B22 | Price | 15.18 | |
| B23 | Effective tax rate | 0.25 | her choice 2026-11-03: the −7.8% reported rate is a one-off valuation-allowance release; cash taxes 61.5 on 103.8 pre-tax; plan taxes at 25.4% |
| B24 | Marginal tax rate | 0.25 | |
| B26 | Revenue growth next year | 0.0440 | plan 2025 revenue 832 / 796.9 |
| B27 | Operating margin next year | 0.3269 | plan 2025 EBIT 272 / 832 (plan basis excludes acquired-intangible amortization, restructuring, cyber) |
| B28 | CAGR years 2–5 | 0.0890 | (plan 2030 revenue 1274.6 / 832)^(1/5) − 1; reproduces the plan's 2030 revenue in the sheet's year 6 |
| B29 | Target margin | 0.4014 | plan 2030 |
| B30 | Year of margin convergence | 6 | 2030 |
| B31 / B32 | Sales to capital | leave default (=K27, global software 1.543) | his default |
| B34 | Riskfree | 0.0443 | 10-yr Treasury 2025-02-05 |
| B37 | Options outstanding? | Yes | |
| B38 / B39 / B40 / B41 | number / strike / maturity / std dev | 0.113 / 0.98 / 3 / 0.568 | options only (RSUs in B21); std dev = US software table |
| B45–B72 | Default assumptions | all "No" | stable CoC = rf + mature ERP 4.23% = 8.66%; ROIC = CoC; g = rf 4.43%; no failure; no NOL |

## Cost of capital worksheet

| Cell | Value | Why |
|---|---|---|
| B11 | I will input | the sheet's 2026 industry betas/ERP post-date the 2025-02-05 valuation; 10.67% is his method (bottom-up beta, synthetic rating) on the course's Jan-2025 data |
| B12 | 0.1067 | report §2 |

## Expected departures from the repo model's DCF (stated in the report)

- 10-year horizon with growth fading to 4.43% after year 5; the repo model stops at 2030.
- Reinvestment = Δrevenue ÷ 1.543 (his industry default); the repo model used the plan's prepayment-funded (negative) reinvestment.
- Stable cost of capital 8.66% (rf + mature ERP) vs the repo model's 8.23%; terminal growth 4.43% vs 2.5%.
- Cost of capital fades 10.67% → 8.66% over years 6–10; the repo model held 10.67% through 2030.
