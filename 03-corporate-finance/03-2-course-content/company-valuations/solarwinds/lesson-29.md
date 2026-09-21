---
title: "SolarWinds (SWI) — Lesson 29: Intrinsic Valuation Foundations"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-09-21
---

# SolarWinds (SWI) — Lesson 29: Intrinsic Valuation Foundations

### Lesson 29 — Intrinsic Valuation Foundations

- **Lesson 29, Session 29 · Part 1 — "Three Ways to Value a Company and the Four Questions Behind Every DCF"** ([transcript](../../04-dividends-and-valuation/lesson-29/session-29-part-1.md))
    - Quote: "When you have shifting, unstable, or unpredictable debt ratios, you should be valuing the entire firm."
    - Question for SWI: Given SWI's debt ratio has shifted materially — high leverage from the 2016 LBO, paydown after the 2018 IPO, and a fresh capital structure imposed by the 2025 Turn/River take-private — does the "shifting debt ratio → value the firm, not just equity" rule mean a FCFF/firm-value DCF is the right frame for SWI's FY2024 (final public-year) valuation, rather than a FCFE/equity-only approach?
    - Sources needed: SWI's book and market debt ratio history, 2018–2024, to confirm how unstable it actually was.
    - Where to find: SEC-EDGAR — SWI 10-Ks FY2019–FY2024, balance sheets (debt levels) and Item 7 MD&A (any stated leverage targets); REPO-SWI-VAL (Step 12 capital structure section has only a current-point-in-time snapshot, not the multi-year trend needed here).
    - Answer: Yes — value the firm; an equity-only model here would require forecasting a debt ratio nobody could have forecast. Book debt (current + long-term carrying value) versus book equity ran $2,242.9M against a −$519.6M stockholders' *deficit* at FY2016 (post-LBO, so >100% of book capital), then $1,924.0M/$2,616.1M at FY2018 (42.4%), $1,913.3M/$2,649.5M FY2019 (41.9%), $1,902.6M/$3,010.7M FY2020 (38.7%), ~$1,881M FY2021, $1,202.1M/$1,369.7M FY2022 (46.7%) after $664.4M of repayments including a $300M voluntary prepayment and a $349.4M refinancing paydown, $1,203.4M/$1,442.0M FY2023 (45.5%) and $1,206.6M/$1,400.7M FY2024 (46.3%) — from `swi-10k-fy2018.md`, `swi-10k-fy2020.md`, `swi-10k-fy2023.md` and `swi-10k-fy2024.md`. On market values the swing is just as violent: 31.7% at the $15.18 undisturbed close, 26.1% at the $18.50 deal price, and roughly 58% under Turn/River's committed $2,225M first-lien + $525M second-lien + $200M revolver (`swi-defm14c-2025-merger-information-statement.md`). That is the textbook "shifting, unstable" case: build FCFF, discount at WACC, and bridge to equity at the end.

## Cumulative Project — Questions for This Lesson

- **What is the market capitalization (market value of equity) for your company, relative to its earnings and cash flows?**
  At the corrected market value of equity (Lesson 13: $3,174.0M at $18.50 on 171,566,604 shares; $3,422.9M on the 185.0M fully-diluted count Lessons 33–35 use), against FY2024 net income of $111.9M that's a **30.6x trailing P/E** ($3,422.9M ÷ $111.9M, established in Lesson 35), and against FY2024 FCFF of $153.8M (Lesson 30) the equivalent enterprise-value multiple is roughly 28x. Both read as expensive on an earnings/cash-flow basis, consistent with Lesson 35's finding that SWI's earnings multiples looked "cheap" only relative to a sector trading at 2–3x the growth rate.

- **How much has that market capitalization changed over time?**
  Substantially, and non-monotonically. At the October 2018 re-IPO, 304.9M shares at $15.00 implied a market cap of roughly **$4.57B** (established in Lesson 17 Part 1). By year-end 2024, the backed-out price of ~$14.00 (established in Lesson 4, derived from Turn/River's disclosed December 2024 offer premium over the 30-day VWAP) on 171.6M shares implies a market cap of roughly **$2.40B** — a decline of almost half, even before adjusting for the 2021 2-for-1 reverse split and N-able spin-off, both of which reduced the share count without a corresponding value transfer to remaining holders' benefit. The undisturbed pre-announcement close of $15.18 (February 5, 2025) puts it back to **$2,604.4M** (established in Lesson 35 Part 1), and the $18.50 deal price brings it to $3,174.0M–$3,422.9M. Net: market cap round-tripped down roughly 45% and back up about 30–40% over six-plus years, ending below the IPO level in nominal terms — consistent with the permanent EV/EBITDA de-rating this project documents in Lesson 3 (a ~46% premium to peers in 2019–2020 collapsing to a ~31–33% discount by 2024–2025).

- **How have earnings/cash flows changed over time?**
  Violently, driven mostly by one non-operating event. EBIT ran −$32.9M (FY2021, established in Lesson 14/27) then −$819.6M (FY2022, dominated by the $891.1M goodwill impairment established in Lessons 12 and 14 — impairment-adjusted EBIT was actually a positive $71.5M that year) then $150.4M (FY2023) then $208.4M (FY2024) — established in Lessons 20 and 31. Net income followed the same V-shape, landing at $111.9M in FY2024. Strip out the one-time impairment and the underlying trend is a steady, real recovery (impairment-adjusted EBIT $71.5M → $150.4M → $208.4M, FY2022–FY2024), but revenue growth over the same window stayed slow (5.0%–5.5% per year, established in Lesson 20), so the earnings recovery is overwhelmingly a margin story (adjusted EBITDA margin 39.0% → 43.3% → 48.3%, established in Lesson 1) rather than a growth one.

## Notes

Lesson 29 sets up Module 4's core valuation method by asking whether SWI should be valued as a firm (FCFF/WACC) or as equity alone (FCFE/cost of equity), and the debt-ratio history it assembles — swinging from over 100% of book capital post-2016-LBO down to ~26% at the 2025 deal price and back up toward ~58% under Turn/River's new financing — makes an unambiguous case for the firm-value approach. This is a foundational methodology decision the rest of Module 4 depends on directly: Lesson 30 builds the FCFF base year, Lesson 33 bridges that firm value back to equity per share, and Lesson 34 assembles the complete DCF using exactly this frame. It also connects backward to Lesson 13's cost-of-capital weighting and Lesson 18's optimal-debt-ratio work, both of which document the same volatile capital structure from a financing-mix rather than a valuation-method angle.
