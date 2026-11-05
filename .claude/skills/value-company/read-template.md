---
title: "Read template — the shape of read.md and the Discretionary Decision convention"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Read template

`read.md` is the main output of every `/value-company` run. It answers two questions about the company on the analysis date: **what situation is it in**, and **what are the people who control it actually trying to do**, whether or not they say so. The course's tools are how it gets there: every corporate finance choice (how much to borrow, what to invest in, how much cash to hand back) is a decision someone made, and decisions reveal goals better than statements do.

Length: two to three pages. A reader should get the read from the first page alone.

## Shape

```markdown
---
title: "<Company> — The read, as of <analysis date>"
status: draft
owner: weprintmoney
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---

# <Company> — The read, as of <analysis date>

<One sentence on what the company is and who controls it. Then the analysis date, and if the run is
blind, a line saying nothing published after that date was used.>

## The read

<Three to five sentences: the situation and the inferred goal, in plain words. This is the paragraph
someone forwards.>

## Signals

| Signal | What it says | What it does | Gap |
|---|---|---|---|
| Control | <stated> | <revealed, with the number> | <none / small / large> |
| ... one row per signal in seeds/signals.yaml that the data supports ... |

<Then one short paragraph per signal with a large gap: the evidence, cited to the ledger or
model-output.md, and the reasoning. Signals with no gap get no paragraph; the table row is enough.>

![Return on capital](exhibits/exhibit-returns.png)
![Cost of capital by debt ratio](exhibits/exhibit-cost-of-capital.png)

## Unstated goals

<Each one in this shape:>

**<The goal, as one sentence about what the controllers want.>** Confidence: high / medium / low.
- Evidence: <two or more signals that point here, each with its number>
- Would be wrong if: <the observable fact that would disprove it, and where it would show up>
- Rival reading: <the most plausible other explanation for the same evidence, and why it is weaker>

## What to watch

<Three to five dated or observable events that would confirm or overturn the read: a debt maturity, a
lock-up expiry, a sponsor's fund life, a proxy vote, a guidance revision, a covenant test.>

## Discretionary decisions

<Every ⚠️ block from the run, collected here as well as where it applies.>

## Sources

<Primary documents only, by name and date.>
```

## How to infer an unstated goal

1. **Start from the gaps, not from a story.** A goal is inferred only where a signal shows a gap between what the company says and what it does. No gap, no inference.
2. **Two signals or no claim.** One gap is a fact worth reporting; a goal needs at least two independent signals pointing the same way. Ownership plus payout is two; payout measured two ways is one.
3. **Name the rival reading.** Every gap has an innocent explanation (a one-time event, an accounting artifact, a deliberate strategy the company did explain). State the best one and say why the evidence favors the inferred goal over it. If it doesn't, drop the goal to low confidence or cut it.
4. **Confidence follows the evidence grade.** High: three or more signals, all from audited filings, rival reading ruled out by a specific fact. Medium: two signals, or a rival reading that remains possible. Low: one strong signal plus circumstantial evidence; say so plainly.
5. **Say who.** "The company wants" hides the answer. Name the controllers (founder, sponsor, board, management) from the control signal, and whose interest the inferred goal serves.
6. **Falsifiable, with a date.** "Would be wrong if" names something observable, ideally with a date: a maturity, a filing, a vote.

## Common patterns

Starting hypotheses, never conclusions. Each needs the two-signal rule and a rival reading before it goes in the read.

| Pattern in the signals | Hypothesis to test | Rival reading to rule out |
|---|---|---|
| Financial-sponsor control + debt above the optimum + payout above FCFE + change-of-control pay | The owners are harvesting and preparing an exit | A one-time recapitalization after an asset sale |
| Founder or family control + debt far below the optimum + cash piling up + low payout | Control and independence come before returns to outside shareholders | Saving for a known, disclosed investment |
| Return on capital below the cost of capital + steady acquisitions + growth targets in pay | Management is building size, not value | Acquisitions are recent and returns lag by design |
| Return on capital well above the cost of capital + low reinvestment + rising buybacks | The core business is ageing and management knows it | Disciplined capital return from a business with few projects |
| Debt design mismatched to the assets (short floating debt on long fixed assets) | The debt was set by a deal or a lender, not by the business | Cheapest available financing at the time, with a disclosed refinancing plan |
| Market price well above the value on management's own plan | The market is pricing an outcome (a sale, a turnaround) that the plan doesn't show | The plan is deliberately conservative |
| Market price well below value on the plan | The market doubts the plan, or the controllers' goals | The plan is promotional |
| Life-cycle stage mature, behaviour young (high reinvestment, no payout, growth narrative) | Management is refusing to act its age | A real new growth line the numbers don't yet show |

## ⚠️ Discretionary Decision

Every judgment call where a reasonable analyst could choose differently gets this block, placed where the choice is used and collected again at the end of the read. The course grades the logic behind each choice, not the number, and a reader of the read needs to know which conclusions rest on a choice.

```markdown
> ⚠️ **Discretionary Decision: <the choice, in a few words>**
> **Chose:** <what was used>. **Why:** <one or two sentences of reasoning, no mechanics>.
> **Alternative:** <the next-best choice> → <what it changes, as a number from model-output.md>.
> **Confidence:** high / medium / low, and what would raise it.
```

These choices always get a block, whether or not the default is used:

- Analysis date, and for a past date, why that date
- Beta: bottom-up or regression, and which industry or segments
- Cost of debt: the company's actual borrowing rate or the synthetic rating's rate
- Weights: market or book
- Which coverage measure sets the synthetic rating (EBIT, EBIT plus acquisition amortization, EBITDA)
- Treatment of R&D (expense or capitalized, and over how many years)
- Forecast source: management's plan, analyst consensus, or history, and the stress cases run against it
- Stable period: beta, debt ratio and return on new capital after the forecast years
- Terminal value method
- Bankruptcy cost in the adjusted present value
- Peer set, and which multiple is the one to price on
- Anything excluded from debt (deferred revenue, purchase commitments) or included (leases not yet started, guarantees)

Add a block for any other choice that moves value per share by more than 5% or flips a signal's gap.
