---
title: "SolarWinds (SWI) — Lesson 24: Trends and Measures (no lecture transcript available)"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-09-21
---

# SolarWinds (SWI) — Lesson 24: Trends and Measures (no lecture transcript available)

### Lesson 24 — Trends and Measures (no lecture transcript available)

The topic is known, not "unknown" — this file previously conflated two different gaps and that was wrong. `lesson-overview.md` in `03-corporate-finance/03-2-course-content/03-financing-mix-and-dividends/lesson-24/` names the topic plainly: **"Trends and Measures"** — market-wide dividend and buyback patterns, with a stated learning objective ("understand how companies have approached setting and changing dividends historically and why more and more companies have shifted in the last few decades toward stock buybacks") — and the folder has real materials: `slides.md`/`slides.pdf`, a dividend-yields-and-payout-ratios spreadsheet for US companies, and a blog reference. What is genuinely missing is narrower: the *lecture transcript*. `session-24-part-1.md` and `session-24-part-2.md` — the files `lesson-overview.md` itself links to — don't exist on disk in this lesson's folder (confirmed by directory listing), even though the two Kaltura video links are present in the overview. `lesson-index.yaml`'s topic field for Lesson 24 reads `"(pending — transcript not on channel)"`, which describes the transcript gap, not a topic gap — the index's own topic field is just stale.

Because there is no transcript, there is no verbatim lecture quote to anchor a SolarWinds-specific question the way every other lesson in this project does — that part of the gap is real and this file still doesn't fabricate one. But the topic being known means this lesson isn't a total blank: the Cumulative Project section below is answerable using SWI's actual dividend history, independent of the missing transcript.

## Cumulative Project — Questions for This Lesson

- **How much (if any) has your company paid out in dividends each year for the last 5 years?**
  SWI paid dividends in exactly two of the last five fiscal years (FY2020–FY2024), and zero in the other three — the opposite of "never paid a dividend," which is the error `valuation-report.md` and several original question stems make (see [`README.md`](README.md)):

  | Fiscal year | Dividend | Aggregate paid |
  |---|---|---|
  | FY2020 | $0 | — |
  | FY2021 | $1.50/share special dividend (paid 2021-08-24, record date 2021-08-09) | $237.2M |
  | FY2022 | $0 | — |
  | FY2023 | $0 | — |
  | FY2024 | $1.00/share special cash dividend (paid 2024-04-15, record date 2024-04-03) | $168.2M |

  Both figures are established across this project (Lessons 8, 17, 19, 25–27) from `swi-10k-fy2023.md` and `swi-10k-fy2024.md` Item 5 dividend-policy disclosures. Total: **$405.4M** over the five-year window, funded without new borrowing in either year (the 2021 payout traced to the N-able spin-off distribution, the 2024 payout matched FCFE almost exactly — established in Lesson 27 Part 2). No dividends were paid before FY2021 (S-1 and the FY2018 10-K both state SWI had never declared or paid a cash dividend) or after FY2024 — the company went private in April 2025 before any FY2025 distribution could occur.

- **What dividend yield and payout ratio does this translate into?**
  Payout ratio is the more answerable half. FY2024: $168.2M paid against FY2024 net income of $111.9M is a **150.2%** payout ratio on net income, or **100.2%** against FY2024 FCFE of $167.8M (established in Lesson 27 Part 2) — essentially a full FCFE sweep. FY2021's $237.2M payout can't be run against net income at all in the conventional sense: FY2021 EBIT was −$32.9M (established in Lesson 27), a loss year, so a payout ratio on net income is negative and not meaningful; the payout is better read as a one-time distribution of the N-able separation proceeds (established in Lesson 27 Part 2) rather than a claim against that year's operating earnings.

  Dividend yield is only partly answerable — the compiled sources don't include a daily/weekly SWI price series (flagged as genuinely unattainable in `sources/README.md`: Stooq blocks automated fetches, Nasdaq drops delisted tickers). For FY2024, using the $15.18 undisturbed pre-announcement close (established in Lesson 8 as the closest available price anchor, though from February 2025 rather than the April 2024 dividend date) as a rough proxy gives an approximate yield of $1.00 ÷ $15.18 ≈ **6.6%** — directionally a real, meaningful yield for a special dividend, but flagged explicitly as an approximation from a nearby date, not the actual record-date price. For FY2021, no comparable price anchor exists anywhere in the compiled sources close to the August 2021 dividend date (the DEF 14A performance-graph data Lesson 8 uses starts its indexed series at 12/31/2019 without giving the underlying absolute price), so a 2021 yield genuinely cannot be computed from what's on disk — a real gap, not one this file is glossing over. What would close it: a historical SWI closing price for August 2021, available only via a paid terminal (Bloomberg/CapIQ/Refinitiv) or a manual Yahoo Finance historical-data export per `sources/README.md`'s documented workaround.

## Notes

This lesson's own transcript is missing, but its topic was never actually unknown — a distinction the file's earlier text collapsed into a single "gap," which this rewrite fixes. Lesson 24 sits between Lesson 23 ("Designing the Right Type of Financing") and Lesson 25 ("Three Schools of Thought on Dividends"), and its confirmed topic — market-wide dividend/buyback trends — fits that position exactly, setting up the dividend-policy module Lessons 25–28 run for SWI specifically. The Cumulative Project answers above are the first place in this project to lay out SWI's full five-year dividend cash-flow record in one table; every later lesson that cites the $1.50 (2021) / $1.00 (2024) dividend history (Lessons 17, 19, 25–27, 33–34, 36) can point back here rather than re-deriving it. The one output this lesson still can't produce is a 2021 dividend yield — a genuine, disclosed data gap (no compiled price series), not an editorial omission.
