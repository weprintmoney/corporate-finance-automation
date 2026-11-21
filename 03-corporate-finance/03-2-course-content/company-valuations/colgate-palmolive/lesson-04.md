---
title: "Colgate-Palmolive (CL) — Lesson 04: Define and Measure Risk"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 04: Define and Measure Risk

### Lesson 04 — Define and Measure Risk

- **Lesson 04, Session 4 · Part 1 — "Danger Plus Opportunity — The Ingredients of a Good Risk and Return Model"** ([transcript](../../01-foundations-and-discount-rates/lesson-04/session-4-part-1.md))
    - Quote: "Risk is equal to danger plus opportunity."
    - Question for Colgate-Palmolive: Does a single-beta model price the risks that matter most for Colgate-Palmolive (customer concentration, regulation, tail events)? Which of those fall into the diversifiable, unpriced bucket, and does Colgate-Palmolive's actual marginal investor diversify them away?
    - Sources needed: Customer concentration; legal and regulatory exposure; currency and country exposure; who holds the stock.
    - Where to find: ledger `governance.marginal_investor`, `country.exposures`, `facts.walmart-share-of-sales`, `facts.legal-matters-2025`, `facts.geographic-risk-notes`, `facts.holders-capital-iq`; `sources/filings/cl-10k-fy2025.txt` Item 1A.
    - Answer: Yes, for the investor who sets the price. The risks that fill Colgate's risk-factor pages are mostly its own. Walmart is about 11% of net sales (`facts.walmart-share-of-sales`). There are 454 talcum powder cases (`facts.legal-matters-2025`). The skin health business missed in China. Raw material costs and currencies move margins. A holder of several hundred stocks sees each of these wash out against other companies' luck, so the model is right to leave them out of the discount rate. They belong in the cash flows. The holders are exactly that kind of investor: 2,356 institutions, led by index funds (`facts.holders-capital-iq`, `governance.marginal_investor`). One risk does not wash out, and the model prices it separately: about two-thirds of sales are outside the United States and 45% are in emerging markets (`country.exposures`), including Argentina, Nigeria and Türkiye, which the 10-K calls hyper-inflationary (`facts.geographic-risk-notes`). That goes into the equity risk premium in lesson 7, not into beta.

- **Lesson 04, Session 4 · Part 2 — "Climbing the Risk Ladder — From Firm-Specific Risk to the Market Portfolio"** ([transcript](../../01-foundations-and-discount-rates/lesson-04/session-4-part-2.md))
    - Quote: "Beta is not a measure of total risk."
    - Question for Colgate-Palmolive: Which of Colgate-Palmolive's recent shocks were firm-specific and which were market-wide? If the marginal investor is not diversified, does a market beta understate the risk they actually bear?
    - Sources needed: Shock history; Colgate and index returns in the months the market moved; regression R-squared.
    - Where to find: ledger `beta.regression_r2`, `facts.regression-diagnostics`, `facts.shareholder-return-2020-2025`, `facts.sp500-november-2026`, `facts.writedowns-2021-2025`; `module-1-cross-checks-output.md` §1.
    - Answer: Firm-specific: the three write-downs, the ERISA settlement, the 2024 downgrade, the fall in volume. Market-wide: the 2022 sell-off and the fall in November 2026, and in both Colgate barely took part. In 2022 the index lost 18.1% and Colgate lost 5.4%; in the first twenty days of November 2026 the index fell 8.8% and Colgate rose 3.6% (`facts.shareholder-return-2020-2025`, `facts.sp500-november-2026`). The regression puts a number on it: the market explains 6.4% of the movement in Colgate's monthly returns (`beta.regression_r2`), so about 94% is the company's own. And Colgate is not a quiet stock. Its monthly returns have been 1.24 times as volatile as the index's (`facts.regression-diagnostics`). It is a stock with a lot of risk, most of which a diversified holder does not bear. For an undiversified holder a market beta would understate the risk badly. That holder is not who sets Colgate's price, so the market beta stands (lesson 11 sizes the difference).

- **Lesson 04, Session 4 · Part 3 — "Proxy Models and the Weakness of Beta — Does the CAPM Actually Work?"** ([transcript](../../01-foundations-and-discount-rates/lesson-04/session-4-part-3.md))
    - Quote: "The actual number is well below 10%."
    - Question for Colgate-Palmolive: Would a proxy-based cost of equity (using Colgate-Palmolive's size and price-to-book) give a materially different number than the CAPM estimate, and if so, which is more defensible for this company?
    - Sources needed: Market value and book value of equity; the CAPM cost of equity.
    - Where to find: ledger `company.equity_value`, `company.equity_book`, `modeling_choices.firm_size_table`; model-output.md §1 and §7.
    - Answer: Not computed, and for Colgate it could not be done sensibly. A proxy model reads risk off size and the ratio of price to book value. The course's coefficients are not in the ledger, so any number would be invented. The inputs also break the method. Size points to low risk: equity is worth $78,466.6M (`company.equity_value`). Price to book is 1,453 times (model-output.md §7), because buybacks have reduced book equity to $54M (`company.equity_book`). A ratio like that carries no information about risk; it records an accounting history. The CAPM estimate of 8.76% (model-output.md §1) is the defensible one here, and its weak point is the beta that goes into it, which lessons 8 to 10 deal with.

## Module 1 Step — Questions for This Lesson

- **Share classes and the marginal investor**
  - How many classes of shares exist and what are the voting rights of each? One class of common stock, one vote a share (`governance.share_classes`). Shares outstanding: 794.9M (`company.shares_basic`).
  - Who are the largest shareholders? Vanguard 10.26%, BlackRock 8.18%, State Street 5.95% from the proxy (`governance.controlling_holders`). Capital IQ, as of 2026-09-30, shows BlackRock 8.80%, two Vanguard entities at 7.13% and 4.40%, State Street 5.86% and T. Rowe Price 3.38% (`facts.holders-capital-iq`). The two sources differ in date and in how they group funds.
  - Is the marginal investor an individual or an institution? An institution. Institutions hold 87.19% of the shares and insiders 0.13% (`facts.institutional-ownership`).
  - Is that marginal investor diversified? Yes. The three largest are index-fund managers and no holder has a controlling stake (`governance.marginal_investor`).

## Notes

The marginal investor is a diversified institution, so only market risk is priced and beta is the right kind of measure. This is the firmest conclusion in Module 1: the ownership data is disclosed and points one way. What it leaves open is which beta. Colgate's own history says its market risk is very low (R-squared of 0.064); lessons 8 to 10 explain why the valuation does not take that at face value.
