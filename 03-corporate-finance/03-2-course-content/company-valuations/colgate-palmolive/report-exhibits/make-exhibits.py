"""Draw the four exhibits for the Colgate-Palmolive final report.

Run from the company folder:  python3 report-exhibits/make-exhibits.py
Reads sources/market-data/cl-vs-sp500-monthly-2020-12-to-2026-11.tsv and model-output.md; the remaining
figures are in professor-spreadsheet/results.md and the ledger (facts.ginzu-sensitivities).
"""
import csv, re, sys, site
sys.path.append(site.getusersitepackages())
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#e4e3df", "#ffffff"
plt.rcParams.update({"font.family": "Arial", "font.size": 10, "axes.edgecolor": GRID, "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False, "axes.spines.right": False,
                     "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE})

def finish(fig, ax, title, source, name):
    ax.set_title(title, loc="left", fontsize=11.5, fontweight="bold", color=INK, pad=12)
    ax.grid(axis="y", color=GRID, linewidth=0.8); ax.set_axisbelow(True)
    ax.tick_params(length=0)
    fig.text(0.01, 0.01, source, fontsize=7.5, color=MUTED, ha="left", va="bottom")
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(f"report-exhibits/{name}.png", dpi=200); plt.close(fig)

# 1. Total return, Colgate against the S&P 500
rows = [r for r in csv.DictReader(open("sources/market-data/cl-vs-sp500-monthly-2020-12-to-2026-11.tsv"), delimiter="\t") if r["month"] >= "2020-12"]
cl = [float(r["cl_adj_close"]) for r in rows]; sp = [float(r["sp500_total_return"]) for r in rows]
cl = [100 * v / cl[0] for v in cl]; sp = [100 * v / sp[0] for v in sp]
x = list(range(len(rows)))
fig, ax = plt.subplots(figsize=(6.5, 3.4))
ax.plot(x, sp, color=ORANGE, linewidth=2, label="S&P 500"); ax.plot(x, cl, color=BLUE, linewidth=2, label="Colgate-Palmolive")
ax.annotate(f"S&P 500  {sp[-1]:.0f}", (x[-1], sp[-1]), xytext=(6, 0), textcoords="offset points", va="center", color=INK, fontsize=9)
ax.annotate(f"Colgate  {cl[-1]:.0f}", (x[-1], cl[-1]), xytext=(6, 0), textcoords="offset points", va="center", color=INK, fontsize=9)
ticks = [i for i, r in enumerate(rows) if r["month"].endswith("-12")]
ax.set_xticks(ticks); ax.set_xticklabels(["Dec " + rows[i]["month"][:4] for i in ticks]); ax.set_xlim(0, len(rows) + 9)
ax.set_ylabel("Value of 100 invested, dividends reinvested"); ax.legend(frameon=False, loc="upper left", fontsize=9)
finish(fig, ax, "Exhibit 1. Colgate and the S&P 500, December 2020 to November 2026", "Source: Yahoo Finance, dividend-adjusted month-end closes; last point 2026-11-20.", "exhibit-1-total-return")

# 2. Cost of capital by debt ratio
sched = []
for line in open("model-output.md"):
    m = re.match(r"\| (\d+)%[^|]*\|.*\| ([\d.]+)% \|\s*$", line)
    if m and "x |" in line or (m and "n/a" in line): sched.append((int(m.group(1)), float(m.group(2))))
sched = [s for s in dict(sched).items() if s[0] <= 50 and s[0] != 10]; sched.sort()
fig, ax = plt.subplots(figsize=(6.5, 3.4))
ax.plot([s[0] for s in sched], [s[1] for s in sched], color=BLUE, linewidth=2, marker="o", markersize=5)
for d, w in sched:
    lab = {9: "Today\n9.34% debt", 20: f"Recommended 20%\n{w:.2f}%", 30: f"Lowest 30%\n{w:.2f}%"}.get(d)
    if lab: ax.annotate(lab, (d, w), xytext=(0, 14), textcoords="offset points", ha="center", color=INK, fontsize=8.5)
ax.annotate(f"{sched[-2][1]:.2f}%", (sched[-2][0], sched[-2][1]), xytext=(-8, 4), textcoords="offset points", ha="right", color=INK, fontsize=8.5)
ax.annotate(f"{sched[-1][1]:.2f}%", (sched[-1][0], sched[-1][1]), xytext=(-8, 0), textcoords="offset points", ha="right", color=INK, fontsize=8.5)
ax.set_xlabel("Debt as a share of firm value"); ax.set_ylabel("Cost of capital"); ax.set_ylim(7, 16)
ax.set_xticks([0, 10, 20, 30, 40, 50]); ax.set_xticklabels([f"{v}%" for v in [0, 10, 20, 30, 40, 50]])
ax.set_yticks(range(7, 17, 2)); ax.set_yticklabels([f"{v}%" for v in range(7, 17, 2)])
finish(fig, ax, "Exhibit 2. Cost of capital at each debt ratio", "Source: Colgate 10-K for 2025; Damodaran ratings spread table, January 2026. All debt repriced at each ratio.", "exhibit-2-cost-of-capital")

# 3. Cash returned against free cash flow to equity
years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
fcfe = [1449, 2251, 2281, 2409, 2518, 2314, 2885, 2712]
ret = [2829, 2816, 3130, 2999, 2999, 2877, 3528, 3033]
opt = [329, 498, 874, 424, 418, 380, 638, 101]
net = [r - o for r, o in zip(ret, opt)]
fig, ax = plt.subplots(figsize=(6.5, 3.4)); w = 0.26
for off, vals, col, lab in ((-w, fcfe, BLUE, "Free cash flow to equity"), (0, ret, ORANGE, "Dividends plus buybacks"), (w, net, AQUA, "Same, less cash from option exercises")):
    ax.bar([i + off for i in range(len(years))], vals, width=w - 0.03, color=col, label=lab)
ax.set_xticks(range(len(years))); ax.set_xticklabels(years); ax.set_ylabel("$ millions")
ax.set_ylim(0, 5200); ax.legend(frameon=False, fontsize=8.5, ncol=1, loc="upper left", handlelength=1.2)
finish(fig, ax, "Exhibit 3. Cash returned against free cash flow to equity, 2018–2025", "Source: Colgate 10-K cash flow statements. Free cash flow to equity as defined in the professor's dividend spreadsheet.", "exhibit-3-cash-returned")

# 4. Value per share by the two long-run assumptions
fig, ax = plt.subplots(figsize=(6.5, 3.4)); w = 0.34
groups = ["New investment earns\nits cost (8.43%)", "New investment\nearns 20%"]
g3, g482 = [51.84, 61.83], [53.82, 79.74]
b1 = ax.bar([i - w / 2 for i in range(2)], g3, width=w - 0.03, color=BLUE, label="Growth forever 3%")
b2 = ax.bar([i + w / 2 for i in range(2)], g482, width=w - 0.03, color=ORANGE, label="Growth forever 4.82%")
for bars in (b1, b2):
    for b in bars: ax.annotate(f"${b.get_height():.2f}", (b.get_x() + b.get_width() / 2, b.get_height()), xytext=(0, 3), textcoords="offset points", ha="center", color=INK, fontsize=9)
ax.axhline(98.71, color=MUTED, linewidth=1.2, linestyle=(0, (4, 3))); ax.annotate("Share price $98.71", (1.45, 98.71), xytext=(0, 4), textcoords="offset points", ha="right", color=INK, fontsize=9)
ax.set_xticks(range(2)); ax.set_xticklabels(groups); ax.set_ylabel("Value per share"); ax.set_ylim(0, 138); ax.set_xlim(-0.6, 1.6)
ax.set_yticks(range(0, 121, 20)); ax.set_yticklabels([f"${v}" for v in range(0, 121, 20)])
ax.legend(frameon=False, fontsize=9, loc="upper left", ncol=2)
finish(fig, ax, "Exhibit 4. Value per share under the two long-run assumptions", "Source: the professor's valuation spreadsheet, filled from the 10-K, 10-Q, S&P Capital IQ consensus and Damodaran's datasets.", "exhibit-4-value-per-share")
print("ok", [s for s in sched])
