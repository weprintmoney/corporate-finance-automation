---
title: "Market Regressions"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/MReg26.html
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

### **January 2026**

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
Regressions of Multiples: US Companies in January 2026*

*T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 13.12 + 10.52 Beta + 36.47 gEPS + 8.46 Payout          (12.20) (10.0)      (7.70)            (6.89) | 38.7% |
| PEG = -0.60 + 0.56 Payout – 1.48 ln(gEPS) + 0.23 Beta            (1.94)   (7.62)            (14.72)           (1.86) | 41.4% |
| PBV= -0.79  -0.47 gEPS +1.49 Beta +20.90 ROE  +0 17 Payout Ratio            (3.17) (0.53)          (6.76)          (34.45)      (1.30) | 66.2% |
| EV/Invested Capital= 5.75 + 1.12 g  - 0.01 ROIC – 0.06 DFR                                    (82.70) (4.16   (0.24)      (44.71) | 49.7% |
| EV/Sales = 6.77  +9.51 g + 0.36 Oper Margin -0.02 DFR- 0.12 Tax rate                     (32.41)  (11.21)   (8.97)                   (6.32)     (10.58) | 24.1% |
| EV/EBITDA= 18.82 + 39.30 g - 0.20 DFR + 1.77 ROC                         (43.19)    (23.04)   (14.08)         (3.19) | 45.9% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t) | |

 

 

*Market-wide Regressions of Multiples – European
companies in January 2026**T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 9.72 + 2.99 Beta + 49.82 gEPS + 7.98 Payout          (8.29)   (4.85)     (11.95)            (9.22) | 20.1% |
| PEG = -0.91 + 0.76 Payout −1.57 ln(gEPS            (2.77)      (3.15)           (11.09) | 30.3% |
| PBV= 0.73 + 3.92 gEPS + 0.13 Beta + 10.75 ROE  - 0.25 Payout Ratio            (3.70) (5.87)          (1.38)          (24.81)      (2.43) | 42.3% |
| EV/Invested Capital= 4.46 + 0.90 g  +1.50 ROIC –0.05 DFR                                    (67.88) (2.92)   (13.63)      (42.64) | 51.3% |
| EV/Sales = 5.08 + 4.03 g + 2.99 Oper Margin -0.02 DFR- 0.09 Tax rate                     (21.01)  (5.39)   (6.95)                   (7.18)     (12.26) | 14.2% |
| EV/EBITDA= 18.15+ 35.25 g - 0.11 DFR -  0.12 Tax Rate + 2.29 ROC                         (28.40)    (13.96)   (10.65)         (5.19)         (5.06) | 26.2% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)(  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t) | |

