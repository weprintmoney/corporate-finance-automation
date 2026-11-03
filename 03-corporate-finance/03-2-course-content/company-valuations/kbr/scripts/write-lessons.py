#!/usr/bin/env python3
"""Write the quick-mode lesson files for KBR (signal questions only). Answers cite inputs.yaml (ledger),
model-output.md (MO §n), alternatives/*-output.md and sources/statements/kbr-stated-positions.md (S#).
Usage (from the kbr/ folder): python3 scripts/write-lessons.py
"""
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FM = """---
title: "KBR, Inc. (KBR) — Lesson {n:02d}: {t}"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# KBR, Inc. (KBR) — Lesson {n:02d}: {t}

"""
ST = "Module 1 Step — Questions for This Lesson"
CP = "Cumulative Project — Questions for This Lesson"

L = {}

L[1] = ("Valuation: The Big Picture / What is Corporate Finance?", ST, [
    ("Which company, and why is it a good subject (data available, decisions to judge)?",
     "KBR, Inc. (NYSE: KBR), a Houston-based provider of government technical services (Mission Technology Solutions, MTS: 72% of FY2025 revenue, `facts.segment-revenue-fy2025`) and energy process technology and engineering (Sustainable Technology Solutions, STS). Type `public`, base year FY2025 (ended 2026-01-02), USD. It is a good subject because the board has made a large, dated decision — a tax-free spin-off of MTS targeted for 2027-01-04 (`facts.spin-target-date`) — and has visibly changed its cash-return behaviour while the spin is pending (`facts.buybacks-q1-2026` $4M vs `facts.buybacks-q1-2025` $156M)."),
    ("Where does it sit on the corporate life cycle, judged by growth, margins, reinvestment and cash use?",
     "Mature. Revenue grew from $6,564M (2022) to $7,786M (2025) (`company.history`), but FY2025 growth was 1% and Q1 FY2026 revenue fell 5% (`facts.q1-2026-revenue-change`). Operating margin rose to 10.0%. Internal reinvestment is small — base-year reinvestment rate −5.83%, or 5.14% excluding acquired-intangible amortization (MO §8) — and growth has been bought: $738M for LinQuest in 2024 (`facts.linquest-acquisition`). Cash has gone mostly to buybacks and dividends ($1,439M over 2022–2025, MO §5). A mature firm acting like one, except for the debt-funded acquisition.")])

L[2] = ("The Objective: Utopia and Let Down", ST, [
    ("Who sits on the board of directors?",
     "Eleven directors (`governance.board`): Stuart Bradie (Chair, President and CEO) and ten independents, led by Lead Independent Director Wendy Masiello; Jack Moore chairs Compensation."),
    ("Whose interests are they most likely to serve?",
     "Management's and diversified institutions'. Directors and officers together own 1.15% (`governance.controlling_holders`); the CEO is also chair. No holder has a board seat or consent right."),
    ("Where does power lie (shareholders, managers, inside shareholders, another party), and what measure of governance strength supports that?",
     "With management, checked by large index and active funds. Evidence: CEO-chair combination, 99% say-on-pay support (S6), double-trigger change-in-control terms (`governance.change_of_control_payouts`), and charter provisions that 'could delay or prevent a change of control' (10-K Item 1A). One countervailing sign: the compensation committee cut the 2025 EPS payout from 68.9% to 13.1% for the HomeSafe loss (`facts.sti-negative-discretion-2025`). A second outside party matters: the US government (57% of revenue, `facts.us-government-revenue-share`), which under a 2026-01-07 Executive Order can seek to limit dividends and buybacks of contractors it judges to underperform (S17).")])

L[3] = ("The Objective: Reality and Reaction", ST, [
    ("If the firm states goals, what is it targeting (growth, profitability, stock price, value)?",
     "Stated: 'unlock the next phase of value creation' through two pure-play companies (S1, S8); pay targets adjusted EPS (45%), adjusted operating cash flow (25%), book-to-bill and relative TSR (S5). For 2026, executive KPIs focus on 'delivering a successful transaction' (S5). No return-on-capital target (S11)."),
    ("If it states none, what does its behaviour say the primary focus is?",
     "Behaviour since 2025-09-24 says the focus is completing the separation cleanly: buybacks stopped (Q1 FY2026 $4M, all withhold-to-cover), the dividend held flat at $0.165 'during the spin transaction' (S16), the ESPP suspended (S20), and the 10-Q commits MTS's new borrowing to paying down KBR debt (S13).")])

