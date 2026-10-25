---
title: "SolarWinds (SWI) — Lesson 23: Designing the Right Type of Financing"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 23: Designing the Right Type of Financing

### Lesson 23 — Designing the Right Type of Financing

- **Lesson 23, Session 23 · Part 1 — "Matching Debt to Assets: The Five Questions That Design the Perfect Financing"** ([transcript](../../03-financing-mix-and-dividends/lesson-23/session-23-part-1.md))
    - Quote: "You'd like to issue debt that behaves like equity, that gives you the flexibility of equity while giving you the tax benefits of debt."
    - Question for SolarWinds: Given the life, currency, cyclicality and pricing power of SolarWinds' assets, what should its debt look like in maturity, fixed versus floating, and currency? Does the company have the pricing power that floating-rate debt requires?
    - Sources needed: Contract length and renewal behaviour; price increases; currency of revenue and costs; terms of the debt.
    - Where to find: `debt.rate_type`, `debt.maturity_years`, `debt.currency`, `country.exposures`, `debt.kd_pretax_observed`; `sources/filings/swi-10k-fy2024.md` (Item 1A on recurring revenue, MD&A on retention and price increases, Item 7A on interest rate and currency risk, note 9).
    - Answer: Floating-rate, medium-term, straight (not convertible) debt, partly in euros, is the design the assets suggest. The actual debt matches on rate type and roughly on maturity, and misses on currency.
        - Duration (life of the assets): the product is software, so spending is mostly salaries (R&D of $108.6M, `company.rd_expense`) and little equipment (capital spending $20.5M against depreciation and amortization of $74.4M, `company.capex`, `company.da`). Cash comes in under contracts: the 10-K says "our subscription products generally have recurring monthly or annual subscription periods" and "the majority of our contracts include annual subscription periods". But customers renew: the maintenance renewal rate was 97% and subscription net retention 99% in FY2024 (facts.maintenance-renewal-rate, facts.net-retention-subscription), so cash flows last longer than any contract. That points to medium-term debt. The lecture's example for a durable media business is four to five years; SolarWinds' loan has 5.0 years left (`debt.maturity_years`).
        - Currency: 64.82% of revenue is United States and 35.18% international (`country.exposures`). The 10-K names the euro, pound and Australian dollar as the main foreign currencies but gives no split by currency, so the 35.18% is an upper bound on foreign-currency revenue (some international sales may be priced in dollars). Costs are also foreign: 1,379 of 2,107 employees work outside the United States (facts.employees-2024). The net foreign exposure is therefore smaller than 35.18% and cannot be sized from the filing. The debt is 100% US dollars (`debt.currency`).
        - Pricing power (floating or fixed): the filing says customers "renew existing subscriptions inclusive of an annual price increase" and that "we typically implement annual price increases for our maintenance services", with 97% maintenance renewal and 99% net retention. That is evidence of pricing power in a period when SOFR rose and fell. It is not proof of inflation pass-through, because revenue from maintenance still fell 4.6% as customers moved to subscriptions. Judgment: enough pricing power to justify floating-rate debt, as the lecture treats Disney. The loan is floating, SOFR plus 2.75% with a 0% floor (`debt.rate_type`, `debt.covenants`).
        - Growth or mature (convertible or straight): operating income is positive at 26.15% of revenue (208.4 ÷ 796.9, ledger) and interest is covered 1.85x (model-output.md §2). Convertibles suit companies with low cash flow today and high cash flow later. SolarWinds' cash flow is here already, so straight debt fits.
        - Other drivers of cash flow: recurring revenue makes cash flow steady (the company's revenue grew in each of 2023 and 2024, `company.history`), so cyclicality is low.
        - Sector shortcut: the lesson's duration spreadsheet (macrodur24) gives a negative duration for the prepackaged software industry, which is not usable; the contract and renewal evidence above replaces it.

- **Lesson 23, Session 23 · Part 2 — "Fixing Debt/Asset Mismatches: Swaps vs. New-Project Financing"** ([transcript](../../03-financing-mix-and-dividends/lesson-23/session-23-part-2.md))
    - Quote: "There are two ways in which companies can adjust debt that doesn't match."
    - Question for SolarWinds: Where does SolarWinds' actual debt mismatch its assets (currency, maturity, rate type)? Is the better fix a swap or a different financing of future projects, and what would it cost?
    - Sources needed: Terms of the loan and revolver, hedging disclosures, interest sensitivity.
    - Where to find: `sources/filings/swi-10k-fy2024.md` note 9 and Item 7A; `debt.*`, `company.debt_total`, `company.ebit`.
    - Answer: Three comparisons.
        - Rate type: floating matches pricing power, but the exposure is unhedged. The 10-K (Item 1A) says "we do not have any existing interest rate swap agreements". A 100 basis point rise in rates would cost about $12.4M a year (facts.interest-sensitivity-100bp), 5.95% of EBIT of $208.4M (12.4 ÷ 208.4). The rate on borrowings fell from 9.11% to 7.11% from year-end 2023 to year-end 2024 (facts.interest-rate-history), so floating has helped.
        - Maturity: the loan amortizes 0.25% a quarter (ledger source note on `debt.maturity_years`), so nearly all principal falls due on 2030-02-05, a single refinancing date. That is a refinancing risk, not a mismatch with the assets.
        - Currency: debt is 0% foreign against at most 35.18% foreign revenue. The company does use purchased foreign currency forward contracts, but only on certain balance-sheet positions, not on the debt or on revenue. The balance-sheet effect is visible: foreign currency translation was a $39.5M loss in 2024 and a $19.9M gain in 2023 (facts.fx-translation-adjustment-2024), booked in equity, not cash.
        - Fix, and cost: the second option (finance future needs differently) fits better than a swap, because SolarWinds has no new projects to finance and spent only $20.5M on capital. The next financing event is the 2030 refinancing, or the revolver: of its $130.0M, $112.5M is a multicurrency tranche (facts.revolver-tranches), 8.8% of total debt of $1,285.0M. A swap would take effect at once, but the filings give no swap or forward quotes, so its cost is not computed here. Cost information needed: the five-year swap rate and the euro/dollar cross-currency basis on the analysis date.

## Cumulative Project — Questions for This Lesson

- **Given its asset/project characteristics, what is the right type of debt for your firm?**
  Floating-rate (pricing power: annual price increases, 97% renewal, 99% net retention), medium-term at four to six years, straight rather than convertible, in dollars and euros in proportion to net foreign cash flow, which the filing does not size. At most 35.18% of debt would be in foreign currency.

- **What are the actual debt characteristics?**
  One first lien term loan, $1,235.7M face (`company.debt_face`), floating at SOFR plus 2.75% (`debt.rate_type`), US dollars (`debt.currency`), 5.0 years to maturity (`debt.maturity_years`), 7.11% effective rate (`debt.kd_pretax_observed`); plus $49.4M of leases (`company.lease_debt`); an undrawn $130.0M revolver (`debt.revolver_undrawn`). Straight debt, no swaps.

- **If there is a mismatch, what is the best way to fix it?**
  Two small ones. Interest rate: leave floating, and add a cap or a swap on part of the loan only if the sponsors want to protect the $12.4M per 100 basis points. Currency: do not swap the term loan; at the 2030 refinancing, or on the revolver, put a euro tranche in proportion to net foreign cash flow once that is measured. Maturity: stagger the 2030 bullet at refinancing.

## Notes

SolarWinds' debt is well designed on rate type and tolerable on maturity; the one real gap is currency, and the filings do not allow it to be sized. This lesson's answers do not change the 21% optimum or the cost of capital. Lesson 22's path (repay from cash flow) is compatible: repaying the floating-rate loan lowers the rate-sensitivity as well.
