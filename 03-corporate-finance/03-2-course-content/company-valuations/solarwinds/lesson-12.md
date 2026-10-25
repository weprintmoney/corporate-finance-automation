---
title: "SolarWinds (SWI) — Lesson 12: Debt: Measure and Cost"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 12: Debt: Measure and Cost

### Lesson 12 — Debt: Measure and Cost

- **Lesson 12, Session 12 · Part 1 — "Cost of Debt and What Counts as Debt"** ([transcript](../../01-foundations-and-discount-rates/lesson-12/session-12-part-1.md))
    - Quote: "All interest-bearing obligations are, obviously, debt. All lease commitments are debt."
    - Question for SolarWinds: What is SolarWinds' total debt once leases and every other fixed, tax-deductible, default-triggering commitment are counted? What on the balance sheet looks like debt but fails the test, and what is off the balance sheet but passes it?
    - Sources needed: Debt note, lease note, balance sheet, commitments note.
    - Where to find: `sources/filings/swi-10k-fy2024.md` notes 7, 9, 15 and the balance sheet; `inputs.yaml` fields `company.debt_face`, `company.debt_book`, `company.lease_debt`, `company.off_balance_sheet_debt`, `company.deferred_revenue`, `company.debt_total`.
    - Answer: Total debt is $1,285.0M (`company.debt_total`) = face value of the term loan $1,235.7M (`company.debt_face`) + lease liabilities $49.4M (`company.lease_debt`) + off-balance-sheet debt $0.0M (`company.off_balance_sheet_debt`). The test: a commitment is debt if the payments are fixed, tax-deductible, and missing them can cost the owners control of the firm. Each item:
        - Face versus book. The balance sheet shows the loan at $1,206.6M (`company.debt_book`), after subtracting $29.1M of unamortized discount and issuance costs. The lenders are owed the full $1,235.7M principal, so face is the right number; the $29.1M is an accounting entry that is written off over the loan's life. Using book value would understate debt by $29.1M (1,235.7 − 1,206.6).
        - Market value. The loan floats at the secured overnight financing rate (SOFR) plus 2.75%, so its price stays near face as rates move (`debt.rate_type`, `meta.omitted`: `company.debt_market`). Face is the market value. At year-end 2023 the effective rate was 9.11%; at year-end 2024 it was 7.11% (note 9, facts.term-loan-rate-2023). Rates and the margin fell, and the loan repriced with them rather than rising in value.
        - Leases. SolarWinds leases all its offices and owns no real estate (note 7). The present value of its operating lease liabilities is $49.4M. The undiscounted payments are $53.6M, less $4.2M of imputed interest (facts.lease-minimum-payments, facts.lease-imputed-interest), and the filing discounts them at 4.8% over a weighted remaining term of 3.6 years (facts.lease-discount-rate, facts.lease-remaining-term). The rule says discount at the company's pre-tax cost of debt, 7.11%, which would lower the $49.4M slightly; the difference is small next to $1,285.0M and we kept the filing's figure. Leases signed but not yet started: none disclosed (`company.off_balance_sheet_debt` note).
        - Deferred revenue, $389.3M (`company.deferred_revenue`), is on the balance sheet and looks like a liability. It is not debt: it is cash customers paid in advance for software. SolarWinds owes service, not cash, and failing to deliver is a contract claim, not a default that hands lenders control.
        - Purchase commitments, $68.4M (`company.off_balance_sheet_debt` note; note 15). These are non-cancellable minimum cloud-hosting purchases over four years. They are off the balance sheet, fixed, and a real obligation, so they were checked against the test and ruled out: they are payments for a service the company uses, they run through cost of revenue, and missing one is a contract claim and not a default. Including them would add $68.4M, 5.3% to debt (68.4 ÷ 1,285.0). Judgment call; a lender-minded reading would count them.
        - Guarantees and similar. No guarantees of joint-venture or special-purpose-vehicle debt (notes 7, 15). The 10-K also describes an indemnity to N-able for Cyber Incident liabilities, whose amount "cannot be determined" and is not recorded (note 15): a contingent claim with no fixed payment, so it fails the test.
        - Revolver. The $130.0M revolving facility was undrawn at year-end (`debt.revolver_undrawn`), so it adds no debt. A $10.0M draw during 2024 was repaid (`company.history`, 2024).

