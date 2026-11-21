"""Build colgate-work-summary.xlsx: the calculations done outside the professor's spreadsheets, with live formulas.

Run from the company folder:  python3 professor-spreadsheet/build-work-summary.py
"""
import csv, sys, site, warnings
sys.path.append(site.getusersitepackages())
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter as L
warnings.simplefilter("ignore")

OUT = "professor-spreadsheet/colgate-work-summary.xlsx"
BLUE = Font(name="Arial", size=10, color="0000FF"); BLK = Font(name="Arial", size=10)
BOLD = Font(name="Arial", size=10, bold=True); H1 = Font(name="Arial", size=13, bold=True)
NOTE = Font(name="Arial", size=9, italic=True, color="555555"); HDR = PatternFill("solid", fgColor="D9E1F2")
PCT = "0.00%"; NUM = "#,##0;(#,##0);-"; DEC = "0.0000"

wb = openpyxl.Workbook()

def sheet(name, widths):
    ws = wb.create_sheet(name)
    for i, w in enumerate(widths, 1): ws.column_dimensions[L(i)].width = w
    return ws

def put(ws, ref, v, font=BLK, fmt=None, wrap=False):
    c = ws[ref]; c.value = v; c.font = font
    if fmt: c.number_format = fmt
    if wrap: c.alignment = Alignment(wrap_text=True, vertical="top")
    return c

def header(ws, row, labels):
    for i, t in enumerate(labels, 1):
        c = ws.cell(row, i, t); c.font = BOLD; c.fill = HDR; c.alignment = Alignment(wrap_text=True, vertical="top")

# ---------------- Read me
ws = wb.active; ws.title = "Read me"; ws.column_dimensions["A"].width = 34; ws.column_dimensions["B"].width = 110
put(ws, "A1", "Colgate-Palmolive (CL) — corporate finance project, working file", H1)
rows = [
 ("Analysis date", "2026-11-20. Base year FY2025 (10-K filed 2026-02-23); trailing twelve months to 2026-09-30. Amounts in $ millions."),
 ("What this file is", "The calculations done outside the professor's spreadsheets, rebuilt with live formulas so each step can be followed. Change a blue cell and the results recalculate."),
 ("Colour code", "Blue text = an input typed in, with its source in the next column. Black = a formula. Grey italic = a note."),
 ("Tab: Cost of capital", "Riskfree rate, equity risk premium weighted by where Colgate sells, bottom-up beta by segment, cost of debt from the rating, cost of capital."),
 ("Tab: Beta regression", "60 monthly returns, CL against the S&P 500 total return index, October 2021 to October 2026."),
 ("Tab: Dividends", "Free cash flow to equity against dividends and buybacks, 2018–2025, with buybacks shown net of option proceeds."),
 ("Tab: Debt design", "Sector sensitivities from macrodur.xlsx weighted by segment, Colgate's own history, and the debt it has."),
 ("Tab: Spreadsheet results", "Outputs read from the three filled professor spreadsheets, with the inputs that differ from their defaults."),
 ("Professor spreadsheets (separate files)", "colgate-capstru-optimal-debt.xlsx (optimal debt ratio) · colgate-dividends-2026-11-20.xlsx (dividend analysis) · colgate-fcffsimpleginzu-2026-11-20.xlsx (valuation). Each is the professor's file with Colgate's inputs entered in the yellow cells."),
 ("Judgment calls to challenge", "1) Operating income 4,225 = reported 3,306 plus the 919 non-cash write-down; restructuring and litigation charges kept in. 2) Cost of debt from the actual A+ rating, not the synthetic AAA. 3) Start-of-November equity risk premium, although the S&P 500 fell 8.8% afterwards. 4) Food Processing beta for Hill's Pet Nutrition. 5) Stable return on capital of 20% in the valuation, against the spreadsheet default of return = cost of capital."),
 ("Sources", "Colgate 10-K FY2025, 10-Q Q3 2026 and 2026 proxy (SEC EDGAR, CIK 0000021665); SEC XBRL company facts; S&P Capital IQ (rating, bond list, consensus); Damodaran data (ERP November 2026, industry betas and ratings table January 2026, regional risk premiums January 2026); FRED 10-year Treasury; Yahoo Finance prices."),
]
for i, (a, b) in enumerate(rows, 3):
    put(ws, f"A{i}", a, BOLD, wrap=True); put(ws, f"B{i}", b, wrap=True)

