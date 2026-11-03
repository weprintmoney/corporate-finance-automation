---
title: "JPMorgan Chase & Co. — The read, as of 2026-06-30"
status: draft
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# JPMorgan Chase & Co. — The read, as of 2026-06-30

JPMorgan Chase is the largest US bank holding company. No shareholder holds more than 10%. Power sits with a combined chairman and CEO, James Dimon (70), and a board of ten independent directors. The Federal Reserve sets the capital floor that actually limits payouts. This is a blind read as of 2026-06-30, in quick mode. It uses nothing filed or published after that date. The latest filing used is the 8-K of 2026-06-25.

**This is a bank, and three of the course's firm-level tools do not fit it.** The debt ratio against its cost-of-capital optimum, the synthetic rating and the debt-design test treat deposits and notes as financing. At a bank they are raw material (lesson 11: "We do not unlever or relever betas, because estimating debt and equity for banks is an exercise in futility"). The leverage and debt-design signals are therefore **not applicable as built**. model-output.md sections 2–4 print a 49% "optimal debt ratio" and a CC synthetic rating, and neither is used. In their place:

- **Leverage:** regulatory capital against its requirements.
- **Payout:** cash returned against the bank version of free cash flow to equity, which is net income minus the growth in required capital (lesson 26).
- **Value against price:** price-to-book against the gap between return on equity and the cost of equity (lesson 35).

`bank-equity.py` computes these from the ledger into `bank-equity-output.md`.

## The read

JPMorgan earns a return on equity roughly double its cost of equity: 17% in 2025 and 19% annualized in the first quarter of 2026, against 8.27%. Its share price of $327.33 is 2.55 times book value. That is what a 16–17% return sustained indefinitely is worth, so the market is not paying for anything beyond the current franchise. The cushion built in 2024 is being spent. Common equity Tier 1 (CET1, Standardized) went from 15.7% to 14.3% of risk-weighted assets. In 2025 the bank returned 86% of its earnings, about $18–21 billion more than its balance-sheet growth left free at the requirement. On 2026-06-24 it announced another $50 billion of buybacks and a 10% dividend increase. Whether that is a deliberate run-down toward the higher requirement due in 2028 (12.5%, or about 13% under the March 2026 proposals) or a steady buffer of 2.5–3 points over whatever requirement applies, the filings can't yet tell; the next three quarters' CET1 will. Against the 2028 floor the true surplus is about $23–33 billion, not $54 billion. The control question is succession. The board says "medium-term", and on 2026-06-25 it made two Co-Presidents and paid $100 million to keep four internal candidates for three years.

## Signals

| Signal | What it says | What it does | Gap |
|---|---|---|---|
| Control | "orderly CEO transition ... in the medium-term" (S-2); Co-Presidents named 2026-06-25 (S-3) | Dimon is chair and CEO at 70 and was paid $43M for 2025 (facts `ceo-pay-2025`, `ceo-age`). $100M of retention awards cliff-vest in mid-2029 and need only 12% average ROTCE against 20–23% actual (facts `retention-awards-total`, `retention-award-rotce-hurdle`, `rotce-2025`, `rotce-2026q1`). Largest holders are index funds: Vanguard 9.86%, BlackRock 7.15% | Medium |
| Lifecycle | "build and invest in the Firm's businesses through ... cycles" (S-5); 2026 outlook: net interest income ~$103B, adjusted expense ~$105B (S-6) | Mature and still growing. Revenue grew 12.3% a year 2022–25 but 2.8% in 2025 (bank-equity-output.md H). Risk-weighted assets grew $224B in 2025 while 86% of earnings went back to shareholders (lessons 01, 31; bank-equity-output.md B) | None |
| Hurdle | No hurdle rate disclosed (S-7) | Cost of equity 8.27%: beta 0.849 (revenue-weighted levered industry betas) × ERP 4.82% + risk-free 4.18%. Range 7.85–9.00% across beta choices (model-output.md section 1; alternatives/) | n/a |
| Returns | "ROE is measured and internal targets for expected returns are established" (S-7); no number | ROE 17%, 18%, 17% in 2023–25, 19% in 1Q26, against 8.27%. Segment ROE 1Q26: CCB 32%, CIB 21%, AWM 44% (bank-equity-output.md C) | None (value-creating) |
| Leverage, as regulatory capital (debt ratio not applicable as built) | "fortress balance sheet" (S-8); "significant excess capital" (S-10); no numeric internal minimum (S-9) | CET1 14.1% (Advanced, binding) against 11.5%: $54.1B over, measured on Advanced RWA. Against 2028's 12.5%: $33.5B over. Against about 13.0% under the re-proposals: $23.2B over. The Standardized ratio fell from 15.7% (2024) to 14.3% (1Q26). Tier 1 leverage 6.6% vs 4.0%, SLR 5.6% vs 4.3% (bank-equity-output.md A) | Medium |
| Debt design | Not applicable as built | USD floating and fixed-to-floating notes due 2030–37. Long-term debt is up 10.2% year on year to $448.8B (lesson 23; bank-equity-output.md H) | n/a |
| Payout | Dividend raise "supported by ... strong financial performance"; buybacks for "flexibility" (S-15, S-16) | 2025: returned $47.7B (85.7% of net income) against bank FCFE of $26.5–29.9B. 1Q26: $12.4B against $8.7–9.6B. 2024: $32.6B against $47.0B. FCFE uses Standardized RWA. Peers: BAC 97%, WFC 108%, C 130%, GS 103%, PNC 57%, USB 48%; JPMorgan pays out less than every money-center peer (bank-equity-output.md B, F) | Medium |
| Value against price | No target (S-17) | P/B 2.55x on 1Q26 book (2.56x on year-end 2025 book in the model and peer table; P/TBV 3.01x). Justified 2.66x at ROE 17%, ke 8.27%, g 3%. Price implies a sustained ROE of 16.4%. Peer P/B-on-ROE line gives 2.72x (bank-equity-output.md E, F) | Small |

