---
title: "SolarWinds (SWI) — Lesson 35: Relative Valuation"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 35: Relative Valuation

### Lesson 35 — Relative Valuation

- **Lesson 35, Session 35 · Part 1 — "Pricing vs. Valuing: Defining, Describing, Analyzing, and Applying Multiples"** ([transcript](../../04-dividends-and-valuation/lesson-35/session-35-part-1.md))
    - Quote: "You're trying to attach a number to a company based on how similar companies are being priced out there."
    - Question for SolarWinds: On a consistently defined multiple and peer set, where does SolarWinds sit relative to its peers: at a premium, a discount, or in line? Which multiple fits this business best, and why?
    - Sources needed: SolarWinds' equity value, debt, cash, revenue, EBITDA, net income and book equity; the same items for each peer, at the same date.
    - Where to find: `company.*`, `peers`; `sources/peer-filings/peer-facts-2025-02-05.md`; model-output.md §7.
    - Answer: SolarWinds' enterprise value is $3,630.6M (equity $2,604.9M + debt $1,285.0M − cash $259.3M). Against the eight-peer medians (model-output.md §7):
        - EV / revenue 4.56x vs 3.32x: a premium.
        - EV / EBITDA 12.84x vs 16.39x (six peers): a discount.
        - Price / earnings 23.28x vs 26.57x (seven peers): a discount.
        - Price / book 1.86x vs 4.58x: a discount.
        - Definitions are consistent. Debt is borrowings plus leases for SolarWinds and for every peer, cash includes short-term investments, EBITDA is operating income plus D&A with stock compensation left in as a cost, and every figure is from the latest fiscal year ended by 2025-02-05 with prices from 2025-02-05, but the fiscal periods are not the same: NetApp's year ended in April 2024, NetScout's in March 2024 and Open Text's in June 2024 (`sources/peer-filings/peer-facts-2025-02-05.md`). Company-adjusted EBITDA of $384.7M (`company.ebitda_adjusted`) adds stock compensation back and is not used; peers are not on that basis.
        - Reading the pattern: SolarWinds' EBITDA margin is 35.5% (282.8 ÷ 796.9, my arithmetic) against a peer median of 22.5% (my arithmetic from `peers`), so it looks dear on revenue and cheap on EBITDA. It is a high-margin business priced below peers on cash earnings.
        - Best fit: EV / EBITDA, see the project question below.

- **Lesson 35, Session 35 · Part 2 — "Backing Out What Drives a Multiple: Why Cheap Stocks Usually Deserve to Be Cheap"** ([transcript](../../04-dividends-and-valuation/lesson-35/session-35-part-2.md))
    - Quote: "Most companies that look cheap deserve to be cheap."
    - Question for SolarWinds: If SolarWinds looks cheap or expensive against its peers, is that explained by its growth, risk and margins (a regression of the multiple on those drivers), or is there a mispricing left over?
    - Sources needed: Peer multiples with their growth, margin and leverage.
    - Where to find: `peers[].growth`, `peers[].ebit_margin`, `peers[].debt_ratio`; model-output.md §7. The model computes medians only; the regression below is my side calculation on the ledger rows.
    - Answer: Mostly explained, with a modest leftover that points up. Growth does not explain it: SolarWinds grew 5.0% (2024 revenue $796.9M ÷ 2023 $758.7M − 1, `company.history`) against a peer median of 4.1%. Risk may: debt is 33.03% of capital (model-output.md §1) against a peer median of 11.7% (`peers[].debt_ratio`), and a levered beta of 1.6714 signals more risk. EV / EBITDA is capital-structure neutral in principle, so any debt effect is a risk effect, not a mechanical one. Margin points the other way.
        - Regression, EV / revenue on EBIT margin across the eight peers: EV/revenue = 2.45 + 10.43 × margin, R² 0.42. SolarWinds' 26.2% margin predicts 5.18x against the actual 4.56x, an implied $17.00 a share (EV 5.18 × $796.9M = $4,129.3M, less debt $1,285.0M, plus cash $259.3M, less the $187.0M option and RSU claim, over 171.6M shares; before the claim it is $18.09, and $187.0M ÷ 171.6M = $1.09 a share). Eight points and one outlier (NetScout's loss includes a goodwill impairment) make this a sanity check, not an estimate; dropping NetScout lifts R² to 0.68 and the prediction to 6.61x.
        - EV / EBITDA is not regressed: six usable peers cannot support a multi-variable fit.
        - Conclusion: SolarWinds is cheap on EBITDA partly because it carries more risk and has a thinner growth record than the plan implies. After adjusting for margin there is some leftover that points to a price above $15.18, but it is within the noise of an eight-company sample.

