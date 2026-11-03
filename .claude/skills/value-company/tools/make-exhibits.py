#!/usr/bin/env python3
"""Charts for a /value-company read, built from a company's model-output.md and inputs.yaml.

Every number is read from those two files; none is typed in here, so the charts rebuild after any
model change. Generalizes company-valuations/solarwinds/report-exhibits/make-exhibits.py.

Charts (key: file):
  cost-of-capital  exhibit-cost-of-capital.png   cost of capital at each debt ratio; actual vs. optimum   [core]
  returns          exhibit-returns.png           return on capital by year against the cost of capital    [core]
  payout           exhibit-payout.png            free cash flow to equity against cash returned
  value            exhibit-value.png             value per share by method against the market (and deal) price
  ownership        exhibit-ownership.png         controlling holders' stakes (only if the ledger lists any)

Usage:
  python3 make-exhibits.py <company-folder>                 # core charts into <company-folder>/exhibits/
  python3 make-exhibits.py <company-folder> --all           # every chart the data supports
  python3 make-exhibits.py <company-folder> --charts value,payout --out /tmp/x
Needs matplotlib and pyyaml. A chart whose data is missing from the model output is skipped with a
message, never drawn from defaults.
"""
import argparse
import pathlib
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yaml

CORE = ["cost-of-capital", "returns"]
ALL = ["cost-of-capital", "returns", "payout", "value", "ownership"]

# Palette: categorical slots 1-2 from the dataviz reference palette (a validated light-mode pair), plus text tokens.
BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#898781", "#e6e5e1", "#fcfcfb"
plt.rcParams.update({
    "font.family": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"], "font.size": 10,
    "axes.edgecolor": MUTED, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.color": GRID,
    "grid.linewidth": 0.8, "axes.axisbelow": True, "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "savefig.dpi": 200, "text.parse_math": False,
})


class Missing(Exception):
    pass


# ---------- reading the model output and ledger ----------
def section(model, n):
    m = re.search(rf"^## {n}\. .*?(?=^## \d|\Z)", model, re.S | re.M)
    if not m:
        raise Missing(f"model-output.md has no section {n}")
    return m.group(0)


def tables(text):
    """All markdown tables in text, as lists of row dicts keyed by header."""
    out, cur = [], []
    for line in text.splitlines() + [""]:
        if line.startswith("|"):
            cur.append([c.strip() for c in line.strip().strip("|").split("|")])
        elif cur:
            out.append([dict(zip(cur[0], r)) for r in cur[2:]])
            cur = []
    return out


def table_with(ts, header):
    for tb in ts:
        if tb and header in tb[0]:
            return tb
    raise Missing(f"no table with a '{header}' column")


def num(s):
    s = s.replace("*", "").replace("$", "").replace(",", "").replace("M", "").replace("%", "").replace("x", "").replace("−", "-")
    m = re.search(r"-?\d+(\.\d+)?", s)
    if not m:
        raise Missing(f"no number in '{s}'")
    return float(m.group(0))


def row(rows, key, label):
    for r in rows:
        if r[key].replace("*", "").startswith(label):
            return r
    raise Missing(f"no row starting '{label}'")


def lv(x):
    return x.get("value") if isinstance(x, dict) and "value" in x else x


def money(v, d=0):
    return ("−" if v < 0 else "") + f"${abs(v):,.{d}f}M"


class Ctx:
    def __init__(self, folder):
        self.folder = folder
        self.model = (folder / "model-output.md").read_text()
        self.L = yaml.safe_load((folder / "inputs.yaml").read_text())
        meta = self.L.get("meta", {})
        self.name = lv(meta.get("company")) or folder.name
        self.short = self.name.replace(" Corporation", "").replace(" Inc.", "").replace(", Inc.", "").replace(" Inc", "")
        self.poss = self.short + ("'" if self.short.endswith("s") else "'s")
        self.date = str(lv(meta.get("analysis_date")))
        self.base_year = lv(meta.get("base_year"))

    def wacc(self):
        s1 = table_with(tables(section(self.model, 1)), "Item")
        return num(row(s1, "Item", "Cost of capital (WACC)")["Value"])


def finish(fig, title, subtitle, source, path, left=0.1):
    fig.text(0.01, 0.97, title, fontsize=12.5, fontweight="bold", color=INK, va="top")
    fig.text(0.01, 0.905, subtitle, fontsize=9.5, color=INK2, va="top")
    fig.text(0.01, 0.015, "Source: " + source, fontsize=7.5, color=MUTED, va="bottom")
    fig.subplots_adjust(top=0.78, bottom=0.2, left=left, right=0.97)
    fig.savefig(path)
    plt.close(fig)


