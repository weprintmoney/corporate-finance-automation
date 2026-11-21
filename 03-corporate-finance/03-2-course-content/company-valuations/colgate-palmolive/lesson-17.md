---
title: "Colgate-Palmolive (CL) — Lesson 17: The Trade Off"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 17: The Trade Off

### Lesson 17 — The Trade Off

- **Lesson 17, Session 17 · Part 1 — "Debt vs. Equity and the Corporate Life Cycle"** ([transcript](../../02-investment-returns-and-financing/lesson-17/session-17-part-1.md))
    - Quote: "One of the most common problems among corporations is corporations that refuse to act their age."
    - Question for Colgate-Palmolive: Does Colgate-Palmolive's leverage fit its life-cycle stage, or is it a legacy of past ownership (a buyout, a founder's aversion to debt, a family tradition)? How has the debt ratio moved over the years in the ledger, and does the trend match the company's age?
    - Sources needed: Debt and market value of equity over several years; ownership history.
    - Where to find: ledger `company.history`, `company.debt_total`, `company.equity_value`, `facts.debt-ratio-history`, `facts.ciq-return-on-capital`, `governance.marginal_investor`; modules-2-4-cross-checks-output.md §5.
    - Answer: Colgate is a mature company (lesson 1): sales growing about 3% a year, large and steady cash flows, little need to reinvest. The life-cycle view says such a company should carry meaningful debt, because it has the earnings to use the tax deduction and the stability to service the interest. Colgate carries 9.34% (model-output.md §1). In its payout it acts its age, returning all the cash it generates. In its borrowing it does not.
      The ratio has not moved toward a higher level (`facts.debt-ratio-history`):

        | Year end | Debt with leases $M | Market value of equity $M | Debt ratio |
        |---|---|---|---|
        | 2020 | 8,205 | 72,674 | 10.14% |
        | 2021 | 7,821 | 71,727 | 9.83% |
        | 2022 | 9,257 | 65,412 | 12.40% |
        | 2023 | 9,064 | 65,475 | 12.16% |
        | 2024 | 8,512 | 73,871 | 10.33% |
        | 2025 | 8,554 | 63,314 | 11.90% |
        | 2026-11-20 | 8,084 | 78,467 | 9.34% |

      Debt has stayed between about $7.8 billion and $9.3 billion for six years. The ratio moves between 10% and 12% mainly because the share price moves. (The year-end rows use debt at carrying value; the last row uses fair value, as the ledger does.) Capital IQ's debt to EBITDA tells the same story: 1.7 to 2.2 times throughout (`facts.ciq-return-on-capital`).
      It is not a legacy of ownership. There is no founder, family or buyout sponsor; the largest holders are index funds (`governance.marginal_investor`). The 10-K calls its approach "prudent management of our capital structure" (`facts.capital-structure-statements`), and says nothing of a target ratio. Our reading, as inference: the low ratio is a management preference for a high credit rating and steady access to commercial paper, not a constraint anyone imposed.

