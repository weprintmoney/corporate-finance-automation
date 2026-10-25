---
title: "SolarWinds (SWI) — Lesson 04: Define and Measure Risk"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 04: Define and Measure Risk

### Lesson 04 — Define and Measure Risk

- **Lesson 04, Session 4 · Part 1 — "Danger Plus Opportunity — The Ingredients of a Good Risk and Return Model"** ([transcript](../../01-foundations-and-discount-rates/lesson-04/session-4-part-1.md))
    - Quote: "Risk is equal to danger plus opportunity."
    - Question for SolarWinds: Does a single-beta model price the risks that matter most for SolarWinds (customer concentration, regulation, tail events)? Which of those fall into the diversifiable, unpriced bucket, and does SolarWinds' actual marginal investor diversify them away?
    - Sources needed: customer base and concentration; regulatory and tail-event history; who holds and trades the stock.
    - Where to find: ledger `governance.marginal_investor`, `country.exposures`; `sources/filings/swi-10k-fy2024.md` (Item 1A); `sources/filings/swi-8k-2020-12-14-sunburst-followup.md`.
    - Answer: Mostly yes, with one caveat. Customer concentration is low: the company has over 300,000 customers (`facts.sunburst-customers`), and sells to US federal departments in a portion of its license and subscription sales that "in certain calendar quarters, particularly the first and third calendar quarters, may be meaningful" (10-K FY2024, Item 1A), with no dollar figure given. The shocks that hurt, SUNBURST and the SEC suit (lesson 3), are specific to SolarWinds. A well-diversified investor holds hundreds of stocks, so one firm's attack or lawsuit washes out, and the single-beta model correctly leaves them out of beta. The marginal investor is exactly that: diversified institutions holding the roughly 34% public float set the traded price (`governance.marginal_investor`). The caveat: unpriced in beta does not mean costless. The attack lowered expected cash flows and the multiple (`facts.ev-ntm-ebitda-history`), and that belongs in the forecast, not in the discount rate. Country exposure is the one market risk the model prices separately: 35.18% of revenue is international (`country.exposures`; lesson 7).

- **Lesson 04, Session 4 · Part 2 — "Climbing the Risk Ladder — From Firm-Specific Risk to the Market Portfolio"** ([transcript](../../01-foundations-and-discount-rates/lesson-04/session-4-part-2.md))
    - Quote: "Beta is not a measure of total risk."
    - Question for SolarWinds: Which of SolarWinds' recent shocks were firm-specific and which were market-wide? If the marginal investor is not diversified, does a market beta understate the risk they actually bear?
    - Sources needed: shock history; multiples for SolarWinds and peers through the shocks; ownership.
    - Where to find: ledger `company.history`, `governance.marginal_investor`; `sources/deal-docs/swi-defm14c-2025-merger.md` (Goldman Sachs, historical multiples); model-output.md §1.
    - Answer: Firm-specific: the December 2020 attack, the 2023 SEC complaint, and the 2021 spin-off of N-able. Both: the 2022 collapse in the multiple. Goldman's average enterprise value to next-twelve-months EBITDA multiple for SolarWinds fell from 14.0 times in 2021 to 9.9 times in 2022, while the software peers' fell from 12.0 to 11.0 (`facts.ev-ntm-ebitda-history`). The peers' 1.0-turn drop is the market-wide part. SolarWinds' further 3.1 turns is its own (arithmetic). The same year the company booked an $891.1M goodwill write-down (`company.history`, 2022 note), which pushed EBIT to −$819.6M. If the marginal investor were undiversified, market beta would understate the risk borne. Here the investors who set the price are diversified, so the market beta stands. The sponsors are the undiversified holders (66.34%, `facts.sponsors-pct-2024-proxy`), but they did not set the market price; they would matter in a private sale, which is why the deal was a negotiation. There is no regression beta to compare, since none could be computed (`meta.omitted`); the model uses the bottom-up unlevered beta of 1.22, relevered to 1.6714 (model-output.md §1).

- **Lesson 04, Session 4 · Part 3 — "Proxy Models and the Weakness of Beta — Does the CAPM Actually Work?"** ([transcript](../../01-foundations-and-discount-rates/lesson-04/session-4-part-3.md))
    - Quote: "The actual number is well below 10%."
    - Question for SolarWinds: Would a proxy-based cost of equity (using SolarWinds' size and price-to-book) give a materially different number than the CAPM estimate, and if so, which is more defensible for this company?
    - Sources needed: market value and book value of equity; peer price-to-book; the CAPM cost of equity.
    - Where to find: ledger `company.equity_value`, `company.equity_book`, `beta.unlevered_bottom_up`, `modeling_choices.firm_size_table`; model-output.md §1 and §7.
    - Answer: Not computed, and not recommended as the base. A proxy model maps cost of equity from size and price-to-book, and the course's coefficients are not in the ledger, so a number would be invented. The inputs point one way. Market value of equity is $2,604.9M (`company.equity_value`), under the $5 billion line for the small-firm tables (`modeling_choices.firm_size_table`). Price to book is 1.86 times against the peer median of 4.58 times (model-output.md §7). A small, low price-to-book stock would score as higher risk on a proxy model. But the book value is distorted: $2,363.2M of goodwill from the 2016 buyout sits in $1,400.7M of book equity (`company.goodwill`, `company.equity_book`), so the low ratio says more about accounting than risk. The CAPM estimate is already high at 12.65% (model-output.md §1), because the beta is relevered at 33.03% debt. Keep CAPM as the base case and treat any proxy figure as a cross-check.

## Module 1 Step — Questions for This Lesson

- **Share classes and the marginal investor**
  - How many classes of shares exist and what are the voting rights of each? One class of common stock, one vote a share; 50 million preferred shares are authorized and none issued (`governance.share_classes`).
  - Who are the largest shareholders? Silver Lake, 36.56%, and Thoma Bravo, 29.79% (`governance.controlling_holders`). Basic shares were 171.6M (`company.shares_basic`).
  - Is the marginal investor an individual or an institution? An institution: diversified institutions holding the public float of roughly 34% (`governance.marginal_investor`). The proxy lists no other 5% holder.
  - Is that marginal investor diversified? Yes. The sponsors are not diversified in this position, but they were not the ones trading at the margin.

## Notes

The single-beta model is adequate here because the investors who price the stock are diversified. The attack and the lawsuit go in the cash flows. Lesson 8 shows why no regression could be run, later Module 1 lessons build the bottom-up beta this lesson relies on and assemble the 12.65% cost of equity.
