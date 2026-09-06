---
title: "Market Regressions"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/MReg25.html
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

### **January 2025**

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
Regressions of Multiples: US Companies in January 2025*

*T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 16.09 + 9.30 Beta + 51.92 gEPS + 7.53 Payout          (0.93) (6.82)      (11.84)            (6.11) | 24.4% |
| PEG = 0.10 Payout –1.14 ln(gEPS) + 1.12 Beta            (2.96)            (13.03)           (13.03) | 14.8% |
| PBV= 1.79 + 5.71 gEPS + 0.88 Beta + 9.09 ROE  - 0.06 Payout Ratio            (8.07) (8.29)          (3.95)          (17.70)      (11.68 | 35.8% |
| EV/Invested Capital= 6.02 + 2.24 g  + 3.25 ROIC – 0.09 DFR                                    (62.30) (5.13)   (15.55)      (38.68) | 56.4% |
| EV/Sales = 5.45  +7.96 g + 3.55 Oper Margin -0.06 DFR- 04 Tax rate                     (32.41)  (9.66)   (15.64)                   (19.68)     (7.27) | 31.8% |
| EV/EBITDA= 35.25 + 23.00 g - 0.40 DFR -  0.51 Tax Rate + 0.26 ROC                         (40.93)    (10.77)   (20.99)         (14.89)      (0.38) | 40.1% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t) | |

 

 

*Market-wide Regressions of Multiples – European
companies in January 2025**T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 12.58 + 3.70 Beta + 45.97 gEPS + 6.97 Payout          (8.70)   (4.65)     (9.57)            (8.48) | 16.0% |
| PEG = 1.27 ln(gEPS) + 0.08 Beta            (28.71)           (1.20) | 49.3% |
| PBV= 1.88 + 3.12 gEPS + 0.20 Beta + 6.52 ROE  - 0.06 Payout Ratio            (9.91) (5.41)          (1.95)          (14.28)      (3.14) | 20.6% |
| EV/Invested Capital= 5.08 + 1.86 g  + 0.004 ROIC – 0.07 DFR                                    (74.39) (5.59)   (0.08)      (42.43) | 44.9% |
| EV/Sales = 4.10  + 4.81 g + 1.57 Oper Margin -0.04 DFR- 0.02 Tax rate                     (39.26)  (10.12)   (11.32)                   (23.14)     (5.96) | 29.1% |
| EV/EBITDA= 18.47+ 27.76 g - 0.12 DFR -  0.14 Tax Rate + 3.64 ROC                         (38.90)    (13.81)   (15.36)         (10.05)         (13.16) | 35.4% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)(  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t) | |

