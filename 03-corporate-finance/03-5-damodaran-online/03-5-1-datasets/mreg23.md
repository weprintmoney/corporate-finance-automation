---
title: "Market Regressions"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/MReg23.html
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
-->

Market Regressions

### **January 2023**

### **Regressions of Multiples on Fundamentals: Market Wide**

The following regressions were run across five groupings. The first and
most comprehensive set of regressions were run across all traded companies
in the United States. The second set of regressions were run across all traded
companies in Western Europe and the UK. The third set of regressions were
run across companies in emerging markets in Asia, Eastern Europe and Latin
America. The fourth set of regressions were run across just Japanese companies. The final set is across all companies globally. If a regression yielded a large negative constant, I reran the regression without the constant to reduce the problem of negative predicted values for the multiples.

[1. United States](#USRegressions)  
[2. Europe](#Euroregressions)  
[3. Emerging Markets](#EmergRegressions)  
[4. Japan](#Japanregressions)[5. Global](#Global)

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
PBV for Disney=2.32 + 4.60 gEPS - 1.33 Beta + 8.90 ROE
+ 0.80 Payout Ratio  
= 2.32 + 4.60 (.12) -1.33 (1.10) + 8.90 (.162) + 0.80 (.20)= 3.01

At its actual
price to book ratio of 3.90, Disney is close to correctly valued.

The PEG regression uses the natural log of the expected growth rate. Thus, if your expected growth rate is 15%, you will use ln(.15) = -1.8971

*Market-wide
Regressions of Multiples: US Companies in January 2023*

*T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 8.63 + 2.23 Beta + 46.20 gEPS + 19.30 Payout          (5.13)  (1.83)     (10.42)            (13.71) | 25.0% |
| PEG = 6.71 + 1.20 Payout – 1.57 ln(gEPS) -0.77 Beta            (27.75)   (7.71)            (19.04)           (5.72) | 56.6% |
| PBV= 2.32 + 4.60 gEPS - 1.33 Beta + 8.90 ROE  + 0.80 Payout Ratio            (8.18) (6.62)          (6.40)          (18.49)      (3.74) | 36.9% |
| EV/Invested Capital= 3.53 + 1.30 g  + 7.30 ROIC – 4.20 DFR                                    (23.12)   (3.42)      (20.07)     (15.38) | 56.7% |
| EV/Sales = 2.32  + 2.60 g + 10.60 Oper Margin -1.40 DFR- 3.50 Tax rate                     (10.66)  (5.49)   (21.61)                          (4.27)     (5.42) | 30.6% |
| EV/EBITDA= 23.93 + 25.40 g - 8.20 DFR -  34.40Tax Rate                         (22.07)    (6.44)   (3.43)         (7.73) | 5.3% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t) | |

 

 

*Market-wide Regressions of Multiples – European
companies in January 2023**T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 1.59 + 2.33 Beta + 41.50 gEPS + 27.00 Payout          (1.09)  (2.66)     (10.70)            (20.99) | 36.6% |
| PEG = 4.50 + 0.50 Payout – 1.19 ln(gEPS) + . 0.176 Beta            (21.17)   (3.11)            (16.61)           (2.21) | 30.1% |
| PBV= -0.04 + 4.10 gEPS + 0.07 Beta + 9.60 ROE  + 1.80 Payout Ratio            (0.12) (6.62)          (0.46)          (17.57)      (9.03) | 28.5% |
| EV/Invested Capital= 3.10 + 1.90 g  + 6.00 ROIC – 3.20 DFR                                    (21.38)   (5.84)      (14.06)     (16.79) | 55.9% |
| EV/Sales = 2.20  + 2.60 g + 5.10 Oper Margin + 3.90 DFR- 4.90 Tax rate                     (8.92)  (5.47)   (7.65)                          (12.64)     (7.04) | 15.9% |
| EV/EBITDA= 19.78 + 8.00 g - 9.90 DFR -  13.60 Tax Rate                         (39.45)    (6.69)   (11.02)         (7.88) | 8.8% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)(  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t) | |

 

*Market-wide
Regressions of Multiples – Japanese Companies in January 2023*

*T
statistics in brackets below coefficients*

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 0.17 + 1.38 Beta + 123.20 gEPS + 28.10 Payout          (0.06)  (0.98)     (19.05)            (7.51 | 55.4% |
| PEG = 4.30 + 1.40 Payout – 1.24 ln(gEPS) + 1.90 Beta            (13.01)   (3.60)            (10.34)           (1.38) | 25.9% |
| PBV= -0.10  +7.30 gEPS + 0.18 Beta + 12.40 ROE  + 2.00 Payout Ratio            (0.35) (12.01)          (1.36)          (10.71)      (0.71) | 34.4% |
| EV/Invested Capital= 2.14 + 3.30 g  + 7.80 ROIC – 2.80 DFR                                    (10.87)   (6.79)      (8.60)     (8.80) | 53.6% |
| EV/Sales = 1.21  + 4.00 g + 9.30 Oper Margin -1.00 DFR- 2.90 Tax rate                     (5.53)  (8.82)   (13.82)                          (0.48)     (4.09) | 44.7% |
| EV/EBITDA= 19.94 + 1.40 g - 0.60 DFR -  23.00Tax Rate                         (27.44)    (0.53)   (0.68)         (10.81) | 3.50% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)(  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |

*Market-wide
Regressions of Multiples – Emerging Market companies in January 2023*

*T
statistics in brackets below coefficients*

 

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 10.88 + 1.76 Beta + 43.90 gEPS + 6.90 Payout          (8.40)  (2.74)     (17.34)            (4.44) | 17.6% |
| PEG = 3.40 + 0.60 Payout – 0.55 ln(gEPS) - 0.268 Beta            (27.88)   (4.83)            (13.25)           (5.80) | 21.5% |
| PBV= 0.87  +3.10 gEPS + 0.23 Beta + 6.00 ROE  + 1.00 Payout Ratio            (5.32) (11.97)          (3.24)          (20.30)      (0.95) | 28.0% |
| EV/Invested Capital= 2.80 + 1.20 g  + 4.00 ROIC – 2.90 DFR                                    (32.42)   (8.16)      (16.27)     (22.72) | 58.4% |
| EV/Sales = 3.22  + 1.60 g + 4.40 Oper Margin + 1.50 DFR- 2.80 Tax rate                     (16.86)  (5.35)   (8.80)                          (5.36)     (4.65) | 5.6% |
| EV/EBITDA= 30.93 + 4.90 g - 17.30 DFR -  40.40 Tax Rate                         (47.60)    (6.08)   (15.48)         (18.08) | 11.9% |
| gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)(  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |

*Market-wide
Regressions of Multiples –Global companies in January 2023*

*T
statistics in brackets below coefficients*

 

|  |  |
| --- | --- |
| Regression | R Squared |
| PE = 8.17 + 0.98 Beta + 50.80 gEPS + 18.20 Payout          (11.01)  (2.18)     (28.07)            (23.84) | 23.6% |
| PEG = 4.99 + 1.00 Payout – 1.16 ln(gEPS) - 0.262 Beta            (50.22)   (12.95)            (33.53)           (6.08) | 36.6% |
| PBV= 1.09  +3.60 gEPS - 0.16 Beta + 7.50 ROE  + 0.80 Payout Ratio            (9.46) (15.64)          (2.67)          (34.75)      (8.69) | 28.1% |
| EV/Invested Capital= 3.01 + 1.40 g  + 6.40 ROIC – 3.20 DFR                                    (44.69)   (10.13)      (34.69)     (31.07) | 56.1% |
| EV/Sales = 2.68  + 2.50 g + 8.10 Oper Margin + 2.10 DFR- 5.10 Tax rate                     (23.97)  (11.49)   (28.98)                          (13.26)     (15.15) | 17.8% |
| EV/EBITDA= 25.62 + 9.20 g - 11.40 DFR -  32.70Tax Rate                         (66.53)    (12.09)   (15.23)         (22.54) | 7.5% |
| ERP = Total Equity Risk Premium for country in which company is incorporated  gEPS = Expected growth rate in EPS for next 5 years (analyst estimates)  g = Expected growth rate in revenues for next 5 years (if not available, use gEPS)  Payout = Dividends/Earnings  ROIC = Return on capital = EBIT (1- tax rate)/ Invested Capital  Operating Margin = Pre-tax Operating Income/ Sales  Invested Capital = Book value of equity + Book value of debt - Cash  ROE = Net Income/ Book value of Equity  Tax Rate = Effective tax rate  = Taxes paid/ Taxable Income  DFR = Total Debt/(Total Debt + Market value of equity)  RIR = Reinvestment Rate = (Cap Ex – Depreciation + Chg in WC)/ EBIT (1-t)  WACC = Cost of capital in US dollars | |
