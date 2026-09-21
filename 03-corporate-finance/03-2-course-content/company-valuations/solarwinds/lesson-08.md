---
title: "SolarWinds (SWI) — Lesson 08: Regression Betas"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-09-20
---

# SolarWinds (SWI) — Lesson 08: Regression Betas

### Lesson 08 — Regression Betas

- **Lesson 08, Session 8 · Part 1 — "Estimating Regression Betas — The Four Choices"** ([transcript](../../01-foundations-and-discount-rates/lesson-08/session-8-part-1.md))
    - Quote: "There's a reason why services latch on to the S&P 500 for U.S. companies."
    - Question for SWI: Since SWI was delisted in April 2025, a regression run today has no live price data — what's the last usable 2–5 year pre-acquisition window, and does a regression beta from that stale window still represent SWI's risk today?
    - Sources needed: Historical daily/weekly SWI (NYSE: SWI) price and dividend data through the April 2025 delisting; S&P 500 index returns for the same window.
    - Where to find: NEWS-WEB / financial data providers (Yahoo Finance, Nasdaq historical data) for SWI's 2018–2025 price history; SEC-EDGAR (10-K/10-Q) confirms SWI paid no common dividend, simplifying the return calc.
    - Answer: The tradable history runs from the NYSE listing on October 19, 2018 (IPO priced at $15.00 on October 18) to the Form 25 delisting request on April 16, 2025 (swi-10k-fy2018.md, Item 5; swi-8k-2025-04-16-merger-closing.md, Item 3.01) — about 78 months, and the raw price series is not compiled here (see the sources README's unattainable table). The citation's premise is also wrong: SWI paid a $1.50 special dividend in August 2021 and a $1.00 special dividend ($168.2M aggregate) on April 15, 2024, alongside a July 2021 N-able spin-off and a 1-for-2 reverse split on July 30, 2021 (swi-def14a-2024.md; swi-10k-fy2024.md, Liquidity and Capital Resources) — four corporate actions that any honest return series has to adjust for. The only internally consistent window is roughly August 2021 through February 5, 2025, the last undisturbed trading day before announcement (swi-defm14c-2025-merger-information-statement.md), because from February 7 the stock was pinned near $18.50 and its measured beta collapses toward zero — about 42 monthly observations, still contaminated by SUNBURST litigation and the SEC complaint. And it doesn't describe today's SWI regardless: the post-close capital structure is $2.75B of debt against a $1.67B equity check, a D/E near 165% versus roughly 49% at the undisturbed price. Use a bottom-up beta; the regression is not stale, it's dead.

- **Lesson 08, Session 8 · Part 2 — "Interpreting the Regression Beta — Jensen's Alpha, Standard Error, R-Squared"** ([transcript](../../01-foundations-and-discount-rates/lesson-08/session-8-part-2.md))
    - Quote: "Standard errors are features, not bugs. They're part of the process, we've got to learn to deal with them."
    - Question for SWI: Using SWI's actual pre-delisting regression beta and its standard error, how wide is the confidence interval — and is it too wide to trust a standalone regression-based cost of equity for SWI?
    - Sources needed: SWI's regression beta output (beta, standard error, R-squared) against the S&P 500 over ~5 years of monthly returns pre-April 2025.
    - Where to find: NEWS-WEB / a financial data terminal (Bloomberg/Capital IQ) beta page if accessible; otherwise self-computed from the raw price data in Part 1's sources; REPO-BETAS gives an industry-level cross-check rather than a firm-specific number.
    - Answer: A monthly firm-specific regression is not attainable from the compiled sources, so the best available substitute is the DEF 14A pay-versus-performance table, which indexes $100 invested on 12/31/2019: SWI at 81, 57, 38, 51 for 2020–2023 against the S&P 500 Information Technology index at 142, 190, 135, 211 (swi-def14a-2024.md, Pay versus Performance). Converting those to annual returns (SWI −19.0%, −29.6%, −33.3%, +34.2%; index +42.0%, +33.8%, −29.0%, +56.3%) and regressing gives a beta of 0.55 with an R² of 0.43 and a standard error of 0.44 — with only four observations, the 95% confidence interval runs from roughly −1.4 to +2.5. That interval contains zero, one, and the industry beta simultaneously, which is Damodaran's point stated brutally: the estimate is arithmetically real and informationally empty, and the repo's cited 0.88 regression beta is inside it too, so quoting either number to two decimals is false precision. Discard the regression rather than averaging it in, and relever the Software (System & Application) cash-corrected unlevered beta of 1.2482 to SWI's own capital structure instead (damodaran-industry-betas-software.md).

## Notes

This lesson is about the mechanics and honest limits of a regression beta: the four estimation choices (index, period, interval, return type) in Part 1, and reading the standard error/R²/confidence interval rather than the point estimate alone in Part 2. SWI is close to a worst case for this method — delisted since April 2025, a thin float even while public, and a price series so contaminated by corporate actions (a spin-off, a reverse split, two special dividends, and eleven months pinned near the deal price) that no clean regression window exists. The confidence-interval exercise in Part 2 makes the point concrete: a four-observation regression on the DEF 14A performance table gives a beta whose 95% interval runs from roughly −1.4 to +2.5, wide enough to contain zero, one, and the industry average simultaneously — which is exactly why the project abandons regression betas for a bottom-up build starting in Lesson 9. This is the direct setup for Lessons 9–11, which construct and defend that bottom-up beta.
