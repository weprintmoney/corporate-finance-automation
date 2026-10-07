---
title: "Capital IQ pulls: forecast inputs for the AI observability market exercise"
status: active
owner: weprintmoney
created: 2026-10-07
last_updated: 2026-10-07
---

# Capital IQ forecast inputs

Pulled 2026-10-07 from the NYU academic Capital IQ account (classic platform, `https://www.capitaliq.com/CIQDotNet/`). These feed the 2029-2031 market forecast in the `weprintmoney/arize-ai` repo (`docs/01-market-intelligence/market-forecast-2029-2031.md`), facets F1 (hardware) and F7 (buyer economics). All figures are USD millions as shown on the named CIQ page; fiscal periods differ by company and are stated per column. Transcripts were not pulled: the Transcripts section sits behind an End User Agreement that has not been accepted.

## 1. Capital expenditure, five largest AI infrastructure buyers

Source page: Financials > Cash Flow, line "Capital Expenditure" (sign flipped to positive).

| Company (CIQ ID) | Fiscal year end | FY-4 | FY-3 | FY-2 | FY-1 | Latest FY | LTM |
|---|---|---|---|---|---|---|---|
| Microsoft (21835) | June | FY22 23,886 | FY23 28,107 | FY24 44,477 | FY25 64,551 | FY26 115,948 | same as FY26 |
| Amazon (18749) | December | CY22 63,645 | CY23 52,729 | CY24 82,999 | CY25 131,819 | n/a | Jun-2026 173,028 |
| Alphabet (29096) | December | CY22 31,485 | CY23 32,251 | CY24 52,535 | CY25 91,447 | n/a | Jun-2026 132,402 |
| Meta (20765463) | December | CY22 31,186 | CY23 27,045 | CY24 37,256 | CY25 69,691 | n/a | Jun-2026 89,325 |
| Oracle (22247) | May | FY23 8,695 | FY24 6,866 | FY25 21,215 | FY26 55,663 | n/a | Aug-2026 75,660 |

Earlier years on the same pages: Microsoft FY21 20,622; Amazon CY21 61,053; Alphabet CY21 24,640; Oracle FY22 4,511.