L[4] = ("Define and Measure Risk", ST, [
    ("How many classes of shares exist and what are the voting rights of each?",
     "One class, one vote per share; no preferred issued (`governance.share_classes`)."),
    ("Who are the largest shareholders?",
     "FMR LLC 15.0%, Vanguard 9.85%, BlackRock 9.28% (`governance.controlling_holders`; dates of the 13G filings are in the ledger — the Vanguard and BlackRock figures are from early 2024)."),
    ("Is the marginal investor an individual or an institution?",
     "An institution (`governance.marginal_investor`)."),
    ("Is that marginal investor diversified?",
     "Yes; index funds and a large active manager. So market (beta) risk is the relevant risk. Shares outstanding 126.79M (`company.shares_basic`).")])

L[7] = ("Country Risk Premiums", ST, [
    ("What is the best measure of the company's country exposure (revenues, production, assets)?",
     "Revenues by destination: KBR's work is performed where the customer is, and the 10-K discloses revenue by destination for both segments."),
    ("What is the geographic breakdown of that measure?",
     "US 54.5%, Europe (mostly UK) 20.3%, Middle East 10.2%, Australia 7.0%, Africa 3.3%, Other 2.9%, Asia 1.8% (`country.exposures`)."),
    ("What is the weighted average ERP?",
     "5.38% (`country.weighted_erp`), against the 4.57% mature premium (`market.mature_erp`). Regional premiums are simple averages of the countries KBR names (sources/market-data/country-exposure-2026-06-30.md) — a discretionary decision; with no country premiums the cost of capital falls from 9.14% to 8.41% and value rises to $61.39 (alternatives/erp-us-only-output.md)."),
    ("Why might that ERP change?",
     "The spin moves it. MTS is mostly US and UK government work; STS is 30% Middle East plus Africa and Asia (10-K Note 3). After 2027-01-04 'New KBR' (STS) will carry a materially higher country premium than today's blend, and SpinCo a lower one.")])

L[10] = ("Bottom-Up Betas", ST, [
    ("What is the bottom-up unlevered beta from comparable firms, cash-corrected?",
     "0.9932 (`beta.unlevered_bottom_up`)."),
    ("If the company has several businesses, what is each segment's beta and the weighted average?",
     "MTS as Aerospace/Defense 0.8694, weight 53.8%; STS as Engineering/Construction 1.1374, weight 46.2%; weights from FY2025 segment adjusted EBITDA (`beta.segments`). Revenue weights give 0.945 and value $52.18 (alternatives/beta-revenue-weights-output.md); MTS as Computer Services gives value $50.78 (alternatives/beta-mts-computer-services-output.md). The beta choice moves value by less than 2%.")])

L[12] = ("Debt: Measure and Cost", ST, [
    ("Does the company have an agency rating? What default spread and pre-tax cost of debt does it imply?",
     "None named in the fetched filings (`debt.rating_actual` null). The observed cost — interest $158M over average face debt — is 6.07% (`debt.kd_pretax_observed`), which is SOFR-plus-margin pricing on secured term loans, not investment-grade pricing."),
    ("What synthetic rating does interest coverage imply, and what cost of debt?",
     "EBIT coverage 4.92x → A- on the small-firm table, spread 0.89%, cost 5.33% (MO §2)."),
    ("If the two differ, why?",
     "Coverage flatters KBR: $210M of EBIT is equity earnings of unconsolidated affiliates, $103M of the rise from one LNG project (`facts.equity-earnings-affiliates`), and interest is cut by $21M of swap income locked at 0.89% on $400M until January 2027 (`facts.swaps-expiring-jan-2027`). Lenders price leverage (2.3x net debt/EBITDA, `facts.net-leverage-q1-2026`) and security. Using the synthetic rate lowers the cost of capital to 8.92% (alternatives/kd-synthetic-output.md)."),
    ("What is the market value of interest-bearing debt? If the debt is fixed-rate and rates have moved since it was issued, how far is market value from book?",
     "89% of face debt floats; the 4.75% notes ($250M) trade at $246M (10-K Note 20). Market ≈ face; face $2,617M used (`company.debt_face`)."),
    ("What is the debt value of lease commitments, including leases signed but not yet started?",
     "$301M (`company.lease_debt`: operating $292M + finance $9M). The lease note (10-K Note 15) does not mention leases signed but not yet commenced; none added."),
    ("Does the company guarantee debt of joint ventures or special-purpose vehicles, or have take-or-pay capacity contracts, that pass the debt test but sit off the balance sheet?",
     "JV performance guarantees are joint and several but not estimable (10-K Note 11). Receivables sold to MUFG ($2,094M sold in FY2025) are a financing that leaves no outstanding balance in the 10-K. Neither is added; listed under `meta.omitted`."),
    ("How much interest was capitalized into construction, and what does coverage look like once it is added back?",
     "None disclosed; KBR is a services firm with $42M of capex (`company.capex`)."),
    ("Did the company lengthen the depreciation lives of servers or equipment, and how much did that raise operating income?",
     "No change in useful lives is disclosed; the PP&E note gives estimated useful lives by class with no change described (10-K Note 7)."),
    ("What marginal tax rate applies to the after-tax cost of debt?",
     "25% (`market.tax_rate_marginal`); after-tax cost of debt 4.55% (MO §1).")])

