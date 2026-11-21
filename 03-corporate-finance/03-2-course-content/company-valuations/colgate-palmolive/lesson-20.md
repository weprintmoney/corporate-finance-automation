---
title: "Colgate-Palmolive (CL) — Lesson 20: The Cost of Capital: Wrap Up"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 20: The Cost of Capital: Wrap Up

### Lesson 20 — The Cost of Capital: Wrap Up

- **Lesson 20, Session 20 · Part 1 — "Letting Operating Income React to Distress"** ([transcript](../../03-financing-mix-and-dividends/lesson-20/session-20-part-1.md))
    - Quote: "In other words, the caution I'd added earlier about it's better to be underlevered than overlevered, applies in spades now."
    - Question for Colgate-Palmolive: If Colgate-Palmolive's rating fell, how much operating income would it lose through customer flight, supplier terms or lost contracts? Is a small indirect-cost sensitivity (a few percent) or a large one the right assumption for this business, and what past shock gives evidence?
    - Sources needed: What Colgate sells and to whom; any past downgrade and what happened to operating income after it.
    - Where to find: ledger `debt.rating_actual`, `facts.sp-rating-action`, `company.history`, `facts.operating-income-stability`, `facts.walmart-share-of-sales`, `facts.product-mix-2025`, `facts.debt-cross-checks`, `facts.cost-of-capital-grid`.
    - Answer: A small one. The businesses that lose customers when their credit weakens are those whose customers depend on the company being there later: airlines selling tickets for next year, software firms selling multi-year support, makers of machines that need spare parts. Nobody checks a credit rating before buying toothpaste, soap or a bag of pet food. The purchase is small, used up in weeks, and carries no promise that depends on Colgate's future.
      Where a lower rating could cost operating income:
        - Retailers. Walmart is about 11% of sales (`facts.walmart-share-of-sales`). A large retailer might press a weakened supplier on price. But the retailer needs the brands on its shelf, which limits the pressure.
        - Suppliers. Working capital released $344M in 2025, most of it from accounts payable and other working capital (`company.change_wc`). Suppliers to a junk-rated company shorten terms, and that cash would flow back out.
        - Funding. Commercial paper would become costly or unavailable below a top short-term rating, and Colgate would draw its bank line instead.
      The one piece of evidence in our files is small but consistent: S&P's action of April 2024 is recorded as a downgrade (`facts.sp-rating-action`), and operating income before write-downs was $4,268M in 2024 against $3,984M in 2023 (`company.history`). A move within the A range did nothing visible. That bounds the effect from below; it says nothing about what a fall to junk would do, and no such episode exists for Colgate.
      Why the caution in the quote still applies: the model's schedule assumes operating income is the same at every debt ratio. For Colgate that is nearly true up to about 30%. Beyond it the cliff is already steep without any loss of income (lesson 18), and suppliers and funding would make it steeper. So the indirect costs do not change the optimum; they add to the reasons for stopping short of it.

