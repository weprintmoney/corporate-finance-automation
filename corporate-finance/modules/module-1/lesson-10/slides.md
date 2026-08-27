## Session 10: Bottom-Up Betas

*If you cannot find comparable companies, it is because you have not looked hard enough.*

*Aswath Damodaran*

---

## Betas Are Weighted Averages

- The beta of a portfolio is always the market-value weighted average of the betas of the individual investments in that portfolio.
- Thus:
  - The beta of a mutual fund is the weighted average of the betas of the stocks and other investments in that portfolio.
  - The beta of a firm after a merger is the market-value weighted average of the betas of the companies involved in the merger.

---

## Bottom-Up Versus Top-Down Beta

- The top-down beta for a firm comes from a regression.
- The bottom-up beta can be estimated by doing the following:
  - Find out the businesses that a firm operates in.
  - Find the unlevered betas of other firms in these businesses.
  - Take a weighted (by sales or operating income) average of these unlevered betas.
  - Lever up using the firm's debt/equity ratio.
- The bottom-up beta is a better estimate than the top-down beta for the following reasons:
  - The standard error of the beta estimate will be much lower.
  - The betas can reflect the current (and even expected future) mix of businesses that the firm is in, rather than the historical mix.

---

## Disney's Businesses: The Financial Breakdown (from 2013 Annual Report)

*(diagram)*

---

## Unlevered Betas for Businesses

| Business | Comparable Firms | Sample Size | Median Beta | Median D/E | Tax Rate | Company Unlevered Beta | Cash/Firm Value | Business Unlevered Beta |
|----------|-----------------|-------------|-------------|------------|----------|------------------------|-----------------|-------------------------|
| Media Networks | US firms in broadcasting | 26 | 1.43 | 71.09% | 40.00% | 1.0024 | 2.80% | 1.0313 |
| Parks & Resorts | Global firms in amusement park business | 20 | 0.87 | 46.76% | 35.67% | 0.6677 | 4.95% | 0.7024 |
| Studio Entertainment | US movie firms | 10 | 1.24 | 27.06% | 40.00% | 1.0668 | 2.96% | 1.0993 |
| Consumer Products | Global firms in toys/games production and retail | 44 | 0.74 | 29.53% | 25.00% | 0.6034 | 10.64% | 0.6752 |
| Interactive | Global computer gaming firms | 33 | 1.03 | 3.26% | 34.55% | 1.0085 | 17.25% | 1.2187 |

---

## A Closer Look at the Process: Studio Entertainment Betas

| Company Name | Levered Beta | Market Cap | Total Debt | Firm Value | Cash | Cash/Firm Value | Enterprise Value | Marginal Tax Rate | Gross D/E Ratio | Unlevered Beta | Pure Play Beta | EV/Sales |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SFX Entertainment | 1.12 | 728.80 | $98.89 | $837.69 | $143.60 | 17.14% | $694.09 | 40.00% | 13.39% | 1.04 | 0.58 | 3.21 |
| Mass Hysteria Entertainment | 1.19 | $3.97 | $1.13 | $3.18 | $0.34 | 0.00% | $1.37 | 40.00% | 477.94% | 0.031 | 0.89 | — |
| Medient Studios | 0.93 | $1.37 | $6.39 | $4.31 | $0.05 | 0.81% | $6.34 | 40.00% | 99.07% | — | 1.26 | — |
| POW! Entertainment | 0.94 | $0.43 | $3.89 | $9.85 | — | — | — | 40.00% | 8.65% | — | 1.03 | — |
| MGM Holdings | 1.29 | 3,631.70 | $142.16 | $3,773.86 | $140.70 | 3.73% | $3,633.16 | 40.00% | 3.91% | — | 1.23 | — |
| Lions Gate Entertainment | 1.20 | 4,719.60 | $1,283.20 | $6,002.80 | $67.20 | 1.12% | $5,935.60 | 40.00% | 27.19% | — | 1.10 | — |
| DreamWorks Animation | 1.32 | 2,730.00 | $348.30 | $3,078.30 | $156.40 | 5.08% | $2,921.90 | 40.00% | 12.76% | — | 1.25 | — |
| Twenty-First Century Fox | 1.28 | 77,743.50 | $20,943.00 | $98,686.50 | $6,681.00 | 6.77% | $92,005.50 | 40.00% | 26.94% | — | 1.10 | — |
| Independent Film Development | 1.32 | $2.28 | $0.30 | — | — | — | — | 40.00% | 72.35% | — | 0.60 | — |
| Odyssey Pictures Corp | 0.30 | $0.96 | $1.12 | $0.05 | $0.00 | 0.10% | $1.94 | 40.00% | 551.12% | 0.031 | 0.97 | — |
| **Average** | 1.61 | — | — | — | — | 2.20% | — | 40.00% | 129.33% | 0.92 | 1.25 | — |
| **Aggregate** | 2.60 | $89,572.64 | $22,822.82 | $112,395.45 | $7,189.43 | 6.40% | $105,206.02 | 40.00% | 25.48% | 1.24 | 1.10 | — |
| **Median** | 1.35 | — | — | — | — | 2.96% | — | 40.00% | 27.06% | 1.17 | 1.03 | — |