- **Lesson 17, Session 17 · Part 2 — "The Trade-Off on Debt: Tax Benefits, Discipline, Bankruptcy and Agency Costs"** ([transcript](../../02-investment-returns-and-financing/lesson-17/session-17-part-2.md))
    - Quote: "The biggest plus of using debt is the tax code rewards you for borrowing money."
    - Question for Colgate-Palmolive: For Colgate-Palmolive, how large are the tax benefit and the discipline benefit of debt against the bankruptcy, agency and flexibility costs? Judged qualitatively from the trade-off alone, does the company carry too much or too little debt?
    - Sources needed: Tax rates, interest, operating income and its stability, ownership by managers, acquisition record, covenants, unused credit.
    - Where to find: ledger `market.tax_rate_marginal`, `market.tax_rate_effective`, `company.debt_total`, `debt.covenants`, `debt.revolver_undrawn`, `company.goodwill`, `company.rd_expense`, `facts.debt-trade-off-sizes`, `facts.operating-income-stability`, `facts.insiders-pct-proxy`, `facts.acquisitions-2018-2025`; model-output.md §2 and §8.
    - Answer: Item by item.

        | Factor | Colgate's position | Points toward |
        |---|---|---|
        | Tax benefit | Marginal rate 25%; effective rate 23.5%, so it pays close to the full rate and can use every deduction. Today's debt saves $66.8M of tax a year, 2.1% of after-tax operating income, or $2,021M as a perpetuity, 2.34% of firm value (`facts.debt-trade-off-sizes`) | More debt: the benefit is real and barely used |
        | Discipline | Directors and officers own 0.43% (`facts.insiders-pct-proxy`). Free cash flow to the firm is $3,578.8M. $3,894M went to acquisitions from 2018 to 2025 and write-downs over the same years were 57% of that (`facts.acquisitions-2018-2025`) | More debt: managers with spare cash and little of their own money at stake have spent it badly at least once |
        | Bankruptcy cost | Low probability: operating income covers interest 15.82 times, and its largest one-year fall since 2016 was 7.4% (`facts.operating-income-stability`). Low cost if it happened: people keep buying toothpaste from a company in trouble | More debt |
        | Agency cost | Lenders worry when a borrower can switch to riskier projects unseen. Colgate's business is stable and easy to follow, and it borrows at an A+ rating with covenants only on its bank lines (`debt.covenants`) | More debt |
        | Flexibility | Investment needs are small and predictable (capital spending $564M). $3,641M of credit lines are unused (`debt.revolver_undrawn`) | More debt: little need to hold capacity in reserve |

      Every factor points the same way. Qualitatively, Colgate has too little debt. The two cautions are the ones a number has to settle (lessons 18 to 20): its assets are brands, which cannot be pledged or sold piecemeal the way a factory can, and about 45% of sales come from emerging markets, where a currency or political shock can cut dollar earnings.

## Cumulative Project — Questions for This Lesson

- **What are the different kinds or types of financing that this company has used to raise funds? Where do they fall in the continuum between debt and equity?**
  Colgate uses plain instruments at the two ends of the continuum and nothing in between (`facts.financing-types-2025`, `facts.debt-detail-2025`).
    - Pure debt: fixed-rate senior notes and medium-term notes in dollars and euros, $7,767M at an average rate of 2.9%, maturing from 2026 to 2078; a smaller amount of floating-rate notes; commercial paper ($147M at year end, but an average daily balance of $1,611M during 2025, so it is used more than the year-end figure shows); a $3,000M revolving credit facility, undrawn.
    - Debt by the course's test: operating leases of $566M and finance leases of $72M.
    - Pure equity: one class of common stock, one vote per share. Employee stock options and restricted units are claims on equity (`company.options_value`).
    - Hybrids: none. The word "convertible" does not appear in the 10-K. The company has authority to issue preference stock; the balance sheet in our files shows none used for financing.
  A company uses convertibles or preferred stock when straight debt is expensive or its cash flows are too uncertain for fixed payments. Colgate has neither problem, so plain debt is the right tool.

- **How large, in qualitative or quantitative terms, are the advantages to this company from using debt? How large, in qualitative or quantitative terms, are the disadvantages to this company from using debt? From the qualitative trade off, does this firm look like it has too much or too little debt?**
  Advantages: a tax saving worth $2,021M today on $8,084M of debt, which would be $6,491M on debt of $25,965M at a 30% ratio (`facts.debt-trade-off-sizes`); and discipline on a management team that owns 0.43% of the shares and has written down more than half of what it spent on acquisitions since 2018. Disadvantages: an expected bankruptcy cost that is small because earnings are steady and the product is a staple; agency costs that are small because lenders already lend to Colgate on A+ terms; and a loss of flexibility that matters little because Colgate's investment needs are small. From the trade-off alone, too little debt. How much more is the subject of lessons 18 to 21; whether to act on it, of lesson 22.

## Notes

The qualitative answer is that Colgate is under-borrowed, and has been at about the same level for six years. Confidence in the direction is high: all five factors agree, and none rests on an estimate. This lesson does not say how much more debt; the trade-off table cannot. It also flags the two facts that should make the quantitative answer cautious: brand assets and emerging-market earnings.

One point of language for later lessons. On its balance sheet Colgate looks almost entirely debt-financed (book debt 99.37% of book capital, lesson 13). That is an effect of buybacks on book equity. At market value it is among the less indebted companies in its industry (lesson 21).