**Computed here.** Sum of the latest twelve months available for the five: 115,948 + 173,028 + 132,402 + 89,325 + 75,660 = **586,363**. Sum for the year nearest calendar 2023 (Microsoft FY23, Amazon CY23, Alphabet CY23, Meta CY23, Oracle FY24): 28,107 + 52,729 + 32,251 + 27,045 + 6,866 = **146,998**. Ratio: **4.0x in about three years**. Limits: fiscal years are not aligned; capex is total, not AI-only (Amazon's includes fulfilment); finance leases are excluded.

Cash from operations, latest twelve months, same pages: Microsoft 182,935; Amazon 161,403; Alphabet 185,675; Meta 130,301; Oracle 46,940. Oracle's capex exceeds its operating cash flow (75,660 vs 46,940); Amazon's does too (173,028 vs 161,403).

## 2. NVIDIA and Cisco

Source page: Financials > Cash Flow.

| Company (CIQ ID) | Line | FY-4 | FY-3 | FY-2 | FY-1 | Latest FY | LTM |
|---|---|---|---|---|---|---|---|
| NVIDIA (32307), FY ends late January | Cash from Ops. | FY22 9,108 | FY23 5,641 | FY24 28,090 | FY25 64,089 | FY26 102,718 | Jul-2026 134,360 |
| NVIDIA | Capital Expenditure | 976 | 1,833 | 1,069 | 3,236 | 6,042 | 7,354 |
| NVIDIA | Repurchase of Common Stock | 1,904 | 11,514 | 12,316 | 40,636 | 48,034 | 64,414 |
| Cisco (19691), FY ends late July | Cash from Ops. | FY21 15,454 | FY22 13,226 | FY23 19,886 | FY24 10,880 | FY25 14,193 | FY26 14,177 |
| Cisco | Capital Expenditure | 692 | 477 | 849 | 670 | 905 | 1,410 |

## 3. Dynatrace and Datadog

Source pages: Financials > Income Statement, Cash Flow, Key Stats, Segments.

| Line | Dynatrace (628406634) FY26, Mar-2026 | Dynatrace LTM Jun-2026 | Datadog (134521275) CY25 | Datadog LTM Jun-2026 |
|---|---|---|---|---|
| Total revenue | 2,018.4 | 2,095.6 | 3,427.2 | 3,966.7 |
| Revenue growth | 18.8% | 17.9% | 27.7% | 31.5% |
| Gross margin | 81.7% | 81.6% | 80.0% | 79.5% |
| R&D expense | 479.9 | 509.0 | 1,548.5 | 1,733.2 |
| R&D as % of revenue (computed) | 23.8% | 24.3% | 45.2% | 43.7% |
| SG&A | 907.9 | 929.7 | 1,221.6 | 1,385.0 |
| Operating income (GAAP) | 263.9 | 273.1 | (42.8) | 19.2 |
| Stock-based compensation | 299.6 | 301.3 | 750.7 | 823.0 |
| Cash from operations | 561.9 | 598.4 | 1,050.1 | 1,229.0 |
| Capital expenditure | 32.2 | 27.8 | 49.6 | 46.9 |
| Share repurchases | 500.6 | 728.3 | none | none |

**Computed here.** Datadog's trailing R&D is 1,733.2 / 509.0 = **3.4x Dynatrace's** in dollars. Datadog's stock-based compensation alone (823.0) exceeds Dynatrace's entire R&D line. Dynatrace returned 728.3 to shareholders through buybacks in the same twelve months, which is 1.43x its R&D.

Consensus estimates shown on Key Stats (CIQ mean; these did load on 2026-10-07, unlike the Estimates page on 2026-10-05):

| | Dynatrace FY27E | FY28E | FY29E | Datadog CY26E | CY27E | CY28E |
|---|---|---|---|---|---|---|
| Revenue | 2,319.9 | 2,663.3 | 3,038.9 | 4,471.6 | 5,479.0 | 6,755.6 |
| Growth | 14.9% | 14.8% | 14.1% | 30.5% | 22.5% | 23.3% |
| EBIT margin (non-GAAP basis in estimates) | 29.6% | 30.5% | 31.7% | 22.9% | 23.6% | 24.8% |

**Computed here.** Consensus FY29 revenue growth plus EBIT margin for Dynatrace is 14.1 + 31.7 = 45.8. Dynatrace's stated aim is "Rule of 50" by fiscal 2029; the company's definition may use ARR growth and free-cash-flow margin, so this is an approximation, but on these estimates the Street is not yet modelling it.

Dynatrace revenue by geography, FY26 (Segments page, filed 2026-05-20): United States 927.7 (46.0%); North America excluding United States 89.8 (4.4%); Europe, Middle East and Africa 648.9 (32.1%); Asia Pacific 193.1 (9.6%); Latin America 158.9 (7.9%). Total 2,018.4.

Datadog revenue by geography, CY25 (filed 2026-02-18): United States 2,320.3 (67.7%); North America excluding United States 112.8 (3.3%); International 994.1 (29.0%). Total 3,427.2.

Dynatrace Customers page lists Amazon Web Services, Google and Microsoft Azure as distributors (source: FY2026 Form 10-K). The Industry Specific page is empty, so customer counts and retention are not available from CIQ and must come from the 10-K.

## Not available or not pulled

| Item | Result |
|---|---|
| Transcripts | End User Agreement click-through not accepted; not pulled |
| Industry Specific (customer counts, ARR, NRR) | Empty grid for Dynatrace |
| Quarterly capex series | Annual and LTM only in this pull |
| Dell, HPE, Supermicro | Not pulled yet |