**Leverage (regulatory capital).** "Excess capital" depends on which requirement it is measured against. Against today's 11.5% the surplus is $54,098M, 6.2% of market value. That requirement is frozen through 2027-09-30, because the stress capital buffer is held at 2.5% (S-10). The 10-Q says the GSIB surcharge rises to 5.5% from 2028-01-01 under current rules. It also says the March 2026 re-proposals would lift required CET1 a further ~4% (S-11). On that basis the surplus is $23,178M–$33,484M (bank-equity-output.md A). The Standardized ratio has fallen 1.4 points in five quarters, but CET1 capital itself rose every period ($275.5B, $288.5B, $291.2B), and the cushion over the requirement in force went from 3.4 points (15.7% against 12.3% in 2024, when the stress buffer was 3.3%) to 2.8 points (14.3% against 11.5%) (facts `cet1-requirement-2024`). So the actions fit a run-down toward the 2028 number, and they also fit a steady buffer over the current one. Separately, equity allocated to Corporate was cut from $120.9B to $98.4B on 2026-01-01 and moved into CIB (+$17.0B) and CCB (+$5.5B). That is an internal reallocation, not a distribution (facts).

**Payout.** Lesson 26's bank FCFE is net income minus the increase in risk-weighted assets times the capital ratio held. In 2024 JPMorgan paid out less than that and CET1 rose to 15.7%. In 2025 and 1Q26 it paid out more under every target ratio. The difference came out of the cushion (bank-equity-output.md B). Part of 2025's RWA growth was the Apple Card forward commitment, about $110B of RWA at year-end that fell to about $30B by 2026-03-31. Even after that release CET1 fell 0.3 points in 1Q26, and buybacks ran at $8.3B for the quarter.

**Control.** The board's own words put CEO succession in the "medium-term" (S-2). On 2026-06-25 it named Doug Petno and Troy Rohrbaugh Co-Presidents. Marianne Lake, CEO of Consumer & Community Banking, retired. Petno, Rohrbaugh, Mary Erdoes and Jennifer Piepszak received retention awards that vest only if they stay to mid-2029 and do not vest on retirement. The 12% ROTCE condition sits far below the 20–23% the firm earns, so the awards pay for staying, not for performance (S-3).

No charts: make-exhibits.py's cost-of-capital chart would draw the non-applicable section 3, and its returns chart needs `company.history`, which is omitted for a bank (`meta.omitted`). The tables in bank-equity-output.md carry the same findings.

## Unstated goals

**Management (Dimon and the Operating Committee, with board approval) is distributing capital down toward the CET1 requirement it expects in 2028, about 12.5–13%, not holding today's 2.5–3 point buffer over 11.5%, to keep ROE and ROTCE near their 2025–26 levels while still calling the balance sheet a fortress.** Confidence: low.
- Evidence:
  - Leverage (regulatory capital): Standardized CET1 went 15.7% → 14.6% → 14.3%. The 10-Q quantifies a higher 2028 requirement (S-11), and against it the surplus is only $23–33B (bank-equity-output.md A).
  - Payout: $47.7B returned in 2025, 85.7% of net income, against bank FCFE of $26.5–29.9B. A new $50B authorization (5.7% of market value), effective 2026-07-01 per the 8-K of 2026-06-24, is the same size as 2025's and lasts about six quarters at the 1Q26 pace (bank-equity-output.md B, G).
  - These two are the same capital identity seen twice (paying out more than FCFE is what lowers the ratio), so this is one signal, plus the context that ROE runs 8.7–10.7 points above the 8.27% cost of equity (bank-equity-output.md C).