# ---------- charts ----------
def cost_of_capital(c, path):
    sched = table_with(tables(section(c.model, 3)), "Debt ratio")
    pts = [(num(r["Debt ratio"]), num(r["WACC"]), r["Debt ratio"]) for r in sched]
    opt = next(((x, y) for x, y, lab in pts if "optimum" in lab), None)
    cur = next(((x, y) for x, y, lab in pts if "current" in lab), opt)
    if opt is None:
        raise Missing("schedule marks no optimum")
    cap = max(40, cur[0] + 10)
    near = [(x, y) for x, y, _ in pts if x <= cap]
    far = [(x, y) for x, y, _ in pts if x > cap]
    fig, ax = plt.subplots(figsize=(7, 3.9))
    ax.plot([p[0] for p in near], [p[1] for p in near], color=BLUE, lw=2, marker="o", ms=5, zorder=3)
    marks = [(opt, BLUE, f"Optimum: {opt[0]:.0f}% debt, {opt[1]:.2f}%", (opt[0], opt[1] - 0.075), "center")]
    if cur != opt:
        marks.append((cur, ORANGE, f"Actual: {cur[0]:.0f}% debt, {cur[1]:.2f}%", (cur[0] - 1, cur[1] + 0.06), "right"))
    for (x, y), col, lab, xy, ha in marks:
        ax.scatter([x], [y], s=90, color=col, edgecolor=SURFACE, linewidth=2, zorder=4)
        ax.annotate(lab, (x, y), xytext=xy, fontsize=9, color=INK, fontweight="bold", ha=ha)
    ax.set_xlabel("Debt as a share of firm value (%)")
    ax.set_ylabel("Cost of capital (%)")
    ax.set_xlim(-1, cap + 2)
    ax.set_ylim(opt[1] - 0.12, max(y for _, y in near) + 0.06)
    if far:
        ax.text(near[-1][0] - 1.5, near[-1][1], f"rises to {far[0][1]:.2f}% at {far[0][0]:.0f}% debt", fontsize=8, color=INK2, ha="right", va="center")
    if cur == opt:
        title = f"{c.short} carries about its optimal debt ratio, {opt[0]:.0f}%"
    elif cur[0] > opt[0]:
        title = f"Cost of capital is lowest at {opt[0]:.0f}% debt; {c.short} carries {cur[0]:.0f}%"
    else:
        title = f"Cost of capital is lowest at {opt[0]:.0f}% debt; {c.short} carries only {cur[0]:.0f}%"
    rt = lv(c.L.get("market", {}).get("ratings_table")) or ""
    finish(fig, title,
           "Cost of capital at each debt ratio; rating and interest rate recalculated at each step",
           f"Calculated from {c.poss} FY{c.base_year} filings and Damodaran's ratings and default spreads"
           + (f" ({pathlib.Path(str(rt)).stem.replace('ratings-spreads-', '')})" if rt else ""), path)
    return title


def returns(c, path):
    s8 = tables(section(c.model, 8))
    by_year = next((tb for tb in s8 if tb and "ROIC" in tb[0] and "Year" in tb[0]), None)
    if not by_year:
        raise Missing("section 8 has no by-year ROIC table (company.history)")
    wacc = c.wacc()
    yrs = [r["Year"] for r in by_year]
    roic = [num(r["ROIC"]) for r in by_year]
    fig, ax = plt.subplots(figsize=(7, 3.6))
    bars = ax.bar(yrs, roic, color=[BLUE if v < wacc else ORANGE for v in roic], width=0.5, zorder=3)
    for b, v in zip(bars, roic):
        ax.text(b.get_x() + b.get_width() / 2, v + (0.2 if v >= 0 else -0.2), f"{v:.2f}%", ha="center",
                va="bottom" if v >= 0 else "top", fontsize=9, color=INK)
    ax.axhline(wacc, color=INK2, lw=1.2, ls="--", zorder=2)
    ax.text(len(yrs) - 0.6, wacc + 0.25, f"Cost of capital {wacc:.2f}% ({c.date})", ha="right", fontsize=9, color=INK2)
    ax.set_ylabel("Return on invested capital (%)")
    ax.set_ylim(min(0, min(roic) * 1.2), max(wacc, max(roic)) * 1.25)
    above = sum(v >= wacc for v in roic)
    if above == 0:
        title = "Return on capital stayed below the cost of capital every year"
    elif above == len(roic):
        title = "Return on capital beat the cost of capital every year"
    else:
        title = f"Return on capital beat the cost of capital in {above} of {len(roic)} years"
    finish(fig, title,
           "After-tax operating income (excluding impairments) ÷ invested capital, against today's cost of capital",
           f"Calculated from {c.poss} filings, FY{yrs[0]}–FY{yrs[-1]}; cost of capital as of {c.date}", path)
    return title


