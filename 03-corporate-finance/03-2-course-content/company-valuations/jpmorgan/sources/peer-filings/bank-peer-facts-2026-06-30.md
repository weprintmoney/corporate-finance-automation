---
title: "bank peer facts 2026 06 30"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Bank peer facts as of 2026-06-30

Generated 2026-11-03 by a scratch wrapper around tools/fetch-peer-facts.py (its own functions: SEC XBRL company facts filtered to 10-Ks filed on or before 2026-06-30, share counts filed on or before 2026-06-30, the close actually traded on 2026-06-30). The stock tool crashes on banks (no revenue tag) and picked WFC's 2019 year, so this wrapper uses bank tags: net income, dividends, buybacks, stockholders' equity. P/B here is market cap over total stockholders' equity, preferred included; JPM's own ratios in the read come from its filings. Values in $ millions.

| Ticker | Company | FY end | Net income | NI to common | Common div paid | Buybacks | Equity (total) | Equity prior | Preferred | Shares (M) | Close | Close date | Market cap | P/B (total equity) | ROE (NI/avg equity) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| JPM | JPMORGAN CHASE & CO | 2025-12-31 | 57,048 | 55,681 | 16,625 | 31,591 | 362,438 | 344,758 | n/a | 2,679.5 | 327.33 | 2026-06-30 | 877,084 | 2.42 | 16.1% |
<!-- JPM: shares=EntityCommonStockSharesOutstanding (10-Q as of 2026-03-31, filed 2026-05-01); tags ni=NetIncomeLoss div=PaymentsOfDividends bb=PaymentsForRepurchaseOfCommonStock eq=StockholdersEquity -->
| BAC | BofA Finance LLC | 2025-12-31 | 30,509 | 29,055 | 8,083 | 21,433 | 303,243 | 295,559 | n/a | 7,096.6 | 56.98 | 2026-06-30 | 404,364 | 1.33 | 10.2% |
<!-- BAC: shares=EntityCommonStockSharesOutstanding (10-Q as of 2026-04-30, filed 2026-05-01); tags ni=NetIncomeLoss div=DividendsCommonStockCash bb=PaymentsForRepurchaseOfCommonStock eq=StockholdersEquity -->
| C | Citigroup Inc | 2025-12-31 | 14,306 | 13,021 | 5,372 | 13,250 | 212,291 | 208,598 | 20,050 | 1,749.3 | 139.96 | 2026-06-30 | 244,835 | 1.15 | 6.8% |
<!-- C: shares=EntityCommonStockSharesOutstanding (10-K as of 2026-01-31, filed 2026-02-20); tags ni=NetIncomeLoss div=PaymentsOfDividends bb=PaymentsForRepurchaseOfCommonStock eq=StockholdersEquity -->
| WFC | WELLS        FARGO & COMPANY/MN | 2025-12-31 | 21,338 | 20,285 | 5,434 | 17,516 | 181,117 | 179,120 | 16,608 | 3,060.2 | 82.64 | 2026-06-30 | 252,894 | 1.40 | 11.8% |
<!-- WFC: shares=EntityCommonStockSharesOutstanding (10-Q as of 2026-04-17, filed 2026-04-29); tags ni=NetIncomeLoss div=PaymentsOfDividendsCommonStock bb=PaymentsForRepurchaseOfCommonStock eq=StockholdersEquity -->
| GS | The Goldman Sachs Group, Inc. | 2025-12-31 | 17,176 | 16,300 | 5,277 | 12,360 | 124,972 | 121,996 | 15,153 | 295.0 | 1011.37 | 2026-06-30 | 298,362 | 2.39 | 13.9% |
<!-- GS: shares=EntityCommonStockSharesOutstanding (10-Q as of 2026-04-17, filed 2026-05-01); tags ni=NetIncomeLoss div=PaymentsOfDividends bb=PaymentsForRepurchaseOfCommonStock eq=StockholdersEquity -->
| MS | MORGAN STANLEY | 2025-12-31 | 16,861 | 16,249 | 6,593 | n/a | 111,632 | 104,511 | n/a | 1,577.3 | 209.04 | 2026-06-30 | 329,716 | 2.95 | 15.6% |
<!-- MS: shares=EntityCommonStockSharesOutstanding (10-Q as of 2026-04-30, filed 2026-05-05); tags ni=NetIncomeLoss div=PaymentsOfDividends bb=None eq=StockholdersEquity -->
| PNC | PNC Financial Services Group, Inc. | 2025-12-31 | 6,997 | 6,576 | 2,635 | 1,338 | 60,585 | 54,425 | n/a | 401.6 | 246.22 | 2026-06-30 | 98,873 | 1.63 | 12.2% |
<!-- PNC: shares=EntityCommonStockSharesOutstanding (10-Q as of 2026-04-14, filed 2026-05-05); tags ni=ProfitLoss div=PaymentsOfDividendsCommonStock bb=PaymentsForRepurchaseOfCommonStock eq=StockholdersEquity -->
| USB | US BANCORP \DE\ | 2025-12-31 | 7,570 | 7,194 | 3,168 | 489 | 65,193 | 58,578 | n/a | 1,552.3 | 60.40 | 2026-06-30 | 93,759 | 1.44 | 12.2% |
<!-- USB: shares=EntityCommonStockSharesOutstanding (10-Q as of 2026-04-30, filed 2026-05-04); tags ni=NetIncomeLoss div=PaymentsOfDividendsCommonStock bb=PaymentsForRepurchaseOfCommonStock eq=StockholdersEquity -->