*Market-wide Regressions of Multiples – Japanese
companies in January 2026**T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 4.51 + 4.28 Beta + 42.26 gEPS + 10.46 Payout          (3.50)  (7.32)     (9.05)            (5.78) | 34.5% |
| PEG = -0.70 + 0.35 Payout – l1.19 n(gEPS) + 0.23 Beta           (2.45)            (4.81)           (1249)  (2.68) | 32.4% |
| PBV= -0.55 + 4.64 gEPS + 0.38 Beta +14.23 ROE           (2.63)          (6.72)          (3.84)      (14.99) | 44.1% |
| EV/Invested Capital= 3.01 + 8.96 g  + 0.16 ROIC –0.04 DFR                                    (42.62) (16.82)   (4.57)      (27.22) | 46.9% |
| EV/Sales = 2.48  + 11.54 g + 0.44 Oper Margin -0.01 DFR- 0.03 Tax rate                     (13.12)  (16.88)   (6.38)                    (2.90)     (5.06) | 24.4% |
| EV/EBITDA= 10.94 + 35.22 g - 0.05 DFR + 1.22 ROIC                         (20.89)    (8.71)   (4.25)         (2.99) | 6.7% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)(  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |

*Market-wide Regressions of Multiples – Emerging Market companies in January 2026**T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 14.47 - 0.51 Beta + 52.25 gEPS + 2.22 Payout          (10.35)  (1.33)     (23.99)            3.24 | 27.2% |
| PEG =-0.78 + 0.82 Payout – 1.43 ln(gEPS) - 0.09 Beta            (4.50)   (10.65)            (30.50)           (1.95) | 51.9% |
| PBV= 1.32  +2.73 gEPS + 0.43 Beta + 4.53 ROE            (14.31) (11.36)          (8.04)          (19.16) | 26.3% |
| EV/Invested Capital= 3.42 + 2.74 g  + 0.11 ROIC – 0.04 DFR                                    (98.22) (20.69)   (5.51)      (61.47) | 48.8% |
| EV/Sales = 4.10  + 3.17 g + 0.65 Oper Margin - 0.01 DFR- 0.03 Tax rate                     (33.23)  (9.48)   (5.95)                    (3.38)     (8.02) | 5.4% |
| EV/EBITDA= 21.24 + 33.07 g - 0.12 DFR -  0.19 Tax Rate - 4.88 ROC                         (35.57)    (23.20)   (14.38)         (9.41)              (6.98) | 23.7% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |

*Market-wide Regressions of Multiples – Global companies in January 2026**T
statistics in brackets below coefficients*

 

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 21.11 + 2.22 Beta + 21.49 gEPS + 0.89 Payout          (40.64)  (7.16)     (18.23)            (1.66) | 10.3% |
| PEG = -0.12 + 0.56 Payout + 0.48 ln(gEPS) - 0.13 Beta            (1.20)   (12.83)            (12.83)           (3.73) | 41.4% |
| PBV= 0.71  + 1.13 gEPS - 0.12 Beta + 16.72 ROE - 0.11 Payout Ratio            (7.52) (6.91)          (2.59)          (64.18)     (1.86) | 53.8% |
| EV/Invested Capital= 4.67 + 1.53 g  + 0.04 ROIC – 0.05DFR                                    (159.95) (13.36)   (2.96)      (93.17) | 44.5% |
| EV/Sales =5.44  + 4.97 g + 0.38 Oper Margin -0.01 DFR- 0.07 Tax rate                     (59.84)  (17.34)   (16.53)                     (4.36)     (21.18) | 13.3% |
| EV/EBITDA= 21.79 + 30.86 g - 0.13 DFR - 0.24 Tax Rate + 2.72 ROC                         (61.21)    (36.81)   (22.87)         (18.36)    (9.98) | 36.2% |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |

### Regressions classified by Multiples

*Market-wide
Regressions of Multiples: PE Ratios in January 2026*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| PE = 13.12 + 10.52 Beta + 36.47 gEPS + 8.46 Payout          (12.20) (10.0)      (7.70)            (6.89) | 38.7% | US |
| PE = 9.72 + 2.99 Beta + 49.82 gEPS + 7.98 Payout          (8.29)   (4.85)     (11.95)            (9.22) | 20.1% | Europe |
| PE = 4.51 + 4.28 Beta + 42.26 gEPS + 10.46 Payout          (3.50)  (7.32)     (9.05)            (5.78) | 34.5% | Japan |
| PE = 19.38 + 6.55 Payout  (no other variables significant)          (7.27)    (2.22) | 3.4% | Aus, NZ & Canada |
| PE = 14.47 - 0.51 Beta + 52.25 gEPS + 2.22 Payout          (10.35)  (1.33)     (23.99)            (3.24) | 27.2% | Emerging Markets |
| PE = 21.11 + 2.22 Beta + 21.49 gEPS + 0.89 Payout          (40.64)  (7.16)     (18.23)            (1.66) | 10.3% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: PEG Ratios in January 2026*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| PEG = -0.60 + 0.56 Payout – 1.48 ln(gEPS) + 0.23 Beta            (1.94)   (7.62)            (14.72)           (1.86) | 41.4% | US |
| PEG = -0.91 + 0.76 Payout −1.57 ln(gEPS            (2.77)      (3.15)           (11.09) | 30.3% | Europe |
| PEG = -0.70 + 0.35 Payout – l1.19 n(gEPS) + 0.23 Beta           (2.45)            (4.81)           (1249)  (2.68) | 32.4% | Japan |
| PEG =-0.78 + 0.82 Payout – 1.43 ln(gEPS) - 0.09 Beta            (4.50)   (10.65)            (30.50)           (1.95) | 51.9% | Emerging Markets |
| PEG = -1.83 + 0.84 Payout −1.74 ln(gEPS)  + 0.54 Beta            (3.33)      (3.45)           (10.76)  (2.05) | 40.9% | Aus, NZ & Canada |
| PEG = -0.12 + 0.56 Payout + 0.48 ln(gEPS) - 0.13 Beta            (1.20)   (12.83)            (12.83)           (3.73) | 41.4% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: PBV Ratios in January 202*6

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| PBV= -0.79  -0.47 gEPS +1.49 Beta +20.90 ROE  +0 17 Payout Ratio            (3.17) (0.53)          (6.76)          (34.45)      (1.30) | 66.2% | US |
| PBV= 0.73 + 3.92 gEPS + 0.13 Beta + 10.75 ROE  - 0.25 Payout Ratio            (3.70) (5.87)          (1.38)          (24.81)      (2.43) | 42.3% | Europe |
| PBV= -0.55 + 4.64 gEPS + 0.38 Beta +14.23 ROE           (2.63)          (6.72)          (3.84)      (14.99) | 44.1% | Japan |
| PBV= 1.32  +2.73 gEPS + 0.43 Beta + 4.53 ROE            (14.31) (11.36)          (8.04)          (19.16) | 26.3% | Emerging Markets |
| PBV= 2.69  + 0.83 ROE  (other variables were not statistically significant)            (69.9) (5.52) | 1.1% | Aus, NZ & Canada |
| PBV= 0.71  + 1.13 gEPS - 0.12 Beta + 16.72 ROE - 0.11 Payout Ratio            (7.52) (6.91)          (2.59)          (64.18)     (1.86) | 53.8% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: EV to Invested Capital Ratios in January 2026*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| EV/Invested Capital= 5.75 + 1.12 g  - 0.01 ROIC – 0.06 DFR                                    (82.70) (4.16   (0.24)      (44.71) | 49.7% | US |
| EV/Invested Capital= 4.46 + 0.90 g  +1.50 ROIC –0.05 DFR                                    (67.88) (2.92)   (13.63)      (42.64) | 51.3% | Europe |
| EV/Invested Capital= 3.01 + 8.96 g  + 0.16 ROIC –0.04 DFR                                    (42.62) (16.82)   (4.57)      (27.22) | 46.9% | Japan |
| EV/Invested Capital= 3.42 + 2.74 g  + 0.11 ROIC – 0.04 DFR                                    (98.22) (20.69)   (5.51)      (61.47) | 48.8% | Emerging Markets |
| EV/Invested Capital= 3.82 + 0.71 g  + 0.11 ROIC – 0.04 DFR                                    (41.62) (3.36)   (1.47)      (23.35) | 43.5% | Aus, NZ & Canada |
| EV/Invested Capital= 4.67 + 1.53 g  + 0.04 ROIC – 0.05DFR                                    (159.95) (13.36)   (2.96)      (93.17) | 44.5% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: EV to Sales Ratios in January 2026*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| EV/Sales = 6.77  +9.51 g + 0.36 Oper Margin -0.02 DFR- 0.12 Tax rate                     (32.41)  (11.21)   (8.97)                   (6.32)     (10.58) | 24.1% | US |
| EV/Sales = 5.08 + 4.03 g + 2.99 Oper Margin -0.02 DFR- 0.09 Tax rate                     (21.01)  (5.39)   (6.95)                   (7.18)     (12.26) | 14.2% | Europe |
| EV/Sales = 2.48  + 11.54 g + 0.44 Oper Margin -0.01 DFR- 0.03 Tax rate                     (13.12)  (16.88)   (6.38)                    (2.90)     (5.06) | 24.4% | Japan |
| EV/Sales = 4.10  + 3.17 g + 0.65 Oper Margin - 0.01 DFR- 0.03 Tax rate                     (33.23)  (9.48)   (5.95)                    (3.38)     (8.02) | 5.4% | Emerging Markets |
| EV/Sales = 2.71  +6.07 g + 5.51 Oper Margin -0.01 DFR- 0.02 Tax rate                     (7.93)  (7.70)   16.39)                   (1.01)     (2.06) | 44.7% | Aus, NZ & Canada |
| EV/Sales =5.44  + 4.97 g + 0.38 Oper Margin -0.01 DFR- 0.07 Tax rate                     (59.84)  (17.34)   (16.53)                     (4.36)     (21.18) | 13.3% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: EV to EBITDA Ratios in January 2026*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| EV/EBITDA= 18.82 + 39.30 g - 0.20 DFR + 1.77 ROIC                         (43.19)    (23.04)   (14.08)         (3.19) | 45.9% | US |
| EV/EBITDA= 18.15+ 35.25 g - 0.11 DFR -  0.12 Tax Rate + 2.29 ROIC                         (28.40)    (13.96)   (10.65)         (5.19)         (5.06) | 26.2% | Europe |
| EV/EBITDA= 10.94 + 35.22 g - 0.05 DFR + 1.22 ROIC                         (20.89)    (8.71)   (4.25)         (2.99) | 6.7% | Japan |
| EV/EBITDA= 21.24 + 33.07 g - 0.12 DFR -  0.19 Tax Rate - 4.88 ROIC                         (35.57)    (23.20)   (14.38)         (9.41)              (6.98) | 23.7% | Emerging Markets |
| EV/EBITDA= 19.04 + 16.95 g - 0.12 DFR -  0.14 Tax Rate  - 1.43 ROIC                         (12.01)    (5.66)   (4.86)         (2.71)    (2.03) | 17.9% | Aus, NZ & Canada |
| EV/EBITDA= 21.79 + 30.86 g - 0.13 DFR - 0.24 Tax Rate + 2.72 ROIC                         (61.21)    (36.81)   (22.87)         (18.36)    (9.98) | 36.2% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |
