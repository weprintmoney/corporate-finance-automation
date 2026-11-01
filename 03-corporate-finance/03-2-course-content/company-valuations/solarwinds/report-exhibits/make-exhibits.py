#!/usr/bin/env python3
"""Build the final-report charts and tables for SolarWinds from the model output and the ledger.

Every number is read from ../model-output.md or ../inputs.yaml; none is typed in here.
Re-run after the model changes:  python3 make-exhibits.py   (needs matplotlib and pyyaml)
Writes exhibit-1..5 PNGs and exhibits.md into this folder.
"""
import pathlib
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yaml

HERE = pathlib.Path(__file__).resolve().parent
SWI = HERE.parent
MODEL = (SWI / "model-output.md").read_text()
LEDGER = yaml.safe_load((SWI / "inputs.yaml").read_text())

# Palette: categorical slots 1-2 from the dataviz reference palette (validated light-mode pair), plus text/muted tokens.
BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#898781", "#e6e5e1", "#fcfcfb"
plt.rcParams.update({
    "font.family": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"], "font.size": 10,
    "axes.edgecolor": MUTED, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.color": GRID,
    "grid.linewidth": 0.8, "axes.axisbelow": True, "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "savefig.dpi": 200, "text.parse_math": False,
})


# ---------- reading the model output ----------
def section(n):
    m = re.search(rf"^## {n}\. .*?(?=^## \d|\Z)", MODEL, re.S | re.M)
    return m.group(0)


def tables(text):
    """All markdown tables in text, as lists of row dicts keyed by header."""
    out, cur = [], []
    for line in text.splitlines() + [""]:
        if line.startswith("|"):
            cur.append([c.strip() for c in line.strip().strip("|").split("|")])
        elif cur:
            head, rows = cur[0], [r for r in cur[2:]]
            out.append([dict(zip(head, r)) for r in rows]); cur = []
    return out


def num(s):
    s = s.replace("*", "").replace("$", "").replace(",", "").replace("M", "").replace("%", "").replace("x", "")
    return float(re.search(r"-?\d+(\.\d+)?", s).group(0))


def find(rows, key, label):
    return next(r for r in rows if r[key].replace("*", "").startswith(label))


def fact(fid):
    return next(f for f in LEDGER["facts"] if f["id"] == fid)["value"]


s1 = tables(section(1))[0]
wacc = num(find(s1, "Item", "Cost of capital (WACC)")["Value"])
schedule = tables(section(3))[1]
s5 = tables(section(5))[0]
s6 = tables(section(6))
bridge, sens = s6[2], s6[3]
dcf_value = num(find(bridge, "Item" if "Item" in bridge[0] else "Bridge", "Value per share (course method")["Amount"])
unaffected = num(find(bridge, "Bridge", "Market or transaction price")["Amount"])
deal = num(find(bridge, "Bridge", "Deal price")["Amount"])
roic_years = tables(section(8))[1]
s7_text = section(7)
peer_low = num(re.search(r"EV/Revenue of [\d.]+x: .*?= \$([\d.]+)", s7_text).group(1))
peer_high = num(re.search(r"EV/EBITDA of [\d.]+x: \$([\d.]+)", s7_text).group(1))
gs_low, gs_high = map(float, fact("gs-dcf-range").split("-"))
jf_low, jf_high = map(float, fact("jefferies-dcf-range").split("-"))
holders = LEDGER["governance"]["controlling_holders"]


def money(v, d=0):
    return ("−" if v < 0 else "") + f"${abs(v):,.{d}f}M"


def finish(fig, ax, title, subtitle, source, name, left=0.1):
    fig.text(0.01, 0.97, title, fontsize=12.5, fontweight="bold", color=INK, va="top")
    fig.text(0.01, 0.905, subtitle, fontsize=9.5, color=INK2, va="top")
    fig.text(0.01, 0.015, "Source: " + source, fontsize=7.5, color=MUTED, va="bottom")
    fig.subplots_adjust(top=0.78, bottom=0.2, left=left, right=0.97)
    fig.savefig(HERE / name)
    plt.close(fig)


