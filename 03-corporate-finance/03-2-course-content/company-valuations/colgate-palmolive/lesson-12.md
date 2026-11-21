---
title: "Colgate-Palmolive (CL) — Lesson 12: Debt: Measure and Cost"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 12: Debt: Measure and Cost

### Lesson 12 — Debt: Measure and Cost

- **Lesson 12, Session 12 · Part 1 — "Cost of Debt and What Counts as Debt"** ([transcript](../../01-foundations-and-discount-rates/lesson-12/session-12-part-1.md))
    - Quote: "All interest-bearing obligations are, obviously, debt. All lease commitments are debt."
    - Question for Colgate-Palmolive: What is Colgate-Palmolive's total debt once leases and every other fixed, tax-deductible, default-triggering commitment are counted? What on the balance sheet looks like debt but fails the test, and what is off the balance sheet but passes it?
    - Sources needed: Debt note, fair value note, lease note, commitments and pension notes.
    - Where to find: `sources/filings/cl-10k-fy2025.txt` notes 6, 7, 10, 13, 15 and 16; ledger `company.debt_face`, `company.debt_book`, `company.debt_market`, `company.lease_debt`, `company.debt_total`, `facts.debt-detail-2025`, `facts.lease-detail-2025`, `facts.off-balance-sheet-commitments`, `facts.pension-underfunding-2025`, `facts.debt-cross-checks`.
    - Answer: Total debt is $8,084.0M (`company.debt_total`): interest-bearing debt at market value, $7,518.0M, plus operating lease liabilities, $566.0M. Item by item:
        - Interest-bearing debt. The balance sheet carries $7,988M: notes of $7,767M, commercial paper of $147M, finance leases of $72M and $2M of other loans (`facts.debt-detail-2025`). Its estimated fair value is $7,518M, $470M or 5.9% lower (`company.debt_market`, `facts.debt-cross-checks`). The notes carry an average coupon of 2.9%, set when rates were lower, so they trade below face. Market value is the right weight in a cost of capital, and the filing supplies it, so no estimate is needed. Using carrying value would add $470M and change the debt ratio by about half a point.
        - Leases. $566M of operating lease liabilities, the present value of $660M of payments over a weighted remaining term of seven years, discounted in the filing at 4.8% (`facts.lease-detail-2025`). Discounting at today's 5.74% would give a slightly lower figure; the difference is small against $8,084M and the filing's number is kept. No material lease has been signed that has not yet started.
        - Looks like debt, fails the test: pension and retiree benefit plans are underfunded by $1,283M (`facts.pension-underfunding-2025`). The course does not count this in debt for the cost of capital: the payments are not fixed in the way interest is. It is a claim on the firm, and it is flagged for the step from firm value to equity value (lesson 33).
        - Off the balance sheet: purchase obligations of $637M for materials and services (`facts.off-balance-sheet-commitments`). They are legally binding and fixed, so they were checked. Ruled out, by judgment: they pay for goods the company will use within a few years, and missing one is a contract dispute, not a default. Counting them would raise debt 7.9% to $8,721M.
        - Nothing else. No guarantee of another party's debt, no capitalized interest, and supplier finance balances that the filing calls not material (`facts.off-balance-sheet-commitments`). The $3,000M revolving credit facility backs the commercial paper and is undrawn (`debt.revolver_undrawn`).

- **Lesson 12, Session 12 · Part 2 — "From Ratings to Cost of Debt — Actual vs. Synthetic Ratings"** ([transcript](../../01-foundations-and-discount-rates/lesson-12/session-12-part-2.md))
    - Quote: "If you have an actual rating, don't go looking for trouble. Just use the actual rating."
    - Question for Colgate-Palmolive: Does Colgate-Palmolive have an agency rating? If not, what synthetic rating does its interest coverage imply, and is there an observed market rate on its own debt that is a better estimate than either? If the synthetic and observed numbers disagree, what explains the gap?
    - Sources needed: Agency rating; operating income and interest expense; the ratings table; coupons on recent issues.
    - Where to find: ledger `debt.rating_actual`, `facts.sp-rating-action`, `company.ebit`, `company.interest_expense`, `debt.kd_pretax_observed`, `modeling_choices.kd_source`, `modeling_choices.coverage_numerator`, `facts.debt-cross-checks`, `facts.debt-detail-2025`; model-output.md §1 and §2; `sources/market-data/ratings-spreads-2026-01-01.json`; `sources/capital-iq/credit-ratings.tsv`.
    - Answer: It has one: S&P rates Colgate A+, outlook stable (`debt.rating_actual`). The spread for that rating in Damodaran's January 2026 table is 0.70%, so the pre-tax cost of debt is 5.04% + 0.70% = 5.74% (model-output.md §1). The synthetic rating disagrees, and says Colgate is safer than S&P does. Interest coverage is $4,225.0M ÷ $267.0M = 15.82 times, which is AAA on the large-company table, a spread of 0.40% and a cost of debt of 5.44%. All three earnings measures give AAA (model-output.md §2):

        | Numerator | Amount | Coverage | Synthetic rating | Spread | Implied cost of debt |
        |---|---|---|---|---|---|
        | EBIT (chosen) | $4,225.0M | 15.82x | AAA | 0.40% | 5.44% |
        | EBIT + acquisition amortization | $4,303.0M | 16.12x | AAA | 0.40% | 5.44% |
        | EBITDA (standardized) | $4,855.0M | 18.18x | AAA | 0.40% | 5.44% |

      The owner's decision is the actual rating, 5.74%; the alternative is the synthetic 5.44%. Reason: the course's rule is to use an agency rating when there is one, and here the agency has information the ratio lacks. Why they differ, as analysis:
        - Part of the coverage is borrowed from the past. Interest of $267M reflects coupons averaging 2.9%. At today's 5.74% the same debt would cost $464M a year and coverage would be 9.11 times (`facts.debt-cross-checks`). That is still above the 8.5 times that marks AAA in the table, so old coupons narrow the gap but do not close it.
        - A rating agency looks past one ratio. Colgate pays out everything it earns: $9,438M returned in three years against $8,204M of free cash flow to equity, book equity of $54M, and a new $5 billion buyback authorization (model-output.md §5; `company.equity_book`; `facts.payout-policy-2025`). About 45% of sales are in emerging markets. And S&P's last action, in April 2024, is recorded as a downgrade (`facts.sp-rating-action`). S&P's stated reasons are not in our files, so this is inference; what is on record is that the agency moved Colgate down while coverage stayed above 15 times.
        - The table is coarse. It maps one number to a rating for all large companies.

      An observed rate exists but is not a better estimate: the 2.9% average coupon is history (`debt.kd_pretax_observed`), and the two 2025 issues, five-year dollar notes at 4.20% and ten-year euro notes at 3.25%, are a year old, shorter or in another currency (`facts.debt-detail-2025`). The choice barely matters to the answer: with 5.44% the cost of capital would be 8.32% and not 8.34% (model-output.md §3), because debt is 9.34% of the capital.

