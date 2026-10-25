---
title: "SolarWinds (SWI) — Lesson 05: The Risk-Free Rate"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 05: The Risk-Free Rate

### Lesson 05 — The Risk-Free Rate

- **Lesson 05, Session 5 · Part 1 — "Matching the Risk-Free Rate to Currency and Time Horizon"** ([transcript](../../01-foundations-and-discount-rates/lesson-05/session-5-part-1.md))
    - Quote: "There is no global risk-free rate."
    - Question for SolarWinds: What currency are SolarWinds' cash flows in, what is the right risk-free rate in that currency and horizon, and does any part of the business (foreign revenue, foreign debt, a new owner's capital structure) argue for a different currency choice?
    - Sources needed: reporting currency; currencies of revenue and debt; 10-year US Treasury on 2025-02-05; the buyer's financing currency.
    - Where to find: ledger `meta.currency`, `market.risk_free_rate`, `country.exposures`, `debt.currency`; `sources/filings/swi-10k-fy2024.md` (Item 7A, Note 9); `sources/market-data/rates-2025-02-05.md`; `sources/deal-docs/swi-8k-2025-04-16-merger-closing.md`.
    - Answer: US dollars, and nothing argues for a change. SolarWinds reports in dollars (`meta.reporting_currency`), the management forecast is in dollars (`forecast.years`), and the term loan is a US dollar loan (`debt.currency`). A 10-year bond matches the long life of the cash flows. Foreign revenue: the company sells in euros, British pounds and Australian dollars, and its European subsidiaries use the euro as their functional currency (`facts.fx-currencies`; 10-K FY2024, Item 7A). That affects the dollar size of the cash flows, which the forecast already states in dollars; it is not a reason to discount at a euro rate. Foreign debt: the revolver may borrow in euros, but it was undrawn at year end (`debt.revolver_undrawn`). The new owner's capital structure: Turn/River's vehicle financed the deal with dollar loans of $2,225.0M, $200.0M and $525.0M (`facts.new-debt-2025`). That changes leverage, which belongs in beta and the weights, not the risk-free rate. The 10-year Treasury closed at 4.43% on 2025-02-05 (`market.govt_bond_rate`).

- **Lesson 05, Session 5 · Part 2 — "Netting Out the Default Spread — Risk-Free Rates in Difficult Currencies"** ([transcript](../../01-foundations-and-discount-rates/lesson-05/session-5-part-2.md))
    - Quote: "The key to currency is to stay consistent, pick a currency and do both your returns and your hurdle rate in that currency."
    - Question for SolarWinds: If any of SolarWinds' revenue or debt is in a currency whose government bond is not risk-free, what default spread must be netted out to get the risk-free rate, and does treating that slice separately move the cost of capital?
    - Sources needed: the currencies involved; their governments' ratings and default spreads; the US rating on the analysis date.
    - Where to find: `sources/market-data/country-risk-2025-01-01.json`; ledger `market.sovereign_default_spread`, `country.exposures`; `sources/filings/swi-10k-fy2024.md` (Item 7A).
    - Answer: The only currency that needs netting is the dollar, and the spread is zero. Moody's rated the United States Aaa on the analysis date, so its default spread is 0.00% (`market.sovereign_default_spread`) and the risk-free rate equals the bond rate, 4.43% (`market.risk_free_rate`). Moody's downgraded the US on 2025-05-16, after the analysis date, which would put a spread above zero in any later valuation. The foreign slice: the two largest named currencies' governments carry little default risk in the January 2025 table: Germany (euro) and Australia are Aaa with a spread of 0.00%, and the United Kingdom is Aa3 with a spread of 0.59% (`facts.default-spreads-2025-01`). Because the valuation is in dollars, those spreads are not netted from anything. Treating the slice separately would not move the cost of capital: the filing gives no split of revenue by currency, so it cannot be built, and the discount rate stays in dollars. The international revenue share, 35.18% (`country.exposures`), enters through the equity risk premium instead (lesson 7).

## Module 1 Step — Questions for This Lesson

- **Currency and risk-free rate**
  - What currency does the company report in? US dollars (`meta.reporting_currency`).
  - What currencies are its revenues in? Mostly dollars, with part in euros, pounds and Australian dollars (`facts.fx-currencies`). By customer shipping address, $516.6M of $796.9M is United States and $280.3M international (`country.exposures`), but the filing does not say how much of the international part is billed in foreign currency.
  - What currency will the analysis use, and why? US dollars: reporting, forecast and debt are all in dollars, and the cash flows and discount rate must be in the same currency.
  - What is the 10-year government bond rate in that currency on the analysis date, and what is the government's rating? 4.43% on 2025-02-05 (`market.govt_bond_rate`, FRED DGS10); Aaa from Moody's.
  - What default spread goes with that rating, and what risk-free rate is left after netting it? 0.00%, so 4.43% (`market.sovereign_default_spread`, `market.risk_free_rate`).
  - Is the equity risk premium measured over that same risk-free rate, or over the gross bond rate? With a zero spread the two are the same. One timing difference: Damodaran's premium of 4.27% is measured on his start-of-month rate of 4.54%, and the risk-free rate here is the 4.43% daily close, 0.11 points lower, inside the 0.25-point tolerance (`sources/market-data/rates-2025-02-05.md`).

## Notes

Rates are as of 2025-02-05, not today, so the value can be compared with the $15.18 and $18.50 prices. The risk-free rate of 4.43% feeds the 12.65% cost of equity in lesson 12 (model-output.md §1). The ledger's README says all revenue is invoiced in dollars; Item 7A of the 10-K says part is sold in other currencies. The conclusion (dollar analysis) is unchanged.