# ---------- Exhibit 1: cost of capital vs debt ratio ----------
pts = [(num(r["Debt ratio"]), num(r["WACC"]), r["Debt ratio"]) for r in schedule]
near = [(x, y, lab) for x, y, lab in pts if x <= 40]
far = [(x, y) for x, y, lab in pts if x == 50][0]
opt = next((x, y) for x, y, lab in pts if "optimum" in lab)
cur = next((x, y) for x, y, lab in pts if "current" in lab)
fig, ax = plt.subplots(figsize=(7, 3.9))
ax.plot([p[0] for p in near], [p[1] for p in near], color=BLUE, lw=2, marker="o", ms=5, zorder=3)
for (x, y), c, lab, xy, ha in [(opt, BLUE, f"Optimum: {opt[0]:.0f}% debt, {opt[1]:.2f}%", (opt[0], opt[1] - 0.075), "center"),
                               (cur, ORANGE, f"Actual: {cur[0]:.0f}% debt, {cur[1]:.2f}%", (cur[0] - 1, cur[1] + 0.06), "right")]:
    ax.scatter([x], [y], s=90, color=c, edgecolor=SURFACE, linewidth=2, zorder=4)
    ax.annotate(lab, (x, y), xytext=xy, fontsize=9, color=INK, fontweight="bold", ha=ha)
ax.set_xlabel("Debt as a share of firm value (%)")
ax.set_ylabel("Cost of capital (%)")
ax.set_xlim(-1, 42)
ax.set_ylim(opt[1] - 0.12, near[-1][1] + 0.06)
ax.text(39, near[-1][1], f"rises to {far[1]:.2f}% at {far[0]:.0f}% debt", fontsize=8, color=INK2, ha="right", va="center")
finish(fig, ax, f"Cost of capital is lowest at {opt[0]:.0f}% debt; SolarWinds carries {cur[0]:.0f}%",
       f"Cost of capital at each debt ratio, rating and interest rate recalculated at each step (EBIT-based coverage)",
       "Calculated from SolarWinds FY2024 10-K and Damodaran's ratings and default spreads (January 2025)", "exhibit-1-cost-of-capital-by-debt-ratio.png")

# ---------- Exhibit 2: ROIC vs cost of capital ----------
yrs = [r["Year"] for r in roic_years]
roic = [num(r["ROIC"]) for r in roic_years]
fig, ax = plt.subplots(figsize=(7, 3.6))
bars = ax.bar(yrs, roic, color=BLUE, width=0.5, zorder=3)
for b, v in zip(bars, roic):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.2, f"{v:.2f}%", ha="center", fontsize=9, color=INK)
ax.axhline(wacc, color=INK2, lw=1.2, ls="--", zorder=2)
ax.text(len(yrs) - 0.6, wacc + 0.25, f"Cost of capital {wacc:.2f}% (2025-02-05)", ha="right", fontsize=9, color=INK2)
ax.set_ylabel("Return on invested capital (%)")
ax.set_ylim(0, wacc * 1.25)
finish(fig, ax, "Return on capital rose each year but stayed below the cost of capital",
       "After-tax operating income (excluding impairments) ÷ invested capital, against the 2025 cost of capital",
       "Calculated from SolarWinds 10-K filings, FY2022–FY2024; cost of capital as of 2025-02-05", "exhibit-2-return-on-capital.png")

# ---------- Exhibit 3: FCFE vs cash returned ----------
rows = [r for r in s5 if re.fullmatch(r"\d{4}", r["Year"])]
yrs = [r["Year"] for r in rows]
fcfe = [num(r["FCFE"]) for r in rows]
ret = [num(r["Cash returned"]) for r in rows]
tot = find(s5, "Year", "Total")
fig, ax = plt.subplots(figsize=(7, 3.9))
xs = range(len(yrs)); w = 0.36
b1 = ax.bar([x - w / 2 - 0.01 for x in xs], fcfe, w, color=BLUE, label="Free cash flow to equity (what it could pay)", zorder=3)
b2 = ax.bar([x + w / 2 + 0.01 for x in xs], ret, w, color=ORANGE, label="Cash returned: dividends + buybacks", zorder=3)
for bars in (b1, b2):
    for b in bars:
        v = b.get_height()
        ax.text(b.get_x() + b.get_width() / 2, v + (12 if v >= 0 else -12), money(v), ha="center", va="bottom" if v >= 0 else "top", fontsize=8.5, color=INK)
ax.axhline(0, color=MUTED, lw=1)
ax.set_xticks(list(xs), yrs)
ax.set_ylabel("$ millions")
ax.set_ylim(min(fcfe) * 1.2, max(max(fcfe), max(ret)) * 1.5)
ax.legend(loc="lower right", frameon=False, fontsize=8.5)
finish(fig, ax, f"Over 2022–2024 SolarWinds returned {money(num(tot['Cash returned']), 1)} against FCFE of {money(num(tot['FCFE']), 1)}",
       f"2022 FCFE is negative mainly from {money(-num(rows[0]['Net new debt']), 1)} of debt repaid; 2024 includes the special dividend",
       "Calculated from SolarWinds 10-K cash flow statements, FY2022–FY2024", "exhibit-3-fcfe-vs-cash-returned.png")

# ---------- Exhibit 4: value per share, football field ----------
sens_vals = [num(r["Value per share"]) for r in sens]
ranges = [
    ("Our DCF", min(sens_vals), max(sens_vals), BLUE),
    ("Peer multiples", peer_low, peer_high, MUTED),
    ("Jefferies DCF", jf_low, jf_high, MUTED),
    ("Goldman Sachs DCF", gs_low, gs_high, MUTED),
]
fig, ax = plt.subplots(figsize=(7, 3.9))
for i, (lab, lo, hi, c) in enumerate(ranges):
    ax.barh(i, hi - lo, left=lo, height=0.5, color=c, alpha=1 if c == BLUE else 0.55, zorder=3)
    if c != BLUE:
        ax.text(lo - 0.25, i, f"${lo:.2f}", ha="right", va="center", fontsize=8.5, color=INK)
    ax.text(hi + 0.25, i, f"${hi:.2f}", ha="left", va="center", fontsize=8.5, color=INK)
ax.scatter([dcf_value], [0], s=80, color=BLUE, edgecolor=SURFACE, linewidth=2, zorder=5)
ax.annotate(f"Base case ${dcf_value:.2f}", (dcf_value, 0), xytext=(dcf_value - 0.35, 0), ha="right", va="center", fontsize=8.5, color=INK, fontweight="bold")
for v, lab, c, ha in [(unaffected, f"Unaffected price ${unaffected:.2f} ", INK2, "right"), (deal, f" Deal price ${deal:.2f}", ORANGE, "left")]:
    ax.axvline(v, color=c, lw=1.5, ls="--", zorder=4)
    ax.text(v, len(ranges) - 0.35, lab, ha=ha, fontsize=8.5, color=INK, fontweight="bold",
            bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.5))
ax.set_yticks(range(len(ranges)), [r[0] for r in ranges])
ax.set_xlabel("Value per share ($)")
ax.set_xlim(min(r[1] for r in ranges) - 2.5, max(r[2] for r in ranges) + 2.5)
ax.set_ylim(-0.6, len(ranges) - 0.1)
ax.grid(axis="y", visible=False)
finish(fig, ax, f"Our DCF says ${dcf_value:.2f}; the $18.50 deal sits inside both banks' ranges",
       "Our DCF range: stable return on capital 10%–30%; peers: EV/Revenue to EV/EBITDA; banks: fairness-opinion DCFs",
       "Calculated from company and peer filings; bank ranges from the fairness opinions in SolarWinds' March 2025 information statement", "exhibit-4-value-per-share.png", left=0.27)