- **Lesson 12, Session 12 · Part 2 — "From Ratings to Cost of Debt — Actual vs. Synthetic Ratings"** ([transcript](../../01-foundations-and-discount-rates/lesson-12/session-12-part-2.md))
    - Quote: "If you have an actual rating, don't go looking for trouble. Just use the actual rating."
    - Question for SolarWinds: Does SolarWinds have an agency rating? If not, what synthetic rating does its interest coverage imply, and is there an observed market rate on its own debt that is a better estimate than either? If the synthetic and observed numbers disagree, what explains the gap?
    - Sources needed: Agency rating if any; EBIT, interest expense, the January 2025 coverage-to-rating table; the term loan's rate.
    - Where to find: `debt.rating_actual`, `company.ebit`, `company.interest_expense`, `debt.kd_pretax_observed`, `modeling_choices.coverage_numerator`; model-output.md §2; `sources/market-data/ratings-spreads-2025-01-01.json`.
    - Answer: No agency rating is disclosed in the 10-K or the merger document (`debt.rating_actual` is null), and Capital IQ shows only a statistical score, so a synthetic rating is built. Interest coverage = operating income ÷ interest expense. Using EBIT: $208.4M ÷ $112.4M = 1.85x, which is a B- on Damodaran's small-firm table (market cap under $5 billion; `modeling_choices.firm_size_table`), a default spread of 4.42% and an implied pre-tax cost of debt of 8.85% (risk-free 4.43% + 4.42%; model-output.md §2). The result depends on which earnings figure goes on top, so all three are shown (model-output.md §2):

        | Numerator | Amount | Coverage | Synthetic rating | Spread | Implied cost of debt |
        |---|---|---|---|---|---|
        | EBIT (chosen) | $208.4M | 1.85x | B- | 4.42% | 8.85% |
        | EBIT + acquisition amortization | $261.3M | 2.32x | B | 3.00% | 7.43% |
        | EBITDA (standardized) | $282.8M | 2.52x | B+ | 2.61% | 7.04% |

      A fourth row in the model, the company's own adjusted EBITDA of $384.7M, gives 3.42x and BB with a 6.26% cost of debt. It is shown, not used, because it adds back stock-based compensation, restructuring and Cyber Incident costs that the company pays for. The ledger chooses EBIT (`modeling_choices.coverage_numerator`): stock compensation of $76.5M is a real cost of retaining staff, and the table was built on operating income. The case for the other two is that the $52.9M of acquisition amortization (`company.acquisition_amortization`) is a non-cash charge left over from the 2016 buyout and acquisitions, so lenders would not count it. Observed rate: the term loan carried an effective rate of 7.11% at year-end (`debt.kd_pretax_observed`; SOFR plus 2.75%; at the analysis date SOFR was 4.33%, so the coupon was about 7.08%). That is a market price for SolarWinds' own debt, set by lenders who read the credit agreement, so it beats both synthetic figures, and it is the rate in the cost of capital (`modeling_choices.kd_source: observed`; after-tax 5.33%, model-output.md §1). The gap: the EBIT-based synthetic rate is 1.74 points above the observed rate (8.85% − 7.11%). The EBIT and EBITDA versions bracket it (8.85% and 7.04%), and the observed rate sits almost on the EBITDA one. Reasons for the gap: (1) lenders on a leveraged loan of this kind price off EBITDA and recurring revenue (93.5% of revenue, facts.recurring-revenue-share), which the EBIT table understates; (2) the loan is first-lien secured, so it is senior to other claims and priced below the company's unsecured risk; (3) the table's coverage bands come from a broad sample of firms, not software companies with 99% net retention; (4) the margin was reset by negotiation, not by a formula. In credit terms, the covenants only spring when the revolver is more than 35% drawn (`debt.covenants`), so lenders had little operating pressure on the company.

## Module 1 Step — Questions for This Lesson

- **Cost of debt** (`m1-step-12`)
    - Does the company have an agency rating? What default spread and pre-tax cost of debt does it imply? No rating is disclosed. No spread is taken from one. The model uses the observed rate of 7.11%.
    - What synthetic rating does interest coverage imply, and what cost of debt? B- at 1.85x on EBIT, with an implied cost of debt of 8.85%. Under EBIT plus acquisition amortization, B and 7.43%; under EBITDA, B+ and 7.04% (model-output.md §2).
    - If the two differ, why? Observed 7.11% against synthetic 8.85%: senior secured status, lenders pricing off EBITDA and recurring revenue, and a negotiated margin (see Part 2).
    - What is the market value of interest-bearing debt? If the debt is fixed-rate and rates have moved since it was issued, how far is market value from book? The loan is floating-rate, so market value is face, $1,235.7M. Book value is $29.1M lower, from accounting discount and fees, not from market moves. There is no fixed-rate debt.
    - What is the debt value of lease commitments, including leases signed but not yet started? $49.4M, the present value of operating lease liabilities. No signed-but-not-started leases.
    - Does the company guarantee debt of joint ventures or special-purpose vehicles, or have take-or-pay capacity contracts, that pass the debt test but sit off the balance sheet? No guarantees. The nearest thing to take-or-pay is $68.4M of minimum cloud-hosting purchases, which we ruled out as debt (judgment; adding it would raise debt 5.3% to $1,353.4M, 1,285.0 + 68.4).
    - How much interest was capitalized into construction, and what does coverage look like once it is added back? Zero (`company.interest_capitalized`). The company builds nothing that would carry capitalized interest. Coverage stays at 1.85x. It does capitalize software development (capital spending of $20.5M, `company.capex`, includes $14.4M of it), but not the interest on its loan.
    - Did the company lengthen the depreciation lives of servers or equipment, and how much did that raise operating income? No change is disclosed. Equipment, servers and computers are depreciated over 3 to 5 years, software 3 to 5 (`company.depreciation_life_change`; note 2). Property and equipment depreciation is small, $8.7M a year (facts.ppe-depreciation-2024), against $74.4M of total depreciation and amortization (`company.da`), so even a change would barely move operating income. Operating income is not flattered by this lever.
    - What marginal tax rate applies to the after-tax cost of debt? 25%: federal 21% plus state (`market.tax_rate_marginal`). The after-tax cost of debt is 7.11% × (1 − 0.25) = 5.33% (model-output.md §1).

## Notes

Debt is $1,285.0M, the sum of face value and leases. Deferred revenue is out. The $68.4M of purchase commitments is out by judgment, and the effect of leaving it out is stated. The synthetic rating ranges from B- to B+ depending on the earnings measure, and the observed 7.11% is used because it is a price lenders actually set for SolarWinds' own loan. All three coverage rows feed the optimal-debt analysis in Module 3 (model-output.md §3).

Two later uses: the debt total sets the weights in lesson 13 (33.03% debt), and the gap between synthetic and observed rates returns when the optimal capital structure is tested, since moving the numerator from EBIT to EBITDA moves the optimal debt ratio from 21% to 28% (model-output.md §3).
