---
title: "SolarWinds (SWI) — Lesson 36: Final Thoughts"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 36: Final Thoughts

### Lesson 36 — Final Thoughts

- **Lesson 36, Session 36 · Part 1 — "Ten Lessons Revisited: Governance, Risk, and the Marginal Investor"** ([transcript](../../04-dividends-and-valuation/lesson-36/session-36-part-1.md))
    - Quote: "Not everyone will agree on every decision being the best decision from their interests."
    - Question for SolarWinds: Across stockholders, lenders, managers and society, whose interests have driven SolarWinds' biggest decisions in the years in the ledger, and where is the sharpest conflict? Does the governance work in the earlier lessons answer this, or leave it open?
    - Sources needed: Ownership and board; the covenants; the sale process and adviser disclosures; executive payouts; the history of dividends and debt.
    - Where to find: `governance.*`, `debt.covenants`, `company.history`; `sources/deal-docs/swi-defm14c-2025-merger.md` (Background of the Merger, opinions of Goldman Sachs and Jefferies); `sources/filings/swi-10k-fy2023.md` and `swi-10k-fy2024.md`.
    - Answer: Stockholders drove the big decisions, and the stockholders who mattered were the two sponsors. The sharpest conflict is inside the stockholder group: the sponsors, who control, against the public holders, who do not.
        - Stockholders. Silver Lake (36.56%) and Thoma Bravo (29.79%) held 66.35% at the 2024 proxy, with the public float about 34% (`governance.controlling_holders`, `governance.marginal_investor`). Decisions in the ledger years: the 2021 N-able spin-off and a $1.50 special dividend of $237.2M (`facts.special-dividend-2021`); the 2022 repayment of $664.4M of debt (`company.history`); the $1.00 special dividend of $168.2M in April 2024; and the February 2025 sale at $18.50. Each returned cash or value to holders, led by the largest.
        - Sale process. The sponsors' written consent, holding about 65% of votes, approved the merger the day it was signed, so no vote was held (`facts.sponsor-voting-power-2025-02`). Public holders had appraisal rights, and the board could still take a better bid until 2025-03-09 (`facts.window-shop-end`). Three directors on the board are Silver Lake designees (`governance.board`), and one, Michael Widmann, sat on the three-person committee that ran the process (deal document, Background of the Merger). NYSE rules count him as independent; Silver Lake was a seller.
        - Advisers. Goldman Sachs's $42M fee depends on the deal closing (`facts.adviser-fees-and-conflicts`). Jefferies' fee is $6.25M and it was paid about $39M over two years by Silver Lake and Thoma Bravo and their portfolio companies. Both advisers had paid relationships with the sellers' firms.
        - Lenders. The credit agreement restricts dividends, and a change of control is an event of default (`debt.covenants`). The sale therefore repaid the lenders. Their interest did not drive it.
        - Managers. Three executives were due $38.96M on a change of control, the CEO $22.99M, most of it accelerated equity (`governance.change_of_control_payouts`). They also wrote the forecast the banks used.
        - Society and customers. The SUNBURST attack (2020) fell on customers; the filings give no measure of any cost that fell on them, and no decision in the ledger turns on it.
        - Does earlier governance work answer it? In part. The ownership table and consent rights show who decides. What stays open is whether $18.50 was the best price available. The 2023 market check approached 13 parties and ended with no bid; the highest indication on record is Party A's $13.00, revised down from about $14.00 (`facts.market-check-2023`). No rival bid appears after signing, and the merger closed on 2025-04-16 (`sources/deal-docs/swi-8k-2025-04-16-merger-closing.md`).

- **Lesson 36, Session 36 · Part 2 — "The Trade-Off on Debt and the Three First Principles of Corporate Finance"** ([transcript](../../04-dividends-and-valuation/lesson-36/session-36-part-2.md))
    - Quote: "If you cannot find investments that make your hurdle rate, find a way to get the cash back to your stockholders."
    - Question for SolarWinds: Tie the three first principles together: did its return on capital clear its cost of capital, was its capital structure near the optimum, and did its payout follow from the first two answers? What one-paragraph narrative explains the company as it is run today?
    - Sources needed: Return on invested capital by year, the cost of capital, the optimal debt ratio, free cash flow to equity against cash returned.
    - Where to find: `company.history`, `company.invested_capital`, `company.debt_total`, `company.equity_value`; model-output.md §1, §3, §5.
    - Answer: Investment: no. Financing: no. Payout: it fit the first answer and contradicted the second.
        - Investment. After-tax return on book invested capital was about 6.7% in 2024 and 4.8% in 2023 (EBIT × (1 − 25%) ÷ invested capital: $156.3M ÷ $2,348.0M for 2024, my arithmetic from `company.history`); 2022 was 2.69% once the $906.4M of non-cash impairments is taken out (§8). The cost of capital is 10.23% (model-output.md §1). Book capital includes $2,363.2M of buyout goodwill (`company.goodwill`), so the book return understates the business's own return, but the plan's 10% stable return is itself only equal to the cost of capital.
        - Financing. Debt is $1,285.0M, 33.03% of $3,889.9M of firm value; the optimum is 21% under EBIT coverage, 26% or 28% under looser numerators (model-output.md §3). The model's synthetic rating is B- at 1.85x coverage (§2). Moving to 21% is worth $0.52 a share on the DCF measure and up to $1.28 on adjusted present value (lesson 34; §6, §9).
        - Payout. With returns below cost of capital, the lecture says return the cash, and the sponsors did. But debt above the optimum says repay debt first. In 2024 the company returned $194.7M against free cash flow to equity of $127.0M, $67.7M more than it generated (model-output.md §5).
        - Narrative: see the project question below.

