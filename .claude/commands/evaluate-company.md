# /evaluate-company

Guide the user through a 12-step corporate finance company valuation based on Module 1 of the Applied Corporate Finance course. Each step studies the relevant lesson from this repo, then researches the user's chosen company and appends findings to a running valuation report.

## Setup

Before starting, determine the output path for the report:
- Report file: `corporate-finance/modules/company-valuations/<company-slug>-valuation.md`
- Create the `company-valuations/` directory if it doesn't exist

---

## Step 1 — Pick a company

Read and internalize:
- `corporate-finance/modules/module-1/lesson-01/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-01/slides.md`

Then ask the user: **"Pick a company to value."**

Wait for the user's answer before proceeding. Once they give a company name:
- Set `<COMPANY>` as the company name used throughout all remaining steps
- Set `<SLUG>` as the kebab-case version of the company name (e.g. "Apple Inc." → `apple`)
- Create the report file at `corporate-finance/modules/company-valuations/<SLUG>-valuation.md` with this header:

```markdown
# Company Valuation: <COMPANY>
*Applied Corporate Finance — Module 1 Analysis*

---
```

Confirm to the user which company you'll be evaluating and that the report file has been created. Then proceed automatically through all remaining steps without pausing unless you need the user to clarify something.

---

## Step 2 — Corporate Governance

Read and internalize:
- `corporate-finance/modules/module-1/lesson-02/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-02/slides.md`
- `corporate-finance/modules/module-1/lesson-02/blog-alibaba-governance.md`
- `corporate-finance/modules/module-1/lesson-02/blog-family-companies-4c-tradeoff.md`

Research `<COMPANY>` using web search and any available tools. Answer:
1. Who sits on the board of directors?
2. Whose interests are they most likely to serve?
3. If there is a measure of corporate governance strength, what does it reveal about where power lies — shareholders, managers, inside shareholders, or some other entity?

Append to the report:

```markdown
## Step 2 — Corporate Governance

### Board of Directors
...

### Governance Assessment
...

### Power Structure
...
```

---

## Step 3 — Stated Objectives

Read and internalize:
- `corporate-finance/modules/module-1/lesson-03/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-03/slides.md`
- `corporate-finance/modules/module-1/lesson-03/blog-jan-2016-data-update-5-corporate-governance.md`

Research `<COMPANY>`. Answer:
1. If the firm has stated goals or objectives, what is it targeting — growth, higher profitability, higher stock price, or higher value?
2. If there are no stated goals, what does the company's behavior suggest is the primary focus?

Append to the report:

```markdown
## Step 3 — Stated Objectives

### Stated Goals
...

### Inferred Focus (if no stated goals)
...
```

---

## Step 4 — Share Classes and Marginal Investor

Read and internalize:
- `corporate-finance/modules/module-1/lesson-04/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-04/slides.md`
- `corporate-finance/modules/module-1/lesson-04/reading-modified-capm.md` (if present)
- `corporate-finance/modules/module-1/lesson-04/blog-how-much-diversification-is-too-much.md`

Research `<COMPANY>`. Answer:
1. How many classes of shares exist? What are the voting rights of each?
2. Who are the largest shareholders?
3. What type of investor — individual or institutional — is most likely to be the marginal investor?
4. Is that marginal investor likely to be diversified?

Append to the report:

```markdown
## Step 4 — Share Classes and Marginal Investor

### Share Structure
...

### Largest Shareholders
...

### Marginal Investor
...

### Likely Diversification of Marginal Investor
...
```

---

## Step 5 — Currency and Risk-Free Rate

Read and internalize:
- `corporate-finance/modules/module-1/lesson-05/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-05/slides.md`
- `corporate-finance/modules/module-1/lesson-05/blog-risk-free-rates-and-value-dealing-with-historically-low-risk-free-rates.md`
- `corporate-finance/modules/module-1/lesson-05/blog-negative-interest-rates.md`

