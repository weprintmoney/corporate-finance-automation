---
title: "SolarWinds (SWI) — Lesson 08: Regression Betas"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 08: Regression Betas

### Lesson 08 — Regression Betas

- **Lesson 08, Session 8 · Part 1 — "Estimating Regression Betas — The Four Choices"** ([transcript](../../01-foundations-and-discount-rates/lesson-08/session-8-part-1.md))
    - Quote: "There's a reason why services latch on to the S&P 500 for U.S. companies."
    - Question for SolarWinds: For SolarWinds, which index, return interval and window are available for a regression beta, and are they clean enough (listing age, thin trading, a delisting, a change in the business) to give a usable estimate?
    - Sources needed: SolarWinds' daily or weekly price history and dividends; the S&P 500 for the same dates; listing, delisting and corporate-action dates.
    - Where to find: `meta.omitted`; `sources/README.md` (Could not be obtained); `sources/filings/swi-10k-fy2018.md` (cover page); `sources/filings/swi-10k-fy2023.md` and `swi-10k-fy2024.md` (dividends, reverse split, N-able); `sources/deal-docs/swi-8k-2025-04-16-merger-closing.md` (Item 3.01).
    - Answer: In principle: the S&P 500 as the index, a weekly or monthly interval, a five-year window, and returns that include dividends. In practice: no, and the data would not be clean. The stock traded on the NYSE from 2018-10-19 until delisting at the 2025-04-16 closing (`facts.listing-dates`). Four events break the series: the N-able spin-off on 2021-07-19, a one-for-two reverse split on 2021-07-30, a $1.50 special dividend paid 2021-08-24 and a $1.00 special dividend paid 2024-04-15 (`facts.corporate-actions-2021`; `facts.special-dividend-2021`; `company.history`). Dividends have to be in the returns. The business also changed: the spin-off removed the managed-service business, and the SUNBURST attack fell in a five-year window ending February 2025. From the announcement on 2025-02-07 the price was pinned near the $18.50 offer, so a usable window ends on 2025-02-05. After the spin-off that leaves about three and a half years. Thin trading adds noise: stock held by non-affiliates was worth only $661.3M on 2024-06-28 (`facts.float-nonaffiliate-value`). The raw price history could not be obtained: free sources no longer serve delisted tickers, and Capital IQ's chart module did not load (`sources/README.md`). No regression was run, and the bottom-up beta replaces it.

## Module 1 Step — Questions for This Lesson

- **Regression beta**
  - What is the regression beta, against which index, over what window and interval? Not computed. The fields `beta.regression_beta`, `beta.regression_se`, `beta.regression_r2` and `beta.jensens_alpha` are listed under `meta.omitted`, because no price history for a delisted ticker could be obtained. The bottom-up unlevered beta, 1.22, is used instead (`beta.unlevered_bottom_up`).
  - What are the standard error and R-squared, and is the estimate reliable? Not available. For scale, the proxy's pay-versus-performance table gives only four annual points for SolarWinds against a peer group (`facts.tsr-2023`), too few for a regression, and the filings give no beta or R-squared.

## Skipped

- l08-p2 (regression beta, standard error, R-squared and Jensen's alpha): no regression exists to interpret. `meta.omitted` lists all four fields with the reason. If price data is added later, the lesson 8 spreadsheet method applies and the entry should be answered then.

## Notes

This lesson closes the door on a regression beta for SolarWinds and says why. The next lessons build the bottom-up beta from the software industry's unlevered 1.22 (cash-corrected, 333 firms) and relever it to 1.6714 at the actual debt ratio (model-output.md §1). The reasons the regression would have been poor are independent of data access: the spin-off, the attack, a thin float and a price pinned by a pending deal.
