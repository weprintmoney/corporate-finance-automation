---
title: "SolarWinds (SWI) — Lesson 16: Loose Ends"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 16: Loose Ends

### Lesson 16 — Loose Ends

- **Lesson 16, Session 16 · Part 1 — "Currency Consistency: Redoing the DCF in a Foreign Currency"** ([transcript](../../02-investment-returns-and-financing/lesson-16/session-16-part-1.md))
    - Quote: "A good project in U.S. dollars should remain a good project in nominal Reais."
    - Question for SolarWinds: If SolarWinds has foreign operations, what currency should they be valued in, and would a foreign-currency analysis at a matching discount rate give the same answer as the home-currency one? What inflation differential does the conversion assume?
    - Sources needed: Revenue by geography; the currencies the company sells and spends in; the risk-free rate.
    - Where to find: `country.exposures`, `meta.currency`, `market.risk_free_rate`; `sources/filings/swi-10k-fy2024.md` Item 7A and Note 16.
    - Answer: Value them in US dollars, the currency SolarWinds reports in (`meta.currency`, `meta.reporting_currency`). International revenue is 35.18% of the total (`country.exposures`, $280.336M of $796.895M). The company sells in euros, pounds and Australian dollars, and its European subsidiaries keep their books in euros before everything is translated into dollars (10-K Item 7A). A euro analysis would give the same answer as a dollar one if cash flows and discount rate were converted consistently: the discount rate in euros equals (1 + dollar rate) × (1 + euro inflation) ÷ (1 + dollar inflation) − 1. The conversion therefore assumes whatever gap between expected euro and dollar inflation you pick. This run does not need one. No euro or pound inflation forecast is in `sources/`, and the model discounts dollar cash flows at the dollar rate (risk-free 4.43%, `market.risk_free_rate`). Doing it in euros would add an assumption and no information.

- **Lesson 16, Session 16 · Part 2 — "Payback, What-If Analysis, Monte Carlo, and the Hedging Decision"** ([transcript](../../02-investment-returns-and-financing/lesson-16/session-16-part-2.md))
    - Quote: "Does hedging that risk create a benefit that is greater than the cost?"
    - Question for SolarWinds: Which risks does SolarWinds hedge or insure against (currency, interest rates, commodity, cyber, regulatory), and does the benefit exceed the cost? Could investors diversify any of these more cheaply than the company can hedge them?
    - Sources needed: Hedging and insurance disclosures; the rate type of the debt; cyber costs and insurance recoveries; renewal rates.
    - Where to find: `debt.rate_type`, `country.exposures`, `company.history`; `sources/filings/swi-10k-fy2024.md` (Item 7A, Note 15 insurance coverage, MD&A non-GAAP reconciliation).
    - Answer: Three risks, three different answers.
        - **Interest rates: not hedged.** The term loan floats at SOFR plus 2.75% (`debt.rate_type`) and the company has no interest rate swaps (10-K Item 1A). A rise of one percentage point would add about $12.4M of interest a year (facts.interest-sensitivity-100bp), against interest expense of $112.4M (`company.interest_expense`). Investors cannot diversify a loan that is specific to this company, but a hedge is optional because the covenant test is distant (lesson 19). A $12.4M swing is small beside EBIT of $208.4M (`company.ebit`).
        - **Currency: hedged only a little.** The company buys forward contracts to cover some foreign-currency balance-sheet positions and says it hedges revenue and expense exposure "only to a limited extent" (10-K Item 7A and Item 1A). Translation risk is not hedged: the 2024 translation loss was $39.5M (facts.fx-translation-adjustment-2024). Costs partly offset revenue, since 1,379 of 2,107 employees work outside the US (facts.employees-2024) in Europe, Singapore, the Philippines and India. Investors can diversify currency exposure themselves for almost nothing, so a large corporate hedge would be hard to justify. Offshore cash is only $24.8M, 55.2% of it in euros (facts.offshore-cash), so there is little to protect.
        - **Cyber: insured, and the insurance was too small.** The cyber policy covers $15M and the directors-and-officers policy $50M (facts.cyber-insurance-limits). Gross cyber-incident costs were $56.4M in 2022, $17.7M in 2023 and $10.3M in 2024, and insurance paid back $30.2M and $19.8M in 2022 and 2023 (facts.cyber-costs-2022-2024). Net cost was $26.2M, a $2.1M recovery, and $10.3M. The $26M securities class-action settlement paid in March 2023 was reimbursed entirely by the D&O policy, so that cover paid for itself. By 2024 the company had used up its coverage limits and carried the SEC lawsuit costs itself (10-K Item 1A). Cyber risk specific to one company is a risk investors diversify away, so the premium is justified only where it buys protection against costs that can sink the company, such as class-action damages. On benefits, the company never disclosed what it spent on security, so the cost side cannot be measured. The evidence on the benefit side is retention. The maintenance renewal rate fell from 94% in 2019 to 91% in 2020 and recovered to 93% (2022), 96% (2023) and 97% (2024); subscription net retention rose from 97% to 99% in 2024 (facts.maintenance-renewal-rate, facts.net-retention-subscription). Customers did not leave.
        - **Regulatory: no hedge.** The SEC action over the company's security disclosures is a loss it carries itself (10-K Note 15).

## Cumulative Project — Questions for This Lesson

- **If your firm has foreign operations, what currency are the operations reported in?**
  US dollars. `meta.currency` and `meta.reporting_currency` are both USD. The foreign subsidiaries first keep books in euros and then translate to dollars (10-K Item 7A). International revenue is 35.18% of the total, US revenue 64.82% (`country.exposures`).

- **What cost of equity/capital would you use for the foreign operations, given currency choice and business?**
  The same dollar cost of capital as the rest of the company, 10.23% (model-output.md §1), for two reasons. The cash flows are in dollars, so the dollar risk-free rate of 4.43% applies. The business is the same product sold in Europe, so the bottom-up beta of 1.22 (`beta.unlevered_bottom_up`) does not change by geography. The foreign risk goes into the equity risk premium, not into a second discount rate. The premium used is 4.92%, the average of 4.27% on US revenue and 6.11% on international revenue, weighted 64.82% and 35.18% (`country.weighted_erp`, `country.exposures`). The 6.11% is a judgment: it is the mature premium of 4.27% plus the EMEA country premium of 1.84%, applied to all international revenue because most international offices are in Europe. Western Europe alone would add 1.12%, the global average 1.43% (`country.exposures` note). For a project wholly in Europe, arithmetic gives cost of equity of 4.43% + 1.6714 × 6.11% = 14.64%, and a cost of capital of about 11.57% at the company's weights (illustration; not used).

## Notes

Currency consistency changes nothing here: one currency, one discount rate, with the foreign risk carried in the 4.92% premium. The hedging test says SolarWinds' open positions (floating-rate debt, translation) are small against its earnings. The cyber story is the useful one: a $15M policy against tens of millions of loss, with the D&O policy doing the real work. Lesson 20 uses the renewal figures to size indirect distress costs. Limits: the security spend and a euro inflation path are not in the sources.