L[13] = ("Weights for Cost of Capital", CP, [
    ("Counting both interest bearing debt and lease commitments, what is the market debt ratio for the firm?",
     "39.99% — debt $2,918M against equity $4,378M at $34.53 (MO §1). The ratio is high partly because the share price is well below the $49.45 average KBR paid in its FY2025 buybacks (10-K Note 17)."),
    ("What is the cost of capital of the firm, using market values for weights? How different would it have been, if you had used book values?",
     "9.14% at market weights (cost of equity 12.19%, levered beta 1.49). At book weights 7.16%, because book debt is 65.8% of book capital after years of buybacks (MO §1).")])

L[14] = ("From Hurdle Rates to Cash Flows", CP, [
    ("What return on capital did your firm generate last year?",
     "14.96% after tax on invested capital of $3,900M (MO §8). Goodwill is 68.6% of that capital."),
    ("If you have returns on capital over time for your firm, is there a trend in those returns?",
     "Rising: 10.83% (2023), 12.41% (2024), 14.96% (2025) (MO §8). Part of the 2025 rise is the LNG equity-earnings jump; removing the $103M increase gives 12.98% (alternatives/margin-ex-lng-uplift-output.md)."),
    ("How do the returns on capital (equity) compare to the costs of capital (equity)?",
     "ROIC 14.96% vs WACC 9.14% (spread 5.82%, EVA $227M); ROE 27.61% vs cost of equity 12.19% (MO §8). ROE is inflated by the small book equity left after buybacks."),
    ("Are the projects in the future likely to look like the projects in the past? Why or why not?",
     "Not for the combined company: after 2027-01-04 KBR will be STS only. STS has higher margins (adjusted EBITDA margin 22.5% vs MTS 10.4%, `facts.segment-adj-ebitda-margin-fy2025`) and the LNG equity earnings, but more commodity-cycle and country risk. MTS returns depend on US defense budgets and recompetes.")])

L[18] = ("Cost of Capital Approach to Optimal Debt Ratio", CP, [
    ("What is your firm's current debt ratio (and cost of capital)?",
     "40% and 9.14% (8.92% on the schedule's synthetic rate) (MO §1, §3)."),
    ("Based upon the cost of capital approach, what is the optimal debt ratio for your firm?",
     "42% on EBIT, 46% on EBIT plus acquisition amortization, 51% on EBITDA (MO §3). With operating income 20% lower the optimum is 34%; 30% lower, 29% (MO §4). Excluding the LNG uplift it is 37% (alternatives/margin-ex-lng-uplift-output.md). On the large-firm table it would be 64% (alternatives/firm-size-large-output.md), but KBR's $4.4B equity value puts it on the small table.")])

L[21] = ("Adjusted Present Value Approach", CP, [
    ("What is the optimal debt ratio using the APV approach?",
     "69% at a 15% bankruptcy cost (`debt.bankruptcy_cost`), 42% at 40% (MO §9). The APV result is unreliable here: tax benefits are counted on all debt at the full rate while the default probabilities jump in coarse Altman steps. The cost-of-capital answer (around 40%) is the one to use.")])