# ---------------- Cost of capital
ws = sheet("Cost of capital", [44, 16, 16, 16, 16, 70])
put(ws, "A1", "Cost of capital", H1)
header(ws, 3, ["Riskfree rate", "Value", "", "", "", "Source"])
put(ws, "A4", "10-year US Treasury"); put(ws, "B4", 0.0504, BLUE, PCT); put(ws, "F4", "FRED DGS10, close on 2026-11-19", NOTE)
put(ws, "A5", "US sovereign default spread (Aa1)"); put(ws, "B5", 0.0022, BLUE, PCT); put(ws, "F5", "Damodaran ERPNov26.xlsx", NOTE)
put(ws, "A6", "Riskfree rate", BOLD); put(ws, "B6", "=B4-B5", BOLD, PCT)

header(ws, 8, ["Equity risk premium by region of sales", "Weight", "Country risk premium", "ERP", "Weight × ERP", "Source"])
put(ws, "A9", "Mature market premium (implied, S&P 500)"); put(ws, "D9", 0.0361, BLUE, PCT); put(ws, "F9", "Damodaran ERPNov26.xlsx, start of November 2026, measured over the riskfree rate", NOTE)
put(ws, "A10", "United States"); put(ws, "B10", 0.3333, BLUE, PCT); put(ws, "C10", 0, BLUE, PCT); put(ws, "F10", "10-K note 14: about two-thirds of sales are outside the United States", NOTE)
put(ws, "A11", "Emerging markets"); put(ws, "B11", 0.45, BLUE, PCT); put(ws, "C11", "=C20", BLK, PCT); put(ws, "F11", "10-K note 14: about 45% of sales from emerging markets", NOTE)
put(ws, "A12", "Other developed markets"); put(ws, "B12", "=1-B10-B11", BLK, PCT); put(ws, "C12", 0.0104, BLUE, PCT); put(ws, "F12", "Remainder; Western Europe country risk premium, Damodaran January 2026", NOTE)
for r in (10, 11, 12):
    put(ws, f"D{r}", f"=$D$9+C{r}", BLK, PCT); put(ws, f"E{r}", f"=B{r}*D{r}", BLK, PCT)
put(ws, "A13", "Weighted equity risk premium", BOLD); put(ws, "B13", "=SUM(B10:B12)", BLK, PCT); put(ws, "E13", "=SUM(E10:E12)", BOLD, PCT)

header(ws, 15, ["Emerging-market country risk premium", "2025 sales", "Country risk premium", "Sales × premium", "", "Source"])
em = [("Latin America", 4776, 0.0439), ("Asia Pacific", 2814, 0.0149), ("Africa/Eurasia", 1172, 0.0426)]
for i, (n, s, p) in enumerate(em, 16):
    put(ws, f"A{i}", n); put(ws, f"B{i}", s, BLUE, NUM); put(ws, f"C{i}", p, BLUE, PCT); put(ws, f"D{i}", f"=B{i}*C{i}", BLK, NUM)
    put(ws, f"F{i}", "Segment sales: 10-K MD&A. Premium: Damodaran regional averages, January 2026", NOTE)
put(ws, "A19", "Total"); put(ws, "B19", "=SUM(B16:B18)", BLK, NUM); put(ws, "D19", "=SUM(D16:D18)", BLK, NUM)
put(ws, "A20", "Sales-weighted premium", BOLD); put(ws, "C20", "=D19/B19", BOLD, PCT)

header(ws, 22, ["Bottom-up beta by segment", "2025 sales", "Weight", "Unlevered beta", "Weight × beta", "Source"])
put(ws, "A23", "Oral, Personal and Home Care"); put(ws, "B23", 15769, BLUE, NUM); put(ws, "D23", 0.7411, BLUE, DEC); put(ws, "F23", "Damodaran US industry betas, January 2026: Household Products (110 firms), cash-corrected", NOTE)
put(ws, "A24", "Hill's Pet Nutrition"); put(ws, "B24", 4613, BLUE, NUM); put(ws, "D24", 0.4694, BLUE, DEC); put(ws, "F24", "Same dataset: Food Processing (78 firms). A judgment: there is no pet food industry in the dataset", NOTE)
for r in (23, 24):
    put(ws, f"C{r}", f"=B{r}/$B$25", BLK, PCT); put(ws, f"E{r}", f"=C{r}*D{r}", BLK, DEC)
