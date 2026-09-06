---
title: "Market Regressions"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/MReg24.html
---

<!--
/\* Font Definitions \*/
@font-face
{font-family:Times;
panose-1:2 0 5 0 0 0 0 0 0 0;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:3 0 0 0 1 0;}
/\* Style Definitions \*/
p.MsoNormal, li.MsoNormal, div.MsoNormal
{mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE
{mso-style-name:"";
mso-spl-e:yes;}
span.GramE
{mso-style-name:"";
mso-gram-e:yes;}
@page Section1
{size:8.5in 11.0in;
margin:1.0in 1.25in 1.0in 1.25in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-paper-source:0;}
div.Section1
{page:Section1;}
div.MsoNormal1 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal1 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal1 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE1 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE1 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal2 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal2 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal2 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE2 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal3 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal3 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal3 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
div.MsoNormal4 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal4 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal4 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE3 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE4 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE5 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal5 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal5 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal5 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE2 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE6 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal6 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal6 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE3 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE7 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal7 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal7 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal7 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE4 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE8 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal8 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal8 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal8 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal61 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE31 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE71 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE9 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal62 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE32 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE72 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal621 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE321 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE721 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal622 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE322 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE722 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal611 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE711 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal6111 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE7111 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal612 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal613 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal614 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal615 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal616 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE7112 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal617 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE311 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE712 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal618 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE312 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE713 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal619 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE313 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE714 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal6110 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE314 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE715 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal51 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal71 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE81 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal72 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE82 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE821 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal6171 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE3111 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE7121 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal6172 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE3112 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE7122 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal6173 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE3113 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE7123 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal52 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE21 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE61 {mso-style-name:"";
mso-spl-e:yes;}
span.GramE315 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE716 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal6112 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE316 {mso-style-name:"";
mso-gram-e:yes;}
span.GramE3151 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE7161 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal61121 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE31511 {mso-style-name:"";
mso-gram-e:yes;}
span.GramE3161 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE71611 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal61122 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE31512 {mso-style-name:"";
mso-gram-e:yes;}
span.GramE3162 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE71612 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal61123 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE31513 {mso-style-name:"";
mso-gram-e:yes;}
span.GramE3163 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE71613 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal6113 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal61131 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6161 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal73 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal611211 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE315111 {mso-style-name:"";
mso-gram-e:yes;}
span.GramE31611 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE716111 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE822 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE823 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal74 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE83 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE824 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE825 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal75 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE84 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal711 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE811 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE8241 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal751 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.SpellE841 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE826 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal9 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal9 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal9 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal63 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6121 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6174 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal712 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal721 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal731 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE33 {mso-style-name:"";
mso-gram-e:yes;}
span.GramE3114 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE73 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE7124 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE812 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE827 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE828 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE829 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal10 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal10 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal10 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6122 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6175 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal713 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal722 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal732 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE5 {mso-style-name:"";
mso-gram-e:yes;}
span.GramE3115 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE10 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE7125 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE813 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE8210 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal6114 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE317 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE717 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal101 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal61141 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal714 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal7121 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal7131 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE3171 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE7171 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE814 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE8121 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE8131 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal11 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal11 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal11 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6115 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6123 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6176 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal715 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal723 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal733 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE318 {mso-style-name:"";
mso-gram-e:yes;}
span.GramE3116 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE718 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE7126 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE815 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE8211 {mso-style-name:"";
mso-spl-e:yes;}
p.MsoNormal102 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal111 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal61151 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal716 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal7122 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal7132 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE3181 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE7181 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE816 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE8122 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE8132 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal12 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal12 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal12 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal1021 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal1111 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal611511 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6177 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal61741 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal91 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE3117 {mso-style-name:"";
mso-gram-e:yes;}
span.GramE31141 {mso-style-name:"";
mso-gram-e:yes;}
span.GramE31811 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE7127 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE71241 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE71811 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal13 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal13 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal13 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal10211 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal11111 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6115111 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal724 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal7211 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal92 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE318111 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE718111 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE8212 {mso-style-name:"";
mso-spl-e:yes;}
span.SpellE8271 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal14 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal14 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal14 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal102111 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal111111 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal61151111 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal6124 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal61211 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal93 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE3181111 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE7181111 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal15 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal15 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal15 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal1021111 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal1111111 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal611511111 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal94 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
span.GramE31811111 {mso-style-name:"";
mso-gram-e:yes;}
span.SpellE71811111 {mso-style-name:"";
mso-spl-e:yes;}
div.MsoNormal16 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
li.MsoNormal16 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
p.MsoNormal16 {mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";}
-->

Market Regressions

### **January 2024**

### **Regressions of Multiples on Fundamentals: Market Wide**

The following regressions were run across five groupings. The first and
most comprehensive set of regressions were run across all traded companies
in the United States. The second set of regressions were run across all traded
companies in Western Europe and the UK. The third set of regressions were
run across companies in emerging markets in Asia, Eastern Europe and Latin
America. The fourth set of regressions were run across just Japanese companies. The final set is across all companies globally. If a regression yielded a large negative constant, I reran the regression without the constant to reduce the problem of negative predicted values for the multiples. You can find the multiples classified by region as well as by multiple.

|  |  |
| --- | --- |
| Region | Multiple |
| [1. United States](#USRegressions)  [2. Europe](#Euroregressions)  [3. Emerging Markets](#Emergregressions)  [4. Japan](#Japanregressions)[5. Global](#Global) | [1. PE](#PERegressions)  [2. PBV](#PBVregressions)  [3. PEG](#PEGRegressions)  [4. EV/Sales](#EVICregressions)[5. EV/IC](#Global)  [6. EV to EBITDA](#EVEBITDAregressions) |

**Using the regressions** should be pretty straightforward,
if you can get the data on the independent variables for your company and
stay true to decimal format. (25% gets entered as 0.25). As an example, assume
that you are looking at Disney in January 2022 and decide to use the US
market regression for price to book ratio. Here are the inputs:  
g = The analyst estimate of earnings
growth rate for the next 5 years is 12% (if you do not have analyst estimates,
substitute your own).   
Payout ratio = 20%
  
ROE =The return on equity last
year was 16.2%  
Beta =1.10  
*Using the PBV regression:*  
PBV for Disney= 2.10 + 6.07 gEPS + 0.69 Beta + 5.09 ROE
- 0.33 Payout Ratio  
=2.10 + 6.07 (0.12) + 0.69 (1.10) + 5.09 (.162) - 0.33 (.20) = 4.35

At its actual
price to book ratio of 3.90, Disney is under valued.

The PEG regression uses the natural log of the expected growth rate. Thus, if your expected growth rate is 15%, you will use ln(.15) = -1.8971

### Regressions classified by Region

### 

*Market-wide
Regressions of Multiples: US Companies in January 2024*

*T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 19.34 Beta + 68.70 gEPS + 10.37 Payout          (23.78)      (68.70)            (10.37) | 33.6% |
| PEG = 0.24 + 0.87 Payout – 0.58 ln(gEPS) - 1.28 Beta            (27.75)   (7.71)            (19.04)           (5.72) | 8.6% |
| PBV= 2.10 + 6.07 gEPS + 0.69 Beta + 5.09 ROE  - 0.33 Payout Ratio            (7.30) (8.96)          (3.24)          (11.71)      (1.76) | 21.9% |
| EV/Invested Capital= 5.78 + 0.66 g  + 0.57 ROIC – 6.20 DFR                                    (54.84)   (1.64)      (5.95)     (39.88) | 44.2% |
| EV/Sales = 3.81  + 9.86 g + 8.19 Oper Margin -1.60 DFR- 5.88 Tax rate                     (29.70)  (19.48)   (25.12)                   (7.36)     (13.43) | 36.0% |
| EV/EBITDA= 27.61 + 40.22 g - 25.06 DFR -  37.09Tax Rate                         (44.93)    (24.65)   (18.92)         (14.67) | 45.5% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t) | |

 

 

*Market-wide Regressions of Multiples – European
companies in January 2024**T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 11.89 + 1.47 Beta + 32.44 gEPS + 13.18 Payout          (8.82)   (1.93)     (9.96)            (10.01) | 15.5% |
| PEG = 0.42 + 0.96 Payout – 0.92 ln(gEPS) – 0.12 Beta            (1.59)   (5.88)            (10.82)           (1.36) | 19.5% |
| PBV= 1.20 + 3.25 gEPS + 0.06 Beta + 5.78 ROE  + 1.36 Payout Ratio            (4.43) (5.65)          (0.42)          (12.69)      (6.29) | 17.1% |
| EV/Invested Capital= 3.56 + 2.82 g  + 4.,10 ROIC – 3.54 DFR                                    (37.70)   (10.07)      (19.87)     (31.52) | 51.7% |
| EV/Sales = 1.52  + 5.96 g + 6.13 Oper Margin + 2.04 DFR- 0.15 Tax rate                     (11.26)  (14.61)   (16.10)                          (11.35)     (0.40) | 14.3% |
| EV/EBITDA= 21.10 + 26.59 g - 12.75 DFR -  18.40 Tax Rate                         (43.03)    (16.19)   (14.78)         (11.33) | 23.6% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)(  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t) | |

*Market-wide Regressions of Multiples – Japanese
companies in January 2024**T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 4.65 + 6.94 Beta + 25.75 gEPS + 17.17 Payout          (2.38)  (6.92)     (3.80)            (7.84) | 23.2% |
| PEG = -0.31 Payout – 1.06 ln(gEPS) + 0.16 Beta            (1.40)            (14.84)           (1.61) | 34.9% |
| PBV= 0.48 gEPS + 0.78 Beta + 10.30 ROE  + 0.10 Payout Ratio           (0.76)          (8.50)          (10.67)      (0.05) | 34.9% |
| EV/Invested Capital= 3.55 + 1.22 g  + 0.64 ROIC – 4.30 DFR                                    (31.39)   (2.34)      (9.61)     (29.28) | 41.1% |
| EV/Sales = 1.13  + 3.82 g + 8.97 Oper Margin + 0.33 DFR- 1.59 Tax rate                     (8.90)  (7.69)   (22.25)                          (2.12)     (4.42) | 29.1% |
| EV/EBITDA= 16.40 + 29.78 g - 2.07 DFR -  13.21 Tax Rate                         (19.45)    (8.86)   (1.91)         (4.97) | 6.60% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)(  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |

*Market-wide Regressions of Multiples – Emerging Market companies in January 2024**T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 15.02 + 0.06 Beta + 41.70 gEPS + 3.71 Payout          (15.78)  (0.12)     (22.31)            (3.91) | 24.8% |
| PEG = 1.06 +0.20 Payout – 0.43 ln(gEPS) - 0.12 Beta            (8.81)   (2.72)            (11.24)           (2.57) | 9.0% |
| PBV= 0.99  +1.80 gEPS - 0.13 Beta + 9.50 ROE  + 1.80 Payout Ratio            (6.67) (7.89)          (1.77)          (27.35)      (2.61) | 32.9% |
| EV/Invested Capital= 3.29 + 1.25 g  + 0.96 ROIC – 3.76 DFR                                    (64.77)   (9.52)      (11.37)     (59.55) | 50.1% |
| EV/Sales = 3.07  + 1.48 g + 4.29 Oper Margin - 0.24 DFR- 2.22 Tax rate                     (37.19)  (8.97)   (18.42)                          (1.92)     (8.18) | 8.9% |
| EV/EBITDA= 23.99 + 12.69 g - 14.49 DFR -  22.25 Tax Rate                         (54.14)    (14.01)   (19.28)         (15.67) | 16.7% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |

*Market-wide Regressions of Multiples – Global companies in January 2024**T
statistics in brackets below coefficients*

 

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 16.90 + 3.20 Beta + 51.53 gEPS + 2.68 Payout          (22.96)  (6.53)     (27.77)            (3.98) | 17.2% |
| PEG = 1.21 + 0.17 Payout – 0.70 ln(gEPS) + 0.001 Beta            (9.82)   (2.36)            (16.96)           (0.02) | 8.0% |
| PBV= 2.29  + 3.12 gEPS - 0.16 Beta + 6.61 ROE - 0..29 Payout Ratio            (20.31) (13.52)          (2.49)          (29.17)     (3.43) | 19.8% |
| EV/Invested Capital= 4.70 + 0.70 g  + 0.86 ROIC – 5.00 DFR                                    (113.51)   (5.25)      (18.30)     (93.76) | 44.3% |
| EV/Sales = 3.35  + 3.36 g + 6.45 Oper Margin - 0.52 DFR- 3.82 Tax rate                     (58.99)  (21.73)   (41.35)                     (5.85)     (20.93) | 18.0% |
| EV/EBITDA= 24.82 + 26.15 g - 17.85 DFR -  25.43 Tax Rate                         (95.20)    (38.53)   (36.49)         (27.01) | 28.9% |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |

### Regressions classified by Multiples

*Market-wide
Regressions of Multiples: PE Ratios in January 2024*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| PE = 19.34 Beta + 68.70 gEPS + 10.37 Payout          (23.78)      (68.70)            (10.37) | 33.6% | US |
| PE = 11.89 + 1.47 Beta + 32.44 gEPS + 13.18 Payout          (8.82)   (1.93)     (9.96)            (10.01) | 15.5% | Europe |
| PE = 4.65 + 6.94 Beta + 25.75 gEPS + 17.17 Payout          (2.38)  (6.92)     (3.80)            (7.84) | 23.2% | Japan |
| PE = 15.02 + 0.06 Beta + 41.70 gEPS + 3.71 Payout          (15.78)  (0.12)     (22.31)            (3.91) | 24.8% | Aus, NZ & Canada |
| PE = 14.41 - 1.24 Beta + 92.94 gEPS + 7.49 Payout          (6.91)  (0.74)     (14.80)            (5.31) | 40.5% | Emerging Markets |
| PE = 16.90 + 3.20 Beta + 51.53 gEPS + 2.68 Payout          (22.96)  (6.53)     (27.77)            (3.98) | 17.2% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: PEG Ratios in January 2024*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| PEG = 0.24 + 0.87 Payout – 0.58 ln(gEPS) - 1.28 Beta            (27.75)   (7.71)            (19.04)           (5.72) | 8.6% | US |
| PEG = 0.42 + 0.96 Payout – 0.92 ln(gEPS) – 0.12 Beta            (1.59)   (5.88)            (10.82)           (1.36) | 19.5% | Europe |
| PEG = -0.31 Payout – 1.06 ln(gEPS) + 0.16 Beta            (1.40)            (14.84)           (1.61) | 34.9% | Japan |
| PEG = 1.06 +0.20 Payout – 0.43 ln(gEPS) - 0.12 Beta            (8.81)   (2.72)            (11.24)           (2.57) | 9.0% | Emerging Markets |
| PEG =0.32 Payout – 1.64 ln(gEPS) - 0.54 Beta            (1.09)            (16.80)           (2.72) | 46.2% | Aus, NZ & Canada |
| PEG = 1.21 + 0.17 Payout – 0.70 ln(gEPS) + 0.001 Beta            (9.82)   (2.36)            (16.96)           (0.02) | 8.0% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: PBV Ratios in January 2024*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| PBV= 2.10 + 6.07 gEPS + 0.69 Beta + 5.09 ROE  - 0.33 Payout Ratio            (7.30) (8.96)          (3.24)          (11.71)      (1.76) | 21.9% | US |
| PBV= 1.20 + 3.25 gEPS + 0.06 Beta + 5.78 ROE  + 1.36 Payout Ratio            (4.43) (5.65)          (0.42)          (12.69)      (6.29) | 17.1% | Europe |
| PBV= 0.48 gEPS + 0.78 Beta + 10.30 ROE  + 0.10 Payout Ratio           (0.76)          (8.50)          (10.67)      (0.05) | 34.9% | Japan |
| PBV= 0.99  +1.80 gEPS - 0.13 Beta + 5.52 ROE  - 0.09 Payout Ratio            (10.73) (7.78)          (7.45)          (8.87)      (0.56) | 36.9% | Emerging Markets |
| PBV= 3.07  +1.80 gEPS - 1.49 Beta + 9.50 ROE  + 1.80 Payout Ratio            (6.67) (7.89)          (1.77)          (27.35)      (2.61) | 32.9% | Aus, NZ & Canada |
| PBV= 2.29  + 3.12 gEPS - 0.16 Beta + 6.61 ROE - 0..29 Payout Ratio            (20.31) (13.52)          (2.49)          (29.17)     (3.43) | 19.8% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: EV to Invested Capital Ratios in January 2024*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| EV/Invested Capital= 5.78 + 0.66 g  + 0.57 ROIC – 6.20 DFR                                    (54.84)   (1.64)      (5.95)     (39.88) | 44.2% | US |
| EV/Invested Capital= 3.56 + 2.82 g  + 4.,10 ROIC – 3.54 DFR                                    (37.70)   (10.07)      (19.87)     (31.52) | 51.7% | Europe |
| EV/Invested Capital= 3.55 + 1.22 g  + 0.64 ROIC – 4.30 DFR                                    (31.39)   (2.34)      (9.61)     (29.28) | 41.1% | Japan |
| EV/Invested Capital= 3.29 + 1.25 g  + 0.96 ROIC – 3.76 DFR                                    (64.77)   (9.52)      (11.37)     (59.55) | 50.1% | Emerging Markets |
| EV/Invested Capital= 2.38 + 0.71 g  + 4.62 ROIC – 2.06 DFR                                    (17.66)   (2.27)      (11.40)     (12.29) | 44.4% | Aus, NZ & Canada |
| EV/Invested Capital= 4.70 + 0.70 g  + 0.86 ROIC – 5.00 DFR                                    (113.51)   (5.25)      (18.30)     (93.76) | 44.3% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: EV to Sales Ratios in January 2024*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| EV/Sales = 3.81  + 9.86 g + 8.19 Oper Margin -1.60 DFR- 5.88 Tax rate                     (29.70)  (19.48)   (25.12)                   (7.36)     (13.43) | 36.0% | US |
| EV/Sales = 1.52  + 5.96 g + 6.13 Oper Margin + 2.04 DFR- 0.15 Tax rate                     (11.26)  (14.61)   (16.10)                          (11.35)     (0.40) | 14.3% | Europe |
| EV/Sales = 1.13  + 3.82 g + 8.97 Oper Margin + 0.33 DFR- 1.59 Tax rate                     (8.90)  (7.69)   (22.25)                          (2.12)     (4.42) | 29.1% | Japan |
| EV/Sales = 3.07  + 1.48 g + 4.29 Oper Margin - 0.24 DFR- 2.22 Tax rate                     (37.19)  (8.97)   (18.42)                          (1.92)     (8.18) | 8.9% | Emerging Markets |
| EV/Sales = 1.39  + 3.02 g + 4.31 Oper Margin + 1.21 DFR+ 3.18 Tax rate                     (5.82)  (5.00)   (9.36)                          (3.15)     (4.78) | 14.7% | Aus, NZ & Canada |
| EV/Sales = 3.35  + 3.36 g + 6.45 Oper Margin - 0.52 DFR- 3.82 Tax rate                     (58.99)  (21.73)   (41.35)                     (5.85)     (20.93) | 18.0% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: EV to EBITDA Ratios in January 2024*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| EV/EBITDA= 27.61 + 40.22 g - 25.06 DFR -  37.09Tax Rate                         (44.93)    (24.65)   (18.92)         (14.67) | 45.5% | US |
| EV/EBITDA= 21.10 + 26.59 g - 12.75 DFR -  18.40 Tax Rate                         (43.03)    (16.19)   (14.78)         (11.33) | 23.6% | Europe |
| EV/EBITDA= 16.40 + 29.78 g - 2.07 DFR -  13.21 Tax Rate                         (19.45)    (8.86)   (1.91)         (4.97) | 6.60% | Japan |
| EV/EBITDA= 23.99 + 12.69 g - 14.49 DFR -  22.25 Tax Rate                         (54.14)    (14.01)   (19.28)         (15.67) | 16.7% | Emerging Markets |
| EV/EBITDA= 19.73 + 12.89 g - 14.19 DFR -  6.74 Tax Rate                         (18.06)    (4.54)   (7.04)         (2.13) | 10.0% | Aus, NZ & Canada |
| EV/EBITDA= 24.82 + 26.15 g - 17.85 DFR -  25.43 Tax Rate                         (95.20)    (38.53)   (36.49)         (27.01) | 28.9% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |
