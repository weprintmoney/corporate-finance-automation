---
title: "SolarWinds (SWI) — Lesson 10: Bottom-up Betas"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 10: Bottom-up Betas

### Lesson 10 — Bottom-up Betas

- **Lesson 10, Session 10 · Part 1 — "Bottom-Up Betas — Why They Beat Regression"** ([transcript](../../01-foundations-and-discount-rates/lesson-10/session-10-part-1.md))
    - Quote: "A bottom-up beta is more precise, more forward-looking, and more dynamic than a regression beta."
    - Question for SolarWinds: Is SolarWinds single-business enough to use one industry unlevered beta, or does it have segments different enough to need separate betas weighted by value? Which comparable set, and why?
    - Sources needed: Segment disclosure in the 10-K; the industry beta file; the list of businesses the industry group covers.
    - Where to find: `sources/filings/swi-10k-fy2024.md` note 16; `sources/market-data/industry-betas-2025-01-05.json`; `inputs.yaml` `beta.unlevered_bottom_up`; `meta.omitted`.
    - Answer: One business, one beta. The 10-K says "We operate as a single reportable segment," and the chief executive, who allocates resources, assesses performance at the consolidated level (note 16). The only breakdown is by contract type: subscription $304.5M (38.2%), maintenance $440.6M (55.3%) and license $51.8M (6.5%) (facts.subscription-revenue, facts.maintenance-revenue, facts.license-revenue). That is how customers pay, not what they buy, and no filing gives profit or capital by product. Inventing segment weights would produce precision the data does not support, so `beta.segments` is not in the ledger. The comparable set is Damodaran's US Software (System & Application) group, January 2025: 333 firms, unlevered beta corrected for cash 1.22 (`beta.unlevered_bottom_up`). The steps behind 1.22: the group's levered beta of 1.24 (facts.industry-software-levered-beta) is unlevered at the group's own debt to equity of 4.9% (facts.industry-software-de-ratio) and tax, giving 1.1960 (facts.industry-software-unlevered-raw); then cash is removed, because cash has a beta near zero and dilutes the business beta, at 1.74% of firm value (facts.industry-software-cash-share), giving 1.22. This group fits because it holds the same kind of firm: infrastructure and application software sold on license, maintenance and subscription. Averaging 333 firms shrinks the error that makes a single firm's regression noisy. It uses the January 2025 file, because the valuation date is 2025-02-05.

- **Lesson 10, Session 10 · Part 2 — "Bottom-Up Beta by Business — Aggregating and Levering"** ([transcript](../../01-foundations-and-discount-rates/lesson-10/session-10-part-2.md))
    - Quote: "Because the movie business is riskier than Disney as a company, you should demand much more of it, a higher hurdle rate."
    - Question for SolarWinds: If SolarWinds has businesses with different risk, what hurdle rate should each carry, which one is riskier than the company as a whole, and where would using one company-wide rate lead to the wrong investment decision?
    - Sources needed: Any split of the firm into businesses with different risk; the company-wide hurdle rate; a beta for each candidate business.
    - Where to find: 10-K note 16 and MD&A; model-output.md §1; industry beta file.
    - Answer: The company-wide hurdle rates are a 12.65% cost of equity and a 10.23% cost of capital (model-output.md §1). The filings support one business, so each carries that rate. The candidate for a riskier piece is the newer observability subscription work (growing, 30.0% subscription revenue growth in 2024, facts.subscription-growth-2024) against the maintenance base that is shrinking (maintenance revenue fell 4.6%, facts.maintenance-decline-2024). If it were split out, the right comparison would be a higher-beta group such as Software (Internet) at 1.60 unlevered (facts.industry-beta-software-internet), against 1.22 for the whole. That figure is an illustration of the gap, not a ledger input: there is no revenue, profit or capital figure for observability alone, so no weighted average can be built. Where one rate misleads: a single 10.23% bar is too low for a bet on a new observability product and too high for a renewal-driven maintenance conversion. The practical risk is capital spent on acquisitions at the company-wide rate; the balance sheet carries $2,363.2M of goodwill (`company.goodwill`), mostly from the 2016 buyout. Whether a project clears 10.23% is a coarse test for either business.

## Module 1 Step — Questions for This Lesson

- **Bottom-up unlevered beta** (`m1-step-10`)
    - What is the bottom-up unlevered beta from comparable firms, cash-corrected? 1.22, from 333 US software (system and application) firms, January 2025 (`beta.unlevered_bottom_up`).
    - If the company has several businesses, what is each segment's beta and the weighted average? SolarWinds has one reportable segment, so there is one beta, 1.22, at 100% weight. No segment table is built. The ledger's `beta.segments` is therefore empty and is listed in `meta.omitted`.

## Notes

The unlevered beta of 1.22 is the single most consequential risk input in the run: it feeds the levered beta of 1.6714 and the cost of equity of 12.65% (model-output.md §1). The case for one beta rests on the segment note, so it is a disclosure-based choice, not a convenience.

Lesson 11 tests whether the sample should be global; lesson 13 weights this beta and the debt into the cost of capital.