put(ws, "A25", "Unlevered beta", BOLD); put(ws, "B25", "=SUM(B23:B24)", BLK, NUM); put(ws, "E25", "=SUM(E23:E24)", BOLD, DEC)

header(ws, 27, ["Capital structure at market values", "Value", "", "", "", "Source"])
cs = [("Shares outstanding (millions)", 794.920513, "0.000", "10-Q cover, 2026-09-30"), ("Share price", 98.71, "0.00", "NYSE close 2026-11-20"),
      ("Debt at fair value", 7518, NUM, "10-K note 7, 2025-12-31"), ("Operating lease liabilities", 566, NUM, "10-K (XBRL OperatingLeaseLiability), 2025-12-31")]
for i, (n, v, f, s) in enumerate(cs, 28):
    put(ws, f"A{i}", n); put(ws, f"B{i}", v, BLUE, f); put(ws, f"F{i}", s, NOTE)
put(ws, "A32", "Equity (E)"); put(ws, "B32", "=B28*B29", BLK, NUM)
put(ws, "A33", "Debt (D)"); put(ws, "B33", "=B30+B31", BLK, NUM)
put(ws, "A34", "Debt ratio D/(D+E)"); put(ws, "B34", "=B33/(B33+B32)", BLK, PCT)
put(ws, "A35", "Debt to equity D/E"); put(ws, "B35", "=B33/B32", BLK, DEC)

header(ws, 37, ["Cost of capital", "Value", "", "", "", "Source"])
put(ws, "A38", "Marginal tax rate"); put(ws, "B38", 0.25, BLUE, PCT); put(ws, "F38", "Damodaran country tax rates: United States, federal plus state", NOTE)
put(ws, "A39", "Levered beta"); put(ws, "B39", "=E25*(1+(1-B38)*B35)", BLK, DEC)
put(ws, "A40", "Cost of equity"); put(ws, "B40", "=B6+B39*E13", BLK, PCT)
put(ws, "A41", "Default spread for A+"); put(ws, "B41", 0.007, BLUE, PCT); put(ws, "F41", "S&P rating A+ (Capital IQ); spread from Damodaran ratings table, January 2026. Synthetic rating from coverage would be AAA, spread 0.40%", NOTE)
put(ws, "A42", "Pre-tax cost of debt"); put(ws, "B42", "=B4+B41", BLK, PCT); put(ws, "F42", "Spreads are measured over the Treasury rate, so the base is B4, not B6", NOTE)
put(ws, "A43", "After-tax cost of debt"); put(ws, "B43", "=B42*(1-B38)", BLK, PCT)
put(ws, "A44", "Cost of capital", BOLD); put(ws, "B44", "=B40*(1-B34)+B43*B34", BOLD, PCT)
put(ws, "F44", "8.35% here against 8.34% in the professor's spreadsheets: they were given the premium rounded to 5.38%; this tab carries it unrounded.", NOTE)
put(ws, "A46", "Return on invested capital, FY2025", BOLD)
roic = [("Operating income as reported", 3306, "10-K income statement"), ("Add back: goodwill and intangible write-down", 919, "10-K cash flow statement (skin health unit, mainly Filorga)"),
        ("Total equity with noncontrolling interests", 365, "10-K balance sheet"), ("Debt at carrying value", 7988, "10-K note 7"), ("Cash and marketable securities", 1395, "10-K balance sheet"),
        ("Write-downs since 2021 added back to capital", 2211, "XBRL GoodwillAndIntangibleAssetImpairment: 571 (2021), 721 (2022), 919 (2025)")]
for i, (n, v, s) in enumerate(roic, 47):
    put(ws, f"A{i}", n); put(ws, f"B{i}", v, BLUE, NUM); put(ws, f"F{i}", s, NOTE)
put(ws, "A53", "Operating income used"); put(ws, "B53", "=B47+B48", BLK, NUM)
put(ws, "A54", "Invested capital"); put(ws, "B54", "=B49+B50-B51+B52", BLK, NUM)
put(ws, "A55", "Return on invested capital", BOLD); put(ws, "B55", "=B53*(1-B38)/B54", BOLD, PCT)
put(ws, "A56", "Return less cost of capital"); put(ws, "B56", "=B55-B44", BLK, PCT)

