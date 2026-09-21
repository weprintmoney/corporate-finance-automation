---
title: "SolarWinds (SWI) — Lesson 09: Beta Fundamentals"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-09-20
---

# SolarWinds (SWI) — Lesson 09: Beta Fundamentals

### Lesson 09 — Beta Fundamentals

- **Lesson 09, Session 9 · Part 1 — "Determinants of Beta and Regression Pitfalls — Stories Behind Company Betas"** ([transcript](../../01-foundations-and-discount-rates/lesson-09/session-9-part-1.md))
    - Quote: "Companies that produce very discretionary products will have high betas."
    - Question for SWI: Is SWI's core product (IT infrastructure monitoring/observability software) a discretionary or non-discretionary spend for its customers, and does that explain where its historical beta sat relative to peers like Datadog and Dynatrace?
    - Sources needed: A qualitative read of SWI's product line (mission-critical monitoring vs. discretionary IT spend) from its business description; comparable betas for observability/IT-ops peers.
    - Where to find: SEC-EDGAR (10-K Item 1, Business); PEER-FILINGS for comparable public peers' betas and business descriptions; REPO-BETAS for the broader software industry beta as a sanity check.
    - Answer: Non-discretionary, and the filings prove it with retention rather than adjectives: FY2024 subscription net retention was 99%, the perpetual-license maintenance renewal rate was 97%, and recurring revenue was 93.5% of the $796.9M total across 300,000+ customers (swi-10k-fy2024.md, MD&A and Item 1). The portfolio is network, infrastructure, application performance, database and ITSM monitoring — the visibility layer an IT organization cannot run blind without — so the underlying business risk is genuinely low, and that is not where SWI's risk comes from. The peer contrast makes the point: Datadog grew 28% to $3.43B and Dynatrace 19% to $2.02B while SWI grew 5.0%, and both peers are effectively unlevered (Dynatrace's $400M revolver sits undrawn with $399.0M available; Datadog's $983M of notes are 0.00%-coupon 2029 converts) against SWI's $1.24B first-lien term loan (dt-dynatrace-10k.md; ddog-datadog-10k.md; pd-pagerduty-10k.md; swi-10k-fy2024.md, Note 9). SWI is a low-business-risk asset wearing a high-financial-risk capital structure — a combination a regression on a stock with only ~35% public float (Silver Lake 35.5% plus Thoma Bravo 28.9%) will systematically fail to detect.

- **Lesson 09, Session 9 · Part 2 — "The Three Determinants of Beta — Business, Operating Leverage, Financial Leverage"** ([transcript](../../01-foundations-and-discount-rates/lesson-09/session-9-part-2.md))
    - Quote: "It makes your equity earnings much more volatile and through that, it makes your beta higher."
    - Question for SWI: Given SWI's LBO-era debt load, how much of its (formerly public) equity beta was inflated by financial leverage versus its underlying unlevered business beta?
    - Sources needed: SWI's total debt and market value of equity (last public-era market cap) to compute debt-to-equity; marginal tax rate; unlevered beta for the observability/IT-ops software sector.
    - Where to find: SEC-EDGAR (10-K FY2024 balance sheet for total debt; income statement for effective/marginal tax rate; last 10-K/DEF14A for share count and price); REPO-BETAS (Damodaran sector unlevered betas — software/IT services).
    - Answer: Roughly a quarter of the levered beta, once the inputs are right. Debt is the $1,235.7M term loan principal plus $49.4M of capitalized operating leases = $1,285.0M; equity is $3,202.9M at the $18.50 deal price on 173.1M shares (D/E = 40.1%) or $2,604.9M at the last undisturbed close of $15.18 on 171.6M shares (D/E = 49.3%) (swi-10k-fy2024.md, Notes 7 and 9; swi-defm14c-2025-merger-information-statement.md). Relevering the 1.2482 cash-corrected unlevered beta at a 25% marginal rate (federal 21% plus blended state — the reported −7.8% effective rate is a valuation-allowance artifact, not a marginal rate) gives 1.62 at the deal price and 1.71 at the undisturbed price, so financial leverage contributes 0.37–0.46 of beta, or 23–27% of the total (damodaran-industry-betas-software.md). That also condemns the repo's Step 11, whose D/E of 0.281 came from treating the $4.4B headline enterprise value as equity: correcting it raises the levered beta by 0.07–0.16 and the cost of equity by 30–70bp. Empirically none of this leverage showed up in the traded beta of 0.55–0.88, which indicts the regression rather than the Hamada arithmetic.

## Notes

Lesson 9 decomposes beta into its three determinants — business risk, operating leverage, financial leverage — and this is the lesson that most directly diagnoses what's wrong with the report's existing beta build. Part 1 establishes that SWI's underlying business (mission-critical monitoring, 93.5% recurring revenue) is genuinely low-risk, so the company's risk is almost entirely a financial-leverage story; Part 2 quantifies that story and, in doing so, catches the report's Step 11 debt-to-equity error at its source — using the $4.4B enterprise value as if it were equity value, understating D/E and therefore the levered beta and cost of equity. This is the first lesson to name that specific error explicitly; see the correction documented in [`README.md`](README.md) rather than re-deriving it in every later lesson that touches beta or WACC weights. It sets up Lesson 10's decision to use one industry-wide unlevered beta (since SWI is single-business) and Lesson 13's cost-of-capital-weights rebuild.
