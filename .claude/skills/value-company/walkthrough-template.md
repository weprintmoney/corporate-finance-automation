---
title: "Walkthrough template — plain-language trail for a company valuation"
status: active
owner: weprintmoney
created: 2026-10-24
last_updated: 2026-10-24
---

# Walkthrough template

`walkthrough.md` tells the story of valuing one company from the first question to the final number, for a reader who has never studied finance. It is written one section at a time, as each step finishes. It is not a summary written afterward.

## File shape

```markdown
---
title: "<Company> — How this valuation was built"
status: active
owner: weprintmoney
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---

# <Company> — How this valuation was built

## How to read this

<Three or four sentences: what the document is, that every number in it comes from a named source
document or from the model, and that each section has the same six parts.>

## The valuation in ten sentences

<Written last. The whole story, start to finish, no jargon.>

## Where the numbers come from

<Plain description of each group of documents in sources/. "The company's annual reports filed with
the SEC for 2022 through 2024." "The annual reports of three competitors." "Interest rates from the
Federal Reserve's public database, fetched on 2026-10-24.">

## Step 1: <question in plain words>
...
## Step 36: <question in plain words>

## Corrections made along the way

<One line per correction: date, what was wrong, what it was changed to, which steps it touched.>

## Glossary

<Every term that needed defining, alphabetical, one or two sentences each.>
```

## The six parts of every step section

Same order every time. Use these exact italic labels.

1. *What we wanted to know.* The question, in plain words. One or two sentences.
2. *Why it matters.* What changes in the final answer if this is wrong. One or two sentences.
3. *What we did.* The logic. If there is a formula, show it, then show it again with this company's numbers in it. If there is a judgment call, say so and name the options.
4. *The numbers and where they came from.* Each figure with the document named the way a person would name it, then the file. Example: "The 2024 annual report (Form 10-K) filed with the SEC on 2025-02-19, note 9 on debt. File: `sources/sec-filings/swi-10k-fy2024.md`."
5. *What we decided, and what we didn't.* The chosen number or conclusion. For judgment calls: the alternatives and why they lost. For arithmetic: say it is arithmetic.
6. *How sure we are.* Disclosed vs. estimated. What would change the answer.

## Plain-language rules

- Define a term the first time it appears, in the sentence where it appears. Add it to the glossary.
- Spell out every abbreviation the first time. "Earnings before interest and taxes (EBIT)".
- Never point backward with "as established in step 12". Restate the fact: "the company's debt of $1,285 million (step 12)".
- Every formula is followed by a worked example using this company's real numbers.
- Say which numbers were read straight from a document and which were estimated, every time.
- Mark judgment calls as judgment calls. A reader should be able to tell arithmetic from opinion.
- One idea per sentence. Short sentences. Active voice.
- It is one story about one company, told in order. Not an outline, not a checklist, not a list of concepts.
- No filler, no throat-clearing, no "it is worth noting". Start with the fact.
- Numbers: units stated ($ millions, %, x), rounding consistent with the ledger, no false precision.
- Every number in the walkthrough must appear in `inputs.yaml` or `model-output.md`. `tools/check-walkthrough.py` enforces this.

## A worked sample

> ## Step 12: How much does SolarWinds really owe?
>
> *What we wanted to know.* The company's total debt. Debt matters because it makes the company riskier and because lenders get paid before shareholders.
>
> *Why it matters.* Debt sets the weights in the cost of capital and gets subtracted from the company's value to find what the shares are worth. Too low a debt figure makes the shares look more valuable than they are.
>
> *What we did.* The balance sheet says $1,206.6 million. We didn't stop there, for two reasons. First, that figure is after accountants subtracted $29.1 million of fees and discounts from when the loan was taken out; the bank is still owed the full $1,235.7 million. Second, the company has signed office leases it can't walk away from. Professor Damodaran's test: if a payment is fixed, tax-deductible, and missing it could cost you control of the company, it's debt. Leases pass all three. The lease note puts their value at $49.4 million.
>
> *The numbers and where they came from.* Loan at face value, $1,235.7 million; lease liabilities, $49.4 million; deferred revenue, $389.3 million. All from SolarWinds' 2024 annual report (Form 10-K), filed with the SEC on 2025-02-19: balance sheet, note 7 (leases), note 9 (debt). File: `sources/sec-filings/swi-10k-fy2024.md`.
>
> *What we decided, and what we didn't.* Total debt is $1,285.0 million ($1,235.7M + $49.4M). This is arithmetic once the two inputs are chosen. We did not count the $389.3 million of deferred revenue. That is money customers paid in advance for software. The company owes them service, not cash, and missing it wouldn't trigger a default.
>
> *How sure we are.* High. Every figure is disclosed directly. Nothing estimated.
