---
title: Accounting Primer — Reading Financial Statements
status: active
owner: weprintmoney
created: 2026-09-01
last_updated: 2026-09-01
---

# A Primer on Financial Statements

> Source: [Aswath Damodaran, NYU Stern](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/AccPrimer/accstate.htm) — converted to markdown 2026-09-01.

> Note: This is a faithful study adaptation of Damodaran's primer. Structure, tables, formulas, and every substantive point are preserved; connective prose is closely paraphrased rather than copied verbatim.

Most of the raw information used in valuation and corporate finance comes out of financial statements, so understanding the basic statements — and the ratios built on them — is a necessary first step for either pursuit. But there is a gap between what accountants set out to measure and what financial analysts want measured. Much of that gap comes from different objectives: accounting measures a firm's *current standing and immediate past performance*, while financial analysis is fundamentally *forward-looking*.

The primer therefore starts with an inventory of the information an analyst wants about a firm, then examines how accounting statements try to supply it — and where they fall short.

## Informational Needs

Before getting into accounting principles and statement mechanics, start with the more fundamental question: when analyzing a firm, what do we actually want to know? The frame is the firm described from a financial standpoint — the "financial balance sheet":

*[Figure 1: A two-column financial balance sheet. Assets side — **Assets in Place** (existing investments that generate cash flows today; includes both long-lived fixed assets and short-lived working-capital assets) and **Growth Assets** (the expected value that will be created by future investments). Liabilities side — **Debt** (a fixed claim on cash flows; little or no role in management; fixed maturity; tax deductible) and **Equity** (a residual claim on cash flows; a significant role in management; perpetual life). Takeaway: this is the finance view of a firm, as opposed to the accounting balance sheet.]*

A financial analysis of a firm should be able to answer these questions:

- What are the assets the firm already has in place, and how much are they worth?
- What are the firm's growth assets, and what is their value?
- What is the firm earning on its assets in place, and what can it expect to earn on those assets and on its growth assets?
- What mix of debt and equity is the firm using to finance these assets?
- How much risk is there in the firm, and what is the cost of its debt and equity financing?