- Would be wrong if Standardized CET1 stays at 14.0% or higher at each quarter-end from 2026-06-30 to 2027-03-31 while buybacks run at $8B or more a quarter. That pattern fits a fixed buffer, not a run-down. Source: the earnings 8-Ks of mid-July 2026, mid-October 2026, mid-January 2027 and mid-April 2027.
- Rival reading (strong): there is no run-down target. Management keeps a buffer of roughly 2.5–3 points over the requirement in force and returns the rest. The ratio fell because RWA grew 12.8% in 2025 and grew again in 1Q26 even after the Apple Card release. Evidence for the rival:
  - CET1 capital rose every period.
  - Over 2024–1Q26, cash returned ($92.7B) was only about $6B above FCFE at 11.5% ($86.5B) (bank-equity-output.md B).
  - The cushion over the requirement in force moved only from 3.4 to 2.8 points.
  - JPMorgan pays out less than every money-center peer.
  The goal's only edge is that buybacks rose to $8.3B a quarter from 3Q25, after the buffer cut was announced (facts `buybacks-1q25` to `buybacks-2026q1`), and that the ratio kept falling in 1Q26. That is too thin for more than low confidence.

**The board is staging a CEO succession within the life of the retention awards, which vest in mid-2029, and is paying so that the runners-up do not leave.** Confidence: low.
- Evidence:
  - Control: the proxy names the transition "medium-term" (S-2). Two Co-Presidents now run the two largest businesses, and one candidate (Lake) has retired (S-3).
  - Pay against returns: $100M of retention awards with a 12% ROTCE hurdle, 8–11 points below current ROTCE, so they are insurance against departures, not incentives (S-3).
  - Both pieces of evidence come from the June 2026 control filings. That is one signal plus circumstantial support, so the confidence is low.
- Would be wrong if, by 2027-06-30, Petno or Rohrbaugh leaves JPMorgan before a successor is named, or the board names an outside CEO (8-K item 5.02). The goal's horizon runs to mid-2029, so the absence of an announcement by 2027-06-30 does not test it; within the backtest window it is mostly untestable.
- Rival reading: the promotions fill the gap Lake's retirement left in Consumer & Community Banking, and Dimon stays CEO for years. The awards are a defence against poaching, not a clock. This reading is about as plausible as the goal, which is why the goal is held at low confidence.

## What to watch

1. **A dividend increase above $1.65 a quarter, announced by 2027-06-30.** It would most likely come with the 2027 stress-test results in late June 2027 (the 2026 announcement was on June 24). A March 2027 increase would also count. Confidence: medium. Timing risk: if the Fed publishes after June 2027, the announcement falls outside the window.
2. **Standardized CET1 at or below 13.8% at 2027-03-31, with at least $25B of buybacks over 3Q26–1Q27**, from the earnings 8-Ks of mid-October 2026, mid-January 2027 and mid-April 2027. This separates the first goal (a run-down toward about 13%) from its rival (a steady buffer, CET1 at 14.0% or above). Confidence: low.
3. **A new common share buyback authorization of $40B or more (about 4.5% of market value), announced by 2027-06-30**, alongside the 2027 stress-test results. It would succeed the $50B program the 8-K of 2026-06-24 made effective 2026-07-01. Confidence: low. At about six quarters of capacity, the current program may not need renewing by then, and the 2025 and 2026 announcements fell on July 1 and June 24.
4. **The board names Dimon's successor as CEO, or sets a date for him to step down as CEO, by 2027-06-30** (8-K item 5.02). Confidence: low. If either Co-President leaves before a successor is named, that falsifies the second goal; no announcement in the window does not.

## Discretionary decisions

> ⚠️ **Discretionary Decision: analysis date**
> **Chose:** 2026-06-30, the backtest date, using the 10-K for 2025, the 1Q26 10-Q and every 8-K through 2026-06-25. **Why:** set by the protocol. **Alternative:** none. **Confidence:** high.

> ⚠️ **Discretionary Decision: debt set to zero; leverage and debt-design signals not applicable as built**
> **Chose:** `company.debt_total` = 0, so the hurdle rate is the cost of equity. Leverage is read from regulatory capital. **Why:** lessons 11, 20 and 26 treat a bank's debt as raw material; the task brief says the same. **Alternative:** counting $448.8B of long-term debt gives a 34% debt ratio and a meaningless WACC. The firm method's "optimum" is 49% (model-output.md section 3), which would have JPMorgan add $430B of debt. **Confidence:** high.

