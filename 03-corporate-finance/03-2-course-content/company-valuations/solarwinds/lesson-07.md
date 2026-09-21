---
title: "SolarWinds (SWI) — Lesson 07: Country Risk Premiums"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-09-21
---

# SolarWinds (SWI) — Lesson 07: Country Risk Premiums

### Lesson 07 — Country Risk Premiums

- **Lesson 07, Session 7 · Part 1 — "Implied Equity Risk Premiums and Building Country Risk Off Them"** ([transcript](../../01-foundations-and-discount-rates/lesson-07/session-7-part-1.md))
    - Quote: "a company's risk does not come from where it's incorporated but from where it does business."
    - Question for SWI: SWI is US-incorporated — but how much of its revenue is actually generated internationally, and should its equity risk premium reflect a revenue-weighted blend of country premiums rather than the flat US number?
    - Sources needed: SWI's revenue-by-geography breakdown; current implied ERP for the US and premiums for whatever countries appear.
    - Where to find: SEC-EDGAR (10-K FY2024, geographic revenue disclosure, typically in the segment/geographic-information footnote); DAMODARAN-SITE for the current implied ERP and country premium table; REPO-COUNTRY-RISK as a repo-cached fallback.
    - Answer: The geographic footnote splits FY2024 revenue as $516.6M United States (64.8%) and $280.3M international (35.2%), with no non-US country reaching the 10% disclosure threshold (swi-10k-fy2024.md, Note 16 Operating Segments and Geographic Information); the MD&A's "approximately 69% North America" figure is a wider region, not the US line, and shouldn't be used as the country-risk weight. The compiled snapshot puts the US total ERP at 4.46% — a 4.23% mature-market implied premium plus a 0.23% Aa1 sovereign premium (damodaran-country-risk-premium-us.md) — and because the footnote refuses to name any individual foreign country, a genuine country-by-country weighting cannot be built from these sources at all. Apply a deliberately generous flat 100bp premium to the entire 35.2% international slice and the weighted ERP only reaches 4.81%, a 35bp move worth about 57bp of cost of equity at a levered beta of 1.62. Do the calculation for completeness and then stop caring: the disclosed exposures are Euro, British Pound and Australian Dollar, with operations in the US, Europe, Singapore, the Philippines and India (swi-10k-fy2024.md, Item 7A) — overwhelmingly developed-market. Country risk is a rounding error on this company next to the capital-structure error buried in the repo's existing beta build.

- **Lesson 07, Session 7 · Part 2 — "Company Equity Risk Premiums and Implied ERP"** ([transcript](../../01-foundations-and-discount-rates/lesson-07/session-7-part-2.md))
    - Quote: "For every one of these companies, I'm looking past the country of incorporation to where they do business."
    - Question for SWI: What would a revenue-weighted equity risk premium look like for SWI given its actual customer/revenue geography, versus just using the flat US implied premium?
    - Sources needed: SWI 10-K/10-Q geographic revenue split (domestic vs. international, ideally by region); country-level ERP table.
    - Where to find: SEC-EDGAR (10-K geographic revenue note); DAMODARAN-SITE (current ERP by country); REPO-COUNTRY-RISK; REPO-SWI-VAL (check whether a cost-of-equity section already exists and what ERP it assumed).
    - Answer: Using the actual footnote weights of 64.8% US / 35.2% international against the compiled 4.46% US total ERP, the revenue-weighted premium lands between 4.46% (international carrying developed-market risk identical to the US) and 4.81% (international carrying a flat 100bp premium) (swi-10k-fy2024.md, Note 16; damodaran-country-risk-premium-us.md). The repo's existing Step 7 answer of 4.56% sits inside that band and survives as a number, but its inputs don't: the 69% weight is North America rather than the US, and the 20% EMEA / 11% APAC-LatAm split appears nowhere in any SWI filing — it was invented. Use 4.46% as the base case and 4.81% as the high case; the WACC swing between them is roughly 40bp, which is not where this valuation is won or lost. The error actually worth fixing is in the repo's Step 11, which used the $4.4B headline deal value as market value of equity — $4.4B is enterprise value, while equity was $18.50 × 173.1M shares = $3.20B (swi-defm14c-2025-merger-information-statement.md, beneficial ownership table) — and that single substitution understates D/E, the levered beta, and the cost of equity by far more than any country-risk refinement will move them.

## Cumulative Project — Questions for This Lesson

Module 1's `lesson-overview.md` files (Lessons 1–12) don't carry a separate "## Project Questions" section — that section only starts appearing at Lesson 13 (see `03-corporate-finance/03-2-course-content/02-investment-returns-and-financing/lesson-13/lesson-overview.md` onward). For Module 1, the Cumulative Project's equivalent deliverable is the 12-step cost-of-capital report already in [`valuation-report.md`](valuation-report.md) (Steps 2–12, plus the summary WACC table) — that work is complete. See [`README.md`](README.md) for the two confirmed corrections to that report's own figures (the equity-value/WACC-weight error and the Silver Lake/Thoma Bravo ownership-concentration error) that this lesson-by-lesson project surfaced independently but did not rewrite back into the report itself.

## Notes

Lesson 7 extends the ERP discussion into country risk specifically: risk comes from where a company does business, not where it's incorporated. Applied to SWI, the honest finding is that the 10-K's geographic footnote is too coarse to build a real country-by-country premium — it discloses only a US/international split with no single foreign country naming 10% of revenue — so both video parts converge on the same practical answer: bound the weighted ERP between 4.46% and 4.81% and move on, because the swing is roughly 40 basis points of WACC against a 236-basis-point beta error elsewhere in the report. It matters for SWI mainly as a discipline check: it's tempting to keep refining an input that's already precise enough, and this lesson is the clearest place the project explicitly says "stop here." The answer also flags, again, the equity-vs-enterprise-value mixup in the report's Step 11 — see the correction in [`README.md`](README.md) — which this lesson's second answer identifies as the far larger error hiding one step away. Connects to Lesson 5 (risk-free rate) and Lesson 6 (ERP mechanics) as the three lessons that jointly build the discount rate's risk-premium side.