*[Figure 2: The same financial-balance-sheet layout with the analyst's questions mapped onto each quadrant — Assets in Place: "What are the assets in place? How valuable are these assets? How risky are these assets?"; Growth Assets: "What are the growth assets? How valuable are these assets?"; Debt: "What is the value of the debt? How risky is the debt?"; Equity: "What is the value of the equity? How risky is the equity?" Takeaway: every valuation question maps to one of the four boxes.]*

Accounting statements give some information on all of these questions, but they fall short both in **timeliness** and in **how they measure asset value, earnings, and risk**.

## How Accountants Measure Earnings

Two basic principles govern the accounting measurement of earnings:

- **Accrual accounting.** Revenue from selling a good or service is recognized in the period in which the good is sold or the service is performed (wholly or substantially) — not when cash arrives. On the expense side, a matching effort ties expenses to the revenues they generate.
- **Categorization of expenses into operating, financing, and capital expenses.**
  - *Operating expenses* — in theory, provide benefits only in the current period (e.g., the labor and materials used to make products sold this period).
  - *Financing expenses* — arise from non-equity financing used to raise capital; interest expense is the most common example.
  - *Capital expenses* — expected to generate benefits over multiple periods (e.g., the cost of buying land and buildings).

The income statement is where accountants measure how profitable a firm was during the period. Its key line items, the principles behind each, and the measurement issues:

| Item | Accounting Principles | Issues in Measurement |
|---|---|---|
| **Revenues** | Only revenues from sales made *during the period* count — not cash receipts. Cash collected now on prior-period sales is excluded; current-period sales not yet collected are included. | • For [contract work](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/AccPrimer/accrev.htm) and multi-year projects, revenues can be posted as work is completed. <br>• Some firms try to record as many sales as possible before period-end to inflate current income. |
| **(minus) Operating Expenses** (excl. depreciation) | Only expenses incurred to create *current-period* revenues belong here — labor, materials, marketing, G&A. Material bought but not used in production carries over as inventory. Inventory must be valued to estimate operating expenses; firms may value it at the cost of material bought at period-end (FIFO), at the start of the period (LIFO), or at an average price. | • Accounting rules force [R&D costs](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/AccPrimer/research.htm) to be expensed as incurred — violating the principle that operating expenses should generate current-period revenues. <br>• Where a lease [qualifies as an operating lease](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/AccPrimer/lease.htm), lease payments are treated as operating expenses. <br>• [One-time restructuring charges](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/AccPrimer/onetime.htm) can also qualify as operating expenses. |
| **(minus) Depreciation and Amortization** | A capital expense (one expected to generate income over multiple periods) is written off over its lifetime — depreciation for tangible assets (machinery), amortization for intangibles (a copyright). Because the value lost each period is subjective, schedules are mechanized: *straight line* (equal write-off each period) or *accelerated* (more in early years, less later). | • In the US, depreciation must be based on original cost (book value); some high-inflation economies allow asset revaluation. <br>• Accounting depreciation may bear little or no resemblance to *economic* depreciation (the actual loss in value from using the asset). <br>• US firms may use different methods for tax vs. reporting — typically accelerated for tax (lowers taxable income and taxes), straight line for reporting. |
| **= Operating Income (EBIT)** | Revenues minus operating expenses and depreciation. Designed to measure the income generated by the firm's *assets in place*. | • To the extent R&D is really a capital expense, operating leases are really financing expenses, and accounting depreciation is not economic depreciation — operating income can mislead. |
| **(minus) Interest Expenses** | Most directly, interest on debt from lenders (banks) or public bonds; also includes imputed interest on capital leases. Substantial interest income on cash and marketable securities is usually shown here as well. | • Interest is tax deductible and must be netted out to reach taxable income. <br>• Some firms carry *non-cash* interest expenses — tax deductible, but they must be tracked for cash-flow purposes. |
| **= Taxable Income** | If the reported depreciation equals tax depreciation, operating income minus interest expense yields taxable income. | • Where tax and reporting computations differ (especially depreciation), reported taxable income differs from — and is generally *higher* than — taxable income in the tax books. |
| **(minus) Taxes** | Taxes due and payable on current-period income: `Tax = Taxable Income × Tax Rate` | • Firms report an "effective" tax rate = taxes ÷ reported taxable income. Since reported taxable income usually exceeds true taxable income, the effective rate usually understates the firm's true average tax rate. |
| **= Net Income** | Income after taxes and interest. | • With preferred stockholders present, preferred dividends are subtracted to get net income to *common* stockholders. |
| **(minus) Losses (+ Profits) not associated with operations** | Expenses or income unrelated to operations. | — |
| **(minus) Profits or Losses from Accounting Changes** | Changes in accounting methods (e.g., how inventory is valued) can produce earnings effects. | — |
| **/ Number of Shares Outstanding** | Actual shares outstanding = *primary* shares. With options and convertibles outstanding, their embedded shares are sometimes added to get *fully diluted* shares. | • Options, warrants and convertibles are all equity; simply adding the shares their holders are entitled to is a poor way to handle those holders' claims on the firm's equity. |
| **= Earnings per Share** | Can be computed on a primary or fully diluted basis. | — |

## How Accountants Value Assets

A firm's assets are measured and reported on its balance sheet. They fall broadly into fixed assets, current assets, intangible assets, and financial assets. Three basic principles underlie accounting asset valuation:

- **An abiding belief in book value as the best estimate of value.** Accounting starts from book value; absent a compelling reason otherwise, historical cost is treated as the best estimate of an asset's value.
- **A distrust of market or estimated value.** Where a market value exists that differs from book value, accounting convention views it with suspicion — as too volatile and too easily manipulated. The suspicion runs deeper still for values estimated from expected future cash flows.
- **Better to underestimate value than overestimate it.** Given multiple valuation approaches, convention favors the more conservative (lower) estimate — e.g., when both market and book values are available, rules often require the *lesser* of the two.

| Item | Principles Governing Measurement | Measurement Issues |
|---|---|---|
| **Fixed Assets** | Tangible assets with long lives. US GAAP requires valuation at historical cost, adjusted for the estimated loss in value from aging (depreciation). | • Accounting depreciation follows mechanistic rules (straight line or accelerated) and bears no resemblance to economic depreciation. <br>• Under inflation, historical cost can significantly *undervalue* older fixed assets. <br>• The recorded asset value has little or no relationship to the asset's earning power. |
| **Current Assets** | Assets with short lives (generally < 1 year): inventory (raw materials and finished goods), accounts receivable, cash. Receivables are recorded at the amount owed at the time of the credit sale; firms may set aside a reserve for *expected bad debts*, which reduces receivables. Cash is at face value. [Inventory can be valued three ways](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/AccPrimer/inventory.htm): cost of material bought at period-end (FIFO), at period-start (LIFO), or a weighted average. | • The discretion on inventory valuation and bad-debt reserves invites game playing. In inflationary periods, switching FIFO → LIFO lowers *reported* earnings — but if the change is for reporting only, neither true income nor cash flows are affected. |
| **Financial Investments** | Three types: <br>• *Minority, passive* (< 20% ownership): if long-term, recorded at book value with interest/dividends flowing to the income statement; if short-term, marked to market with gains/losses recorded each period. <br>• *Minority, active* (20–50%): recorded at original acquisition cost, adjusted each period for the proportional share of the investee's profits or losses (the equity approach). <br>• *Majority, active* (controlling interest): the two firms' income statements and balance sheets are consolidated in full; the portion held by others appears as *minority interest*. | • Financial investments have an observable market value. Recording them at a book value far below market suggests they are misvalued. |
| **Intangible Assets** | In an acquisition accounted for with [purchase accounting](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/AccPrimer/goodwill.htm), the excess of acquisition price over the target's book value is *goodwill*, amortized over 40 years (amortization not tax deductible). Patents or copyrights acquired from others can be shown as intangible assets; their amortization usually *is* tax deductible. | • [Goodwill](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/AccPrimer/goodwill.htm) is not really an asset: if book value measures assets in place and a fair price was paid, the difference measures *growth assets*; if the acquirer overpaid, goodwill mostly reflects the overpayment. <br>• Treating *acquired* patents as assets while internally developed patents never reach the balance sheet is an inconsistency. |

## How Accountants Value Liabilities

The principles behind the measurement of liabilities and equity:

- **A rigid categorization of financing into debt or equity**, based on the nature of the obligation. To be recognized as a liability, an obligation must meet three requirements:
  1. It must be expected to lead to a future cash outflow (or loss of a future cash inflow) at a specified or determinable date;
  2. The firm cannot avoid the obligation; and
  3. The transaction giving rise to the obligation has already happened.

  Consistent with conservatism in asset valuation, accountants recognize as liabilities only cash-flow obligations that cannot be avoided; a *residual* obligation is treated as equity.
- **Historical cost over market value or expected cash flows.** How liabilities and equity are measured is inextricably linked to how assets are measured: since assets are carried primarily at historical cost/book value, debt and equity are measured primarily at book value too.

| Item | How It Is Measured | Measurement Issues |
|---|---|---|
| **Current Liabilities** | Liabilities coming due within the next year: short-term debt, accounts and salaries payable, and long-term debt maturing within the year. Recorded at the actual amounts due. | • Generally recorded at values close to true value — book ≈ market here. |
| **Long Term Debt** | Long-term bank debt and corporate bonds. Measured as the present value of payments due, discounted at the interest rate *at the time of borrowing*. The PV is **not** recomputed as rates change afterward. | • If rates rise after issuance, book value overstates market value of the debt; if rates fall, book understates market. <br>• Foreign-currency debt must be adjusted for exchange-rate changes. <br>• Convertible debt is shown at book value as debt; on conversion it becomes equity. |
| **Other Long Term Liabilities** | Three primary items: (1) leases qualifying as *capital leases* — PV of lease payments shown as long-term debt; (2) an underfunded [defined-benefit pension or health care plan](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/AccPrimer/emplben.htm) — the underfunding is a long-term liability; (3) *deferred taxes* (e.g., from accelerated depreciation and favorable inventory methods) shown as a liability. | • Unlike long-term debt, these are not interest-bearing. They are liabilities in the broadest sense, but the absence of a cash-flow claim argues for caution in treating them as debt — and it is unclear what claims these holders would have if the firm defaulted. |
| **Preferred Stock** | Generally carries a fixed dividend; in some cases dividends cumulate if unpaid. Carried at original issue price, plus any cumulated unpaid dividends. Convertible preferred is treated the same, becoming equity on conversion. | • Accountants have historically treated preferred stock as quasi-equity or equity (preferred holders can't force default; no finite life). To a financial analyst, preferred stock looks like very expensive, unsecured debt. |
| **Common Equity** | A historical-cost measure: original proceeds from issuing the equity, plus earnings since (or minus losses), minus dividends paid out. | • Stock repurchased for short periods (for reissue or option exercises) can be shown as *treasury stock*, reducing book equity. Treasury stock cannot be kept on the books indefinitely — buybacks force a reduction of book equity by the repurchase value. Since buybacks happen at market prices, they can slash book equity. <br>• Extended losses or massive buybacks can leave a firm with *negative* book equity. |

## How Accountants Measure Profitability

The income statement gauges profitability in absolute terms; percentage returns matter just as much. Two basic gauges: profitability **relative to capital employed** (a rate of return on investment — from the equity investors' viewpoint or for the entire firm) and profitability **relative to sales** (a profit margin).

| Measure | Definition | Remarks |
|---|---|---|
| **Return on Capital** | `EBIT (1 − tax rate) / (Book Value of Debt + Book Value of Equity)` | • Using pre-tax operating income instead makes this a *pre-tax* return on capital. <br>• Book value proxies for capital invested; if book value is a poor estimate, return on capital is mis-estimated. |
| **Return on Assets** | `EBIT (1 − tax rate) / Book Value of Assets` | • Assets differ from capital by *current liabilities* (capital excludes them). <br>• In finance, return on capital can be compared to the cost of capital; return on assets cannot. |
| **Return on Equity** | `Net Income / Book Value of Equity` | • Measures profitability of the equity invested in the firm. <br>• ROE can be raised by increasing net income *or* lowering book equity (e.g., via buybacks). <br>• If book equity goes negative (after extended losses), ROE can no longer be computed. |
| **Net Margin** | `Net Income / Sales` | • Average profit per dollar of sales. <br>• Because it is measured after financial expenses, it is lower for highly levered firms. |
| **Operating Margin** | `EBIT (1 − tax rate) / Sales` | • Based on income before interest expense, so far more comparable across firms with different leverage. |

## How Accountants Measure Leverage

Leverage, unsurprisingly, is measured with book values of debt and equity. The most widely used ratios:

| Leverage Measure | Definition | Remarks |
|---|---|---|
| **Debt/Capital** | `Book Value of Debt / (Book Value of Debt + Book Value of Equity)` | • Both ratios measure degree of leverage, but both are heavily influenced by how far book value diverges from market value. <br>• Since market equity typically far exceeds book equity while market debt ≈ book debt, these ratios tend to *overstate* leverage. <br>• They also depend on what counts as debt — operating leases don't show up as debt, so they don't affect measured leverage. |
| **Debt/Equity** | `Book Value of Debt / Book Value of Equity` | (see above — same remarks apply) |
| **Cash Fixed Charges Coverage** | `EBITDA / Cash Fixed Charges` | • Coverage ratios measure capacity to meet cash-flow obligations; low ratios and/or variable earnings mean higher default risk. <br>• Fixed charges exclude discretionary outlays such as capital expenditures — which may nonetheless be essential to long-term survival. |
| **Interest Coverage** | `EBIT / Interest Expenses` | (see above — same remarks apply) |

## In Summary

Financial statements remain the primary information source for most investors and analysts. Mastery of every FASB rule isn't required, but the basics are: what the statements measure, the GAAP conventions beneath them, and the ratios that accompany financial analysis. The key caveat — financial statements and ratios are a *means to an end*: understanding and valuing the firm. Kept in that frame, they are useful.
