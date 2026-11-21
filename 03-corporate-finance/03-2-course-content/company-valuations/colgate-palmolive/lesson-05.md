---
title: "Colgate-Palmolive (CL) — Lesson 05: The Risk-Free Rate"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 05: The Risk-Free Rate

### Lesson 05 — The Risk-Free Rate

- **Lesson 05, Session 5 · Part 1 — "Matching the Risk-Free Rate to Currency and Time Horizon"** ([transcript](../../01-foundations-and-discount-rates/lesson-05/session-5-part-1.md))
    - Quote: "There is no global risk-free rate."
    - Question for Colgate-Palmolive: What currency are Colgate-Palmolive's cash flows in, what is the right risk-free rate in that currency and horizon, and does any part of the business (foreign revenue, foreign debt, a new owner's capital structure) argue for a different currency choice?
    - Sources needed: Reporting currency; revenue by geography; currency of the debt; the 10-year government bond rate on the analysis date.
    - Where to find: ledger `meta.currency`, `market.govt_bond_rate`, `market.sovereign_default_spread`, `market.risk_free_rate`, `country.exposures`, `debt.currency`, `facts.euro-debt-share`, `facts.rates-snapshot`; `sources/market-data/market-rates-2026-11-19.json`.
    - Answer: Colgate earns its cash in dozens of currencies and reports it in US dollars. The analysis is in US dollars, with a risk-free rate of 4.82% (`market.risk_free_rate`): the 10-year Treasury at 5.04% less a default spread of 0.22% for the United States' Aa1 rating. Reason for dollars: the statements, the analysts' forecasts and the share price are all in dollars, and the rule is to keep cash flows and discount rate in one currency. Two things might argue otherwise and neither does. Foreign revenue is about two-thirds of sales (`country.exposures`), but it reaches us already translated, so currency weakness shows up in the reported cash flows; 2025 sales lost 0.3% to exchange rates (`facts.sales-drivers-2025`). Foreign debt: 35.9% of the rated notes are in euros (`facts.euro-debt-share`), which is a financing choice that offsets European earnings; it does not change the currency of the valuation. The alternative would be to value each region in its own currency with its own risk-free rate. Done consistently it gives the same value, and it needs revenue by currency, which the 10-K does not give. Horizon: the 10-year rate, because the cash flows run for decades and the 10-year bond is the longest liquid benchmark the course uses.

- **Lesson 05, Session 5 · Part 2 — "Netting Out the Default Spread — Risk-Free Rates in Difficult Currencies"** ([transcript](../../01-foundations-and-discount-rates/lesson-05/session-5-part-2.md))
    - Quote: "The key to currency is to stay consistent, pick a currency and do both your returns and your hurdle rate in that currency."
    - Question for Colgate-Palmolive: If any of Colgate-Palmolive's revenue or debt is in a currency whose government bond is not risk-free, what default spread must be netted out to get the risk-free rate, and does treating that slice separately move the cost of capital?
    - Sources needed: Sovereign ratings and default spreads for the analysis currency and for the main operating countries.
    - Where to find: ledger `market.sovereign_default_spread`, `country.exposures`, `facts.us-country-premium-treatment`, `facts.geographic-risk-notes`; `sources/market-data/country-risk-2026-07-01.json`.
    - Answer: The currency that needs netting is the dollar itself. The United States is rated Aa1, so its bond rate carries a default spread of 0.22%, and the risk-free rate is 5.04% − 0.22% = 4.82% (`market.sovereign_default_spread`). Much of Colgate's revenue is in currencies whose governments are far from risk-free: the pesos of Mexico and Argentina, the Brazilian real, the Turkish lira, the Nigerian naira (`facts.geographic-risk-notes`). We do not compute a risk-free rate in any of them, because no cash flow in the model is in those currencies. Their risk enters once, through the country risk premium on the 45% of sales in emerging markets (lesson 7). Treating that slice in local currency would need local inflation and local cash flows the filings do not provide, and would add nothing if done consistently. So the cost of capital does not move.

## Module 1 Step — Questions for This Lesson

- **Currency and risk-free rate**
  - What currency does the company report in? US dollars (`meta.reporting_currency`).
  - What currencies are its revenues in? About one-third US dollars. The rest is spread over the currencies of Latin America ($4,776M of sales), Europe ($2,962M), Asia Pacific ($2,814M) and Africa/Eurasia ($1,172M), plus Hill's sales abroad (`facts.segment-results-2025`). The 10-K gives no split by currency.
  - What currency will the analysis use, and why? US dollars: the statements, forecasts and share price are in dollars, and one currency throughout keeps inflation assumptions consistent (`meta.currency`).
  - What is the 10-year government bond rate in that currency on the analysis date, and what is the government's rating? 5.04% at the close on 2026-11-19, the latest close before the analysis date (`market.govt_bond_rate`). Moody's rates the United States Aa1.
  - What default spread goes with that rating, and what risk-free rate is left after netting it? 0.22%; 4.82% (`market.sovereign_default_spread`, `market.risk_free_rate`).
  - Is the equity risk premium measured over that same risk-free rate, or over the gross bond rate? Over the netted rate. Damodaran's start-of-November premium is 3.61% over his dollar risk-free rate of 4.72% and 3.39% over the Treasury rate of 4.94%; the ledger uses the first pairing (`facts.rates-snapshot`, `market.mature_erp`). The Treasury rate rose 0.10 points between the start of the month and 2026-11-19, inside the 0.25-point tolerance in the skill, so one cost of capital is shown.

## Notes

The risk-free rate is 4.82% in US dollars. It is the least uncertain input in the cost of capital: a market rate, read from the Federal Reserve's public series, with one published adjustment. The only judgment is whether to net the 0.22%; the course now does, and the equity risk premium is measured to match. Cost of debt is the exception to the netting: default spreads for company ratings are measured over the Treasury rate, so lesson 12 adds its spread to 5.04%, not to 4.82%.
