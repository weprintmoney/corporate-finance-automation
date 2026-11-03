---
title: "Comcast Corporation (CMCSA) — Lesson 07: Country Risk Premiums"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Comcast Corporation (CMCSA) — Lesson 07: Country Risk Premiums

Quick mode, blind, as of 2026-06-30: only the question-bank entries tagged with a signal are answered. Numbers cite `inputs.yaml` fields or `model-output.md` sections.

## Module 1 Step — Questions for This Lesson

- **What is the best measure of the company's country exposure (revenues, production, assets)?**
  Revenues. Sky's UK, Italian and German operations and the Beijing and Osaka parks earn local-currency revenue from local customers; production location matters less than where customers pay.

- **What is the geographic breakdown of that measure?**
  Comcast does not publish revenue by country. The ledger estimates 82% US, 9% UK, 4% Italy, 2% Germany, 1.5% China and 1.5% Japan from Note 3's international lines (`country.exposures`, each marked an estimate with a range).

- **What is the weighted average ERP?**
  4.77% (`country.weighted_erp`), against a US-only 4.57% (`market.mature_erp`; rule 15, US country risk premium zero). ⚠️ The country weights are an estimate; using US only lowers the cost of capital to 6.06% and raises value to $44.15 (`alternatives/erp-us-only-output.md`).

- **Why might that ERP change?**
  Italy's premium (2.46% over mature) is the swing factor. More directly, the planned NBCUniversal spin takes Sky, Universal Beijing and the Osaka exposure out, leaving a remaining Comcast close to 100% US.

## Notes

Weighted ERP 4.77% feeds the cost of equity in lesson 13.
