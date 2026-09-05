---
title: "Amgenpricing"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/blog/AmgenPricing.pdf
---

## **Labeling and Relative Valuation**

In 
 relative 
 valuation, 
 a 
 company 
 is 
 priced 
 based 
 on 
 how 
 the 
 market 
 is 
 pricing 
 "similar" 
 or 
 "comparable" 
 companies. 
 That 
 is 
 an 
 unexceptional 
 statement, 
 but 
 "comparable" 
 and 
 "similar" 
 are 
 subjective 
 judgments. 
 Consider 
 pricing Amgen, 
 a 
 company 
 that 
 arguably 
 can 
 be 
 included 
 in 
 either 
 the 
 biotech 
 or 
 pharmaceutical 
 sector. 
 Comparing 
 it 
 to 
 the 
 distribution 
 of 
 PEs 
 in 
 each 
 sector, 
 here 
 is 
 what 
 we 
 get:

|                                        | Pharmaceutical | Biotechnology | Amgen        |
|----------------------------------------|----------------|---------------|--------------|
| Number of firms                        | 111            | 337           |              |
| Number of firms with positive earnings | 32             | 38            |              |
| % of firms with positive earnings      | <b>28.83%</b>  | <b>11.28%</b> |              |
|                                        |                |               |              |
| Average                                | <b>48.84</b>   | <b>249.37</b> |              |
| Minimum                                | 1.03           | 1.71          |              |
| 25th Percentile                        | 15.39          | 19.56         |              |
| Median                                 | <b>27.74</b>   | <b>45.51</b>  | <b>23.47</b> |
| 75th Percentile                        | 52.57          | 143.14        |              |
| Maximum                                | 467.56         | 2234.19       |              |

First, 
 notice 
 that 
 in 
 both 
 subsets, 
 there 
 are 
 far 
 more 
 firms 
 where 
 PE 
 ratio 
 is 
 not 
 meaningful 
 than 
 where 
 PE 
 ratios 
 can 
 be 
 estimated. 
 In 
 fact, 
 only 
 11.28% 
 of 
 the 
 biotechnology 
 firms 
 have 
 PE 
 ratios 
 that 
 can 
 be 
 computed 
 and 
 I 
 use 
 R&D 
 adjusted 
 net 
 income, 
 which 
 should 
 boost 
 net 
 income 
 at 
 many 
 of 
 these 
 companies. 
 The 
 sampling 
 bias 
 is 
 immense.

At 
 its 
 R&D 
 adjusted 
 PE 
 of 
 23.47, 
 Amgen 
 is 
 close 
 to 
 the 
 median 
 (about 
 the 
 45th percentile) 
 of 
 pharmaceutical 
 companies 
 but 
 it 
 is 
 closer 
 to 
 the 
 25th percentile, 
 if 
 you 
 use 
 biotech 
 companies 
 as 
 your 
 comparable 
 list. 
 In 
 fact, 
 if 
 you 
 took 
 large-‐cap 
 market 
 cap 
 firms 
 (with 
 market capitalizations 
 that 
 exceed 
 \$25 billion) 
 as your 
 comparables, 
 Amgen 
 starts 
 to 
 look 
 over 
 priced.

In 
 fact, 
 you 
 could 
 use 
 the 
 raw 
 data 
 on 
 the 
 companies 
 to 
 create 
 your 
 own 
 "comparable" list 
 for 
 Amgen 
 and 
 make 
 your 
 own 
 judgments 
 on 
 whether 
 it 
 is 
 cheap 
 or 
 expensive. 
 You 
 can 
 even 
 try 
 to 
 control 
 for 
 differences 
 in 
 risk, 
 growth 
 and 
 cash 
 flows.