## Cumulative Project — Questions for This Lesson

- **What multiples of earnings, book value and revenue does your company trade at?**
  At $15.18 on 2025-02-05 (model-output.md §7): price / earnings 23.28x (equity $2,604.9M ÷ net income $111.9M); price / book 1.86x (÷ book equity $1,400.7M); EV / revenue 4.56x (EV $3,630.6M ÷ revenue $796.9M); EV / EBITDA 12.84x (÷ standardized EBITDA $282.8M).

- **Which of these multiples is the best one to price your company on?**
  EV / EBITDA. Revenue multiples ignore that peer margins run from −18% to 31% (`peers[].ebit_margin`). Price / book is set aside for two reasons. SolarWinds' book equity of $1,400.7M sits on $2,363.2M of goodwill from the 2016 buyout (`company.goodwill`), so it says nothing about earning power. And among the peers, NetApp and Teradata trade at more than twenty times book value because share buybacks have shrunk their equity, so the peer median is not a clean yardstick either. Price / earnings depends on the debt mix and on one-time items (2022 had an $891.1M impairment, `company.history`); SolarWinds' 33% debt differs from peers'. EV / EBITDA is before interest, so leverage does not distort it, and it uses the same stock-compensation treatment across the set. Its weakness is the sample: six peers (NetScout's EBITDA is negative and Open Text does not report D&A in a taggable form).

- **What are the "comparable" firms that you would use in pricing your company?**
  Eight US-listed software and infrastructure companies: Akamai, NetApp, NetScout, OneSpan, Open Text, Progress, Qualys and Teradata (`peers`). They are the companies in Jefferies' fairness-opinion set that file with the SEC; four others were dropped: Check Point, TeamViewer and Trend Micro file outside the US on different accounting, and Informatica has since been acquired and its price history is no longer available (`sources/peer-filings/peer-facts-2025-02-05.md`). They are mature, with growth from −9.3% to 9.6% except Open Text, whose 28.6% is the Micro Focus acquisition. None is a direct observability competitor. Datadog, Dynatrace and PagerDuty were considered and rejected, because their growth would make their multiples a price for growth SolarWinds does not have.

- **Based upon the multiple and comparables, what price would you attach to your company?**
  $19.95 a share at the peer-median EV / EBITDA of 16.39x (model-output.md §7), after subtracting the $187.0M option and RSU claim as the DCF does. At the peer-median EV / revenue of 3.32x the figure is $8.34. The two disagree by $11.61 because revenue multiples ignore SolarWinds' margin; we weight EV / EBITDA. Cross-checks on my arithmetic: price / earnings at the 26.57x median gives about $16.24 (26.57 × $111.9M ÷ 171.6M = $17.33, less the $1.09 a share option and RSU claim, $187.0M ÷ 171.6M); and removing Qualys, the highest EV / EBITDA at 25.07x, lowers the median to 15.40x and the price to about $18.31 (the earlier $19.40 less the same $1.09). Pricing range, $16 to $20, with $19.95 as the model's point. Relative valuation prices SolarWinds around or above the $18.50 deal, while the DCF (lesson 34) puts it at $13.00. A multiple of EBITDA does not ask how much of that EBITDA must be reinvested to grow; the DCF does. That is the main reason the two methods disagree.

## Notes

Lesson 35 is the market's answer, to be set against the DCF's. SolarWinds trades at a discount on cash-earnings multiples and a premium on revenue; the peer-median EV / EBITDA implies $19.95, above the $18.50 deal and above the $15.18 unaffected price. Lesson 36 combines this with the DCF. Limits: six to eight peers, none a direct competitor, medians pulled up by Qualys, and a standardized EBITDA that burdens stock compensation. Jefferies applied 9x to 12x to company-adjusted EBITDA, a different base (`facts.jefferies-public-comps-range`); on our $282.8M the same multiples would not be comparable.
