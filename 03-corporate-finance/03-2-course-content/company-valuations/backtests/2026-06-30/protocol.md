---
title: "Backtest protocol — /value-company reads as of 2026-06-30"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Backtest protocol: reads as of 2026-06-30

Written and committed before any read was produced. The scoring rules below are fixed; a change after the reads exist is recorded as a dated amendment at the end, with the reason, and both scores are reported.

## Question

Does a `/value-company` quick read, built only from what was public on 2026-06-30, anticipate what the companies did afterwards better than an informed reader without the method?

## Companies

KBR, CTVA, CMCSA, ETN, KO, JPM, HD. Chosen by Charlcye Mitchell on 2026-11-03 and handed over as tickers only. The runner was not told which companies had an event after the analysis date.

JPM is a bank. The course treats debt at a bank as raw material, not financing, so the cost-of-capital optimum and the debt-design signal don't apply. JPM is run anyway, as a test of whether the read recognizes where the method stops, and is scored separately from the other six.

## Why 2026-06-30

The runner's training data ends in June 2026. Events after the analysis date can't come from memory, only from documents, and the documents are cut off at that date.

## What the runner may use

- SEC filings with a filing date on or before 2026-06-30, fetched by `tools/fetch-filings.py --cutoff 2026-06-30`, which writes `sources/published.yaml` from EDGAR's filing dates.
- Market data from `scripts/refresh-market-data.py --as-of 2026-06-30`, and closing prices on or before 2026-06-30.
- Peer fundamentals from `tools/fetch-peer-facts.py --date 2026-06-30`.
- What the runner knows from training about events before 2026-06-30.

## What the runner may not use

- Web search, news, or any page not fetched by the tools above.
- Any filing dated after 2026-06-30. `validate-ledger.py` with `meta.blind: true` enforces this on the ledger.

## Known leaks

1. **Ticker list (2026-11-03).** Resolving the tickers to SEC company numbers read SEC's current ticker list, and all seven are on it. So none had completed a delisting by 2026-11-03. Nothing else about the period after 2026-06-30 was seen.
2. **Prior knowledge before the cutoff.** The runner knows each company's history up to mid-2026, including restructurings announced before the cutoff. That is fair: it was public on the analysis date.

## Outputs per company

`company-valuations/<slug>/read.md` in quick mode, with `meta.blind: true`. Each read states unstated goals with confidence and a falsifier, and a "What to watch" list. Every watch item is dated or tied to an observable event between 2026-07-01 and 2027-06-30.

## Control

For each company, a fresh-context agent with no tools gets only the ticker, the date 2026-06-30 and this prompt: "As of 2026-06-30, describe this company's situation and the goals its management or owners are pursuing but not stating. List up to five specific things you expect it to do or announce in the next twelve months, each with a confidence of high, medium or low." Its answers are saved to `control/<ticker>.md` before any outcome is looked at. The control isolates what the method adds beyond the model's general knowledge.

## Scoring

Charlcye compiles each company's material events from 2026-07-01 to the scoring date, without showing them to the runner until every read and control answer is committed. A material event is any of: an acquisition, sale, spin-off or split; a change of 10% or more in total debt; a new, cut or raised dividend, or a buyback authorization of 2% or more of market value; a CEO or CFO change; an activist stake or settlement; a guidance change of 5% or more; a credit-rating change.

Per company, every material event and every prediction (read goals at medium or high confidence, read watch items, control predictions) is scored once:

| Code | Meaning |
|---|---|
| Hit | A prediction whose type and direction match a material event |
| Miss | A material event no prediction anticipated; record the signal that would have caught it |
| False alarm | A prediction whose own date passed without the event, or whose falsifier occurred |
| Open | A prediction whose window hasn't closed; rescored at 2027-06-30 |

Net score = hits − false alarms, for the method and for the control.

Reported:
- Net score, method vs. control, for the six non-bank companies, and for JPM separately.
- A calibration table: hit rate by confidence level, method and control.
- Each miss, with the signal that would have caught it.

**Pass**, decided in advance: across the six non-bank companies, the method's net score beats the control's, and no high-confidence unstated goal in a read is falsified. With six companies and four months, a pass is evidence the method adds something, not proof; a fail on the margin is a reason to look at the misses, not to drop the method.

## Rescoring

Open predictions are rescored at 2027-06-30 under the same rules.

