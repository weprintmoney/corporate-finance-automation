---
title: "Colgate-Palmolive (CL) — Lesson 16: Loose Ends"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 16: Loose Ends

### Lesson 16 — Loose Ends

- **Lesson 16, Session 16 · Part 1 — "Currency Consistency: Redoing the DCF in a Foreign Currency"** ([transcript](../../02-investment-returns-and-financing/lesson-16/session-16-part-1.md))
    - Quote: "A good project in U.S. dollars should remain a good project in nominal Reais."
    - Question for Colgate-Palmolive: If Colgate-Palmolive has foreign operations, what currency should they be valued in, and would a foreign-currency analysis at a matching discount rate give the same answer as the home-currency one? What inflation differential does the conversion assume?
    - Sources needed: Reporting currency, share of sales by region, the risk-free rate, inflation rates by currency.
    - Where to find: ledger `meta.currency`, `country.exposures`, `market.risk_free_rate`, `facts.currency-and-hedging-2025`, `facts.geographic-risk-notes`, `facts.regional-hurdle-rates`. Expected inflation by currency is not in `sources/`.
    - Answer: Colgate has large foreign operations: about two-thirds of sales are outside the United States and about 45% are in emerging markets (`country.exposures`). They are valued in US dollars, with everything else in this project: the cash flows are the dollar figures Colgate reports, the risk-free rate is the dollar rate of 4.82%, and the risk of operating abroad is carried by the equity risk premium, not by the currency.
      A valuation of, say, the Brazilian business in reais would give the same answer if it were done consistently: cash flows forecast in reais with Brazilian inflation in them, and a discount rate raised by the difference between Brazilian and US inflation. The formula is: local rate = (1 + dollar rate) × (1 + local inflation) ÷ (1 + US inflation) − 1. The conversion assumes that the exchange rate moves over time by the inflation difference. We did not run the foreign-currency version: expected inflation rates by country are not in our source files, and a consistent version would only reproduce the dollar answer. The practical warning for Colgate is the opposite error: discounting reais or pesos at a dollar rate, or forecasting dollar cash flows that assume local prices rise while the currency holds. Colgate names Argentina, Nigeria and Türkiye as hyper-inflationary economies (`facts.geographic-risk-notes`), where that error would be largest.

- **Lesson 16, Session 16 · Part 2 — "Payback, What-If Analysis, Monte Carlo, and the Hedging Decision"** ([transcript](../../02-investment-returns-and-financing/lesson-16/session-16-part-2.md))
    - Quote: "Does hedging that risk create a benefit that is greater than the cost?"
    - Question for Colgate-Palmolive: Which risks does Colgate-Palmolive hedge or insure against (currency, interest rates, commodity, cyber, regulatory), and does the benefit exceed the cost? Could investors diversify any of these more cheaply than the company can hedge them?
    - Sources needed: Derivatives and risk-management disclosures; who owns the shares.
    - Where to find: ledger `facts.currency-and-hedging-2025`, `debt.rate_type`, `debt.currency`, `governance.marginal_investor`, `facts.sales-drivers-2025`; `sources/filings/cl-10k-fy2025.txt` MD&A and note 7; modules-2-4-cross-checks-output.md §4.
    - Answer: Colgate hedges three risks, none of them heavily (`facts.currency-and-hedging-2025`):

        | Risk | What it does | Size at the end of 2025 |
        |---|---|---|
        | Currency, transactions | Forward and swap contracts, generally no longer than 12 months | $3,535M notional, 26.0% of a year's sales outside the United States |
        | Currency, investments abroad | Borrows in foreign currency and designates the debt as a hedge of its foreign subsidiaries | $3,942M, 49.3% of debt at carrying value |
        | Commodities | Futures, "on a limited basis", mainly at Hill's | $16M, 0.20% of cost of sales |
        | Interest rates | Mix of fixed and floating debt, with swaps | A one-point rise would add $7M to interest, 0.17% of operating income |

      Does the benefit exceed the cost? The lecture's test has two parts. First, can investors do it themselves more cheaply? For currency, largely yes. Colgate's price is set by diversified institutions holding 87% of the shares (`governance.marginal_investor`). A fund that owns companies around the world already has currencies that offset one another, and it does not need Colgate to smooth the peso. Second, does hedging protect the company from a cost that falls on the company itself, such as distress or having to pass up investments? For Colgate, no: operating income covers interest 15.82 times (model-output.md §2), and a bad currency year does not threaten anything.
      On that test Colgate's practice is about right, and for a reason worth stating: it mostly hedges where hedging is nearly free. Short forward contracts on known purchases cost little. Borrowing in euros to fund European assets is not a derivative at all; it is a choice about which currency to borrow in, and it is the cheapest hedge there is (lesson 23). The company does not try to hedge the translated value of its foreign profits, which would be expensive and which shareholders can diversify. It leans on pricing instead: selling prices rose 2.1% in 2025 while currency took 0.3% off sales (`facts.sales-drivers-2025`).
      What the filing does not give is the cost of the hedging program, so "benefit exceeds cost" is a judgment from its small size and short maturities, not a computed result. The filing reports results, not costs: a $100M gain on fair value hedges in 2025 after a $54M loss in 2024. Insurance against cyber or regulatory events is not quantified in the 10-K and is not assessed here.

