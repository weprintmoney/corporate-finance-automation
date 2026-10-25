---
title: "SolarWinds (SWI) — Lesson 17: The Trade Off"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 17: The Trade Off

### Lesson 17 — The Trade Off

- **Lesson 17, Session 17 · Part 1 — "Debt vs. Equity and the Corporate Life Cycle"** ([transcript](../../02-investment-returns-and-financing/lesson-17/session-17-part-1.md))
    - Quote: "One of the most common problems among corporations is corporations that refuse to act their age."
    - Question for SolarWinds: Does SolarWinds' leverage fit its life-cycle stage, or is it a legacy of past ownership (a buyout, a founder's aversion to debt, a family tradition)? How has the debt ratio moved over the years in the ledger, and does the trend match the company's age?
    - Sources needed: Debt and equity by year; growth and margins (life-cycle stage); peers' debt ratios; the history of the debt.
    - Where to find: `company.history`, `company.debt_total`, `company.equity_value`; `peers`; `sources/filings/swi-10k-fy2018.md` (debt note, selected data).
    - Answer: Both. The company is mature, and the leverage is a legacy of the buyout. It has been shrinking toward what a mature company carries, but is still above its peers.
        - **Stage.** Revenue grew 5.0% in 2024, from $758.7M to $796.9M (`company.history`); 93.5% of it is recurring maintenance and subscription revenue (facts.recurring-revenue-share); GAAP EBIT is $208.4M (`company.ebit`). Slow growth, steady cash, low capital needs: a mature company, which the course says can carry debt.
        - **Legacy.** After the 2016 buyout, debt principal was $2,358.1M at the end of 2017, of which $680.0M was a second-lien loan, against a book equity deficit of $729.8M (facts.debt-principal-2017). The October 2018 IPO raised $375.0M at $15.00 a share (facts.ipo-2018) and part of it repaid $315.0M of that second lien; principal ended 2018 at $1,970.1M (facts.debt-principal-2018). Debt then fell to $1,319.2M in 2022 after $664.4M was repaid that year, then $1,300.4M and $1,285.0M (`company.history`, debt_total). The direction of the debt is down, which is what an inherited stack looks like when it is being managed down, not a target being chosen.
        - **Ratio now.** Debt is 33.03% of the $3,889.9M market value of the firm (model-output.md §1). Book debt including leases is 47.28% of book capital (§1). Against the eight peers it is high: their debt ratios range from 0.88% to 45.28% (`peers`, debt_ratio) with a median of 11.7% (arithmetic on the eight values). Only Open Text (45.28%) and Progress Software (38.46%) carry more. Open Text's growth came from buying Micro Focus (`peers` note). Compare lesson 18, where the cost-of-capital approach puts the optimum at 21%.