def payout(c, path):
    s5 = table_with(tables(section(c.model, 5)), "FCFE")
    rows = [r for r in s5 if re.fullmatch(r"\d{4}", r["Year"])]
    if not rows:
        raise Missing("section 5 has no yearly rows")
    yrs = [r["Year"] for r in rows]
    fcfe = [num(r["FCFE"]) for r in rows]
    ret = [num(r["Cash returned"]) for r in rows]
    fig, ax = plt.subplots(figsize=(7, 3.9))
    xs = range(len(yrs)); w = 0.36
    b1 = ax.bar([x - w / 2 - 0.01 for x in xs], fcfe, w, color=BLUE, label="Free cash flow to equity (what it could pay)", zorder=3)
    b2 = ax.bar([x + w / 2 + 0.01 for x in xs], ret, w, color=ORANGE, label="Cash returned: dividends + buybacks", zorder=3)
    span = max(max(fcfe), max(ret)) - min(0, min(fcfe))
    for bars in (b1, b2):
        for b in bars:
            v = b.get_height()
            ax.text(b.get_x() + b.get_width() / 2, v + (0.02 if v >= 0 else -0.02) * span, money(v), ha="center",
                    va="bottom" if v >= 0 else "top", fontsize=8.5, color=INK)
    ax.axhline(0, color=MUTED, lw=1)
    ax.set_xticks(list(xs), yrs)
    ax.set_ylabel("$ millions")
    ax.set_ylim(min(0, min(fcfe)) * 1.2 - 0.05 * span, max(max(fcfe), max(ret)) * 1.5)
    ax.legend(loc="lower right" if min(fcfe) < 0 else "upper left", frameon=False, fontsize=8.5)
    tf, tr = sum(fcfe), sum(ret)
    if tf <= 0:
        title = f"{yrs[0]}–{yrs[-1]}: {c.short} returned {money(tr, 1)} while FCFE totaled {money(tf, 1)}"
    else:
        verb = "more than" if tr > tf else "less than"
        title = f"{yrs[0]}–{yrs[-1]}: {c.short} returned {money(tr, 1)}, {verb} its {money(tf, 1)} of FCFE"
    finish(fig, title, "Free cash flow to equity against dividends and buybacks, by year",
           f"Calculated from {c.poss} cash flow statements, FY{yrs[0]}–FY{yrs[-1]}", path)
    return title