# ---------------- Beta regression
ws = sheet("Beta regression", [12, 14, 16, 12, 12, 4, 34, 14, 60])
put(ws, "A1", "Regression beta: CL against the S&P 500", H1)
header(ws, 3, ["Month", "CL adjusted close", "S&P 500 total return", "CL return", "Market return"])
data = [r for r in csv.DictReader(open("sources/market-data/cl-vs-sp500-monthly-2020-12-to-2026-11.tsv"), delimiter="\t") if r["month"] <= "2026-10"][-61:]
for i, r in enumerate(data, 4):
    put(ws, f"A{i}", r["month"], BLUE); put(ws, f"B{i}", float(r["cl_adj_close"]), BLUE, "0.000"); put(ws, f"C{i}", float(r["sp500_total_return"]), BLUE, "#,##0.00")
    if i > 4:
        put(ws, f"D{i}", f"=B{i}/B{i-1}-1", BLK, PCT); put(ws, f"E{i}", f"=C{i}/C{i-1}-1", BLK, PCT)
a, b = 5, 3 + len(data)
y, x = f"D{a}:D{b}", f"E{a}:E{b}"
out = [("Observations", f"=COUNT({y})", "0"), ("Beta (slope)", f"=SLOPE({y},{x})", "0.000"), ("Standard error of beta", f"=STEYX({y},{x})/SQRT(DEVSQ({x}))", "0.000"),
       ("R-squared", f"=RSQ({y},{x})", "0.000"), ("Intercept (monthly)", f"=INTERCEPT({y},{x})", PCT),
       ("Annualized standard deviation of CL returns", f"=STDEV({y})*SQRT(12)", PCT)]
header(ws, 3, ["Month", "CL adjusted close", "S&P 500 total return", "CL return", "Market return", "", "Result", "Value", "Note"])
for i, (n, f, fm) in enumerate(out, 4):
    put(ws, f"G{i}", n); put(ws, f"H{i}", f, BOLD, fm)
put(ws, "I5", "Capital IQ shows a five-year beta of 0.31. The cost of capital uses the bottom-up beta instead.", NOTE)
put(ws, "I7", "The market explains about 6% of the stock's movement; the rest is company-specific.", NOTE)
put(ws, "I9", "Simple returns here; the option input in the valuation used log returns (19.08%).", NOTE)
put(ws, "G11", "Source: Yahoo Finance chart endpoint, dividend-adjusted month-end closes, read 2026-11-21.", NOTE)

# ---------------- Dividends
ws = sheet("Dividends", [8, 12, 14, 14, 14, 12, 14, 12, 12, 14, 14, 14, 14])
put(ws, "A1", "Cash returned against free cash flow to equity, 2018–2025", H1)
header(ws, 3, ["Year", "Net income", "D&A plus non-cash write-downs", "Capex plus acquisitions", "Change in non-cash working capital", "Net debt issued", "Free cash flow to equity", "Dividends", "Buybacks", "Cash returned", "Returned less FCFE", "Option exercise proceeds", "Buybacks net of option proceeds"])
dv = [(2025,2132,1549,857,-344,-456,1823,1210,101),(2024,2889,605,561,-360,-408,1789,1739,638),(2023,2300,567,705,-466,-314,1749,1128,380),(2022,1785,1266,1505,675,1647,1691,1308,418),
      (2021,2166,1127,567,142,-175,1679,1320,424),(2020,2695,539,763,-407,-597,1654,1476,874),(2019,2367,519,2046,22,1433,1614,1202,498),(2018,2400,511,1164,119,-179,1591,1238,329)]
for i, (yr, ni, da, cx, wc, nd, dvd, bb, op) in enumerate(dv, 4):
    put(ws, f"A{i}", str(yr), BLUE)
    for col, v in zip("BCDEF", (ni, da, cx, wc, nd)): put(ws, f"{col}{i}", v, BLUE, NUM)
    put(ws, f"G{i}", f"=B{i}-(D{i}-C{i})-E{i}+F{i}", BLK, NUM)
    put(ws, f"H{i}", dvd, BLUE, NUM); put(ws, f"I{i}", bb, BLUE, NUM)
    put(ws, f"J{i}", f"=H{i}+I{i}", BLK, NUM); put(ws, f"K{i}", f"=J{i}-G{i}", BLK, NUM)
    put(ws, f"L{i}", op, BLUE, NUM); put(ws, f"M{i}", f"=I{i}-L{i}", BLK, NUM)
