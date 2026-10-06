---
title: "SolarWinds (SWI) — Lesson 05: The Risk Free Rate"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-10-06
---

# SolarWinds (SWI) — Lesson 05: The Risk Free Rate

### Lesson 05 — The Risk Free Rate

- **Lesson 05, Session 5 · Part 1 — "Matching the Risk-Free Rate to Currency and Time Horizon"** ([transcript](../../01-foundations-and-discount-rates/lesson-05/session-5-part-1.md))
    - Quote: "There is no global risk-free rate."
    - Question for SWI: The valuation currently uses the 10-year UST as the risk-free rate given USD reporting — but SolarWinds draws ~31% of revenue internationally and, post-2025, sits inside Turn/River's private capital structure with new acquisition debt. Does the "match currency to the analysis" principle still hold cleanly, or does the new ownership structure require a blended/entity-specific risk-free rate going forward?
    - Sources needed: Post-acquisition (2025) financing structure and debt currency mix for the $4.4B Turn/River deal; current international revenue mix.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 (revenue by geography) and going-private 8-K/DEFM14A (financing sources); REPO-RATES — current 10Y UST already used as the analysis risk-free rate.
    - Answer: The principle holds cleanly — keep the single USD 10-year Treasury, currently 4.77% (treasury-and-fed-rates.md, DGS10 as of 2026-09-03). Two corrections to the premise. The international share is 35.2%, not 31%: the geographic footnote reports United States $516,559K and International $280,336K of $796,895K total, and the "69%" figure in MD&A is *North America*, which includes Canada (swi-10k-fy2024.md, Note 16). And the new capital structure is *less* multicurrency, not more: the April 2025 financing is a $2.225B first-lien term facility plus a $200.0M revolver and a $525.0M second-lien term facility, all USD-denominated, replacing a facility that had contained a $112.5M multicurrency revolver tranche (swi-8k-2025-04-16-merger-closing.md, Item 1.01; swi-10k-fy2024.md, Note 9). SolarWinds' functional currency is USD, it reports in USD, and it now borrows exclusively in USD, so a blended or entity-specific risk-free rate would introduce error rather than remove it. What the LBO actually changes is leverage — D/E moved from 0.28 to roughly 1.65 ($2.75B debt against Turn/River's $1.670B equity commitment) — which belongs in beta and the capital-structure weights, not in the risk-free rate.

