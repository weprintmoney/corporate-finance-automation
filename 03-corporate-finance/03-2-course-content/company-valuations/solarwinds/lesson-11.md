---
title: "SolarWinds (SWI) — Lesson 11: The \"Right\" Beta"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-09-20
---

# SolarWinds (SWI) — Lesson 11: The "Right" Beta

### Lesson 11 — The "Right" Beta

- **Lesson 11, Session 11 · Part 1 — "Bottom-Up Betas Across Companies — Multi- and Single-Business Cases"** ([transcript](../../01-foundations-and-discount-rates/lesson-11/session-11-part-1.md))
    - Quote: "My sample size would be far too small if I focused just on Brazilian companies."
    - Question for SWI: Since SWI is essentially single-business, should its unlevered beta be built from a *global* sample of observability/IT-ops SaaS peers rather than staying US-only, the way Damodaran went global for Tata Motors and Vale to get sample size?
    - Sources needed: A list of global (not just US) publicly traded observability/ITSM/network-monitoring peers, their regression betas, debt-to-equity ratios, and cash balances.
    - Where to find: PEER-FILINGS (expand beyond DDOG/DT/PD to any listed international peers); DAMODARAN-SITE global industry beta datasets, broader than the repo's cached snapshot.
    - Answer: Go global, and note that SWI's own bankers already did — Goldman's set includes Open Text (Canada) and Jefferies' includes Check Point (Israel), TeamViewer SE (Germany) and Trend Micro (Japan) alongside the US names (swi-defm14c-2025-merger-information-statement.md, Selected Public Companies Analysis). But the sample-size argument that drove Damodaran global for Tata Motors and Vale does not apply here: the compiled Software (System & Application) row already averages 309 firms, with a levered beta of 1.2766 at a 5.58% D/E, a 5.51% effective tax rate, 1.83% cash-to-firm-value, and a cash-corrected unlevered beta of 1.2482 (damodaran-industry-betas-software.md). Going global would be about comparability, not n, and it would barely move the number — the international infrastructure-software names the bankers chose are lower-growth and more mature than the US software average, which nudges the unlevered beta down rather than up, while DDOG/DT/PD are all US-listed and effectively unlevered anyway. Use 1.2482 and spend the estimation effort on the D/E instead: the difference between the repo's 28.1% and the correct 40.1%–49.3% is worth several times more cost-of-equity error than any peer-set geography choice.

- **Lesson 11, Session 11 · Part 2 — "Betas and Cost of Equity for Private Businesses — Bookscape and Total Beta"** ([transcript](../../01-foundations-and-discount-rates/lesson-11/session-11-part-2.md))
    - Quote: "You cannot use a market beta to come up with the cost of equity because that market beta focuses only on the risk you cannot diversify away."
    - Question for SWI: Now that SWI is privately held by Turn/River Capital rather than diversified public shareholders, should its cost of equity going forward use a "total beta" adjustment (market beta ÷ √R²), the way Damodaran did for Bookscape?
    - Sources needed: SWI's last public-era regression beta and R-squared (pre-April 2025); how diversified Turn/River's own portfolio is (a diversified PE fund holding many companies argues against needing the total-beta adjustment).
    - Where to find: NEWS-WEB / financial data terminal for SWI's last regression beta and R² before delisting; Turn/River's own investor materials (fund size, number of portfolio companies) via DEAL-DOCS or NEWS-WEB.
    - Answer: No total-beta adjustment. Bookscape was one family's undiversified wealth in a single store; Turn/River funded this with a $1,670.0M aggregate equity commitment spread across multiple affiliated investment funds plus an unnamed institutional co-investor and $225.0M of SWI's own cash (swi-8k-2025-02-07-merger-agreement-announcement.md; swi-defm14c-2025-merger-information-statement.md) — the compiled sources give no Turn/River fund size or portfolio count, but a multi-fund sponsor syndicating a check alongside a co-investor is a diversified holder by construction. The adjustment that actually belongs here is leverage, not diversification: $2.75B of new term debt ($2.225B first lien plus $525M second lien) against $1,670.0M of equity is a D/E of 164.7%, which relevers the 1.2482 unlevered beta to 2.79 and yields a cost of equity of 4.77% + 2.79 × 4.46% = 17.2% (damodaran-industry-betas-software.md; treasury-and-fed-rates.md). That alone accounts for most of a sponsor's 20%+ target return, with the remainder explained by illiquidity and a five-to-seven-year exit horizon. The repo's total-beta route to a 25.6% cost of equity — dividing by a 0.337 sector correlation that isn't even in the compiled beta file — double-counts firm-specific risk Turn/River has in fact diversified away; reserve total beta for a genuinely single-owner case.

## Notes

Lesson 11 closes out the beta arc by asking two "does this special case apply" questions: should the sample go global for a single-business firm, and should a private company's cost of equity use total beta instead of market beta? For SWI, both answers are "no, and here's the more useful thing to do instead" — the sector sample is already large enough that global comparability wouldn't move the number materially, and Turn/River's multi-fund, co-invested equity check makes it a diversified holder, so leverage (not an undiversified-owner total-beta penalty) is the right adjustment for its post-LBO cost of equity. Both answers reinforce the same running theme from Lessons 4 and 9: the report's real leverage/weights error is worth far more cost-of-equity precision than any beta-methodology refinement. This closes Module 1's cost-of-equity build and hands off directly to Lesson 12's cost-of-debt work, after which Lesson 13 assembles the full WACC.