put(ws, "A12", "Total", BOLD)
for col in "BCDEFGHIJKLM": put(ws, f"{col}12", f"=SUM({col}4:{col}11)", BOLD, NUM)
put(ws, "A14", "Cash returned as % of free cash flow to equity", BOLD); put(ws, "G14", "=J12/G12", BOLD, PCT)
put(ws, "A15", "Gap after option proceeds (returned less FCFE less option proceeds)", BOLD); put(ws, "G15", "=K12-L12", BOLD, NUM)
put(ws, "A16", "Gap after option proceeds as % of cash returned", BOLD); put(ws, "G16", "=G15/J12", BOLD, PCT)
put(ws, "A18", "Source: SEC XBRL company facts for Colgate (net income, D&A, write-downs 571 / 721 / 919 in 2021 / 2022 / 2025, capital spending, acquisitions, changes in receivables, inventories and payables, debt proceeds and repayments, dividends, buybacks, option proceeds); FY2025 10-K cash flow statement for the 2025 payables change.", NOTE)
put(ws, "A19", "Free cash flow to equity = net income − (capex + acquisitions − D&A and write-downs) − change in working capital + net debt issued. It leaves out cash from option exercises, so buybacks are also shown net of that cash.", NOTE)

# ---------------- Debt design
ws = sheet("Debt design", [46, 12, 12, 12, 12, 12, 60])
put(ws, "A1", "Debt design", H1)
mw = openpyxl.load_workbook("professor-spreadsheet/originals/macrodur.xlsx", data_only=True)
sec = {int(r[0]): r for r in mw["Sector Averages by SIC"].iter_rows(values_only=True) if isinstance(r[0], (int, float)) and r[2] is not None}
header(ws, 3, ["Bottom-up: sector averages (macrodur.xlsx)", "Weight", "Duration", "Cyclicality", "Inflation", "Currency", "Note"])
for i, (sic, w, note) in enumerate([(2844, "='Cost of capital'!C23", "Colgate's own SIC code; weight = Oral, Personal and Home Care share of sales"), (2040, "='Cost of capital'!C24", "Stand-in for Hill's: pet food is SIC 2047, inside group 204; 2047 is not in the table")], 4):
    r = sec[sic]; put(ws, f"A{i}", f"SIC {sic}: {r[1]}"); put(ws, f"B{i}", w, Font(name="Arial", size=10, color="008000"), PCT)
    for col, v in zip("CDEF", (-r[2], r[3], r[8], r[9])): put(ws, f"{col}{i}", round(v, 4), BLUE, "0.00")
    put(ws, f"G{i}", note, NOTE)
put(ws, "A6", "Weighted", BOLD)
for col in "CDEF": put(ws, f"{col}6", f"=SUMPRODUCT($B$4:$B$5,{col}4:{col}5)", BOLD, "0.00")
put(ws, "G6", "Sector estimates use quarterly data for 1987–1997. Duration and cyclicality from firm value; inflation and currency from operating income, as the workbook advises.", NOTE)

header(ws, 9, ["Top-down: Colgate's own history", "Operating income", "Firm value", "% chg operating income", "% chg firm value", "", "Note"])
facts = {}
for row in csv.reader(open("sources/filings/cl-multi-year-financials-fy2014-fy2025.tsv"), delimiter="\t"):
    if row[0] == "taxonomy": hdr = row; continue
    facts[row[1]] = {int(yy): float(v) / 1e6 for yy, v in zip(hdr[3:], row[3:]) if v != ""}