L[22] = ("Moving to the Optimal Debt Ratio", CP, [
    ("Is your firm under, over or correctly levered?",
     "About right today (40% vs a 42% optimum, a $38M value gap, MO §3), but over-levered against a lower or stressed operating income (MO §4) and against peers' median 27% (`peers`)."),
    ("If under levered, is it under threat of a hostile acquisition? If over levered, how imminent is the bankruptcy threat?",
     "Neither. Net leverage 2.3x against a 4.0x covenant (`debt.covenants`); liquidity about $1.0B (Q1 release). Takeover exposure is real on price — EV/EBITDA 7.2x vs peer median 10.7x (MO §7) — but the pending tax-free spin restricts a sale of either part for some time after separation (general tax rule, see read.md Outside knowledge)."),
    ("How good are the potential projects that the company can invest in?",
     "Good on paper: ROIC exceeds WACC by 5.8 points (MO §8). But the recent big 'project' was an acquisition, and goodwill dominates capital."),
    ("What is the best path that you see for your firm to get from its actual to its optimal debt ratio?",
     "No move is needed in total. The issue is the split: the 10-Q says MTS will borrow and pay cash to KBR, and KBR will use it to cut debt (S13). That moves debt onto SpinCo, a steadier US-government cash flow better suited to it, and leaves STS (more cyclical, more foreign) with less. That is the right direction.")])

L[23] = ("Designing the Right Type of Financing", CP, [
    ("Given its asset/project characteristics, what is the right type of debt for your firm?",
     "MTS: medium-term, mostly fixed or hedged USD and GBP debt matched to multi-year US and UK government contracts. STS: shorter, lower total debt in USD, because project and licensing cash flows are lumpy and partly tied to energy capex cycles."),
    ("What are the actual debt characteristics?",
     "Mixed rate (`debt.rate_type`): $2,367M floating bank debt plus $250M fixed notes; about $1.56B swapped to fixed, $955M of which expires in January 2027 (`facts.swaps-expiring-jan-2027`). Weighted maturity 3.3 years (`debt.maturity_years`); USD with a GBP term-loan tranche (`debt.currency`). Term Loan A-2 matures August 2027."),
    ("If there is a mismatch, what is the best way to fix it?",
     "The mismatch is timing, not type: short bank debt and expiring swaps against long contracts. The spin financing is the natural fix — SpinCo issues its own term debt and KBR repays bank debt (S13). Watch for KBR to refinance or extend the facility after the spin, and for interest cost to rise as the 0.89% swap ends.")])

L[26] = ("Assessing Dividend Policy and Free Cash Flow to Equity", CP, [
    ("How much has your company returned to its stockholders, in the form of dividends and stock buybacks in the last five years?",
     "$1,439M over 2022–2025: dividends $301M and buybacks (including warrant settlements) $1,138M (MO §5; 2021 not in the fetched filings)."),
    ("How much cash could your company have returned in the last five years? (Estimate FCFE)",
     "$2,326M by the model's formula (MO §5), but that counts the $745M of 2024 net borrowing that paid for LinQuest without deducting the purchase. Treating acquisitions as capex, FCFE is $1,501M (alternatives/acquisitions-as-capex-output.md)."),
    ("If there is a difference, where is it showing up (cash balances, debt ratios)?",
     "With acquisitions counted, KBR returned about what it generated (returned − FCFE = −$62M). Cash rose $111M (MO §5); debt rose from $1,832M of borrowings (2023) to $2,617M face (2025), almost all for LinQuest.")])

L[27] = ("Assessing Dividend Policy: Trust, Projects, and the Cash Matrix", CP, [
    ("If your firm has returned less cash than it can over time and has a big cash balance, do you trust the firm with your cash?",
     "Not applicable in substance: cash of $500M (`company.cash`) includes $52M in JVs and is 7% of revenue, an operating balance."),
    ("If your firm has returned more cash than it can over time, should it scale back cash return?",
     "It roughly matched FCFE after acquisitions, and has already scaled back: Q1 FY2026 buybacks $4M vs $156M a year earlier; dividend flat (`facts.dividend-quarterly-2026`). With ROIC above WACC (MO §8) and $427M of authorization left (`facts.buyback-authorization-remaining`), the pause reads as spin-related, not as a lack of cash.")])

L[28] = ("Me-Too Dividend Policy and Peer Group Assessment", CP, [
    ("How does your company dividend and cash return policy measure up against other companies in the sector?",
     "Dividend payout 20% of net income ($84M / $415M) against peers 0% (CACI, Parsons), 24% (AECOM), 32% (Booz Allen), 53% (Jacobs) (`peers`). KBR was among the heavier buyers of its own stock until 2026. It is within the sector range; the sector's split between payers and non-payers mirrors the coming KBR split (MTS like the government-services group, STS like the engineering group).")])

