---
title: "Review checklist — adversarial pass before a valuation is final"
status: active
owner: weprintmoney
created: 2026-10-24
last_updated: 2026-10-24
---

# Review checklist

Run by a fresh-context subagent given only this file and the company folder. It returns a list of findings, each with file, line, what is wrong, and the evidence. "Looks fine" is not a finding; "checked, matches note 9" is.

The first eleven items are errors that were actually made in the SolarWinds project and only caught lesson by lesson. Check them first.

## Numbers that were wrong once

1. **Equity value vs. enterprise value.** A deal "value" or "price tag" in a headline is usually enterprise value (debt included). Equity value is shares × price. Confirm `company.equity_value` = `company.shares_basic` × `company.share_price` within 1%, and that no share count was backed out of a deal value.
2. **Share count source.** Basic shares come from the cover page of the latest annual or quarterly report. Diluted shares come from the earnings-per-share note. Confirm both sources are the filing, not a data site.
3. **Ownership concentration.** Read the beneficial-ownership table in the proxy (DEF 14A or equivalent). Sponsors and funds are listed separately; do not merge them into one holder, and do not take a press figure. Confirm `governance.controlling_holders` matches the table.
4. **Dividends actually paid.** Read the cash-flow statement and the equity statement for every year in `company.history`. Special dividends count. "Never paid a dividend" needs those statements as evidence.
5. **Lease debt.** From the lease note's present value of lease liabilities, never from an assumed rent multiple. Confirm `company.lease_debt` cites the note.
6. **Debt at face vs. carrying value.** The ledger says which one `company.debt_face` and `company.debt_book` are. If the model uses one, the walkthrough says which and why.
7. **Rating.** `debt.rating_actual` is either an agency rating with the action cited, or null with a statement that the filings disclose none. A rating the filings don't mention is not a rating.
8. **Coverage numerator.** `modeling_choices.coverage_numerator` is stated, and `model-output.md` shows the optimum under all three numerators. If the lesson answers pick one, they say why.
9. **Firm value basis for the optimal-debt loop.** Market value of debt plus equity, computed from the ledger. Not a deal value, not book value.
10. **Stock-based compensation.** Charged as an expense in operating income and in free cash flow. Any EBITDA that adds it back is labeled as the company's adjusted figure, not used as the base.
11. **Deferred revenue.** Not debt. Confirm it is excluded from `company.debt_total`.

## Numbers that could be wrong

12. **Terminal consistency.** Terminal reinvestment rate = terminal growth ÷ stable ROIC. Terminal growth ≤ risk-free rate. Confirm the model output shows both.
13. **Currency consistency.** Risk-free rate, ERP, cash flows, and the debt rate are all in `meta.currency`.
14. **Dates.** Every market input has an `as_of`, and the validator passes its windows (rates 14 days, ERP 45, ratings table and betas 400). No current rate, premium, beta or spread is taken from a lesson spreadsheet or an earlier valuation.
14a. **Risk-free rate and ERP on the same base.** `market.risk_free_rate` = `govt_bond_rate` − `sovereign_default_spread`, and `mature_erp` is the implied premium over that netted rate. A gross Treasury rate paired with a premium over the netted rate (or the reverse) is a finding.
14b. **Cost of debt base.** A rating-based cost of debt is the government bond rate plus the spread, not the netted risk-free rate plus the spread. `model-output.md` section 1 shows which.
14c. **Debt that is easy to miss.** Check the lease note for leases signed but not yet commenced, the commitments and guarantees notes for joint-venture or special-purpose-vehicle debt, and the debt note for capitalized interest. Each one is in the ledger or ruled out with the note cited.
14d. **Inflated coverage.** If the company lengthened depreciation lives or capitalizes interest, the synthetic rating is recomputed without the benefit and the difference is stated.
15. **Peers.** Same fiscal period, same multiple definition (numerator and denominator match), and the peer list in the ledger matches the one used in lesson 35.
16. **Options and RSUs.** Valued as a claim and subtracted from equity value; per-share value uses basic shares, not diluted.
17. **Cash.** The cash figure used in net debt matches the balance sheet, and lesson 33 says whether it is valued at face, discounted, or at a premium.
18. **Tax rate.** The marginal rate is used for the after-tax cost of debt and for levering beta; the effective rate is used only where the ledger says so (base-year cash flow).
19. **Interest coverage.** `company.ebit` ÷ `company.interest_expense` matches what lesson 12 and lesson 18 use.
20. **History arithmetic.** For each year in `company.history`, FCFE = net income − (capex − D&A) − change in working capital + (debt issued − debt repaid). Recompute two years by hand and compare with the model.

## Process

21. **Corrections propagated.** Every entry in the README corrections log has a matching ledger change, a model rerun after it, and a dated note under each affected lesson answer.
22. **Walkthrough trace.** `tools/check-walkthrough.py` passes.
23. **Skipped questions.** Every question-bank entry that applies to the company type has an answer, and every skipped one is listed with a reason.
24. **Readability.** A reader with no finance background can follow the walkthrough. Findings from the reader pass are closed.
25. **Report cites.** Every number in `valuation-report.md` traces to a ledger field or a model-output line.
