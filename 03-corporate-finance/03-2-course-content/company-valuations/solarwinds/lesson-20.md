---
title: "SolarWinds (SWI) — Lesson 20: The Cost of Capital: Wrap Up"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 20: The Cost of Capital: Wrap Up

### Lesson 20 — The Cost of Capital: Wrap Up

- **Lesson 20, Session 20 · Part 1 — "Letting Operating Income React to Distress"** ([transcript](../../03-financing-mix-and-dividends/lesson-20/session-20-part-1.md))
    - Quote: "In other words, the caution I'd added earlier about it's better to be underlevered than overlevered, applies in spades now."
    - Question for SolarWinds: If SolarWinds' rating fell, how much operating income would it lose through customer flight, supplier terms or lost contracts? Is a small indirect-cost sensitivity (a few percent) or a large one the right assumption for this business, and what past shock gives evidence?
    - Sources needed: Operating income and revenue history; renewal rates through the SUNBURST attack; the number of customers affected; supplier commitments.
    - Where to find: `company.history`, `company.ebit`, `debt.rating_actual` (none disclosed); `sources/filings/swi-8k-2020-12-14-sunburst-followup.md`, 10-Ks FY2020, FY2023, FY2024; model-output.md §4.
    - Answer: A small sensitivity, a few percent of operating income, is right for this business. The shock to test it is the December 2020 SUNBURST attack. It hit the company's reputation harder than a rating downgrade would.
        - Scale of the shock: the company told about 33,000 Orion customers who were active on maintenance, and believed fewer than 18,000 had the compromised software installed, out of more than 300,000 customers overall (facts.sunburst-customers).
        - What customers did: the maintenance renewal rate slipped from 94% in 2019 to 91% in 2020, then rose to 93% in 2022, 96% in 2023 and 97% in 2024 (facts.maintenance-renewal-rate, facts.net-retention-subscription). Subscription net retention was 99% in 2024. Revenue stayed flat for two years and then grew: $669.1M (2019), $716.8M (2020), $718.6M (2021), $719.4M (2022), $758.7M (2023) and $796.9M (2024) (facts.revenue-2019-2021, `company.history`). The 2019 to 2021 figures are the filings' restated series without the N-able business that was spun off in 2021.
        - Suppliers: the main supplier commitment is $68.4M of cloud hosting minimums (`company.off_balance_sheet_debt` note). Nothing in the filings links hosting terms to the credit rating.
        - Assumption: I would use about 5% of operating income as the loss from a one- or two-notch downgrade. This is a judgment, with no SolarWinds-specific estimate in the filings. The 10% row in model-output.md §4 is the nearest result, and it moves the optimum from 21% to 19% ($187.6M of EBIT). Even a 30% loss, $145.9M, gives 14% (§4).

- **Lesson 20, Session 20 · Part 2 — "The Four Drivers of Optimal Leverage"** ([transcript](../../03-financing-mix-and-dividends/lesson-20/session-20-part-2.md))
    - Quote: "If you pay no taxes, if you have zero tax rate, debt cannot help you."
    - Question for SolarWinds: Where does SolarWinds sit on the four drivers of optimal leverage (marginal tax rate, operating income as a share of firm value, business risk, and the relative price of debt versus equity), and how does its operating-income-to-value ratio compare with peers that carry different debt?
    - Sources needed: Tax rate; EBIT and firm value; beta; cost of debt and equity; peers' operating margin, revenue, enterprise value and debt ratio.
    - Where to find: `market.tax_rate_marginal`, `company.ebit`, `company.debt_total`, `company.equity_value`, `beta.unlevered_bottom_up`, `peers`; model-output.md §1 and §7.
    - Answer: SolarWinds is mid-range on three drivers and unfavorable on the fourth. The result is an optimum of 21%, below the actual 33% (model-output.md §3).
        - **Tax rate:** 25% marginal (`market.tax_rate_marginal`), usable, since it paid $61.5M of cash taxes in 2024 (facts.cash-flow-items-2024). A good case for debt.
        - **Operating income to value:** EBIT of $208.4M against an enterprise value of $3,630.6M (model-output.md §7) is 5.74% (arithmetic). The eight peers' EBIT as a share of enterprise value (operating margin × revenue ÷ enterprise value, from `peers`) are: Akamai 2.93%, NetApp 4.94%, NetScout −9.79%, OneSpan 6.78%, Open Text 6.58%, Progress 3.15%, Qualys 3.63%, Teradata 6.74%. The median of all eight is 4.29%. SolarWinds sits above it and below the top three.
        - **Debt among peers:** the three peers above SolarWinds carry 1.25% (OneSpan), 45.28% (Open Text) and 13.90% (Teradata) debt. Peers with similar operating income to value therefore have anywhere from almost no debt to nearly half. The ratio alone does not set the debt level, and SolarWinds' 33.03% (model-output.md §1) is above the median of 11.7% (arithmetic on `peers`).
        - **Business risk:** unlevered beta of 1.22 (`beta.unlevered_bottom_up`, software systems and applications), above the market average of 1.0. That argues for less debt.
        - **Relative price of debt:** at the current 33% the schedule's row, which reprices the debt, shows B and a debt cost of 7.43% against 12.65% for equity (today's rating on actual interest is B-). At 21% the rating is A- and debt costs 5.38% against 11.63% (model-output.md §1, §3). Debt is cheap only at the low ratios. Coverage of 1.85x (§2) is what limits it.