def value(c, path):
    s6 = tables(section(c.model, 6))
    bridge = table_with(s6, "Bridge")
    dcf = num(row(bridge, "Bridge", "Value per share (course method")["Amount"])
    price = next((num(r["Amount"]) for r in bridge if r["Bridge"].startswith("Market or transaction price")), None)
    deal = next((num(r["Amount"]) for r in bridge if r["Bridge"].startswith("Deal price")), None)
    ranges = []
    lo, hi = dcf, dcf
    try:
        sens = table_with(s6, "Stable ROIC")
        vals = [num(r["Value per share"]) for r in sens]
        lo, hi = min(vals + [dcf]), max(vals + [dcf])
    except Missing:
        pass
    ranges.append(("DCF, stable-return range", lo, hi, BLUE))
    try:
        stress = table_with(s6, "Case")
        sv = [num(r["Value per share"]) for r in stress]
        ranges.append(("DCF, stress cases", min(sv), max(sv), BLUE))
    except Missing:
        pass
    s7 = section(c.model, 7)
    m_lo = re.search(r"EV/Revenue of [\d.]+x: .*?= \$(\d+(?:\.\d+)?)", s7)
    m_hi = re.search(r"EV/EBITDA of [\d.]+x: \$(\d+(?:\.\d+)?)", s7)
    peer = sorted(float(m.group(1)) for m in (m_lo, m_hi) if m)
    if peer:
        ranges.append(("Peer multiples", peer[0], peer[-1], MUTED))
    for f in c.L.get("facts", []) or []:
        if f.get("exhibit") == "value-range":
            a, b = map(float, str(f["value"]).split("-"))
            ranges.append((f.get("label", f["id"]), a, b, MUTED))
    fig, ax = plt.subplots(figsize=(7, 0.55 * len(ranges) + 2.4))
    for i, (lab, a, b, col) in enumerate(ranges):
        ax.barh(i, max(b - a, 0.05), left=a, height=0.5, color=col, alpha=1 if col == BLUE else 0.55, zorder=3)
        if not (i == 0 and abs(a - dcf) < 0.01):
            ax.text(a - 0.25, i, f"${a:.2f}", ha="right", va="center", fontsize=8.5, color=INK)
        ax.text(b + 0.25, i, f"${b:.2f}", ha="left", va="center", fontsize=8.5, color=INK)
    ax.scatter([dcf], [0], s=80, color=BLUE, edgecolor=SURFACE, linewidth=2, zorder=5)
    ax.annotate(f"Base case ${dcf:.2f}", (dcf, 0), xytext=(dcf, -0.5), ha="left", va="center", fontsize=8.5, color=INK,
                fontweight="bold", bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1), zorder=6)
    lines = [(price, f"Market price ${price:.2f} ", INK2, "right")] if price else []
    if deal:
        lines.append((deal, f" Deal price ${deal:.2f}", ORANGE, "left"))
    for v, lab, col, ha in lines:
        ax.axvline(v, color=col, lw=1.5, ls="--", zorder=4)
        ax.text(v, len(ranges) - 0.35, lab, ha=ha, fontsize=8.5, color=INK, fontweight="bold",
                bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.5))
    ax.set_yticks(range(len(ranges)), [r[0] for r in ranges])
    xs = [r[1] for r in ranges] + [r[2] for r in ranges] + [v for v, *_ in lines]
    ax.set_xlim(min(xs) - 2.5, max(xs) + 2.5)
    ax.set_ylim(-0.8, len(ranges) - 0.1)
    ax.set_xlabel("Value per share ($)")
    ax.grid(axis="y", visible=False)
    if price:
        gap = dcf / price - 1
        title = f"DCF value ${dcf:.2f} is {abs(gap):.0%} {'above' if gap >= 0 else 'below'} the ${price:.2f} market price"
    else:
        title = f"DCF value ${dcf:.2f} a share"
    finish(fig, title, "Value per share by method; bars are ranges, the dot is the base case",
           f"Calculated from {c.poss} and peers' filings; market data as of {c.date}", path, left=0.27)
    return title


def ownership(c, path):
    holders = (c.L.get("governance", {}) or {}).get("controlling_holders") or []
    pairs = [(h["name"], float(lv(h["pct"])) * 100) for h in holders if h.get("pct") is not None]
    if not pairs:
        raise Missing("governance.controlling_holders lists no stakes")
    pairs.append(("All other holders", 100 - sum(p for _, p in pairs)))
    fig, ax = plt.subplots(figsize=(7, 0.45 * len(pairs) + 1.8))
    ys = list(range(len(pairs)))[::-1]
    for y, (name, p) in zip(ys, pairs):
        ax.barh(y, p, height=0.55, color=ORANGE if name != "All other holders" else MUTED, zorder=3)
        ax.text(p + 0.8, y, f"{p:.2f}%", va="center", fontsize=9, color=INK)
    ax.set_yticks(ys, [n for n, _ in pairs])
    ax.set_xlim(0, max(p for _, p in pairs) * 1.2)
    ax.set_xlabel("Share of common stock (%)")
    ax.grid(axis="y", visible=False)
    held = sum(p for _, p in pairs[:-1])
    title = f"{len(pairs) - 1} holder{'s' if len(pairs) > 2 else ''} controlled {held:.2f}% of {c.short}"
    finish(fig, title, "Beneficial ownership of the largest controlling holders; the rest is everyone else",
           f"{c.poss} latest proxy statement, beneficial ownership table", path, left=0.25)
    return title


CHARTS = {"cost-of-capital": cost_of_capital, "returns": returns, "payout": payout, "value": value, "ownership": ownership}


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--charts")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    folder = pathlib.Path(a.folder).resolve()
    out = pathlib.Path(a.out).resolve() if a.out else folder / "exhibits"
    out.mkdir(parents=True, exist_ok=True)
    keys = a.charts.split(",") if a.charts else (ALL if a.all else CORE)
    unknown = [k for k in keys if k not in CHARTS]
    if unknown:
        sys.exit(f"unknown chart(s): {', '.join(unknown)}; choose from {', '.join(CHARTS)}")
    c = Ctx(folder)
    failed = False
    for k in keys:
        try:
            title = CHARTS[k](c, out / f"exhibit-{k}.png")
            print(f"exhibit-{k}.png: {title}")
        except (Missing, KeyError, ValueError, StopIteration) as e:
            print(f"skipped {k}: {e}", file=sys.stderr)
            failed = failed or k in CORE
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
