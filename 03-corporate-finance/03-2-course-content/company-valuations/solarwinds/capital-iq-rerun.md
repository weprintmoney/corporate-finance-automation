---
title: "SolarWinds (SWI) — Capital Structure Rerun: SEC Filings vs. Capital IQ"
status: active
owner: weprintmoney
created: 2026-10-06
last_updated: 2026-10-06
---

# Capital structure rerun: SEC filings vs. Capital IQ

This reruns the project's numeric spine from scratch, twice: once on the SEC-filings inputs the project started with, and once on the [Capital IQ pulls](sources/capital-iq/README.md) from 2026-10-05. The spine is cost of capital, optimal debt ratio, the value of moving to the optimum, and the lesson 34 DCF. Method, beta, risk-free rate, equity risk premium and forecasts are held constant, so every difference comes from the data.

The risk-free rate is 4.55%: the 4.77% 10-year Treasury less Damodaran's 0.22% US default spread. The 4.46% equity risk premium already includes a 0.23% US country risk premium, so using the gross Treasury would count US default risk twice. See the Meetup 2 lens in [lesson-05.md](lesson-05.md). An earlier version of this file used the gross 4.77%. Netting lowers every WACC by about 0.16 points and leaves the optimal debt ratios within a point.

It also settles a conflict between lessons. Lesson 18 put the optimal debt ratio at 13% and lesson 34 put it near 30%.

Script: [`tools/capital-structure-rerun.py`](tools/capital-structure-rerun.py). Run `python3 tools/capital-structure-rerun.py` from this folder.

## Bottom line

- **Optimal debt ratio: 17% base case, 22% upper bound.** SWI's actual ~29% is about 7–12 points over, or $290–510M of excess debt. SWI was over-levered before Turn/River took debt to ~58%.
- **Lesson 18's 13% came from a known-wrong firm value.** It used $5,717M, which treats the $4.4B deal value as equity. On the corrected ~$4.4B, the same method gives 16–17%.
- **Lesson 34's ~30% only appears with company-adjusted EBITDA ($384.7M) as the coverage numerator.** Capital IQ's standardized EBITDA is $273.5M, because it doesn't add back stock-based compensation or one-off items. On that figure the upper bound falls to 22%.
- **Capital IQ moved the answer most where the SEC data needed judgment.** It barely moved the parts that were already hard numbers.

## What changed between the two runs

| Input | A: SEC filings only | B: with Capital IQ | Effect |
|---|---|---|---|
| EBIT | $208.4M (GAAP, includes $10.3M unusual items) | $218.7M (standardized, excludes them) | Coverage 1.85x → 1.95x. Still a B− synthetic rating. Optimum stays at 16–17%. |
| EBITDA for the upper case | $384.7M (company-adjusted) | $273.5M (standardized) | **Largest change.** Upper-bound optimum falls from 31% to 22%. |
| Total debt | $1,285.0M (face + leases) | $1,256.0M (carrying + leases) | Negligible. Debt ratio 28.8% → 28.6%. |
| Equity value | $3,174.0M (171.6M × $18.50) | $3,142.1M (CIQ market cap at $18.31) | Negligible. |
| Pre-tax cost of debt | 7.11% (year-end rate) | 8.2% (CIQ FY2024 weighted average) | WACC 9.94% → 10.18%. DCF $19.33 → $18.68. |
| Credit read | Synthetic B− from EBIT coverage; "B+" cited without a source | Same synthetic B−, plus CIQ's statistical score of bb− | A second, independent read sits two notches above the EBIT-based rating. Not an agency rating. |
| Beta, forecasts, second-lien pricing | Industry beta; management forecasts from the DEFM14C | Unchanged. CIQ's price history, consensus estimates and loan pricing didn't load. | No change. |

## Results

| | A: SEC only | B: with Capital IQ | C: recommended |
|---|---|---|---|
| Debt ratio (market) | 28.8% | 28.6% | 28.6% |
| WACC at actual weights | 9.94% | 10.18% | 9.94% |
| Optimal debt, EBIT coverage | 16% (9.86%) | 17% (9.85%) | 17% (9.85%) |
| Optimal debt, EBIT + 2016-LBO amortization | 21% (9.78%) | 22% (9.77%) | 22% (9.77%) |
| Optimal debt, EBITDA case | 31% (9.62%) | 22% (9.77%) | 22% (9.77%) |
| Value gain from moving to optimum | $22M–$433M | $261M–$435M | $261M–$435M |
| Debt above optimum | −$97M to $572M | $288M–$508M | $288M–$508M |
| DCF value per share (deal: $18.50) | $19.33 | $18.68 | $19.49 |

**C is the recommended set.** It uses Capital IQ's operating data with the 7.11% year-end loan rate. Capital IQ's own tranche detail confirms that rate, and it is more forward-looking than the FY2024 average, which includes higher rates earlier in the year.

The value gain is the change in WACC at current firm value, capitalized as a growing perpetuity at g = 2.5%, as in lesson 19. On 185.0M diluted shares, $261–435M is about $1.41–2.35 per share.

## What the comparison says about Capital IQ

1. **It narrowed a judgment call into a range.** With SEC data alone, the optimum ran from 16% to 31%, depending on which EBITDA you trusted. Capital IQ's standardized EBITDA ($273.5M) lands almost exactly on the project's own "EBIT + LBO amortization" figure ($271.6M). Two independent routes now agree on 22% as the upper bound.
2. **It removed management's framing.** Company-adjusted EBITDA adds back $76.5M of stock-based compensation, a real cost Damodaran insists on charging. Capital IQ's standardized line doesn't add it back. Lesson 34 already makes the same point about the DCF, where SBC is a $7.23/share swing.
3. **It confirmed rather than changed the hard numbers.** Weights, debt, share count and deal values all matched the corrected SEC figures within about 1%. The corrections the project had already made (equity vs. enterprise value, 171.6M shares) were right.
4. **It introduced one input to handle carefully.** The 8.2% weighted-average rate is backward-looking. Used naively, it lowers value per share by about $0.80 ($19.49 → $18.68).
5. **It couldn't help where the project is weakest.** There's no regression beta (price history didn't load), no consensus forecasts and no second-lien pricing. The post-buyout interest estimate in lesson 34 is still unverified.

## Effect on earlier lessons

- **Lesson 18:** the 13% optimum becomes 17%. The 13%–25% range becomes 17%–22%. See the rerun note in [lesson-18.md](lesson-18.md).
- **Lesson 19:** the $416M gain and the $200–280M paydown were built on the $5,717M firm value. They become a $261–435M gain and a $290–510M paydown. See [lesson-19.md](lesson-19.md).
- **Lesson 34:** "already close to its WACC-minimizing ratio (~30%)" is superseded. SWI was 7–12 points over before the buyout. The status-quo DCF moves from $18.42 to $18.68–19.49 depending on the cost-of-debt input, 1%–5% above the deal price. See [lesson-34.md](lesson-34.md).