## Amendments

### 1. After the KO pilot, before any scored run (2026-11-03)

No outcome had been seen; the scorer has not yet compiled events. A pilot run on KO, following the skill as written, found problems that would have affected every run:

- **Post-cutoff material inside the repo.** All meetups (and so `meetup-guidance.md`) are from September–November 2026, and some Damodaran blog posts after 2026-06-30 discuss market events and at least one of the seven companies. The pilot read the meetup guidance. Fix: blind runs now read nothing in the repo dated after the analysis date (SKILL.md rule 13), so they get no meetup guidance. This is now a third known leak, closed for the scored runs.
- **Peer prices.** `fetch-peer-facts.py` returned split-adjusted closes, which corrupted market values and could reveal a later split. It now returns the close that actually traded, and never prints the splits.
- **Debt read as zero.** Untagged borrowings printed as 0; they now print as n/a.
- **No earnings releases.** `fetch-filings.py` now fetches the four latest earnings 8-Ks with their exhibits, so the reads see the company's own guidance as of the cutoff.
- **Instructions.** Several unclear steps in SKILL.md were fixed (README structure, market-data steps), and three rules were added: the "Outside knowledge" section in the read, alternatives as model runs, and the equity risk premium by country.
- **Known and not fixed** (same for every run): in `model.py`, the base-year return on capital excludes the impairment add-back that the by-year table includes; peer multiples don't strip cross-holdings from enterprise value; the beta sensitivity can print a duplicate row. None of these changes a signal's direction.

**The pilot read is not scored.** It is kept in [pilot-ko/](pilot-ko/) as a record, and KO is re-run from scratch under the fixed rules, like the other six. Scoring rules and the pass bar are unchanged.

### 2. Score every company, not only the ones with events (2026-11-03)

Added at Charlcye's direction before any scored read landed and before any outcome was compiled. The skill is meant to value any company, and a read that correctly finds nothing hidden should count. The event scoring above stays as it is, pass bar included. Two measures are added and reported beside it, for all seven companies:

- **Does the read still hold?** For each signal, the read's "What it does" column states a level or direction: returns below or above the cost of capital, debt moving toward or away from the optimum, cash returned above or below free cash flow to equity, and so on. A fresh-context agent checks each one against the company's first two 10-Qs filed after 2026-06-30, and records Held, Broke or Can't tell, citing the filing. This runs only after every read and control answer is committed. Reported per company and in total; the control answers have no signal statements, so this measure has no control comparison.
- **Value against price.** The read's value per share and the 2026-06-30 close are recorded with the close on the scoring date, and whether the price moved toward the value or away from it. Reported only; four months is too short for price to be expected to converge.

### 3. Runs complete; incidents during the runs (2026-11-03)

All seven reads and all seven control answers are committed (last read 2026-11-03 17:53 CT). No outcome has been compiled or looked at. Three incidents during the runs, recorded so the scorer can weigh them:

- **Shared market data refreshed to current values.** The Eaton runner called `scripts/refresh-market-data.py --help`; the script doesn't handle `--help`, so it ran a full refresh into the shared `03-3-supplemental-data/` snapshots (as of 2026-11-01) at about 17:33 CT. The files were restored from git within minutes. Every run used its own `--as-of 2026-06-30` market files, and the blind validator rejects any ledger value dated after the cutoff.
- **The Home Depot runner saw a November 2026 rate.** Checking `git status`, it saw the refreshed snapshot's diff, showing a 10-year Treasury of about 4.91%. It reports that no number in its read uses it. Its rates are from 2026-06-30.
- **The Comcast runner saw that WBD is gone from SEC's current ticker list.** `fetch-peer-facts.py` resolves tickers through SEC's current list and failed on WBD, which suggests Warner Bros. Discovery stopped trading before 2026-11-03. Comcast's read mentions WBD once, in the rival reading of a low-confidence goal, for a fact public before the cutoff (its late-2025 bid). No scored item depends on it.

Tool problems the runners worked around (the exhibit filename pattern in `fetch-filings.py`, a crash on a single n/a return-on-capital year in `make-exhibits.py`, peer-data crashes and zero-filled fields, no bank path in `model.py`) are logged in each company's `README.md`. They are being fixed after the runs so every company ran on the same tools.

Outcomes may now be compiled.