## Cumulative Project — Questions for This Lesson

- **If your firm has foreign operations, what currency are the operations reported in?**
  US dollars. Foreign subsidiaries keep their books in local currencies; assets and liabilities are translated at year-end exchange rates and income at average rates for the year, with translation gains and losses going to equity, not to earnings (`facts.currency-and-hedging-2025`). Subsidiaries in highly inflationary economies are an exception to that treatment. In 2025 foreign exchange reduced reported net sales by 0.3% (`facts.sales-drivers-2025`).

- **What cost of equity/capital would you use for the foreign operations, given currency choice and business?**
  Dollar rates, different by region, because the risk differs by region even though the currency of the analysis does not. Each region gets the mature premium of 3.61% plus its own country risk premium, with the beta of the business (`facts.regional-hurdle-rates`):

  | Operation | Share of company sales | Equity risk premium | Cost of equity | Cost of capital |
  |---|---|---|---|---|
  | Oral, Personal and Home Care, North America | 19.8% | 3.61% | 7.70% | 7.38% |
  | Latin America | 23.4% | 8.00% | 11.21% | 10.56% |
  | Europe | 14.5% | 4.65% | 8.53% | 8.14% |
  | Asia Pacific | 13.8% | 5.10% | 8.89% | 8.46% |
  | Africa/Eurasia | 5.8% | 7.87% | 11.10% | 10.47% |
  | Hill's Pet Nutrition, at the mature premium | 22.6% | 3.61% | 6.65% | 6.43% |

  A plant in Brazil should clear about 10.56%, not the company's 8.34%; a pet food plant in Kansas about 6.43%. Two cautions. The regional premiums are January 2026 figures added to a November mature premium. And Hill's is shown at the mature premium only, because two-thirds of its sales are in the United States (`facts.segment-results-2025`); its foreign third would carry more. The company-wide 8.34% already blends all of this through the weighted premium of 5.38%.

## Notes

Nothing in this lesson changes a ledger value. It adds regional hurdle rates (7.38% to 10.56% for the same business, depending on where it is) and the finding that Colgate's hedging is light, cheap and mostly done through the currency of its debt.

Not done, and why: a foreign-currency valuation (no inflation data in the sources, and it would reproduce the dollar answer); a simulation of value (the valuation lessons use scenarios on the two inputs that matter, the beta and the stable return on capital); payback periods (no project-level data).

Confidence: high on what Colgate hedges, which is disclosed. Moderate on the regional rates, which use regional averages for country risk and assume the same beta everywhere.
