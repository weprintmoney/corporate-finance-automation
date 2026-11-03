---
title: "KBR, Inc. (KBR) — Lesson 12: Debt: Measure and Cost"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# KBR, Inc. (KBR) — Lesson 12: Debt: Measure and Cost

### Lesson 12 — Debt: Measure and Cost

Quick mode: only the question-bank entries tagged with a signal are answered; transcript-layer entries carry no signal and are not part of this run.

## Module 1 Step — Questions for This Lesson

- **Does the company have an agency rating? What default spread and pre-tax cost of debt does it imply?**
  None named in the fetched filings (`debt.rating_actual` null). The observed cost — interest $158M over average face debt — is 6.07% (`debt.kd_pretax_observed`), which is SOFR-plus-margin pricing on secured term loans, not investment-grade pricing.

- **What synthetic rating does interest coverage imply, and what cost of debt?**
  EBIT coverage 4.92x → A- on the small-firm table, spread 0.89%, cost 5.33% (MO §2).

- **If the two differ, why?**
  Coverage flatters KBR: $210M of EBIT is equity earnings of unconsolidated affiliates, $103M of the rise from one LNG project (`facts.equity-earnings-affiliates`), and interest is cut by $21M of swap income locked at 0.89% on $400M until January 2027 (`facts.swaps-expiring-jan-2027`). Lenders price leverage (2.3x net debt/EBITDA, `facts.net-leverage-q1-2026`) and security. Using the synthetic rate lowers the cost of capital to 8.92% (alternatives/kd-synthetic-output.md).

- **What is the market value of interest-bearing debt? If the debt is fixed-rate and rates have moved since it was issued, how far is market value from book?**
  89% of face debt floats; the 4.75% notes ($250M) trade at $246M (10-K Note 20). Market ≈ face; face $2,617M used (`company.debt_face`).

- **What is the debt value of lease commitments, including leases signed but not yet started?**
  $301M (`company.lease_debt`: operating $292M + finance $9M). The lease note (10-K Note 15) does not mention leases signed but not yet commenced; none added.

- **Does the company guarantee debt of joint ventures or special-purpose vehicles, or have take-or-pay capacity contracts, that pass the debt test but sit off the balance sheet?**
  JV performance guarantees are joint and several but not estimable (10-K Note 11). Receivables sold to MUFG ($2,094M sold in FY2025) are a financing that leaves no outstanding balance in the 10-K. Neither is added; listed under `meta.omitted`.

- **How much interest was capitalized into construction, and what does coverage look like once it is added back?**
  None disclosed; KBR is a services firm with $42M of capex (`company.capex`).

- **Did the company lengthen the depreciation lives of servers or equipment, and how much did that raise operating income?**
  No change in useful lives is disclosed; the PP&E note gives estimated useful lives by class with no change described (10-K Note 7).

- **What marginal tax rate applies to the after-tax cost of debt?**
  25% (`market.tax_rate_marginal`); after-tax cost of debt 4.55% (MO §1).

## Notes

Numbers cite `inputs.yaml` fields, `model-output.md` sections (MO §n), `alternatives/` runs, and stated passages (S#) in `sources/statements/kbr-stated-positions.md`.