## Module 1 Step — Questions for This Lesson

- **Cost of debt** (`m1-step-12`)
    - Does the company have an agency rating? What default spread and pre-tax cost of debt does it imply? Yes: S&P A+, stable (`debt.rating_actual`). Spread 0.70%; pre-tax cost of debt 5.74%. The ledger writes the rating as "A1/A+", which is the label of the row in Damodaran's table. A Moody's rating has not been sourced (`sources/README.md`, Still to get), so "A1" is not a sourced fact.
    - What synthetic rating does interest coverage imply, and what cost of debt? AAA at 15.82 times; 5.44% (model-output.md §2). On reported operating income of $3,306M coverage is 12.38 times, still AAA (`facts.debt-cross-checks`).
    - If the two differ, why? The synthetic rating is two rows higher in the table (AAA, then AA, then A+). Coverage is helped by old low coupons, and the agency weighs the payout policy, near-zero book equity and emerging-market exposure, which one ratio cannot see. See Part 2.
    - What is the market value of interest-bearing debt? If the debt is fixed-rate and rates have moved since it was issued, how far is market value from book? $7,518M against a carrying value of $7,988M: 5.9% lower, because about nine-tenths of the debt is fixed-rate and was issued at an average 2.9% (`company.debt_market`, `debt.rate_type`).
    - What is the debt value of lease commitments, including leases signed but not yet started? $566M; none signed and not started (`company.lease_debt`, `facts.lease-detail-2025`).
    - Does the company guarantee debt of joint ventures or special-purpose vehicles, or have take-or-pay capacity contracts, that pass the debt test but sit off the balance sheet? No guarantees disclosed. Purchase obligations of $637M are the nearest thing and are ruled out by judgment; including them would raise debt 7.9% (`facts.off-balance-sheet-commitments`).
    - How much interest was capitalized into construction, and what does coverage look like once it is added back? None is disclosed in the 10-K, so coverage stays at 15.82 times. Interest paid in cash was $270M against expense of $267M (`facts.debt-detail-2025`), which leaves little room for a hidden amount.
    - Did the company lengthen the depreciation lives of servers or equipment, and how much did that raise operating income? No change is disclosed. Machinery and equipment are depreciated over 3 to 15 years and buildings over up to 40 (`facts.depreciation-lives`).
    - What marginal tax rate applies to the after-tax cost of debt? 25% (`market.tax_rate_marginal`). After-tax cost of debt: 5.74% × (1 − 0.25) = 4.30% (model-output.md §1).

## Notes

Debt is $8,084.0M at market value including leases, 9.34% of the firm's value. The cost of debt is 5.74% before tax and 4.30% after. Both are high-confidence figures: the debt's fair value and the rating are disclosed, and the only estimate is the spread attached to the rating, from a table dated January 2026. Because debt is so small a share, none of the judgment calls in this lesson (fair value against carrying value, purchase obligations, actual against synthetic rating) moves the cost of capital by more than a few hundredths of a point.

That completes Module 1. Cost of capital: 90.66% equity at 8.76% and 9.34% debt at 4.30% gives 8.34% (model-output.md §1). After this lesson the model was rerun; its section 1 agrees with every figure quoted in lessons 5 to 12.

The uncertainty in the 8.34% does not come from debt. In order of size it comes from the beta (7.84% to 8.67%, lesson 10), the date of the equity risk premium (up to 8.57%, lesson 6), and the country premium method and weights (lessons 6 and 7).

Two items for a later correction pass, neither changed here: the `debt.rating_actual` label "A1/A+" implies a Moody's rating we have not sourced; and model-output.md §3 puts the "current" row of its debt schedule on the synthetic AAA rate (cost of capital 8.33% at 9%), which is why its value-of-moving figures start from 8.32% and not 8.34%. Lesson 18 should say so when it quotes them.