- **Lesson 20, Session 20 · Part 2 — "The Four Drivers of Optimal Leverage"** ([transcript](../../03-financing-mix-and-dividends/lesson-20/session-20-part-2.md))
    - Quote: "If you pay no taxes, if you have zero tax rate, debt cannot help you."
    - Question for Colgate-Palmolive: Where does Colgate-Palmolive sit on the four drivers of optimal leverage - marginal tax rate, operating income as a share of firm value, business risk, and the relative price of debt versus equity - and how does its operating-income-to-value ratio compare with peers that carry different debt?
    - Sources needed: Tax rate, operating income and EBITDA against firm value, the unlevered beta, the equity risk premium and default spreads; the same ratios for peers.
    - Where to find: ledger `market.tax_rate_marginal`, `market.tax_rate_effective`, `facts.debt-trade-off-sizes`, `beta.unlevered_bottom_up`, `facts.industry-beta-detail`, `country.weighted_erp`, `facts.peer-leverage-capital-iq`, `facts.debt-to-ebitda-at-targets`; model-output.md §3. `peers` is not in the ledger (`meta.omitted`); the comparison uses Capital IQ's candidate list.
    - Answer:

        | Driver | Colgate | Effect on its optimal debt ratio |
        |---|---|---|
        | Marginal tax rate | 25%, and an effective rate of 23.5%, so the deduction is fully usable | Supports debt, about as much as for any US company |
        | Cash flow relative to value | Operating income 4.88% of firm value; EBITDA 5.61% (`facts.debt-trade-off-sizes`) | Holds the ratio down. This is the binding driver |
        | Business risk | Unlevered beta 0.6796 against 0.7557 for the market (`facts.industry-beta-detail`); operating income steady | Supports debt |
        | Price of debt against equity | Equity risk premium 5.38% for Colgate's mix of countries; spreads of 0.40% to 1.11% for ratings from AAA to BBB (the pre-tax costs of debt in model-output.md §3 less the 5.04% bond rate) | Supports debt: borrowing is cheap relative to equity |

      Three drivers say Colgate can carry a lot of debt. The second explains why the answer is 30% and not 50% or 60%. Debt is serviced out of earnings, not out of market value, and the market pays a high price for Colgate's earnings. A dollar of Colgate's EBITDA supports about 17.5 dollars of enterprise value (model-output.md §7), so each percentage point of debt ratio is a large amount of debt relative to the income that has to pay for it. At 30% debt would be 5.35 times EBITDA (`facts.debt-to-ebitda-at-targets`).
      Against the ten candidate peers, on Capital IQ's figures and definitions (`facts.peer-leverage-capital-iq`): Colgate's EBITDA is 5.9% of enterprise value against a median of 7.5%, ninth highest of eleven. Its net debt is 7.2% of enterprise value against a median of 17.6%, fifth lowest of eleven. The companies with the highest earnings relative to value (General Mills, Coty, Smucker, at 10.6% to 11.7%) carry the most debt (32.6% to 42.0%), and those priced most richly (Kimberly-Clark, Church & Dwight, Procter & Gamble, Colgate) carry the least (5.6% to 7.2%). Henkel is the exception, with high earnings relative to value (9.3%) and little debt (6.7%). Otherwise that is the pattern the lecture predicts. It also says Colgate's low ratio is partly a result of its high share price. The peer set is not fixed and these are not the ledger's definitions, so the comparison is indicative.

## Cumulative Project — Questions for This Lesson

- **If your company is a commodity or cyclical company, how would you adjust your optimal debt ratio to reflect earnings volatility?**
  It is neither, so no normalization of earnings is needed beyond what the ledger already does (adding back the $919M write-down). The evidence: operating income before write-downs stayed between $3,554M and $4,268M from 2016 to 2025, and the standard deviation of its yearly change since 2017 is 6.6% (`facts.operating-income-stability`). The sector's sensitivity of firm value to the economy is 0.96 in the professor's table, and Colgate's own regressions on economic growth are not statistically significant (lesson 23; `facts.macro-sensitivity-sector`, `facts.macro-sensitivity-own`).
  The question's logic still applies in a milder form. A cyclical company should set its debt on normal earnings, not peak earnings. Colgate's 2025 operating income of $4,225M is 1% below its 2024 high, so it is near a peak in its own narrow range. The stress test in lesson 19 is how we allowed for that: the recommended 20% is the ratio that holds an A− synthetic rating with income 20% lower, which is lower than any year from 2016 to 2025.

- **If your company is part of a family group, what other considerations might come into play in determining your optimal debt ratio?**
  Not applicable. Colgate is widely held, with no parent, family or group; its three largest holders are index-fund managers with 6% to 10% each (`governance.controlling_holders`). There are no group companies whose debt it guarantees or that would rescue it (`facts.off-balance-sheet-commitments`), so its debt capacity is its own.

- **If your company is privately owned, how would your optimal debt ratio be computed differently?**
  Not applicable; Colgate is listed. For completeness: a private owner is undiversified, so the cost of equity would use total beta (11.50% against 8.76%, `facts.total-beta-illustration`), and equity that expensive would make debt look more attractive at every ratio. Against that, a private firm borrows on worse terms and its owner bears bankruptcy personally. Neither applies here.

## Notes

Nothing here moves the numbers from lessons 18 and 19. The lesson explains them. Colgate's optimal ratio is moderate, not high, because its earnings are small relative to its market value, and the indirect costs of distress are low for a maker of staples but not zero where suppliers and short-term funding are concerned.

Confidence: high that Colgate is not cyclical (ten years of data). Moderate on the indirect-cost judgment: it rests on the nature of the product and on one mild downgrade, because Colgate has never been near distress. The peer comparison uses Capital IQ's figures for a candidate list; when the peer set is fixed (lesson 35) the ranks may shift, though the pattern across ten companies is unlikely to reverse.
