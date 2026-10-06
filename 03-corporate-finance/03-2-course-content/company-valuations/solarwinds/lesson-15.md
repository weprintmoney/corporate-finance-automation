---
title: "SolarWinds (SWI) — Lesson 15: Incremental Cash Flows and Time-Weighted Returns"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-10-06
---

# SolarWinds (SWI) — Lesson 15: Incremental Cash Flows and Time-Weighted Returns

### Lesson 15 — Incremental Cash Flows and Time-Weighted Returns

- **Lesson 15, Session 15 · Part 1 — "Sunk Costs, Non-Incremental G&A, and Time-Weighting Cash Flows"** ([transcript](../../02-investment-returns-and-financing/lesson-15/session-15-part-1.md))
    - Quote: "The first rule in capital budgeting is you have sunk cost, money were already spent, don't consider them."
    - Question for SWI: Using the lecture's "what happens if I take it / what happens if I don't" test, how much of SWI's pre-close diligence and integration spend on the Squadcast acquisition (~March 2025) should be excluded as a sunk cost when evaluating the incremental cash-flow return on continued observability-platform integration, and how much corporate G&A allocated to legacy Orion support is genuinely non-incremental?
    - Sources needed: Disclosed Squadcast deal/integration costs to date; any product-line allocation of corporate G&A that would reveal what's truly incremental versus reallocated elsewhere.
    - Where to find: SEC-EDGAR — SWI 8-K (Squadcast acquisition, ~March 2025) and 10-K FY2024 Item 7 MD&A (M&A/integration cost discussion); REPO-SWI-VAL (Step 4, stated objectives re: Squadcast).
    - Answer: The sunk cost is trivially small, and the Squadcast deal is not in the compiled corpus at all — the FY2024 10-K (filed 2025-02-19), the merger information statement, and both 2025 8-Ks never mention it, because the deal closed after SWI's last public reporting period and no separate 8-K was compiled (sources/README.md; searched across sec-filings/). The only available envelope is the non-GAAP "Acquisition and other costs" line — $1.145M in FY2024, $2.612M in FY2023, $0.540M in FY2022 — which by SWI's own definition captures legal, accounting and advisory fees, integration costs, deferred compensation, severance and retention (swi-10k-fy2024.md, MD&A non-GAAP reconciliation). All acquisition and integration spend across three years is therefore under $4.3M, about 0.5% of one year's revenue: run the "what happens if I take it / what happens if I don't" test and excluding it changes nothing about the decision. On the G&A half, there is no answer to give and no point pretending otherwise — SWI reports one segment with the CODM reviewing only consolidated results (Note 16), so none of the $125.848M of G&A is allocated between Orion and observability. The defensible inference: nearly all of it — public-company costs, finance, legal, the ongoing SEC matter — is non-incremental to any product-line decision, meaning an observability-integration NPV should be charged essentially zero allocated G&A.

- **Lesson 15, Session 15 · Part 2 — "NPV, IRR, and Terminal Value via the Growing Perpetuity"** ([transcript](../../02-investment-returns-and-financing/lesson-15/session-15-part-2.md))
    - Quote: "If you take a project with an NPV of $3.3 billion, your value will increase by $3.3 billion."
    - Question for SWI: What terminal-value growth rate is defensible for SWI's SaaS/observability-transition cash flows beyond a 10-year explicit forecast, given intensifying disruption risk from cloud-native competitors (Datadog, Dynatrace), and does the Turn/River deal's fairness-opinion DCF use a terminal growth rate consistent with the lecture's constraint that it cannot exceed overall economic growth?
    - Sources needed: Banker's DCF assumptions (discount rate, terminal growth rate) from the merger proxy; peer long-term growth assumptions for comparison.
    - Where to find: DEAL-DOCS (Turn/River DEFM14A fairness opinion DCF); PEER-FILINGS (DDOG, DT growth-rate context); DAMODARAN-SITE (long-term GDP growth constraint data).
    - Answer: 2–3% is defensible and both banker DCFs respected the constraint — the indefensible assumption sits in the explicit forecast, not the terminal value. Goldman Sachs used perpetuity growth rates of 2.0%–3.0% with discount rates of 9%–11%, implying terminal NTM Adjusted EBITDA exit multiples of 6.5x–9.8x; Jefferies used 2.5%–3.5% with a 10.70%–11.70% WACC range, both over six-year explicit forecasts (2025–2030), not ten (swi-defm14c-2025-merger-information-statement.md, Opinion of Goldman Sachs and Opinion of Jefferies). Both ranges sit well below the 4.77% 10-year Treasury (treasury-and-fed-rates.md), so Damodaran's cap — terminal growth cannot exceed the risk-free rate as a proxy for nominal economic growth — is satisfied with room to spare, and Goldman's implied terminal multiple is below the ~10.9x LTM Adjusted EBITDA the deal itself paid. The problem is the ramp: management's LRP takes revenue from $796.9M to $1,273M (8.1% CAGR) and EBIT from $208.4M to $511M (16.1% CAGR, operating margin 26.2% → 40.1%) after an actual FY2019–FY2024 revenue CAGR of 3.6% (swi-defm14c-2025-merger-information-statement.md, Certain Company Financial Forecasts; swi-multi-year-financials.md). Meanwhile Datadog grew 27.7% to $3,427M in FY2025 and Dynatrace 18.8% to $2,018M in FY2026 — both already larger than SWI's entire 2030 target (ddog-datadog-10k.md, dt-dynatrace-10k.md). The value is manufactured in that six-year acceleration, not the 2.5% tail.

