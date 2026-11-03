---
title: "The Coca-Cola Company (KO) — Lesson 07: Country Risk Premiums"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# The Coca-Cola Company (KO) — Lesson 07: Country Risk Premiums

### Lesson 07 — Country Risk Premiums

Quick mode: no transcript-layer entries carry a signal for this lesson, so none are answered here.

## Module 1 Step — Questions for This Lesson

- **What is the best measure of the company's country exposure?**
  Revenues by operating segment (`country.exposures`). Operating income would weight Latin America more (its margin is highest), but the segment revenues are the course default and are audited.

- **What is the geographic breakdown of that measure?**
  North America 41.14%, EMEA 22.60%, Latin America 13.21%, Asia Pacific 11.11%, Bottling Investments (India and Africa) 11.94% (`country.exposures`).

- **What is the weighted average ERP?**
  6.50% (`country.weighted_erp`): the 4.57% mature premium (`market.mature_erp`) plus regional country risk premiums of 0% (US), 3.58% (EMEA), 3.87% (Latin America), 1.87% (Asia Pacific) and 3.37% (India and Africa), each an equal-weight average of the main markets in `sources/market-data/country-risk-2026-01-01.json`.
  
  > ⚠️ **Discretionary Decision: country risk premium by region**
  > **Chose:** equal-weight country baskets per segment. **Why:** the filings give revenue by segment, not by country; equal weights over-weight Egypt and Nigeria inside EMEA. **Alternative:** US premium only (4.57%) → cost of capital 6.70% and value per share $64.00 (`alternatives/erp-us-only-output.md`). **Confidence:** medium; a country revenue split would raise it.

- **Why might that ERP change?**
  The CCBA sale (`facts: ccba-sale`) removes most of the Africa revenue and lowers the weighted premium; currency swings in Latin America and Turkey move the weights.

## Notes

The country premium is the single largest gap between this cost of capital and one built on the US premium alone.