Research `<COMPANY>`. Answer:
1. What currency does the company report its financial statements in?
2. What currencies does the company generate its revenues in?
3. What currency will you use for the analysis, and why?
4. What is the current risk-free rate in that currency?

Append to the report:

```markdown
## Step 5 — Currency and Risk-Free Rate

### Reporting Currency
...

### Revenue Currencies
...

### Analysis Currency and Rationale
...

### Risk-Free Rate
...
```

---

## Step 6 — Equity Risk Premium (Mature Market)

Read and internalize:
- `corporate-finance/modules/module-1/lesson-06/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-06/slides.md`
- `corporate-finance/modules/module-1/lesson-06/blog-an-erp-retrospective-looking-back-2014-and-looking-forward-2015.md`
- `corporate-finance/modules/module-1/lesson-06/blog-jan-2016-data-update-1-us-equity-markets.md`
- `corporate-finance/modules/module-1/lesson-06/blog-another-market-crisis-my-survival-manual-journal.md`

Research the current implied ERP for a mature market (US, as of today). Cite your source and method (implied vs. historical). Answer:
1. What is the equity risk premium for a mature market today?

Append to the report:

```markdown
## Step 6 — Equity Risk Premium (Mature Market)

### Current Mature Market ERP
...

### Method and Source
...
```

---

## Step 7 — Country Risk Exposure and Weighted ERP

Read and internalize:
- `corporate-finance/modules/module-1/lesson-07/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-07/slides.md`
- `corporate-finance/modules/module-1/lesson-07/blog-january-2017-data-update-4-country-risk-update.md`
- `corporate-finance/modules/module-1/lesson-07/blog-dark-side-of-globalization-country-risk.md`
- `corporate-finance/modules/module-1/lesson-07/reading-country-risk-2017.md` (if present)