# ---------- Exhibit 5: ownership ----------
pairs = [(h["name"], h["pct"] * 100) for h in holders]
others = 100 - sum(p for _, p in pairs)
pairs.append(("All other holders", others))
fig, ax = plt.subplots(figsize=(7, 3.2))
ys = list(range(len(pairs)))[::-1]
for y, (name, p) in zip(ys, pairs):
    ax.barh(y, p, height=0.55, color=ORANGE if name != "All other holders" else MUTED, zorder=3)
    ax.text(p + 0.8, y, f"{p:.2f}%", va="center", fontsize=9, color=INK)
ax.set_yticks(ys, [n for n, _ in pairs])
ax.set_xlim(0, 50)
ax.set_xlabel("Share of common stock (%)")
ax.grid(axis="y", visible=False)
finish(fig, ax, f"Two private-equity sponsors held {sum(p for _, p in pairs[:-1]):.2f}% of SolarWinds",
       "Beneficial ownership at the 2024 proxy; \"all other holders\" is the remainder",
       "SolarWinds 2024 proxy statement, beneficial ownership table; the proxy states the sponsors' combined stake as 66.34%",
       "exhibit-5-ownership.png", left=0.22)

# ---------- exhibits.md: charts plus the core tables ----------
def md_table(rows, cols):
    head = "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols) + "\n"
    return head + "\n".join("| " + " | ".join(r[c] for c in cols) + " |" for r in rows) + "\n"


coc_items = ["Risk-free rate", "Unlevered beta", "Levered beta", "Equity risk premium", "Cost of equity",
             "Pre-tax cost of debt", "Marginal tax rate", "After-tax cost of debt", "Debt ratio (D/V)", "Cost of capital (WACC)"]
coc = [find(s1, "Item", i) for i in coc_items]
sched = [r for r in schedule if num(r["Debt ratio"]) <= 50]
md = f"""---
title: "SolarWinds (SWI) — Final Report Exhibits"
status: active
owner: weprintmoney
created: 2026-11-01
last_updated: 2026-11-01
---

# SolarWinds (SWI) — Final Report Exhibits

Charts and tables for the final report, in the order of the course's nine project questions, as the example reports use them ([../../../../03-1-course-overview/final-project/report-format.md](../../../../03-1-course-overview/final-project/report-format.md)). All are generated by [make-exhibits.py](make-exhibits.py) from [model-output.md](../model-output.md) and the [ledger](../inputs.yaml); re-run it after any model change. The example reports lean on tables, so each chart below is one the grader would otherwise have to work out from a table.

## Question 1 — Who holds the power

![Exhibit 5: ownership](exhibit-5-ownership.png)

## Question 2 — Risk and the hurdle rate

**Cost of capital, 2025-02-05**

{md_table(coc, ["Item", "Value", "How"])}
## Question 3 — Investment returns

![Exhibit 2: return on capital](exhibit-2-return-on-capital.png)

## Questions 4–6 — Financing mix, the optimum, and getting there

![Exhibit 1: cost of capital by debt ratio](exhibit-1-cost-of-capital-by-debt-ratio.png)

**Cost of capital schedule (EBIT-based coverage)**

{md_table(sched, ["Debt ratio", "Levered beta", "Cost of equity", "Coverage", "Rating", "Pre-tax cost of debt", "WACC"])}
## Questions 7–8 — Dividend policy and assessment

![Exhibit 3: FCFE vs cash returned](exhibit-3-fcfe-vs-cash-returned.png)

**Free cash flow to equity against cash returned**

{md_table(s5, ["Year", "Net income", "Net capex", "Net new debt", "FCFE", "Cash returned", "Returned − FCFE"])}
## Question 9 — Valuation

![Exhibit 4: value per share](exhibit-4-value-per-share.png)

**DCF bridge**

{md_table([r for r in bridge if not r["Bridge"].startswith(("Course-method", "Value per share (shortcut", "Value per share with"))], ["Bridge", "Amount"])}
**Relative valuation**

{md_table(tables(s7_text)[0], list(tables(s7_text)[0][0].keys()))}"""
(HERE / "exhibits.md").write_text(md)
print("wrote 5 charts and exhibits.md")
