---
title: "SolarWinds (SWI) — Lesson 22: Moving to the Optimal Debt Ratio"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 22: Moving to the Optimal Debt Ratio

### Lesson 22 — Moving to the Optimal Debt Ratio

- **Lesson 22, Session 22 · Part 1 — "Under-Levered vs. Over-Levered: Takeover Risk, Bankruptcy Threat, and the Good Projects Test"** ([transcript](../../03-financing-mix-and-dividends/lesson-22/session-22-part-1.md))
    - Quote: "Having too little debt might make you the target of a hostile acquisition."
    - Question for SolarWinds: Is SolarWinds under- or over-levered? If under, is it a takeover target (past returns, size, ownership)? If over, how close is distress? How good are its available projects, and what is the best path and speed to the optimum: recapitalize, or change financing of future projects?
    - Sources needed: Actual and optimal debt ratio; coverage and liquidity; stockholder structure and consent rights; return on invested capital against the cost of capital; the merger chronology.
    - Where to find: model-output.md §1–§4; `company.*`, `debt.*`, `governance.*`, `forecast.years` in inputs.yaml; `sources/filings/swi-def14a-2024.md` (stockholders' agreement); `sources/deal-docs/swi-defm14c-2025-merger.md` (Background of the Merger).
    - Answer: Over-levered, not distressed, with poor projects. So the lecture's route is gradual: use cash flow to pay debt down.
        - Over-levered: actual 33.03% against an optimum of 21% (model-output.md §1, §3). Debt is $468.1M above the optimum (§3). Under the two other coverage numerators the optimum is 26% and 28% (§3), so SolarWinds is above all three.
        - Takeover branch does not apply (the firm is not under-levered). It is also closed by structure: under the stockholders' agreement, any change in control needs the prior written consent of both the Silver Lake funds and the Thoma Bravo funds while the sponsors own at least 30% together; they held 36.56% and 29.79% (`governance.controlling_holders`). No bidder could have gone around them. The merger chronology shows what happened instead: the board sought buyers. In 2023 it approached 13 parties (12 financial sponsors, one strategic), signed nine nondisclosure agreements and received three indications of interest at $12.00 to $13.00 (facts.market-check-2023); all three withdrew by November 2023. Conversations with more than 20 financial and 14 strategic suitors from February 2024 to January 2025 produced no indication of interest (facts.market-check-2024). Jensen's alpha cannot be computed: no price history survives for a delisted stock (`meta.omitted`). The unaffected price of $15.18 against the deal price of $18.50 is a 21.9% premium (18.50 ÷ 15.18 − 1).
        - Bankruptcy threat: not imminent. Coverage is 1.85x on EBIT, a synthetic B- (model-output.md §2); there is no agency rating (`debt.rating_actual`). Cash is $259.3M (`company.cash`), the $130.0M revolver was undrawn (`debt.revolver_undrawn`), the only financial covenant springs when the revolver is more than 35% drawn (`debt.covenants`), the loan is due 2030-02-05, and 2024 free cash flow to equity was positive $127.0M (model-output.md §5). The stress test shows the cushion: with operating income down 30% the optimum falls to 14% (model-output.md §4), so a downturn widens the gap but does not trigger default.
        - Projects: after-tax operating income $208.4M × (1 − 25%) = $156.3M on invested capital of $2,348.0M is a return of 6.66% (model-output.md §8), below the 10.23% cost of capital (model-output.md §1). Book invested capital includes $2,363.2M of goodwill from the 2016 buyout, so the figure measures what the buyers paid, not what the software earns on the money spent building it. Management's plan lifts the operating margin from 32.69% in 2025 to 40.14% in 2030 (`forecast.years`); that is a plan, not a record. Fair reading: the investments inside the company do not clear the hurdle today, and the plan has to be delivered before the answer changes.
        - Path and speed (lecture rule: over-levered, not distressed, no good projects: retire debt out of cash flow, gradually): no sale of assets, no new equity. Management's free cash flow to the firm is $212.0M in 2025 and $258.0M in 2026 (`forecast.years`); after-tax interest at today's level is $112.4M × 75% = $84.3M a year, leaving $127.7M and $173.7M. Cumulatively that is $301.4M over two years and passes the $468.1M gap (the move down to the 21% optimum) in the third year (adding $212.7M for 2027 on the same arithmetic), faster as interest falls. Value of moving is $144.4M, or $10.9M a year (model-output.md §3), so the gain does not justify borrowing to rush. A recapitalization with new debt is the wrong tool in this direction, and any new debt above $300.0M would also have needed both sponsors' consent (facts.sponsor-consent-rights).
        - What the company did instead: in April 2024 it paid a $168.2M special dividend and $26.5M of share withholding for employee taxes on vesting stock (counted as buybacks in `company.history`), while debt stayed at about $1.24 billion. That moved cash out and left debt in place, the opposite of the lecture's advice for this position. The sale to Turn/River closed 2025-04-16.

## Cumulative Project — Questions for This Lesson

- **Is your firm under, over or correctly levered?**
  Over-levered. Actual debt ratio 33.03%, optimum 21% (model-output.md §1, §3); 5 points above even the 28% EBITDA-based optimum. Debt is $468.1M above the optimum.

- **If under levered, is it under threat of a hostile acquisition? If over levered, how imminent is the bankruptcy threat?**
  Over-levered, so the question is bankruptcy, and the threat is not imminent: 1.85x coverage (B-), $259.3M of cash, a $130.0M undrawn revolver, a covenant that only springs above 35% revolver use, and maturity in 2030. The takeover branch is closed in any case: both sponsors (36.56% and 29.79%) must consent to a change in control, so a hostile bid was not possible.

- **How good are the potential projects that the company can invest in?**
  Weak on the record, uncertain on the plan. Return on book invested capital is 6.66% against a 10.23% cost of capital; the discount reflects mostly goodwill. FY2024 revenue grew 5.0% (796.9 ÷ 758.7 − 1, `company.history`); management's plan assumes 8.12% a year to 2030 (`forecast.management_growth`). Outside buyers doubted the plan: bidders in 2023 cited "the relative early stage of the Company's ongoing transition to a subscription-first business model".

- **What is the best path that you see for your firm to get from its actual to its optimal debt ratio?**
  Pay debt down out of operating cash flow over about three years, with no new dividends or buybacks until the ratio is near 21%. No recapitalization, no equity issue. Revisit the speed if operating income falls: at 30% lower the optimum is 14% (model-output.md §4).

## Notes

This lesson turns lesson 18's 21% and lesson 21's APV result into an action. The answer rests on three tests the lecture gives: takeover risk (closed by sponsor consent rights), bankruptcy risk (low, B- with ample liquidity) and project quality (return below the cost of capital). The 2024 special dividend ran against that path; lesson 25 takes it up. The facts used from the merger chronology are listed for the ledger.