L[31] = ("Estimating Growth in Cash Flows", CP, [
    ("What is the historical growth rate in your company's revenues? EBIT? Net income?",
     "Revenue 2022→2025: $6,564M → $7,786M, about 5.9% a year, most of it 2023–2024 and helped by LinQuest; FY2025 +1%. EBIT $343M → $778M; net income $190M → $415M (`company.history`; 2023 net income adjusted for the convertible charge)."),
    ("What are analysts or managers projecting as an expected growth rate in the future?",
     "Management: FY2026 revenue +4% at the midpoint, adjusted EBITDA +4% (`forecast.management_growth`; S21). No analyst consensus is in the sources."),
    ("Assuming that your company continues to earn its current ROIC/ROE and maintaining its existing reinvestment rate, what would the expected growth rate be in earnings?",
     "Close to zero from internal reinvestment: the reinvestment rate is 5.14% ex-acquisition amortization (MO §8) × ROIC 14.96% ≈ 0.8%. Growth beyond that has to come from acquisitions or from capital-light JV earnings. The 4% plan is above what organic reinvestment supports.")])

L[32] = ("Terminal Value in DCF Valuation", CP, [
    ("What return on and cost of capital would you give your firm, when it becomes a mature firm?",
     "Stable ROIC 12% (`forecast.stable_roic`) and a stable cost of capital of 8.02% from beta 1.0 and the peer-median 27% debt ratio (MO §6). At a return equal to the cost of capital value is $42.24; at 15%, $55.21 (MO §6). Using the 42% optimum as the stable debt ratio raises value to $62.02 (alternatives/stable-debt-at-optimum-output.md).")])

L[34] = ("Stories, Numbers, and the Disney DCF Valuation", CP, [
    ("What is the status quo value of your firm?",
     "$51.49 per share against $34.53 (1.49x) (MO §6), on guidance-midpoint revenue, 4% growth and a 10% margin. The market price matches the flat-revenue, 8.5%-margin case ($34.94, MO §6) — the market is pricing the LNG earnings and EUCOM work as fading and no growth."),
    ("What is the value of your firm with these changes made?",
     "Financing lever only: $52.24 at the optimal cost of capital (MO §6), a $0.75 gain. The bigger change on the table is the separation itself, which this single-company model cannot value; the board's case is that two pure plays re-rate toward peer multiples (EV/EBITDA peer median 10.7x vs KBR 7.2x, implying $61.10, MO §7)."),
    ("What is the likelihood that this change will happen?",
     "High for the spin: board-approved, dated (2027-01-04), executive pay tied to it (S5), leadership named for New KBR and an interim SpinCo CEO in place (S3, S4). Not certain: it still needs the IRS ruling or opinion, Form 10 effectiveness and final board approval (S10).")])

L[35] = ("Pricing vs. Valuation: Using Multiples", CP, [
    ("Based upon the multiple and comparables, what price would you attach to your company?",
     "EV/EBITDA is the multiple to price on (services, different leverage). Peer median 10.73x implies $61.10; EV/Revenue implies $42.62 (MO §7). P/E 10.6x vs 18.2x peer median. KBR trades at a discount on every multiple; even at a sum-of-parts discount of a third to the median, the price is below the implied value.")])

L[36] = ("Course Review: Lessons Learned and Ten Principles", CP, [
    ("What is the narrative that you would use to describe your company, as its run today?",
     "A mature, acquisition-built government-services company bolted to a higher-margin energy technology business, earning about 15% on capital and borrowed to its optimum, whose stock has fallen below where it bought back shares a year ago. Management has stopped buybacks and dividend growth to get a tax-free separation done on 2027-01-04, with SpinCo borrowing to pay KBR's debt down. The market prices it as if earnings will shrink.")])

for n, (title, heading, qs) in L.items():
    body = FM.format(n=n, t=title) + "### Lesson {:02d} — {}\n\n".format(n, title)
    body += "Quick mode: only the question-bank entries tagged with a signal are answered; transcript-layer entries carry no signal and are not part of this run.\n\n"
    body += "## {}\n\n".format(heading)
    for q, a in qs:
        body += "- **{}**\n  {}\n\n".format(q, a)
    body += "## Notes\n\nNumbers cite `inputs.yaml` fields, `model-output.md` sections (MO §n), `alternatives/` runs, and stated passages (S#) in `sources/statements/kbr-stated-positions.md`.\n"
    with open(os.path.join(HERE, "lesson-{:02d}.md".format(n)), "w") as fh:
        fh.write(body)
print(len(L), "lesson files")