## Cumulative Project — Questions for This Lesson

- **What is the narrative that you would use to describe your company, as its run today?**
  SolarWinds sells IT monitoring software that customers rarely leave: $796.9M of revenue (2024), a 26.2% EBIT margin, subscription retention of 97% to 99%, growing about 5% a year. Two private-equity firms bought it in 2016, listed it in 2018 and still held 66.35% in 2024. The buyout left $2,363.2M of goodwill, so its book return on capital is about 6.7% against a 10.23% cost of capital, and it carries debt of 33% of capital against an optimum of 21%. Under that control it did what its owners could do with a business that does not need much reinvestment: it spun off N-able, repaid debt, paid two special dividends and, in February 2025, agreed to sell for $18.50 a share in cash to Turn/River Capital. Management's plan for the sale more than doubles EBIT by 2030 ($511M against $208.4M) and treats its cash flow as growing forever without reinvestment. Our DCF does not accept that, and values the shares at $13.00.

### Final deal assessment: $13.00 against $15.18 and $18.50

- Our course-method DCF is $13.00 a share, 0.86x the $15.18 unaffected price and 0.70x the $18.50 deal price (model-output.md §6). The deal premium over the unaffected price is $3.32, or 22% (`facts.premium-over-unaffected`).
- What sits between $13.00 and $18.50 is mostly one assumption. Growing management's 2030 cash flow forever ($5,552.5M of terminal value) instead of reinvesting 25% of after-tax EBIT ($3,808.9M) is worth about $5.67 a share, which would put the DCF at $18.67 (§6, "value per share with the other terminal value"). The deal price is therefore what the plan is worth if SolarWinds can grow without reinvesting.
- The banks' ranges bracket $18.50: Goldman Sachs $14.30 to $23.70 and Jefferies $14.70 to $19.70 on DCF (`facts.gs-dcf-range`, `facts.jefferies-dcf-range`). Jefferies grows terminal-year cash flow at 2.5% to 3.5%, the same method.
- On multiples, the peer-median EV / EBITDA of 16.39x gives $19.95 and the peer-median EV / revenue of 3.32x gives $8.34 (model-output.md §7; both subtract the $187.0M equity claim). The deal's enterprise value is $4,200.3M (my arithmetic: $18.50 × 171.6M + $1,285.0M − $259.3M, basic shares, before the equity claim), 14.85x standardized EBITDA of $282.8M against the 16.39x median, and 5.27x revenue against 3.32x.
- Value of control from the financing lever is $0.52 a share on the DCF measure (lesson 34; the other two measures are $0.84 and $1.28, on different bases, §6, §9). The premium is not explained by better management. It is explained by price paid for the plan's cash flows and by the buyer's financing: $2,750M of term debt (`facts.new-debt-2025`).
- Verdict. For a public holder, $18.50 was a good price: above our $13.00, above every price in the unaffected record (the $15.18 close was the 52-week high, `facts.unaffected-price-record`), and above the highest 2023 indication, $13.00 (revised down from about $14.00). It is inside both banks' ranges. The case for holding out is a belief in management's 2030 cash flows, and that depends on how much reinvestment growth needs after 2030. We do not hold that belief. What the process leaves open is whether another buyer would have paid more; the sources show the sponsors, who controlled the vote, were also the sellers.

## Notes

This closes the cumulative project. The three principles applied to SolarWinds: investment returns below the cost of capital, a debt ratio above the optimum, and a payout that matched the first fact but not the second. The valuation, $13.00, rests on the choice to reinvest in the terminal year; moving that one assumption reproduces the deal price. That is the finding to carry into the report. Open items: no rival bid is recorded after signing in the compiled sources, which is not proof that none was possible; the $2,750M term debt is a commitment, not final terms; the model prints the value per share under the FCFF-growth terminal value ($18.67, §6).