*Market-wide Regressions of Multiples – Japanese
companies in January 2025**T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 8.63 + 3.72 Beta + 38.36 gEPS + 5.99 Payout          (5.43)  (4.66)     (7.77)            (3.44) | 26.4% |
| PEG = 0.08 Payout – 11.09 ln(gEPS) + 0.03 Beta           (0.82)            (24.58)           (0.48) | 49.5% |
| PBV= 3.65 gEPS + 0.24 Beta + 14.83 ROE  - 0.25 Payout Ratio           (4.63)          (2.08)          (12.66)      (1.84) | 51.6% |
| EV/Invested Capital= 2.57 + 2.60 g  + 5.18 ROIC – 0.03 DFR                                    (25.95) (5.60)   (14.49)      (18.73) | 48.0% |
| EV/Sales = 2.06  + 3.09 g + 8.31 Oper Margin -0.008 DFR- 0.03 Tax rate                     (15.39)  (6.75)   (22.53)                    (4.76)     (7.50) | 36.0% |
| EV/EBITDA= 16.50 + 11.45 g - 0.06 DFR -  0.15 Tax Rate + 3.02 ROC                         (30.21)    (5.92)   (8.02)         (9.40)      (3.84) | 16.6% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)(  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |

*Market-wide Regressions of Multiples – Emerging Market companies in January 2025**T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 23.41 - 1.84 Beta + 33.66 gEPS -2.30 Payout          (20.51)  (3.63)     (14.62)            (2.46) | 13.2% |
| PEG = 1.03 - 0.08 Payout – 0.78 ln(gEPS) - 0.123 Beta            (7.79)   (1.12)            (14.92)           (5.38) | 17.2% |
| PBV= 1.37  +2.81 gEPS - 0.26 Beta + 12.37 ROE  - 0.67 Payout Ratio            (12.23) (12.85)          (4.73)          (31.68)      (21.54) | 41.9% |
| EV/Invested Capital= 3.71 + 3.19 g  + 0.78 ROIC – 0.05 DFR                                    (83.41) (17.40)   (11.74)      (50.84) | 43.8% |
| EV/Sales = 3.34  + 3.00 g + 1.51 Oper Margin - 0.034 DFR- 0.004 Tax rate                     (44.54)  (12.32)   (15.84)                    (23.00)     (1.85) | 18.9% |
| EV/EBITDA= 21.09 + 23.79 g - 0.12 DFR -  0.17 Tax Rate + 2.75 ROC                         (42.61)    (16.46)   (16.91)         (11.74)              (6.39) | 16.8% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |

*Market-wide Regressions of Multiples – Global companies in January 2025**T
statistics in brackets below coefficients*

 

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 24.17 - 1.07 Beta + 53.16 gEPS + 1.08 Payout          (38.48)  (2.65)     (27.59)            (2.05 | 16.0% |
| PEG = 1.05 + 0.045 Payout – 1.00 ln(gEPS) -0.044 Beta            (9.03)   (2.47)            (24.58)           (0.98) | 16.1% |
| PBV= 2.47  + 4.00 gEPS - 0.39 Beta + 9.14 ROE - 0.15 Payout Ratio            (27.24) (16.07)          (7.12)          (37.79)     (10.74) | 30.5% |
| EV/Invested Capital= 5.12 + 1.89 g  + 0.76 ROIC – 0.07 DFR                                    (144.33) (11.38)   (15.04)      (83.19) | 43.0% |
| EV/Sales = 4.72  + 3.88 g + 2.61 Oper Margin - 0.04 DFR- 0.03 Tax rate                     (80.73)  (16.27)   (31.18)                     (45.50)     (16.63) | 26.6% |
| EV/EBITDA= 26.48 + 26.97 g - 0.21 DFR - 0.29 Tax Rate + 1.08 ROC                         (84.66)    (26.97)   (37.76)         (27.70)    (4.39) | 32.9% |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |

### Regressions classified by Multiples

*Market-wide
Regressions of Multiples: PE Ratios in January 2025*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| PE = 16.09 + 9.30 Beta + 51.92 gEPS + 7.53 Payout          (0.93) (6.82)      (11.84)            (6.11) | 24.4% | US |
| PE = 12.58 + 3.70 Beta + 45.97 gEPS + 6.97 Payout          (8.70)   (4.65)     (9.57)            (8.48) | 16.0% | Europe |
| PE = 8.63 + 3.72 Beta + 38.36 gEPS + 5.99 Payout          (5.43)  (4.66)     (7.77)            (3.44) | 26.4% | Japan |
| PE = 4.28 + 13.96 Beta + 72.58 gEPS + 4.08 Payout          (1.47)  (7.40)     (8.64)            (1.79) | 46.0% | Aus, NZ & Canada |
| PE = 23.41 - 1.84 Beta + 33.66 gEPS -2.30 Payout          (20.51)  (3.63)     (14.62)            (2.46) | 13.2% | Emerging Markets |
| PE = 24.17 - 1.07 Beta + 53.16 gEPS + 1.08 Payout          (38.48)  (2.65)     (27.59)            (2.05 | 16.0% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: PEG Ratios in January 2025*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| PEG = 0.10 Payout –1.14 ln(gEPS) + 1.12 Beta            (2.96)            (13.03)           (13.03) | 14.8% | US |
| PEG = 1.27 ln(gEPS) + 0.08 Beta            (28.71)           (1.20) | 49.3% | Europe |
| PEG = 0.08 Payout – 11.09 ln(gEPS) + 0.03 Beta           (0.82)            (24.58)           (0.48) | 49.5% | Japan |
| PEG = 1.03 - 0.08 Payout – 0.78 ln(gEPS) - 0.123 Beta            (7.79)   (1.12)            (14.92)           (5.38) | 17.2% | Emerging Markets |
| PEG = 1.63 + 0.27 Payout +- 0.88 ln(gEPS) - 0.90 Beta            (3.39)      (3.08)           (5.76)  (3.75) | 27.5% | Aus, NZ & Canada |
| PEG = 1.05 + 0.045 Payout – 1.00 ln(gEPS) -0.044 Beta            (9.03)   (2.47)            (24.58)           (0.98) | 16.1% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: PBV Ratios in January 2025*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| PBV= 1.79 + 5.71 gEPS + 0.88 Beta + 9.09 ROE  - 0.06 Payout Ratio            (8.07) (8.29)          (3.95)          (17.70)      (11.68 | 35.8% | US |
| PBV= 1.88 + 3.12 gEPS + 0.20 Beta + 6.52 ROE  - 0.06 Payout Ratio            (9.91) (5.41)          (1.95)          (14.28)      (3.14) | 20.6% | Europe |
| PBV= 3.65 gEPS + 0.24 Beta + 14.83 ROE  - 0.25 Payout Ratio           (4.63)          (2.08)          (12.66)      (1.84) | 51.6% | Japan |
| PBV= 1.37  +2.81 gEPS - 0.26 Beta + 12.37 ROE  - 0.67 Payout Ratio            (12.23) (12.85)          (4.73)          (31.68)      (21.54) | 41.9% | Emerging Markets |
| PBV= 3.93  +3.41 gEPS - 1.63 Beta + 3.76 ROE  - 0.13 Payout Ratio            (13.81) (4.39)          (6.38)          (5.04)      (4.41) | 21.4% | Aus, NZ & Canada |
| PBV= 2.47  + 4.00 gEPS - 0.39 Beta + 9.14 ROE - 0.15 Payout Ratio            (27.24) (16.07)          (7.12)          (37.79)     (10.74) | 30.5% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: EV to Invested Capital Ratios in January 2025*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| EV/Invested Capital= 6.02 + 2.24 g  + 3.25 ROIC – 0.09 DFR                                    (62.30) (5.13)   (15.55)      (38.68) | 56.4% | US |
| EV/Invested Capital= 5.08 + 1.86 g  + 0.004 ROIC – 0.07 DFR                                    (74.39) (5.59)   (0.08)      (42.43) | 44.9% | Europe |
| EV/Invested Capital= 2.57 + 2.60 g  + 5.18 ROIC – 0.03 DFR                                    (25.95) (5.60)   (14.49)      (18.73) | 48.0% | Japan |
| EV/Invested Capital= 3.71 + 3.19 g  + 0.78 ROIC – 0.05 DFR                                    (83.41) (17.40)   (11.74)      (50.84) | 43.8% | Emerging Markets |
| EV/Invested Capital= 3.37 + 1.22 g  + 0.74 ROIC – 0.04 DFR                                    (30.61) (2.68)   (3.52)      (13.36) | 22.9% | Aus, NZ & Canada |
| EV/Invested Capital= 5.12 + 1.89 g  + 0.76 ROIC – 0.07 DFR                                    (144.33) (11.38)   (15.04)      (83.19) | 43.0% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: EV to Sales Ratios in January 2025*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| EV/Sales = 5.45  +7.96 g + 3.55 Oper Margin -0.06 DFR- 04 Tax rate                     (32.41)  (9.66)   (15.64)                   (19.68)     (7.27) | 31.8% | US |
| EV/Sales = 4.10  + 4.81 g + 1.57 Oper Margin -0.04 DFR- 0.02 Tax rate                     (39.26)  (10.12)   (11.32)                   (23.14)     (5.96) | 29.1% | Europe |
| EV/Sales = 2.06  + 3.09 g + 8.31 Oper Margin -0.008 DFR- 0.03 Tax rate                     (15.39)  (6.75)   (22.53)                    (4.76)     (7.50) | 36.0% | Japan |
| EV/Sales = 3.34  + 3.00 g + 1.51 Oper Margin - 0.034 DFR- 0.004 Tax rate                     (44.54)  (12.32)   (15.84)                    (23.00)     (1.85) | 18.9% | Emerging Markets |
| EV/Sales = 2.25  +6.71 g + 9.93 Oper Margin -0.002 DFR- 0.04 Tax rate                     (9.85)  (9.31)   (21.25)                   (0.67)     (7.10) | 40.1% | Aus, NZ & Canada |
| EV/Sales = 4.72  + 3.88 g + 2.61 Oper Margin - 0.04 DFR- 0.03 Tax rate                     (80.73)  (16.27)   (31.18)                     (45.50)     (16.63) | 26.6% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |

*Market-wide
Regressions of Multiples: EV to EBITDA Ratios in January 2025*

*T
statistics in brackets below coefficients*

|  |  |  |
| --- | --- | --- |
| Regression | R Squared | Region |
| EV/EBITDA= 35.25 + 23.00 g - 0.40 DFR -  0.51 Tax Rate + 0.26 ROC                         (40.93)    (10.77)   (20.99)         (14.89)      (0.38) | 40.1% | US |
| EV/EBITDA= 18.47+ 27.76 g - 0.12 DFR -  0.14 Tax Rate + 3.64 ROC                         (38.90)    (13.81)   (15.36)         (10.05)         (13.16) | 35.4% | Europe |
| EV/EBITDA= 16.50 + 11.45 g - 0.06 DFR -  0.15 Tax Rate + 3.02 ROC                         (30.21)    (5.92)   (8.02)         (9.40)      (3.84) | 16.6% | Japan |
| EV/EBITDA= 21.09 + 23.79 g - 0.12 DFR -  0.17 Tax Rate + 2.75 ROC                         (42.61)    (16.46)   (16.91)         (11.74)              (6.39) | 16.8% | Emerging Markets |
| EV/EBITDA= 18.83 + 43.48 g - 0.14 DFR -  0.11Tax Rate  + 3.99 ROC                         (14.30)    (9.89)   (6.14)         (3.52)    (2.16) | 24.7% | Aus, NZ & Canada |
| EV/EBITDA= 26.48 + 26.97 g - 0.21 DFR - 0.29 Tax Rate + 1.08 ROC                         (84.66)    (26.97)   (37.76)         (27.70)    (4.39) | 32.9% | Global |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | | |
