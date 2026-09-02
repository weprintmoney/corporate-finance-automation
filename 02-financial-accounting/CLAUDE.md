# Financial Accounting

Foundational accounting: recording transactions, preparing statements, and reading them.

## Core Concepts

| Concept | Notes |
|---------|-------|
| Accounting equation | Assets = Liabilities + Equity |
| Double-entry | Every transaction has equal debits and credits |
| Accrual vs. cash basis | Recognize revenue when earned, expense when incurred |
| GAAP vs. IFRS | Coursework defaults to US GAAP unless noted |

## Financial Statements

| Statement | Answers |
|-----------|---------|
| Balance Sheet | What does the company own and owe at a point in time? |
| Income Statement | How profitable was the period? |
| Cash Flow Statement | Where did cash come from and go? (Operating / Investing / Financing) |
| Statement of Equity | How did equity change over the period? |

## Common Ratios

| Ratio | Formula | Reads |
|-------|---------|-------|
| Current | Current Assets / Current Liabilities | Short-term liquidity |
| Quick | (Current Assets − Inventory) / Current Liabilities | Liquidity minus slow inventory |
| Debt-to-Equity | Total Debt / Total Equity | Leverage |
| Gross Margin | Gross Profit / Revenue | Unit economics |
| ROA | Net Income / Total Assets | Asset efficiency |
| ROE | Net Income / Shareholder Equity | Equity efficiency |

## Doc Index

| File | Description |
|------|-------------|
| [modules/lesson-index.yaml](modules/lesson-index.yaml) | Full lesson map: folder, topic, available file types (10 lessons, module-1) |
| [modules/brightspace-export.py](modules/brightspace-export.py) | Brightspace export script — downloads PDFs, converts with marker, generates lesson-overview.md |

## Navigation

To find a specific lesson, read `modules/lesson-index.yaml`. Jump directly to `modules/module-1/lesson-NN/`. Each lesson folder contains:

- `reading-*.md` — required reading PDFs converted to markdown (marker, vision-native)
- `exercise-*.md` — in-class exercise PDFs converted to markdown
- Raw `.pdf` files alongside their `.md` conversions
- `lesson-overview.md` — lesson summary with video links and file index

## Export script

```bash
# Re-export all lessons (cookies in .brightspace-accounting.env)
python3 02-financial-accounting/modules/brightspace-export.py

# Single lesson
python3 02-financial-accounting/modules/brightspace-export.py --lesson 3

# Re-convert PDFs with marker even if .md exists
python3 02-financial-accounting/modules/brightspace-export.py --reconvert-slides --force
```