- **Lesson 05, Session 5 · Part 2 — "Netting Out the Default Spread — Risk-Free Rates in Difficult Currencies"** ([transcript](../../01-foundations-and-discount-rates/lesson-05/session-5-part-2.md))
    - Quote: "The key to currency is to stay consistent, pick a currency and do both your returns and your hurdle rate in that currency."
    - Question for SWI: The repo's country-risk weighting bundles SWI's ~11% APAC/LatAm revenue into a single blended CRP. Should that slice instead get country-specific risk-free rates (netting local default spreads per this lesson's method) rather than folding everything back into one USD discount rate, and would that meaningfully move the already-computed weighted cost of capital?
    - Sources needed: Country-level (not just region-level) revenue breakdown for SWI's APAC/LatAm segment, local government bond rates and sovereign ratings for those specific countries.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 geographic revenue footnote (may only disclose region-level); REPO-COUNTRY-RISK — country ERP/default-spread data by country; REPO-SWI-VAL — Step 7 (existing region-level country-risk weighting).
    - Answer: You can't, and you shouldn't want to — this is a genuine limit of public disclosure. SolarWinds' geographic footnote is a two-line disclosure: "United States, country of domicile $516,559" and "International $280,336," with the explicit statement that "[o]ther than the United States, no single country accounted for 10% or more of our total revenues during these periods" (swi-10k-fy2024.md, Note 16). There is no region level, let alone country level — so the repo's 69% / 20% EMEA / 11% APAC+LatAm split in Step 7 is an analyst estimate that cannot be traced to the filing, and country-specific risk-free rates for an undisclosed slice would be false precision. Run the sensitivity to see how little is at stake: substituting the disclosed 64.8% / 35.2% weights and blending international at ~4.80% gives 0.648 × 4.46% + 0.352 × 4.80% = 4.58%, against the repo's 4.56% (damodaran-country-risk-premium-us.md, US total ERP 4.46%). That 2 bp of ERP moves the cost of equity ~3 bp at a levered beta of 1.55 and the WACC ~2 bp against a 10.33% base. Keep one USD discount rate, apply the local-default-spread netting method only where a filing actually names material country exposure, and spend the effort on the beta — which swings WACC by 236 bp.

## Cumulative Project — Questions for This Lesson

Module 1's `lesson-overview.md` files (Lessons 1–12) don't carry a separate "## Project Questions" section — that section only starts appearing at Lesson 13 (see `03-corporate-finance/03-2-course-content/02-investment-returns-and-financing/lesson-13/lesson-overview.md` onward). For Module 1, the Cumulative Project's equivalent deliverable is the 12-step cost-of-capital report already in [`valuation-report.md`](valuation-report.md) (Steps 2–12, plus the summary WACC table) — that work is complete. See [`README.md`](README.md) for the two confirmed corrections to that report's own figures (the equity-value/WACC-weight error and the Silver Lake/Thoma Bravo ownership-concentration error) that this lesson-by-lesson project surfaced independently but did not rewrite back into the report itself.

## Notes

This lesson's core point — there is no global risk-free rate; pick a currency and stay consistent — turns out to hold exactly for SWI, in both directions the questions probe. Using the USD 10-year Treasury remains correct even after the 2025 LBO, because SWI's debt, reporting currency, and functional currency are all USD, and going further to country-specific risk-free-rate netting is blocked by disclosure: the 10-K's geographic footnote is only a two-line US/international split with no country-level detail. It matters for SWI mainly as a "don't over-engineer this" result — the corrected 35.2% international revenue share (not 31%, and not the MD&A's 69% North America figure) moves the weighted ERP by only a few basis points, far less than the beta-construction error carried through Lessons 8–11. This connects directly to Lessons 6–7, which build the equity risk premium on top of this risk-free-rate foundation.

## Meetup 2 lens: net the default spread out of the Treasury rate

In [Meetup 2](../../../03-7-meetups/meetup-2-2026-09-22.md) (2026-09-22), Damodaran said the US Treasury rate is no longer a true dollar risk-free rate now that the US has lost its AAA rating. He uses a rate about 22bp below the Treasury, to be consistent with how he cleans default risk out of every other government's bond.

- **This project has not netted it out.** Both answers above use the gross 10-year Treasury of 4.77% (`treasury-and-fed-rates.md`, DGS10 as of 2026-09-03). So do Lesson 13's WACC and the rerun script (`tools/capital-structure-rerun.py`, `RF = .0477`).
- **The current pairing counts US default risk twice.** The 4.46% US equity risk premium is the 4.23% mature-market premium plus a 0.23% US country risk premium (`damodaran-country-risk-premium-us.md`). Damodaran measures that premium against the netted rate. On 2026-01-01 he took the 4.18% Treasury, subtracted 0.23%, and got a 3.95% dollar risk-free rate (`03-4-blogs/posts/2026-02-01-data-update-4-for-2026-the-global-perspective.md`). Adding 4.46% to a gross 4.77% puts the US default spread in both the rate and the premium. His June 2025 post names this exact double-count as the reason to net (`2025-06-02-sovereign-ratings-default-risk-and-markets-the-moody-s-downgrade-aftermath.md`).
- **Recalculated at 22bp:** rf = 4.77% − 0.22% = 4.55%. Levered beta is unchanged at 1.622 (1.2482 × [1 + 0.75 × 1,256.0/3,142.1]). Cost of equity = 4.55% + 1.622 × 4.46% = 11.79%, down from 12.01%. The 7.11% pre-tax cost of debt stays, because it is an observed loan rate (Lesson 12), not rf plus a spread. WACC = 71.4% × 11.79% + 28.6% × 7.11% × 0.75 = 8.42% + 1.52% = **9.94%**, down from 10.10%. Using the dataset's 0.23% gives rf 4.54% and the same 9.94%.
- **Downstream (rerun script with RF = 4.55%, recommended track C):** DCF value per share rises from $18.94 to $19.49, which is 5.4% above the $18.50 deal price instead of 2.4%. The EBIT-coverage optimum stays at 17%. The upper case moves from 21% to 22%. The value gain from moving to the optimum becomes $261–435M (was $241–419M).
- **The bankers' ranges no longer both bracket it.** 9.94% sits inside Goldman's 9%–11% but below Jefferies' 10.70%–11.70% (`swi-defm14c-2025-merger-information-statement.md`; Lesson 15).

**What this changes:** The answer above is right that SWI needs one USD rate. It's wrong that the rate is the Treasury itself. Use 4.55% and carry it through Lessons 13, 18, 19 and 34 and the rerun script. The "deal priced at status-quo value" conclusion in Lesson 34 still holds within about 5%, but the deal now looks slightly cheap rather than fair.

**Open questions:**
- **Valuation date.** 4.77% is a September 2026 rate, while the DCF is compared with a February 2025 deal price. The early-2025 Treasury is not in `sources/`.
- **Spread vintage.** The meetup and the July 2026 post use 0.22%. The dataset behind the 4.46% ERP uses 0.23%. Match the spread to the ERP vintage. The difference is 1bp.