---

## Backing Into a Pure Play Beta: Studio Entertainment

| Component | Weight | Beta |
|-----------|--------|------|
| Movie Business | 97.04% | Beta (movies) = 1.0093 |
| Cash Business | 2.96% | Beta (cash) = 0.0000 |
| Debt | 21.30% | Beta (debt) = 0 |
| Equity | 78.70% | Beta (equity) = 1.24 |
| **Movie Company** | **100.0%** | **Beta (company) = 1.0668** |

1. Start with the median regression beta (equity beta) of 1.24.
2. Unlever the beta, using the median gross D/E ratio of 27.06%:
   - Gross D/E Ratio = 21.30 / 78.70 = 27.06%
3. Take out the cash effect, using the median cash/value of 2.96%:
   - `(0.0296)(0) + (1 − 0.0296)(Beta of movie business) = 1.0668`
   - `Beta of movie business = 1.0668 / (1 − 0.0296) = 1.0993`
   - Alternatively, using the net debt-to-equity ratio:
     - Net D/E ratio = (21.30 − 2.96) / 78.70 = 23.30%
     - `Unlevered beta for movies = 1.24 / [1 + (1 − 0.4)(0.233)] = 1.0879`

---

## Disney's Unlevered Beta: Operations and Entire Company

| Business | Revenues | EV/Sales | Value of Business | Proportion of Disney | Unlevered Beta |
|----------|----------|----------|-------------------|----------------------|----------------|
| Media Networks | $20,356 | 3.27 | $66,580 | 49.27% | 1.0313 |
| Parks & Resorts | $14,087 | 3.24 | $45,683 | 33.81% | 0.7024 |
| Studio Entertainment | $5,979 | 3.05 | $18,234 | 13.49% | 1.0993 |
| Consumer Products | $3,555 | 0.83 | $2,952 | 2.18% | 0.6752 |
| Interactive | $1,064 | 1.58 | $1,684 | 1.25% | 1.2187 |
| **Disney Operations** | **$45,041** | — | **$135,132** | **100.00%** | **0.9239** |

Disney has $3.93 billion in cash, invested in close to riskless assets (with a beta of zero). You can compute an unlevered beta for Disney as a company (inclusive of cash).

---

## The Levered Beta: Disney and Its Divisions

To estimate the debt ratios for each division, we allocate Disney's total debt ($15,961 million) based on identifiable assets:

| Business | Identifiable Assets (2013) | Proportion of Debt | Value of Business | Allocated Debt | Estimated Equity | D/E Ratio |
|----------|--------------------------|-------------------|-------------------|----------------|------------------|-----------|
| Media Networks | $28,627 | 38.04% | $66,580 | $6,072 | $60,508 | 10.03% |
| Parks & Resorts | $22,056 | 29.31% | $45,683 | $4,678 | $41,005 | 11.41% |
| Studio Entertainment | $14,750 | 19.60% | $18,234 | $3,129 | $3,129 | 20.71% |
| Consumer Products | $7,506 | 9.97% | $2,952 | $1,592 | $1,359 | 117.11% |
| Interactive | $2,311 | 3.07% | $1,684 | $490 | $1,194 | 41.07% |
| **Disney** | **$75,250** | **100.00%** | **$121,878** | **$15,961** | — | **13.10%** |

We use the allocated debt to compute D/E ratios and levered betas:

| Business | Unlevered Beta | Value of Business | D/E Ratio | Levered Beta | Cost of Equity |
|----------|---------------|-------------------|-----------|--------------|----------------|
| Media Networks | 1.0313 | $66,580 | 10.03% | 1.0975 | 9.07% |
| Parks & Resorts | 0.7024 | $45,683 | 11.41% | 0.7537 | 7.09% |
| Studio Entertainment | 1.0993 | $18,234 | 20.71% | 1.2448 | 9.92% |
| Consumer Products | 0.6752 | $2,952 | 117.11% | 1.1805 | 9.55% |
| Interactive | 1.2187 | $1,684 | 41.07% | 1.5385 | 11.61% |
| **Disney** | **0.9239** | **$135,132** | **13.10%** | **1.0012** | **8.52%** |

---

## Discussion Issue

- Assume now that you are the CFO of Disney. The head of the movie business has come to you with a new big-budget movie that he would like you to fund. He claims that his analysis of the movie indicates that it will generate a return on equity of 9.5%. Would you fund it?
  - a. Yes. It is higher than the cost of equity for Disney as a company.
  - b. No. It is lower than the cost of equity for the movie business.
- What are the broader implications of your choice?

---

## Task & Reading

- Task: Estimate a bottom-up beta for your company.
- Optional: Read Chapter 4