close = {2016: 65.44, 2017: 75.45, 2018: 59.52, 2019: 68.84, 2020: 85.51, 2021: 85.34, 2022: 78.79, 2023: 79.71, 2024: 90.91, 2025: 79.02}
macro = {int(r[0]): r for r in mw["Annual Data"].iter_rows(min_row=2, values_only=True) if isinstance(r[0], (int, float))}
put(ws, "H9", "Change in 10-year rate", BOLD); put(ws, "I9", "Real GDP growth", BOLD); put(ws, "J9", "Change in inflation", BOLD); put(ws, "K9", "% change in the dollar", BOLD)
for c in "HIJK": ws[f"{c}9"].fill = HDR; ws[f"{c}9"].alignment = Alignment(wrap_text=True, vertical="top"); ws.column_dimensions[c].width = 14
first = 10
for i, yr in enumerate(range(2014, 2026), first):
    oi = facts["OperatingIncomeLoss"][yr] + facts.get("GoodwillAndIntangibleAssetImpairment", {}).get(yr, 0)
    put(ws, f"A{i}", str(yr), BLUE); put(ws, f"B{i}", round(oi, 1), BLUE, NUM)
    d = facts.get("LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities", {}).get(yr) or facts.get("LongTermDebt", {}).get(yr)
    if yr in close and d: put(ws, f"C{i}", round(close[yr] * facts["WeightedAverageNumberOfSharesOutstandingBasic"][yr] + d, 1), BLUE, NUM)
    if i > first: put(ws, f"D{i}", f"=B{i}/B{i-1}-1", BLK, PCT)
    if yr > 2016: put(ws, f"E{i}", f"=C{i}/C{i-1}-1", BLK, PCT)
    m = macro[yr]
    for col, v in zip("HIJK", (m[2], m[4], m[6], m[8])): put(ws, f"{col}{i}", round(v, 6), BLUE, PCT)
last = first + 11
put(ws, "G10", "Operating income: reported, with goodwill and intangible write-downs added back (SEC XBRL). Firm value: year-end close × weighted basic shares + long-term debt. Macro data: macrodur.xlsx, Annual Data sheet.", NOTE)
header(ws, 24, ["One-variable regressions", "vs rate change", "vs GDP growth", "vs inflation change", "vs dollar change", "", "Note"])
put(ws, "A25", "% change in operating income: coefficient"); put(ws, "A26", "   R-squared"); put(ws, "A27", "% change in firm value: coefficient"); put(ws, "A28", "   R-squared")
for col, mc in zip("BCDE", "HIJK"):
    yo, xo = f"$D${first+1}:$D${last}", f"{mc}{first+1}:{mc}{last}"
    yf, xf = f"$E${first+3}:$E${last}", f"{mc}{first+3}:{mc}{last}"
    put(ws, f"{col}25", f"=SLOPE({yo},{xo})", BLK, "0.00"); put(ws, f"{col}26", f"=RSQ({yo},{xo})", BLK, "0.00")
    put(ws, f"{col}27", f"=SLOPE({yf},{xf})", BLK, "0.00"); put(ws, f"{col}28", f"=RSQ({yf},{xf})", BLK, "0.00")
put(ws, "G25", "11 yearly changes for operating income, 9 for firm value. None is statistically significant, so the bottom-up numbers and the intuitive argument carry the debt design.", NOTE)
put(ws, "G27", "Duration from firm value = negative of the rate coefficient (B27).", NOTE)

header(ws, 31, ["The debt Colgate has (rated notes, Capital IQ, 2026-07-17)", "Value", "", "", "", "", "Note"])
dd = [("Rated notes counted", 21, "0", "S&P rated note list; commercial paper programs excluded"), ("Principal, $M", 6869, NUM, "Euro notes converted at 1.174, the rate Capital IQ carries them at"),
      ("Weighted average maturity, years", 9.6, "0.0", "From 2026-11-20; computed in macro-sensitivity.py. Maturity is longer than duration"), ("Euro-denominated share", 0.359, PCT, "Four euro notes: 500, 500, 500 and 600 million"),
      ("Floating-rate share", 0.095, PCT, "Floating-rate medium-term notes")]
for i, (n, v, f, s) in enumerate(dd, 32):
    put(ws, f"A{i}", n); put(ws, f"B{i}", v, BLUE, f); put(ws, f"G{i}", s, NOTE)

# ---------------- Spreadsheet results
ws = sheet("Spreadsheet results", [50, 18, 18, 70])
put(ws, "A1", "Results read from the professor's spreadsheets", H1)
header(ws, 3, ["capstru.xlsx — optimal debt ratio", "Current", "Optimal", "Note"])
cr = [("Debt to capital", 0.0934, 0.30, PCT, "The sheet steps in tens; 40% drops the rating to CCC"), ("Cost of capital", 0.0834, 0.0809, PCT, "Current matches the Cost of capital tab"),
      ("Enterprise value, $M", 85154, 90960, NUM, ""), ("Value per share", 98.71, 106.01, "0.00", "EBITDA 4,855 = operating income 4,225 + D&A 630"), ("Interest coverage", 15.82, 3.18, "0.00", "")]