Research `<COMPANY>`. Answer:
1. What is the best measure of country risk exposure for this company — revenues, production, reserves, or other?
2. What is the geographical breakdown of that measure?
3. Using country ERPs (from Damodaran's data or current sources), compute the weighted average ERP for the company.
4. Why might this ERP change in the future?

Append to the report:

```markdown
## Step 7 — Country Risk and Weighted ERP

### Best Measure of Country Exposure
...

### Geographic Breakdown
| Region/Country | % of [measure] | Country ERP |
|----------------|----------------|-------------|
| ...            | ...            | ...         |

### Weighted Average ERP
...

### Why ERP Might Change
...
```

---

## Step 8 — Regression Beta

Read and internalize:
- `corporate-finance/modules/module-1/lesson-08/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-08/slides.md`
- `corporate-finance/modules/module-1/lesson-08/blog-jan-2017-data-update-4-country-risk.md`
- `corporate-finance/modules/module-1/lesson-08/blog-dark-side-of-globalization-country-risk.md`

Research `<COMPANY>`. Find the regression (historical) beta for the company from a financial data source. Note the index used, the time period, and the R-squared. Assess whether the regression beta is reliable.

Append to the report:

```markdown
## Step 8 — Regression Beta

### Regression Beta
...

### Index, Time Period, R-squared
...

### Reliability Assessment
...
```

---

## Step 9 — Beta Fundamentals

Read and internalize:
- `corporate-finance/modules/module-1/lesson-09/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-09/slides.md`
- `corporate-finance/modules/module-1/lesson-09/slides-part2.md`

Research `<COMPANY>`. Answer:
1. Based on the products and services the firm sells, would you expect a high or low beta? Do different parts of the business have different betas?
2. Based on the cost structure (fixed vs. variable costs), what beta would you expect?
3. Given how much the firm has borrowed, what impact does financial leverage have on its beta?

Append to the report:

```markdown
## Step 9 — Beta Fundamentals

### Product/Service Beta Expectation
...

### Operating Leverage Effect
...

### Financial Leverage Effect
...
```

---

## Step 10 — Bottom-Up Unlevered Beta

Read and internalize:
- `corporate-finance/modules/module-1/lesson-10/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-10/slides.md`
- `corporate-finance/modules/module-1/lesson-10/spreadsheet-bottomup-beta.md` (for methodology reference)

Research `<COMPANY>` and Damodaran's industry beta data. Answer:
1. Estimate a bottom-up unlevered (business) beta for the company using comparable firms' average unlevered betas.
2. If the company is in multiple businesses, estimate the unlevered beta for each segment and the weighted average.

Show your work — list the comparable firms/industry group, the average unlevered beta, and any adjustments.

Append to the report:

```markdown
## Step 10 — Bottom-Up Unlevered Beta

### Business Segments (if applicable)
...

### Comparable Firms / Industry Group
| Segment | Industry | Avg Unlevered Beta | Weight |
|---------|----------|--------------------|--------|
| ...     | ...      | ...                | ...    |

### Estimated Unlevered Beta
...
```

---

## Step 11 — Total Beta and Levered Beta

Read and internalize:
- `corporate-finance/modules/module-1/lesson-11/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-11/slides.md`
- `corporate-finance/modules/module-1/lesson-11/spreadsheet-total-beta-calculator.md` (for methodology reference)

Using the unlevered beta from Step 10 and the company's current debt/equity ratio and marginal tax rate, answer:
1. What is the levered beta for this company (using the standard Hamada equation)?
2. What would the total beta be if all risk (not just market risk) were considered?
3. Compare levered beta vs. total beta — what does the difference imply?

Show calculations.

Append to the report:

```markdown
## Step 11 — Levered Beta and Total Beta

### Inputs
- Unlevered beta: ...
- Debt/Equity ratio: ...
- Marginal tax rate: ...

### Levered Beta (Hamada)
...

### Total Beta
...

### Interpretation
...
```

---

## Step 12 — Cost of Debt

Read and internalize:
- `corporate-finance/modules/module-1/lesson-12/lesson-overview.md`
- `corporate-finance/modules/module-1/lesson-12/slides.md`
- `corporate-finance/modules/module-1/lesson-12/reading-cost-of-capital.md`
- `corporate-finance/modules/module-1/lesson-12/reading-leases-debt-value.md`
- `corporate-finance/modules/module-1/lesson-12/spreadsheet-ratings.md` (for ratings → spread mapping)

Research `<COMPANY>`. Answer:
1. Does the company have a bond rating? If so, what is the default spread and pre-tax cost of debt?
2. Estimate a synthetic rating using interest coverage ratio. What is the implied default spread and cost of debt?
3. If the synthetic rating differs from the actual rating, what might explain the difference?
4. What is the market value of interest-bearing debt?
5. What is the debt value of lease commitments (capitalize operating leases)?
6. What marginal tax rate should be used in the after-tax cost of debt?

Show all calculations.

Append to the report — and add a final **Summary** section that pulls together the key cost-of-capital inputs computed across all steps:

```markdown
## Step 12 — Cost of Debt

### Bond Rating and Spread
...

### Synthetic Rating
| Metric | Value |
|--------|-------|
| EBIT   | ...   |
| Interest expense | ... |
| Interest coverage ratio | ... |
| Synthetic rating | ... |
| Default spread | ... |
| Pre-tax cost of debt | ... |

### Actual vs. Synthetic Rating — Differences and Explanation
...

### Market Value of Debt
...

### Lease Debt Capitalization
...

### Marginal Tax Rate
...

---

## Summary — Cost of Capital Inputs

| Input | Value |
|-------|-------|
| Risk-free rate | ... |
| Mature market ERP | ... |
| Weighted ERP (country-adjusted) | ... |
| Regression beta | ... |
| Unlevered beta | ... |
| Levered beta | ... |
| Cost of equity | ... |
| Pre-tax cost of debt | ... |
| After-tax cost of debt | ... |
| Debt/Capital ratio | ... |
| **WACC** | **...** |
```

---

## Final output

After Step 12, confirm to the user:
- The report file path
- Offer to commit it to the repo via the standard branch → PR → admin merge workflow
