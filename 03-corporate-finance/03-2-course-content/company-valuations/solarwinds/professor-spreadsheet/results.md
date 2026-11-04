---
title: "SolarWinds (SWI) — fcffsimpleginzu.xlsx results"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# SolarWinds in the professor's fcffsimpleginzu.xlsx (Feb 2026 edition) — run 2026-11-03

Google Sheet (her Drive, Corporate Finance folder): "SolarWinds fcffsimpleginzu 2025-02-05"
<https://docs.google.com/spreadsheets/d/18RyIfGFiUzE5I04PMv2s-q_DOStTX9J6N0QHt-7kT9U/edit>
Iterative calculation on (50 iterations, threshold 0.0001). Inputs per [inputs.md](inputs.md) (effective tax 25%, her call).
Cost of capital worksheet: "I will input" 10.67%. Sales to capital: sheet default 1.54 (global software average). All default assumptions left at "No".

## Base run (Valuation output)

| Item | Value |
|---|---|
| Revenue growth | 4.40% (yr 1), 8.90% (yrs 2–5), fading to 4.43% by yr 10 |
| Revenue | 831.96 (yr 1) → 1,263.76 (yr 6) → 1,581.44 (yr 10) |
| EBIT margin | 32.69% (yr 1) → 40.14% (yr 6 on) |
| EBIT | 271.97 → 507.27 (yr 6) → 634.79 (yr 10) |
| Tax rate | 25% throughout |
| Reinvestment | 47.98 (yr 1) … 45.40 (yr 10), = Δrevenue ÷ 1.54 |
| FCFF | 156.00 (yr 1) → 322.21 (yr 6) → 430.70 (yr 10) |
| Cost of capital | 10.67% yrs 1–5, fading to 8.66% by yr 10 |
| Terminal cash flow / cost of capital / growth | 242.85 / 8.66% / 4.43% |
| Terminal value | 5,741.15 |
| PV(terminal value) | 2,200.50 |
| PV(CF over 10 years) | 1,642.72 |
| Value of operating assets | 3,843.23 |
| − Debt | 1,285.00 |
| + Cash | 259.30 |
| Value of equity | 2,817.53 |
| − Options (0.113M at $0.98) | 1.62 |
| Value of equity in common stock | 2,815.91 |
| Shares (171.6 basic + 12.214 RSUs/PSUs) | 183.80 |
| **Value per share** | **$15.32** |
| Price $15.18 as % of value | 99.08% |
| Implied ROIC | 6.44% (base) → 12.90% (yr 5) → 16.35% (yr 10) |

## Sensitivity runs in the same sheet (one change each, then restored)

| Case | Change | Value/share | Equity |
|---|---|---|---|
| Optimal debt ratio (21%) | cost of capital 10.03% | $16.08 | 2,956.6 |
| Revenue at the 2022–2024 rate, plan margins | growth 5.25% yr 1 and yrs 2–5 | $12.65 | 2,327.6 |
| Revenue at 2022–2024 rate, margin held at 2024 plan basis | + margins 29.11% next year and target | $7.77 | 1,428.9 |
| Growth in perpetuity 2.5% instead of the risk-free rate | override B45 | $14.52 | |
| Near-zero reinvestment after year 10, as the plan assumes | override B55 | $16.94 | |
| Base restored | | $15.32 | 2,817.5 |

Financing lever in his sheet: +$0.76 ($139.1M). Deal $18.50 = 1.21x value; market $15.18 = 0.99x.

## Compared with the repo model (final-report as of PR #111)

| | model.py | his sheet |
|---|---|---|
| Value/share | $15.66 | $15.32 |
| Enterprise value | 3,899.8 | 3,843.2 |
| PV explicit CFs | 1,303.2 (6 yrs) | 1,642.7 (10 yrs) |
| PV terminal value | 2,596.7 | 2,200.5 |
| Stable cost of capital | 8.23% | 8.66% (rf + mature ERP 4.23%) |
| Terminal growth | 2.5% | 4.43% (= rf) |
| Reinvestment | plan (negative) | Δrevenue ÷ 1.54 |
| Lever | +$0.69 | +$0.76 |
| Stress (growth 5.25%) | $12.65 | $12.65 |
| Stress (+ margin 29.11%) | $7.79 | $7.77 |