for i, (n, a, b, f, s) in enumerate(cr, 4):
    put(ws, f"A{i}", n); put(ws, f"B{i}", a, BLUE, f); put(ws, f"C{i}", b, BLUE, f); put(ws, f"D{i}", s, NOTE)
header(ws, 10, ["fcffsimpleginzu.xlsx — valuation", "Base case", "All sheet defaults", "Note"])
gz = [("Value of operating assets, $M", 56717, 47989, NUM, "Base case: stable return on capital 20%, growth in perpetuity 3%, stable cost of capital 8.43%"),
      ("Present value of terminal value, $M", 32940, 24519, NUM, "All defaults: return equals cost of capital, growth 4.82%, stable cost of capital 9.05%"),
      ("Value per share", 61.83, 50.90, "0.00", "Price 98.71"),
      ("Price as % of value", 1.5964, 1.9393, PCT, "")]
for i, (n, a, b, f, s) in enumerate(gz, 11):
    put(ws, f"A{i}", n); put(ws, f"B{i}", a, BLUE, f); put(ws, f"C{i}", b, BLUE, f); put(ws, f"D{i}", s, NOTE)
put(ws, "A16", "Sensitivity of the base case (value per share)", BOLD)
sens = [("Growth in perpetuity at the sheet default, 4.82%", 79.74, "With returns above the cost of capital, growth adds value"),
        ("Stable return equal to the cost of capital, growth 4.82%", 53.82, "Stable cost of capital kept at 8.43%"),
        ("Cost of capital 7.84% (beta 0.63)", 63.82, "Low end of the beta range; stable cost of capital unchanged"),
        ("Cost of capital 8.67% (beta 0.80)", 60.56, "High end of the beta range")]
for i, (n, v, s) in enumerate(sens, 17):
    put(ws, f"A{i}", n); put(ws, f"B{i}", v, BLUE, "0.00"); put(ws, f"D{i}", s, NOTE)
put(ws, "A22", "Valuation inputs that differ from the sheet's defaults", BOLD)
vi = [("Cost of capital", "8.34%, entered directly", "So all three spreadsheets use the same number as the Cost of capital tab"),
      ("Stable cost of capital", "8.43%", "Riskfree 4.82% + mature premium 3.61%. The sheet default uses its January premium (4.23%) and gives 9.05%"),
      ("Stable return on capital", "20%", "Under half of the 42% base-year return; household products industry average is 34%"),
      ("Growth in perpetuity", "3%", "Sheet default is the riskfree rate, 4.82%. Analyst consensus revenue growth is 2.3% to 3.5%; sales grew 3.3% a year from 2016 to 2025"),
      ("Revenue growth", "2.25% next year, 3.1% for years 2–5", "Analyst consensus (Capital IQ): 2027 to 2030 revenue grows 3.1% a year"),
      ("Operating margin", "20.5% rising to 21.3% by year 5", "Analyst consensus (21.2% rising to 22%) leaves out restructuring and similar charges. These ran about 0.7% of sales a year from 2023 to September 2026, so the margins are lowered by that much"),
      ("Sales to capital", "2.2", "Colgate's own ratio (sales 20,382 over invested capital 9,169) and the US household products average (2.21). The sheet default is the global average, 1.79"),
      ("Effective tax rate", "23.5%", "23.1% for 2025 excluding the write-down; 23.8% for the first nine months of 2026"),
      ("Trailing operating income", "4,080", "Reported 3,161 plus the 919 write-down booked in Q4 2025")]
for i, (n, v, s) in enumerate(vi, 23):
    put(ws, f"A{i}", n); put(ws, f"B{i}", v, BLUE); put(ws, f"D{i}", s, NOTE)
header(ws, 33, ["dividends.xlsx — 2018–2025", "Total", "", "Note"])
dr = [("Free cash flow to equity, $M", 18819, NUM, "Matches the Dividends tab, G12"), ("Dividends plus buybacks, $M", 24211, NUM, "Matches the Dividends tab, J12"), ("Dividend payout ratio", 0.7254, PCT, "")]
for i, (n, a, f, s) in enumerate(dr, 34):
    put(ws, f"A{i}", n); put(ws, f"B{i}", a, BLUE, f); put(ws, f"D{i}", s, NOTE)

wb.save(OUT); print("saved", OUT, wb.sheetnames)
