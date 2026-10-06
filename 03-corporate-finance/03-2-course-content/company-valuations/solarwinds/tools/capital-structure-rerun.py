"""Rerun SolarWinds' cost of capital, optimal debt ratio and DCF on two input sets.

Track A uses only the SEC filings the project started with. Track B swaps in the
Capital IQ pulls from 2026-10-05. Everything else (method, beta, rates, forecasts)
is held constant so the differences come from the data alone.

Run: python3 tools/capital-structure-rerun.py
"""

# Smaller-and-riskier-firm coverage table (lesson-18 spreadsheet-cost-of-capital-optimal.md).
# Damodaran uses it for firms under ~$5B of market cap. SWI's equity was ~$3.2B.
SMALL = [(-1e5, .14), (.5, .105), (.8, .08), (1.25, .065), (1.5, .055), (2, .045), (2.5, .0375),
         (3, .03), (3.5, .025), (4, .016), (4.5, .0125), (6, .011), (7.5, .01), (9.5, .008), (12.5, .006)]
RATINGS = ["D", "C", "CC", "CCC", "B-", "B", "B+", "BB", "BB+", "BBB", "A-", "A", "A+", "AA", "AAA"]

# Shared inputs (lessons 9-13): cash-corrected Software (System & Application) unlevered beta,
# rf and ERP as used in lesson 34, 25% marginal tax rate.
BU, RF, ERP, T, G = 1.2482, .0477, .0446, .25, .025

# Lesson 34 FCFF: management's uFCF (DEFM14C) less stock-based compensation, 2025-2030.
FCFF = [212, 258, 297, 338, 379, 419]
DILUTED_SHARES = 185.0

TRACKS = {
    "A: SEC filings only": dict(
        ebit=208.4,            # 10-K GAAP operating income, includes $10.3M of unusual items
        ebitda_case=384.7,     # company-defined adjusted EBITDA (10-K non-GAAP)
        amort_case=208.4 + 52.9,  # EBIT + 2016-LBO acquired-intangible amortization
        interest=112.435,      # 10-K Note 16 gross interest expense
        debt=1285.0,           # term loan face 1,235.7 + operating leases 49.4 (lesson 13)
        equity=3174.0,         # 171.6M basic shares x $18.50 deal price
        cash=259.3,
        kd=.0711,              # year-end term loan rate
    ),
    "B: with Capital IQ": dict(
        ebit=218.7,            # CIQ standardized EBIT, excludes unusual items
        ebitda_case=273.5,     # CIQ standardized EBITDA (no SBC or one-off add-backs)
        amort_case=218.7 + 52.9,
        interest=112.4,
        debt=1256.0,           # CIQ total debt: term loan carrying 1,206.6 + leases 49.4
        equity=3142.1,         # CIQ market cap at the last pre-close pricing date ($18.31)
        cash=259.3,
        kd=.082,               # CIQ weighted-average rate on LT debt, FY2024
    ),
}
# Recommended: Capital IQ data, but the forward-looking 7.11% year-end rate (which CIQ's
# tranche detail also confirms) instead of the backward-looking FY2024 average.
TRACKS["C: recommended (Capital IQ data, 7.11% rate)"] = dict(TRACKS["B: with Capital IQ"], kd=.0711)


def spread_for(cov):
    s, r = SMALL[0][1], RATINGS[0]
    for (lo, sp), name in zip(SMALL, RATINGS):
        if cov > lo:
            s, r = sp, name
    return s, r


def wacc_at(d, V, numerator):
    """Damodaran's iterative loop: debt -> interest -> coverage -> rating -> rate."""
    D = d * V
    kd = RF + .02
    for _ in range(50):
        cov = numerator / (D * kd) if D else 1e9
        sp, rating = spread_for(cov)
        kd = RF + sp
    interest = D * kd
    teff = T if interest <= numerator or not D else T * numerator / interest
    bl = BU * (1 + (1 - teff) * d / (1 - d))
    ke = RF + bl * ERP
    return (1 - d) * ke + d * kd * (1 - teff), (numerator / interest if D else None), rating


def optimum(V, numerator):
    grid = [x / 100 for x in range(0, 71)]
    return min(((d, *wacc_at(d, V, numerator)) for d in grid), key=lambda r: r[1])


def dcf(wacc, debt, cash):
    pv = sum(cf / (1 + wacc) ** (i + 1) for i, cf in enumerate(FCFF))
    tv = FCFF[-1] * (1 + G) / (wacc - G)
    ev = pv + tv / (1 + wacc) ** len(FCFF)
    return ev, (ev - (debt - cash)) / DILUTED_SHARES


def run(name, x):
    V = x["debt"] + x["equity"]
    d = x["debt"] / V
    bl = BU * (1 + (1 - T) * x["debt"] / x["equity"])
    ke = RF + bl * ERP
    wacc_actual = (1 - d) * ke + d * x["kd"] * (1 - T)
    cov_ebit = x["ebit"] / x["interest"]
    _, synth = spread_for(cov_ebit)
    rows = {}
    for label, num in [("EBIT", x["ebit"]), ("EBIT + LBO amortization", x["amort_case"]),
                       ("EBITDA case", x["ebitda_case"])]:
        dopt, w, cov, rating = optimum(V, num)
        w_cur = wacc_at(d, V, num)[0]
        gain = (w_cur - w) * V / (w - G)
        rows[label] = (num, dopt, w, rating, w_cur, gain, (d - dopt) * V)
    ev, per_share = dcf(wacc_actual, x["debt"], x["cash"])
    print(f"\n## {name}")
    print(f"Firm value {V:,.1f} | debt ratio {d:.1%} | levered beta {bl:.3f} | cost of equity {ke:.2%}")
    print(f"Pre-tax cost of debt {x['kd']:.2%} | WACC at actual weights {wacc_actual:.2%}")
    print(f"EBIT coverage {cov_ebit:.2f}x -> synthetic {synth}")
    print("| Coverage numerator | $M | Optimal debt | WACC at optimum | Rating at optimum | "
          "Synthetic WACC at current | Value gain from moving | Debt above optimum |")
    print("|---|---|---|---|---|---|---|---|")
    for label, (num, dopt, w, rating, w_cur, gain, excess) in rows.items():
        print(f"| {label} | {num:,.1f} | {dopt:.0%} | {w:.2%} | {rating} | {w_cur:.2%} | "
              f"${gain:,.0f}M | ${excess:,.0f}M |")
    print(f"DCF at {wacc_actual:.2%}: EV ${ev:,.0f}M, value per share ${per_share:.2f} "
          f"(net debt {x['debt'] - x['cash']:,.1f})")


if __name__ == "__main__":
    for name, x in TRACKS.items():
        run(name, x)
