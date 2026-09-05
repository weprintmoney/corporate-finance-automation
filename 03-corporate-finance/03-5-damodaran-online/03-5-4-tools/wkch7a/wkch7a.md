---
title: "Wkch7A"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/wkch/wkch7a.xls
---

# Wkch7A

Source: https://www.stern.nyu.edu/~adamodar/pc/wkch/wkch7a.xls

Sheets: Sheet1

## Sheet1

| Company Name | EV/Trailing Sales | Operating Margin |
|---|---|---|
| Bon-Ton Stores Inc. (NasdaqGS:BONT) | 0.39 | 0.0254 |
| Saks Incorporated (NYSE:SKS) | 0.63 | 0.0479 |
| J. C. Penney Company, Inc. (NYSE:JCP) | 0.43 | -0.1032 |
| Dillard's Inc. (NYSE:DDS) | 0.66 | 0.0798 |
| Sears Holdings Corporation (NasdaqGS:SHLD) | 0.2 | -0.0204 |
| Kohl's Corp. (NYSE:KSS) | 0.76 | 0.098 |
| Nordstrom Inc. (NYSE:JWN) | 1.04 | 0.1086 |
| Macy's, Inc. (NYSE:M) | 0.81 | 0.0963 |
| Median | 0.645 |  |
| Average | 0.615 |  |
|  |  |  |
| a. Based upon the average and the median, JC Penney looks cheap (by about 50%). |  |  |
| b. However, JC Penney also has the most negative operating margin of the sector. To control for this, I ran a regression of EV/Sales against operating margin |  |  |
|  | Coefficients | Standard Error |
| Intercept | 0.497499943600602 | 0.07581135138902895 |
| Operating Margin | 2.827919528264692 | 0.9490734407105629 |
| T (2%) | 3.142668403290983 |  |
| LCL - Lower value of a reliable interval (LCL) |  |  |
| UCL - Upper value of a reliable interval (UCL) |  |  |
| Adjusted R squared of the regression = | 0.53 |  |
| Predicted EV/Sales for JC Penney = | 0.2056586482836858 | ! 0.50 + 2.83 (-.1032) |
| After controlling for operating margin differences, JC Penney looks expensive |  |  |
| You can also ask another question. What would JC Penney's operating margin have to improve to, to justify its EV/Sales ratio |  |  |
| 0.43 = 0.50 + 2.83 (X) |  |  |
| Breakeven operating margin = | -0.02473498233215548 |  |