- **Lesson 17, Session 17 · Part 2 — "The Trade-Off on Debt: Tax Benefits, Discipline, Bankruptcy and Agency Costs"** ([transcript](../../02-investment-returns-and-financing/lesson-17/session-17-part-2.md))
    - Quote: "The biggest plus of using debt is the tax code rewards you for borrowing money."
    - Question for SolarWinds: For SolarWinds, how large are the tax benefit and the discipline benefit of debt against the bankruptcy, agency and flexibility costs? Judged qualitatively from the trade-off alone, does the company carry too much or too little debt?
    - Sources needed: Marginal tax rate, interest expense, cash taxes paid, covenants, asset base, R&D.
    - Where to find: `market.tax_rate_marginal`, `company.debt_total`, `debt.covenants`, `company.goodwill`, `company.rd_expense`; `sources/filings/swi-10k-fy2024.md` (cash flow statement, Note 9).
    - Answer: The tax benefit is real and the cost side is mostly lost flexibility. Judged on this trade-off alone, the company has somewhat too much debt.
        - **Tax benefit.** Interest of $112.4M (`company.interest_expense`) × the 25% marginal rate (`market.tax_rate_marginal`) = $28.1M a year. It is usable: SolarWinds paid $61.5M of cash income taxes in 2024 (facts.cash-flow-items-2024).
        - **Discipline benefit.** Small, and hard to see. Two private equity firms control the company (`governance.controlling_holders`), and the board paid a $168.2M special dividend in April 2024 (`company.history`, 2024), but nothing in the filings ties that payout to pressure from debt service.
        - **Bankruptcy cost.** Coverage is thin. EBIT covers interest 1.85 times, a synthetic B- (model-output.md §2). No agency rating is disclosed (`debt.rating_actual`). But the loan runs to February 2030, and the only financial covenant, a first-lien net leverage test of 7.40 to 1, applies only when more than 35% of the revolver is drawn (`debt.covenants`), and the revolver was undrawn (`debt.revolver_undrawn`: $130.0M). So there was no near-term default trigger.
        - **Agency cost.** Low. Lenders did not lock the company down: the credit agreement allowed the dividend above, and R&D grew to $108.6M (`company.rd_expense`) while levered. The assets are mostly goodwill of $2,363.2M (`company.goodwill`), so lenders have little hard collateral and price it through the rate, SOFR plus 2.75%.
        - **Flexibility cost.** The big one. Cash interest paid was $104.5M against operating cash flow of $188.3M (facts.cash-flow-items-2024), 55.5% (arithmetic). A change of control is an event of default (`debt.covenants`), so any sale had to refinance the loan. It did: Turn/River's closing financing was a $2.225 billion first-lien term loan, a $200.0M revolver and a $525.0M second-lien loan (facts.new-debt-2025).

## Cumulative Project — Questions for This Lesson

- **What are the different kinds or types of financing that this company has used to raise funds? Where do they fall in the continuum between debt and equity?**
  From most debt-like to most equity-like:
    1. Operating leases, $49.4M (`company.lease_debt`). Fixed payments, counted as debt.
    2. The first-lien term loan, $1,235.7M face (`company.debt_face`). Senior, secured, floating-rate (`debt.rate_type`), the purest debt.
    3. The revolving credit facility, $130.0M, undrawn (`debt.revolver_undrawn`).
    4. A second-lien term loan, outstanding at $680.0M at the end of 2017 and gone by the end of 2018 (facts.debt-principal-2017, facts.debt-principal-2018). A step closer to equity, since it ranks behind the first lien.
    5. Deferred revenue, $389.3M (`company.deferred_revenue`). Customers' prepayments. Not debt, because it is owed in service and not cash, and not equity.
    6. Restricted stock units and options, $187.0M at the unaffected price (`company.options_value`). Equity paid to employees. Stock compensation was $76.5M in 2024 (`company.sbc`).
    7. Common stock, sold in the 2018 IPO (facts.ipo-2018). One class, one vote a share, and no preferred stock issued (`governance.share_classes`).
  There is nothing between the loan and the common stock: no convertible debt and no preferred shares. The company uses both ends, never the middle.

- **How large, in qualitative or quantitative terms, are the advantages to this company from using debt? How large, in qualitative or quantitative terms, are the disadvantages to this company from using debt? From the qualitative trade off, does this firm look like it has too much or too little debt?**
  Advantages: a $28.1M a year tax shield (above) and little else. Disadvantages: interest consuming 55.5% of operating cash flow, coverage of 1.85 times (model-output.md §2), an exposure of about $12.4M a year to each point of interest rates (facts.interest-sensitivity-100bp), and a loan that had to be refinanced on a sale. The tax shield is worth about $395M capitalized at the 7.11% loan rate ($28.1M ÷ 0.0711, `debt.kd_pretax_observed`; arithmetic, and a rough figure since debt is repaid over time). The weighing leans to too much debt, and the quantitative test agrees: the cost of capital is lowest at 21% debt against the current 33.03% (model-output.md §3).

## Notes

The qualitative trade-off says SolarWinds carries somewhat too much debt, and lesson 18 confirms it with numbers. The reason is history. The debt was assumed in 2016, not chosen, and it fell as the company grew into it. Lessons 18 to 20 use the coverage, the covenant and the sponsor ownership recorded here.