## Cumulative Project — Questions for This Lesson

- **If your company is a commodity or cyclical company, how would you adjust your optimal debt ratio to reflect earnings volatility?**
  SolarWinds is neither. Revenue rose every year from 2022 to 2024 ($719.4M, $758.7M, $796.9M, `company.history`), and 93.5% of 2024 revenue is recurring (facts.recurring-revenue-share). Operating income has been volatile, but for a one-off reason: the 2022 loss of $819.6M includes an $891.1M goodwill impairment (`company.history`, 2022 note). No commodity adjustment applies. The stress test (model-output.md §4) serves the same purpose. The nearest equivalent of a normalizing step would be to use EBIT of $150.4M, the 2023 level, in place of $208.4M, which gives roughly the 14% to 16% rows of §4. Lesson 19 uses this.

- **If your company is part of a family group, what other considerations might come into play in determining your optimal debt ratio?**
  There is no family. The closest equivalent is the sponsor group: Silver Lake held 36.56% and Thoma Bravo 29.79% at the 2024 proxy (`governance.controlling_holders`). They are separate firms, and each had to consent to a change of control under the stockholders' agreement. Together they held 111,564,519 shares, about 65% of the voting power, when the merger was approved (facts.sponsor-voting-power-2025-02). Three considerations follow. First, the sponsors are not diversified in this position and the public float (about 34%) sets the traded price (`governance.marginal_investor`), so the market beta may understate the risk the sponsors bear. Second, sponsors have an interest in using debt to return cash early, as the 2024 special dividend did ($168.2M, `company.history`), and the interests of two sponsors and the public holders need not match. Third, any large recapitalization needed both sponsors' agreement. None of this changes the model's number. It adds a reason for the board to choose a ratio at or below it.

- **If your company is privately owned, how would your optimal debt ratio be computed differently?**
  SolarWinds was public on the analysis date, 2025-02-05, so the model used market equity of $2,604.9M (`company.equity_value`). It is private since 2025-04-16 (type `delisted`, `meta.type`). Two things change. There is no traded price, so equity weights must come from a valuation (the deal's $18.50 a share, `company.deal_price`, is the only anchor) or from the market values of similar public firms. The cost of equity should reflect the owners' undiversified risk, using total beta instead of market beta. Turn/River's financing at closing was a $2.225 billion first-lien loan, a $200.0M revolver and a $525.0M second-lien loan (facts.new-debt-2025). That is far above the 21% optimum, which shows that an owner maximizing its own return can choose leverage that a public-company cost-of-capital calculation would not.

## Notes

Lesson 20 changes none of the earlier numbers. It tests them: a rating fall costs a few percent of operating income at most on this evidence; the four drivers put SolarWinds above its optimum; and the family-group and private-company questions apply only through the sponsors and after the sale. Open items: the actual cost of SolarWinds' rating on its customer contracts is not disclosed, and the credit agreement's own EBITDA definition is not in the sources.