## Cumulative Project — Questions for This Lesson

- **If you can identify a typical project for your firm, what pattern of cash flows do you foresee for the project?**
  Building on Lesson 14's identification of SWI's typical project (an annual subscription contract, increasingly displacing the legacy perpetual-license-plus-maintenance sale), the cash-flow pattern is: cash collected upfront or annually in advance at signing/renewal (creating a deferred-revenue liability that grew $10.559M in FY2024 alone, per this lesson's Part 1 answer above), revenue recognized ratably over the contract term, and near-zero incremental investment required to deliver it — SWI's entire FY2024 capitalized spend was $20.478M against $796.9M of revenue. There is effectively no "initial outlay, then payback" curve the way a manufacturing or infrastructure project would have; the cash comes in ahead of the accounting revenue, at a marginal cost close to the cost of support and hosting, and the only real "investment" is the R&D and sales cost of winning or renewing the contract in the first place (both of which are expensed, not capitalized, per Lesson 14 MD&A discussion). At the portfolio level this produces the pattern this project keeps finding: high, stable, recurring cash flow (93.5% of FY2024 revenue was recurring, per Lesson 9) with almost no reinvestment drag — which is exactly why FCFF ($197.3M per Lesson 14 Part 1, or $153.8M on the base-year DCF build in Lesson 30) tracks so close to after-tax EBIT rather than falling well below it the way a capital-intensive business's would.

## Notes

Lesson 15 is about isolating truly incremental cash flows (ignoring sunk costs and non-incremental G&A) and about the mechanics of terminal value via a growing perpetuity. For SWI, both questions turn out cleaner than expected: the Squadcast integration spend is immaterial (under $4.3M across three years) and the terminal-growth assumptions both banks actually used (2–3.5%) comfortably respect the "can't exceed the risk-free rate" constraint — the real aggressiveness in the deal's valuation is in the six-year explicit growth ramp, not the terminal tail. That distinction — terminal value is fine, the forecast period is where the optimism lives — is the exact insight Lesson 32 returns to and quantifies precisely for SWI's own terminal year. This lesson also flags that single-segment reporting makes any G&A allocation between legacy and observability lines fundamentally unbuildable, a limitation Lessons 10 and 13 run into as well.

## Meetup 2 lens: AI threatens the growth half of the ramp

In [Meetup 2](../../../03-7-meetups/meetup-2-2026-09-22.md) (2026-09-22), Damodaran argued that AI will make much of software a smaller, more commoditized market. On his view, the 85%–90% gross margins software lived on won't last, and the advantage shifts to the lowest-cost operators. He also expects AI to move value between companies more than create new value.

- **SWI's fat is in the gross margin.** FY2024 GAAP gross margin was 89.5% ($713.6M on $796.9M), at the top of his range. Operating margin was 26.2% ($208.4M), far below the 50% he cited for software (`swi-10k-fy2024.md`). Gross margin is what price competition from AI tools hits first.
- **The LRP assumes that margin holds.** Non-GAAP gross margin is 93.4% in 2025E ($777M on $832M) and 91.5% in 2030E ($1,165M on $1,273M) (`swi-defm14c-2025-merger-information-statement.md`).
- **60% of the EBIT ramp is growth, 40% is margin.** LRP EBIT rises from $272M (2025E) to $511M (2030E), up $239M. At the 2025E margin of 32.7%, 2030E revenue of $1,273M gives $416M. So $144M (60%) comes from revenue growth and $95M (40%) from margin expansion. The growth half is the part exposed to AI.
- **Management already traded growth for cost.** From the 2023 Plan to the January 2025 LRP:
    - 2025E–2027E revenue was cut by $19M, $17M and $10M.
    - Operating expenses for the same years were cut by $34M, $24M and $17M.
    - Adjusted EBITDA went up every year: 393 → 412, 442 → 447, 488 → 492 (same source).

  That is the "lean businesses win" move from the meetup. It's the more credible half of the plan, because cost is within management's control.
- **SWI's 10-K describes the incumbent's bind.** It calls AI "a significant enabler" for its products. It also warns that regulated customers may avoid products that use generative AI, while "failing to adopt generative AI may put us at a competitive disadvantage" (`swi-10k-fy2024.md`, Item 1A). That is the cannibalization problem Damodaran described for Adobe.
- **Who gets the value is open.** In his "factory" framing, the winners are those who use AI to build products. SWI could be one of them, or the value could pass to customers through lower prices. The filings give no evidence either way.

**What this changes:** The Part 2 conclusion stands: the value is in the six-year ramp, not the terminal value. The meetup shows which part to doubt. It's the revenue growth (8.1% CAGR against 3.6% history), not the cost plan. A useful next run would be the DCF with LRP margins and historical revenue growth.

**Open question:** Nothing in `sources/` shows SWI's pricing after 2024, so the gross-margin risk can't be tested on SWI's own data.