> ⚠️ **Discretionary Decision: beta**
> **Chose:** revenue-weighted levered industry betas, 0.849, without relevering. **Why:** the lesson 11 bank method and JPMorgan's mix of trading, banking and wealth businesses. **Alternative:** money-center beta 0.761 → cost of equity 7.85% (alternatives/beta-money-center-output.md); 1.0 → 9.00% (alternatives/beta-market-output.md); all brokerage → 9.83% (alternatives/beta-brokerage-output.md). Across 7.85–9.00% the price implies a sustained ROE of 15.4–18.3% (bank-equity-output.md E). **Confidence:** medium; no regression beta was available.

> ⚠️ **Discretionary Decision: country risk proxies**
> **Chose:** revenue weights from Note 31, with the UK, Japan/China and Brazil standing in for their regions. Weighted ERP 4.82%. **Alternative:** all US → cost of equity 8.06% (alternatives/erp-us-only-output.md). **Confidence:** medium; the choice is immaterial to the read.

> ⚠️ **Discretionary Decision: cost of debt, weights, coverage numerator, R&D, terminal method, bankruptcy cost**
> **Chose:** none of these apply to a bank. The A rating's 5.22% is printed but carries zero weight. No R&D, no firm terminal value, no APV. **Alternative:** n/a. **Confidence:** high.

> ⚠️ **Discretionary Decision: the forward CET1 requirement**
> **Chose:** 12.5% for 2028 under current rules (11.5% + 1.0 point higher GSIB surcharge, S-11) and 13.0% under the re-proposals (12.5% × 1.04, applying the disclosed +4% in required CET1 dollars to today's RWA). **Why:** these are the company's own disclosed estimates. **Alternative:** today's 11.5% → surplus $54.1B instead of $23.2–33.5B (bank-equity-output.md A). The 11.5% basis is what supports reading the payout as "over-capitalized, should return more". **Confidence:** medium. The re-proposal changes RWA as well as ratios, and the company's +4% figure is the only quantification.

> ⚠️ **Discretionary Decision: forecast source and stable period**
> **Chose:** no DCF. Management's 2026 outlook (S-6) is used only as context. Stable growth 3%, sustained ROE 17% (base) and 14% (fade). **Why:** a bank is valued on book value and ROE. 3% lies between fundamental growth of 2.3% and the 4.18% risk-free cap. **Alternative:** g 4% → justified P/B 3.04x instead of 2.66x; ROE 14% → 2.09x (bank-equity-output.md E). **Confidence:** low on the level, which is why the read uses the implied ROE (16.4%) rather than a value per share.

> ⚠️ **Discretionary Decision: peer set and multiple**
> **Chose:** BAC, C, WFC, GS, MS, PNC and USB on price-to-book, regressed on ROE (R² 0.74). **Alternative:** the plain peer median of 1.54x (model-output.md section 7) ignores ROE and would call JPMorgan 66% overvalued. **Confidence:** medium. Peer book values mix total and common equity because of tag gaps in the tool.

## Outside knowledge

- James Dimon has been CEO since the end of 2005 and chairman since the end of 2006, and Marianne Lake was widely described in the press as a CEO candidate. This was public long before 2026-06-30. Used only to frame succession.
- Before 2026-06-30 Dimon said publicly, more than once (for example at the May 2024 investor day), that buying back much stock at prevailing prices was unattractive. This was public before the cutoff. It supports the first goal's account of a measured pace and is not used as evidence for the goal.
- The Fed publishes stress-test results in the last days of June, and banks announce capital actions right after. This pattern is visible in the filings themselves (2025-07-01, 2026-06-24) and was public before the cutoff.
- First Republic Bank was acquired in May 2023 (referenced in the filings). It affects the 2023–24 growth figures.
- Nothing after 2026-06-30 was used. The market data tool fetched Damodaran's archived June 2026 and January 2026 editions and FRED closes on or before 2026-06-30. The peer tool returned closes that traded on 2026-06-30 and 10-K data filed on or before that date.

## Sources

- JPMorgan Chase & Co. Form 10-K for 2025 (filed 2026-02-13) and for 2024 (filed 2025-02-14).
- Form 10-Q for the quarter ended 2026-03-31 (filed 2026-05-01).
- 2026 Proxy Statement (DEF 14A, filed 2026-04-06).
- Form 8-Ks: earnings releases of 2025-07-15, 2025-10-14, 2026-01-13 and 2026-04-14 (financial supplements); stress-test capital releases of 2025-07-01 and 2026-06-24; item 5.02 filings of 2025-12-08, 2026-01-22 and 2026-06-25; note issuances of 2026-01-22, 2026-02-05, 2026-04-23 and 2026-06-02; preferred redemption of 2026-05-27; bylaw amendments.
- Peer 10-K data (SEC XBRL company facts, filed on or before 2026-06-30) for BAC, C, WFC, GS, MS, PNC and USB; closing prices on 2026-06-30.
- Damodaran: implied ERP, June 2026; ratings spreads, country risk premiums and industry betas, January 2026. FRED 10-year Treasury close on 2026-06-30.
