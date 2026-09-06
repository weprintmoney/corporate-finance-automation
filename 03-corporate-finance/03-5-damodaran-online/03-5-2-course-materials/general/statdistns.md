---
title: "Statistical Distributions"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/StatFile/statdistns.htm
---

Statistical Distributions  
<!--
/\* Font Definitions \*/
@font-face
{font-family:"Times New Roman";
panose-1:0 2 2 6 3 5 4 5 2 3;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:50331648 0 0 0 1 0;}
@font-face
{font-family:Arial;
panose-1:0 2 11 6 4 2 2 2 2 2;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:50331648 0 0 0 1 0;}
@font-face
{font-family:"Courier New";
panose-1:0 2 7 3 9 2 2 5 2 4;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:50331648 0 0 0 1 0;}
@font-face
{font-family:"New York";
panose-1:0 2 2 5 2 6 3 5 6 2;
mso-font-alt:"Times New Roman";
mso-font-charset:77;
mso-generic-font-family:roman;
mso-font-format:other;
mso-font-pitch:variable;
mso-font-signature:50331648 0 0 0 1 0;}
@font-face
{font-family:Wingdings;
panose-1:0 5 2 1 2 1 8 4 8 7;
mso-font-charset:2;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:0 0 256 0 -2147483648 0;}
@font-face
{font-family:"Monotype Sorts";
panose-1:0 1 1 6 1 1 1 1 1 1;
mso-font-charset:2;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:0 0 256 0 -2147483648 0;}
@font-face
{font-family:TimesNewRoman;
panose-1:0 0 0 0 0 0 0 0 0 0;
mso-font-alt:Times;
mso-font-charset:77;
mso-generic-font-family:roman;
mso-font-format:other;
mso-font-pitch:auto;
mso-font-signature:50331648 0 0 0 1 0;}
@font-face
{font-family:"Lucida Grande";
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:50331648 0 0 0 1 0;}
@font-face
{font-family:Garamond;
panose-1:0 2 2 4 4 3 3 1 1 8;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:50331648 0 0 0 1 0;}
/\* Style Definitions \*/
p.MsoNormal, li.MsoNormal, div.MsoNormal
{mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
h1
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:6.0pt;
margin-left:0in;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:1;
font-size:12.0pt;
font-family:Times;
mso-font-kerning:0pt;}
h2
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:6.0pt;
margin-left:0in;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:2;
font-size:12.0pt;
font-family:Times;
font-style:italic;}
h3
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:3;
tab-stops:346.5pt;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
font-style:italic;}
h4
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:4;
tab-stops:.5in 5.0in;
font-size:12.0pt;
font-family:"Times New Roman";
font-weight:normal;
font-style:italic;}
h5
{mso-style-next:Normal;
margin-top:6.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:5;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
font-style:italic;}
h6
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:6;
font-size:12.0pt;
font-family:Times;
text-decoration:underline;
text-underline:single;
font-weight:normal;}
p.MsoHeading7, li.MsoHeading7, div.MsoHeading7
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:7;
font-size:12.0pt;
font-family:Times;
font-style:italic;}
p.MsoHeading8, li.MsoHeading8, div.MsoHeading8
{mso-style-next:Normal;
margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:27.0pt;
margin-bottom:.0001pt;
text-align:justify;
text-indent:-27.0pt;
line-height:150%;
mso-pagination:none;
page-break-after:avoid;
mso-outline-level:8;
tab-stops:2.0in 225.0pt;
mso-layout-grid-align:none;
text-autospace:none;
font-size:12.0pt;
font-family:Times;
color:black;
font-style:italic;}
p.MsoHeading9, li.MsoHeading9, div.MsoHeading9
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:9;
font-size:16.0pt;
font-family:Times;
font-style:italic;}
p.MsoToc1, li.MsoToc1, div.MsoToc1
{mso-style-next:Normal;
margin-top:0in;
margin-right:.5in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:dotted 5.75in right blank 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoToc2, li.MsoToc2, div.MsoToc2
{mso-style-next:Normal;
margin-top:0in;
margin-right:.5in;
margin-bottom:0in;
margin-left:.5in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:dotted 5.75in right blank 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoToc3, li.MsoToc3, div.MsoToc3
{mso-style-next:Normal;
margin-top:0in;
margin-right:.5in;
margin-bottom:0in;
margin-left:1.0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:dotted 5.75in right blank 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoToc6, li.MsoToc6, div.MsoToc6
{mso-style-next:Normal;
margin-top:0in;
margin-right:.5in;
margin-bottom:0in;
margin-left:2.5in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:dotted 5.75in right blank 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoFootnoteText, li.MsoFootnoteText, div.MsoFootnoteText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Times;}
p.MsoCommentText, li.MsoCommentText, div.MsoCommentText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoHeader, li.MsoHeader, div.MsoHeader
{margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:center 3.0in right 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoFooter, li.MsoFooter, div.MsoFooter
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:center 3.0in right 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoCaption, li.MsoCaption, div.MsoCaption
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:150%;
mso-pagination:none;
mso-layout-grid-align:none;
text-autospace:none;
font-size:12.0pt;
font-family:TimesNewRoman;
font-style:italic;}
span.MsoFootnoteReference
{font-size:8.0pt;
mso-text-raise:3.0pt;}
span.MsoCommentReference
{font-size:9.0pt;}
span.MsoEndnoteReference
{vertical-align:super;}
p.MsoEndnoteText, li.MsoEndnoteText, div.MsoEndnoteText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoTitle, li.MsoTitle, div.MsoTitle
{margin:0in;
margin-bottom:.0001pt;
text-align:center;
text-indent:.25in;
line-height:150%;
mso-pagination:widow-orphan;
border:none;
mso-border-alt:solid windowtext .5pt;
padding:0in;
mso-padding-alt:1.0pt 4.0pt 1.0pt 4.0pt;
font-size:12.0pt;
font-family:"Times New Roman";
font-weight:bold;}
p.MsoBodyText, li.MsoBodyText, div.MsoBodyText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:.5in 5.0in;
font-size:12.0pt;
font-family:"Times New Roman";}
p.MsoBodyTextIndent, li.MsoBodyTextIndent, div.MsoBodyTextIndent
{margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
text-indent:.5in;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyText2, li.MsoBodyText2, div.MsoBodyText2
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:200%;
mso-pagination:widow-orphan;
border:none;
mso-border-alt:solid windowtext .75pt;
padding:0in;
mso-padding-alt:1.0pt 1.0pt 1.0pt 1.0pt;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyText3, li.MsoBodyText3, div.MsoBodyText3
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
border:none;
mso-border-alt:solid windowtext .5pt;
padding:0in;
mso-padding-alt:1.0pt 4.0pt 1.0pt 4.0pt;
font-size:12.0pt;
font-family:"Times New Roman";}
p.MsoBodyTextIndent2, li.MsoBodyTextIndent2, div.MsoBodyTextIndent2
{margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:.5in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyTextIndent3, li.MsoBodyTextIndent3, div.MsoBodyTextIndent3
{margin-top:0in;
margin-right:0in;
margin-bottom:6.0pt;
margin-left:.25in;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:8.0pt;
font-family:Times;}
a:link, span.MsoHyperlink
{color:blue;
text-decoration:underline;
text-underline:single;}
a:visited, span.MsoHyperlinkFollowed
{color:purple;
text-decoration:underline;
text-underline:single;}
table.MsoNormalTable
{mso-style-parent:"";
font-size:10.0pt;
font-family:"Times New Roman";}
p.MsoCommentSubject, li.MsoCommentSubject, div.MsoCommentSubject
{mso-style-parent:"Comment Text";
mso-style-next:"Comment Text";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
table.MsoTableGrid
{font-size:10.0pt;
font-family:"New York";}
p.Questions, li.Questions, div.Questions
{mso-style-name:Questions;
margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:9.0pt;
margin-bottom:.0001pt;
text-align:justify;
line-height:18.0pt;
mso-pagination:widow-orphan;
font-size:11.0pt;
font-family:Times;}
p.Times12, li.Times12, div.Times12
{mso-style-name:Times12;
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:"New York";}
p.Default, li.Default, div.Default
{mso-style-name:Default;
mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
mso-pagination:none;
mso-layout-grid-align:none;
text-autospace:none;
font-size:12.0pt;
font-family:Garamond;
color:black;}
@page Section1
{size:8.5in 11.0in;
margin:1.0in 1.25in 1.0in 1.25in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-even-header:url(":statdistns\_files:header.htm") eh1;
mso-header:url(":statdistns\_files:header.htm") h1;
mso-paper-source:0;}
div.Section1
{page:Section1;}
@page Section2
{size:11.0in 8.5in;
mso-page-orientation:landscape;
margin:1.25in 1.0in 1.25in 1.0in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-even-header:url(":statdistns\_files:header.htm") eh1;
mso-header:url(":statdistns\_files:header.htm") h1;
mso-paper-source:0;}
div.Section2
{page:Section2;}
/\* List Definitions \*/
@list l0
{mso-list-id:-2;
mso-list-type:simple;
mso-list-template-ids:1044408670;}
@list l0:level1
{mso-level-start-at:0;
mso-level-text:\*;
mso-level-tab-stop:none;
mso-level-number-position:left;
margin-left:0in;
text-indent:0in;}
@list l1
{mso-list-id:1;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l1:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l2
{mso-list-id:2;
mso-list-type:simple;
mso-list-template-ids:721929;}
@list l2:level1
{mso-level-number-format:bullet;
mso-level-text:\F0D8;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Wingdings;}
@list l3
{mso-list-id:3;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l3:level1
{mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l4
{mso-list-id:4;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l4:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l5
{mso-list-id:5;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l5:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l6
{mso-list-id:6;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l6:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l7
{mso-list-id:7;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l7:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l8
{mso-list-id:8;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l8:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l9
{mso-list-id:9;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l9:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l10
{mso-list-id:10;
mso-list-type:simple;
mso-list-template-ids:-1;}
@list l10:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l11
{mso-list-id:11;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l11:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l12
{mso-list-id:12;
mso-list-type:simple;
mso-list-template-ids:-1;}
@list l12:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l13
{mso-list-id:13;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l13:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l14
{mso-list-id:14;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l14:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l15
{mso-list-id:15;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l15:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l16
{mso-list-id:16;
mso-list-type:simple;
mso-list-template-ids:0;}
@list l16:level1
{mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l17
{mso-list-id:17;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l17:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l18
{mso-list-id:18;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l18:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l19
{mso-list-id:19;
mso-list-type:simple;
mso-list-template-ids:0;}
@list l19:level1
{mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l20
{mso-list-id:20;
mso-list-type:simple;
mso-list-template-ids:0;}
@list l20:level1
{mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l21
{mso-list-id:21;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l21:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l22
{mso-list-id:22;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l22:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l23
{mso-list-id:23;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l23:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l24
{mso-list-id:24;
mso-list-type:simple;
mso-list-template-ids:-1;}
@list l24:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l25
{mso-list-id:9180758;
mso-list-type:hybrid;
mso-list-template-ids:319093356 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l25:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l26
{mso-list-id:109327973;
mso-list-type:hybrid;
mso-list-template-ids:-567489648 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l26:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l27
{mso-list-id:149256941;
mso-list-type:hybrid;
mso-list-template-ids:1292944100 66569 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l27:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l28
{mso-list-id:170293029;
mso-list-type:hybrid;
mso-list-template-ids:1116252422 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l28:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l29
{mso-list-id:211889392;
mso-list-type:hybrid;
mso-list-template-ids:1925224762 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l29:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l30
{mso-list-id:219706394;
mso-list-type:hybrid;
mso-list-template-ids:-823884254 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l30:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l31
{mso-list-id:225839322;
mso-list-type:hybrid;
mso-list-template-ids:-2065300282 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l31:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l32
{mso-list-id:228927426;
mso-list-type:hybrid;
mso-list-template-ids:1454285428 1962993086 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l32:level1
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%1\)";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l33
{mso-list-id:237329909;
mso-list-type:hybrid;
mso-list-template-ids:-1206774768 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l33:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l34
{mso-list-id:257711185;
mso-list-type:hybrid;
mso-list-template-ids:-1187500238 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l34:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l35
{mso-list-id:277106196;
mso-list-type:hybrid;
mso-list-template-ids:-639860360 1639433 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l35:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l36
{mso-list-id:296028432;
mso-list-template-ids:890156892;}
@list l36:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l36:level2
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.25in;}
@list l37
{mso-list-id:323827515;
mso-list-type:hybrid;
mso-list-template-ids:172385450 1639433 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l37:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l38
{mso-list-id:326904289;
mso-list-type:hybrid;
mso-list-template-ids:-1017366588 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l38:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l39
{mso-list-id:355741276;
mso-list-type:hybrid;
mso-list-template-ids:-1911276628 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l39:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l40
{mso-list-id:384764695;
mso-list-type:hybrid;
mso-list-template-ids:1607477242 1962993086 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l40:level1
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%1\)";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l41
{mso-list-id:411006689;
mso-list-type:hybrid;
mso-list-template-ids:-1240011340 1962993086 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l41:level1
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%1\)";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l42
{mso-list-id:424232130;
mso-list-type:hybrid;
mso-list-template-ids:-252566632 1962993086 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l42:level1
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%1\)";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l43
{mso-list-id:469448164;
mso-list-type:hybrid;
mso-list-template-ids:1083489122 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l43:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l44
{mso-list-id:528764340;
mso-list-type:hybrid;
mso-list-template-ids:326116900 67698713 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l44:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l45
{mso-list-id:550649145;
mso-list-type:hybrid;
mso-list-template-ids:-26700256 67698703 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l45:level1
{mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l46
{mso-list-id:565578081;
mso-list-type:hybrid;
mso-list-template-ids:-367126848 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l46:level1
{mso-level-start-at:0;
mso-level-number-format:bullet;
mso-level-text:-;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:"Times New Roman";}
@list l47
{mso-list-id:568661108;
mso-list-type:hybrid;
mso-list-template-ids:890156892 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l47:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l48
{mso-list-id:643894136;
mso-list-type:hybrid;
mso-list-template-ids:672927998 1962993086 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l48:level1
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%1\)";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l49
{mso-list-id:666830977;
mso-list-type:hybrid;
mso-list-template-ids:-283721016 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l49:level1
{mso-level-start-at:0;
mso-level-number-format:bullet;
mso-level-text:-;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:"Times New Roman";}
@list l50
{mso-list-id:769207218;
mso-list-template-ids:890156892;}
@list l50:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l50:level2
{mso-level-start-at:0;
mso-level-number-format:bullet;
mso-level-text:-;
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.25in;
font-family:"Times New Roman";}
@list l51
{mso-list-id:773013918;
mso-list-type:hybrid;
mso-list-template-ids:773013628 0 0 -1 -1 -1 -1 -1 -1 -1;}
@list l51:level1
{mso-level-text:"";
mso-level-tab-stop:none;
mso-level-number-position:left;
margin-left:0in;
text-indent:0in;}
@list l51:level2
{mso-level-text:"";
mso-level-tab-stop:none;
mso-level-number-position:left;
margin-left:0in;
text-indent:0in;}
@list l51:level3
{mso-level-start-at:0;
mso-level-text:"";
mso-level-tab-stop:none;
mso-level-number-position:left;
margin-left:0in;
text-indent:0in;}
@list l51:level4
{mso-level-start-at:0;
mso-level-text:"";
mso-level-tab-stop:none;
mso-level-number-position:left;
margin-left:0in;
text-indent:0in;}
@list l51:level5
{mso-level-start-at:0;
mso-level-text:"";
mso-level-tab-stop:none;
mso-level-number-position:left;
margin-left:0in;
text-indent:0in;}
@list l51:level6
{mso-level-start-at:0;
mso-level-text:"";
mso-level-tab-stop:none;
mso-level-number-position:left;
margin-left:0in;
text-indent:0in;}
@list l51:level7
{mso-level-start-at:0;
mso-level-text:"";
mso-level-tab-stop:none;
mso-level-number-position:left;
margin-left:0in;
text-indent:0in;}
@list l51:level8
{mso-level-start-at:0;
mso-level-text:"";
mso-level-tab-stop:none;
mso-level-number-position:left;
margin-left:0in;
text-indent:0in;}
@list l51:level9
{mso-level-start-at:0;
mso-level-text:"";
mso-level-tab-stop:none;
mso-level-number-position:left;
margin-left:0in;
text-indent:0in;}
@list l52
{mso-list-id:773136305;
mso-list-type:hybrid;
mso-list-template-ids:326019312 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l52:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l53
{mso-list-id:779836707;
mso-list-type:hybrid;
mso-list-template-ids:-1727747334 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l53:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l54
{mso-list-id:812021351;
mso-list-type:hybrid;
mso-list-template-ids:985973646 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l54:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l55
{mso-list-id:919407425;
mso-list-type:hybrid;
mso-list-template-ids:-407066002 984073 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l55:level1
{mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l56
{mso-list-id:932740597;
mso-list-type:hybrid;
mso-list-template-ids:81719418 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l56:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l57
{mso-list-id:994602694;
mso-list-type:hybrid;
mso-list-template-ids:-986146608 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l57:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l58
{mso-list-id:1048529191;
mso-list-type:hybrid;
mso-list-template-ids:764045040 67698713 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l58:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l59
{mso-list-id:1086734254;
mso-list-type:hybrid;
mso-list-template-ids:-1905594146 984073 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l59:level1
{mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l60
{mso-list-id:1103300375;
mso-list-type:hybrid;
mso-list-template-ids:1506475840 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l60:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l60:level2
{mso-level-number-format:bullet;
mso-level-text:o;
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:"Courier New";}
@list l61
{mso-list-id:1118447719;
mso-list-type:hybrid;
mso-list-template-ids:-705397800 67698703 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l61:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l62
{mso-list-id:1169903204;
mso-list-type:hybrid;
mso-list-template-ids:-1666385040 66569 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l62:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l63
{mso-list-id:1181318096;
mso-list-type:hybrid;
mso-list-template-ids:-2117569524 1962993086 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l63:level1
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%1\)";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l64
{mso-list-id:1203833637;
mso-list-type:hybrid;
mso-list-template-ids:1524517976 984073 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l64:level1
{mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l65
{mso-list-id:1242065360;
mso-list-type:hybrid;
mso-list-template-ids:391550764 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l65:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l66
{mso-list-id:1300182455;
mso-list-type:hybrid;
mso-list-template-ids:-1295342460 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l66:level1
{mso-level-start-at:0;
mso-level-number-format:bullet;
mso-level-text:-;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:"Times New Roman";}
@list l67
{mso-list-id:1372993904;
mso-list-type:hybrid;
mso-list-template-ids:186563424 1962993086 1962993086 -547825924 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l67:level1
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%1\)";
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l67:level2
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%2\)";
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l67:level3
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:1.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l68
{mso-list-id:1395543049;
mso-list-type:hybrid;
mso-list-template-ids:1532399496 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l68:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l69
{mso-list-id:1406104027;
mso-list-type:hybrid;
mso-list-template-ids:262730674 67698713 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l69:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l70
{mso-list-id:1441490808;
mso-list-type:hybrid;
mso-list-template-ids:-1718335366 67698713 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l70:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l71
{mso-list-id:1443453532;
mso-list-type:hybrid;
mso-list-template-ids:2095607518 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l71:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l72
{mso-list-id:1447238283;
mso-list-type:hybrid;
mso-list-template-ids:393259268 1639433 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l72:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l73
{mso-list-id:1462960626;
mso-list-type:hybrid;
mso-list-template-ids:-1288954390 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l73:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l74
{mso-list-id:1481799903;
mso-list-type:hybrid;
mso-list-template-ids:-1164155844 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l74:level1
{mso-level-start-at:0;
mso-level-number-format:bullet;
mso-level-text:-;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:"Times New Roman";}
@list l75
{mso-list-id:1506554769;
mso-list-type:hybrid;
mso-list-template-ids:281465594 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l75:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.25in;
font-family:Symbol;}
@list l76
{mso-list-id:1526359563;
mso-list-type:hybrid;
mso-list-template-ids:801123544 67698713 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l76:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l77
{mso-list-id:1565141746;
mso-list-template-ids:890156892;}
@list l77:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l77:level2
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.25in;}
@list l78
{mso-list-id:1593513316;
mso-list-type:hybrid;
mso-list-template-ids:-1530083658 67698703 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l78:level1
{mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l79
{mso-list-id:1617130975;
mso-list-type:hybrid;
mso-list-template-ids:1939645904 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l79:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l80
{mso-list-id:1630940792;
mso-list-type:hybrid;
mso-list-template-ids:-420164914 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l80:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l81
{mso-list-id:1641417739;
mso-list-type:hybrid;
mso-list-template-ids:1890072632 67698703 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l81:level1
{mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l82
{mso-list-id:1644119368;
mso-list-type:hybrid;
mso-list-template-ids:670614960 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l82:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l83
{mso-list-id:1645814373;
mso-list-type:hybrid;
mso-list-template-ids:1574238646 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l83:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l84
{mso-list-id:1698235527;
mso-list-type:hybrid;
mso-list-template-ids:-576418486 984073 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l84:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l85
{mso-list-id:1772584662;
mso-list-type:hybrid;
mso-list-template-ids:1560830984 66569 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l85:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l86
{mso-list-id:1789424126;
mso-list-type:hybrid;
mso-list-template-ids:-712725184 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l86:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l87
{mso-list-id:1798646075;
mso-list-type:hybrid;
mso-list-template-ids:-298135760 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l87:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
margin-left:1.0in;
text-indent:-.25in;
font-family:Symbol;}
@list l88
{mso-list-id:1800607208;
mso-list-type:hybrid;
mso-list-template-ids:2146624626 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l88:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.25in;
font-family:Symbol;}
@list l88:level2
{mso-level-start-at:0;
mso-level-number-format:bullet;
mso-level-text:-;
mso-level-tab-stop:1.25in;
mso-level-number-position:left;
margin-left:1.25in;
text-indent:-.25in;
font-family:"Times New Roman";}
@list l89
{mso-list-id:1814250122;
mso-list-type:hybrid;
mso-list-template-ids:-861791902 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l89:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l90
{mso-list-id:1842741515;
mso-list-type:hybrid;
mso-list-template-ids:1287937702 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l90:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l91
{mso-list-id:1854952267;
mso-list-type:hybrid;
mso-list-template-ids:-1653041556 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l91:level1
{mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l92
{mso-list-id:1888447239;
mso-list-type:hybrid;
mso-list-template-ids:-2145490142 66569 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l92:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l93
{mso-list-id:1912351886;
mso-list-type:hybrid;
mso-list-template-ids:-111265558 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l93:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l94
{mso-list-id:1923176224;
mso-list-type:hybrid;
mso-list-template-ids:1058680146 1962993086 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l94:level1
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%1\)";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l95
{mso-list-id:1943876628;
mso-list-type:hybrid;
mso-list-template-ids:-1886624664 66569 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l95:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l95:level2
{mso-level-number-format:bullet;
mso-level-text:o;
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:"Courier New";}
@list l96
{mso-list-id:1967470960;
mso-list-type:hybrid;
mso-list-template-ids:-1694831760 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l96:level1
{mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l97
{mso-list-id:2004820057;
mso-list-type:hybrid;
mso-list-template-ids:-2819868 1639433 -615195418 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l97:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.25in;}
@list l97:level2
{mso-level-start-at:8;
mso-level-tab-stop:1.25in;
mso-level-number-position:left;
margin-left:1.25in;
text-indent:-.25in;}
@list l98
{mso-list-id:2021197135;
mso-list-type:hybrid;
mso-list-template-ids:-1913906968 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l98:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l99
{mso-list-id:2121531634;
mso-list-type:hybrid;
mso-list-template-ids:1884449528 -1241322702 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l99:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.25in;}
@list l0:level1 lfo1
{mso-level-start-at:1;
mso-level-number-format:bullet;
mso-level-numbering:continue;
mso-level-text:\F0B7;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l0:level1 lfo31
{mso-level-number-format:bullet;
mso-level-numbering:continue;
mso-level-text:�;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:0in;
mso-level-legacy-space:0in;
margin-left:0in;
text-indent:0in;
font-size:18.0pt;
font-family:Times;}
@list l2:level1 lfo39
{mso-level-number-format:arabic;
mso-level-numbering:continue;
mso-level-text:"%1\.";
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l1:level1 lfo50
{mso-level-number-format:arabic;
mso-level-numbering:continue;
mso-level-text:"%1\.";
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l0:level1 lfo51
{mso-level-start-at:1;
mso-level-number-format:bullet;
mso-level-numbering:continue;
mso-level-text:\F06F;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:0in;
mso-level-legacy-space:0in;
margin-left:0in;
text-indent:0in;
font-size:11.0pt;
font-family:"Monotype Sorts";}
@list l0:level1 lfo52
{mso-level-start-at:1;
mso-level-number-format:bullet;
mso-level-numbering:continue;
mso-level-text:\2013;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:0in;
mso-level-legacy-space:0in;
margin-left:0in;
text-indent:0in;
font-size:14.0pt;
font-family:Times;}
@list l0:level1 lfo53
{mso-level-start-at:1;
mso-level-number-format:bullet;
mso-level-numbering:continue;
mso-level-text:\F070;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:0in;
mso-level-legacy-space:0in;
margin-left:0in;
text-indent:0in;
font-size:11.0pt;
font-family:"Monotype Sorts";}
@list l4:level1 lfo54
{mso-level-numbering:continue;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l5:level1 lfo55
{mso-level-numbering:continue;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l6:level1 lfo56
{mso-level-numbering:continue;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l7:level1 lfo57
{mso-level-number-format:arabic;
mso-level-numbering:continue;
mso-level-text:"%1\.";
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l8:level1 lfo58
{mso-level-number-format:arabic;
mso-level-numbering:continue;
mso-level-text:"%1\.";
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l9:level1 lfo59
{mso-level-number-format:arabic;
mso-level-numbering:continue;
mso-level-text:"%1\.";
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l10:level1 lfo61
{mso-level-number-format:arabic;
mso-level-numbering:continue;
mso-level-text:"%1\.";
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l14:level1 lfo63
{mso-level-number-format:arabic;
mso-level-numbering:continue;
mso-level-text:"%1\.";
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l16:level1 lfo65
{mso-level-numbering:continue;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l13:level1 lfo66
{mso-level-numbering:continue;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l13:level1 lfo67
{mso-level-numbering:continue;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l9:level1 lfo68
{mso-level-number-format:arabic;
mso-level-numbering:continue;
mso-level-text:"%1\.";
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l15:level1 lfo69
{mso-level-number-format:arabic;
mso-level-numbering:continue;
mso-level-text:"%1\.";
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l0:level1 lfo72
{mso-level-number-format:bullet;
mso-level-numbering:continue;
mso-level-text:\F06E;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:0in;
mso-level-legacy-space:0in;
margin-left:0in;
text-indent:0in;
font-size:15.0pt;
font-family:"Monotype Sorts";}
@list l0:level1 lfo73
{mso-level-number-format:bullet;
mso-level-numbering:continue;
mso-level-text:\2013;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:0in;
mso-level-legacy-space:0in;
margin-left:0in;
text-indent:0in;
font-size:16.0pt;
font-family:Times;}
@list l3:level1 lfo79
{mso-level-numbering:continue;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
ol
{margin-bottom:0in;}
ul
{margin-bottom:0in;}
-->
  

# Statistical Distributions

            Every
statistics book provides a listing of statistical distributions, with their
properties, but browsing through these choices can be frustrating to anyone
without a statistical background, for two reasons. First, the choices seem
endless, with dozens of distributions competing for your attention, with little
or no intuitive basis for differentiating between them. Second, the descriptions
tend to be abstract and emphasize statistical properties such as the moments,
characteristic functions and cumulative distributions. In this appendix, we
will focus on the aspects of distributions that are most useful when analyzing
raw data and trying to fit the right distribution to that data.

## Fitting the Distribution

            When
confronted with data that needs to be characterized by a distribution, it is
best to start with the raw data and answer four basic questions about the data
that can help in the characterization. The first relates to whether the data
can take on only discrete values or whether the data is continuous;
whether a new pharmaceutical drug gets FDA approval or not is a discrete value
but the revenues from the drug represent a continuous variable. The second
looks at the symmetry of the data and if there is asymmetry, which
direction it lies in; in other words, are positive and negative outliers
equally likely or is one more likely than the other. The third question is
whether there are upper or lower limits on the data;; there are some
data items like revenues that cannot be lower than zero whereas there are
others like operating margins that cannot exceed a value (100%). The final and related
question relates to the likelihood of observing extreme values in the
distribution; in some data, the extreme values occur very infrequently whereas
in others, they occur more often.

### Is the data discrete or continuous?

            The
first and most obvious categorization of data should be on whether the data is
restricted to taking on only discrete values or if it is continuous. Consider
the inputs into a typical project analysis at a firm. Most estimates that go
into the analysis come from distributions that are continuous; market size,
market share and profit margins, for instance, are all continuous variables.
There are some important risk factors, though, that can take on only discrete
forms, including regulatory actions and the threat of a terrorist attack; in
the first case, the regulatory authority may dispense one of two or more
decisions which are specified up front and in the latter, you are subjected to
a terrorist attack or you are not.

            With
discrete data, the entire distribution can either be developed from scratch or
the data can be fitted to a pre-specified discrete distribution. With the
former, there are two steps to building the distribution. The first is
identifying the possible outcomes and the second is to estimate probabilities
to each outcome. As we noted in the text, we can draw on historical data or
experience as well as specific knowledge about the investment being analyzed to
arrive at the final distribution.  This
process is relatively simple to accomplish when there are a few outcomes with a
well-established basis for estimating probabilities but becomes more tedious as
the number of outcomes increases. If it is difficult or impossible to build up
a customized distribution, it may still be possible fit the data to one of the
following discrete distributions:

if !supportListsa.    
endifBinomial distribution: The binomial distribution
measures the probabilities of the number of successes over a given number of
trials with a specified probability of success in each try. In the simplest
scenario of a coin toss (with a fair coin), where the probability of getting a
head with each toss is 0.50 and there are a hundred trials, the binomial
distribution will measure the likelihood of getting anywhere from no heads in a
hundred tosses (very unlikely) to 50 heads (the most likely) to 100 heads (also
very unlikely). The binomial distribution in this case will be symmetric,
reflecting the even odds; as the probabilities shift from even odds, the
distribution will get more skewed. Figure 6A.1 presents binomial distributions
for three scenarios – two with 50% probability of success and one with a
70% probability of success and different trial sizes.

*Figure
6A.1: Binomial Distribution*

if !vml![](statdistns_files/image003.png)endif

As the
probability of success is varied (from 50%) the distribution will also shift
its shape, becoming positively skewed for probabilities less than 50% and
negatively skewed for probabilities greater than 50%.[if !supportFootnotes[1]endif](#_ftn1)

if !supportListsb.    
endifPoisson distribution: The Poisson distribution measures
the likelihood of a number of events occurring within a given time interval,
where the key parameter that is required is the average number of events in the
given interval (l). The resulting
distribution looks similar to the binomial, with the skewness being positive
but decreasing with l.  Figure 6A.2 presents three Poisson
distributions, with l ranging from 1 to
10.

*Figure
6A.2: Poisson Distribution*

*if !vml![](statdistns_files/image006.png)endif*

if !supportListsc.    
endifNegative Binomial distribution: Returning again to the
coin toss example, assume that you hold the number of successes fixed at a
given number and estimate the number of tries you will have before you reach
the specified number of successes. The resulting distribution is called the
negative binomial and it very closely resembles the Poisson. In fact, the
negative binomial distribution converges on the Poisson distribution, but will
be more skewed to the right (positive values) than the Poisson distribution
with similar parameters.

if !supportListsd.    
endifGeometric distribution: Consider again the coin toss
example used to illustrate the binomial. Rather than focus on the number of
successes in n trials, assume that you were measuring the likelihood of when
the first success will occur. For instance, with a fair coin toss, there is
a 50% chance that the first success will occur at the first try, a 25% chance
that it will occur on the second try and a 12.5% chance that it will occur on
the third try. The resulting distribution is positively skewed and looks as
follows for three different probability scenarios (in figure 6A.3):

*Figure
6A.3: Geometric Distribution*

if !vml![](statdistns_files/image009.png)endif

Note that the distribution is
steepest with high probabilities of success and flattens out as the probability
decreases. However, the distribution is always positively skewed.

if !supportListse.    
endifHypergeometric distribution: The hypergeometric
distribution measures the probability of a specified number of successes in n
trials, without replacement, from a finite population. Since the
sampling is without replacement, the probabilities can change as a function of
previous draws. Consider, for instance, the possibility of getting four face
cards in hand of ten, over repeated draws from a pack. Since there are 16 face
cards and the total pack contains 52 cards, the probability of getting four
face cards in a hand of ten can be estimated. Figure 6A.4 provides a graph of
the hypergeometric distribution:

*Figure
6A.4: Hypergeometric Distribution*

*if !vml![](statdistns_files/image012.png)endif*

Note
that the hypergeometric distribution converges on binomial distribution as the
as the population size increases.

if !supportListsf.      endifDiscrete
uniform distribution: This is the simplest of discrete distributions and
applies when all of the outcomes have an equal probability of occurring.  Figure 6A.5 presents a uniform discrete
distribution with five possible outcomes, each occurring 20% of the time:

*Figure
6A.5: Discrete Uniform Distribution*  
 if !vml![](statdistns_files/image015.png)endif

The discrete uniform distribution is best reserved for
circumstances where there are multiple possible outcomes, but no information
that would allow us to expect that one outcome is more likely than the others.

With continuous data, we cannot
specify all possible outcomes, since they are too numerous to list, but we have
two choices. The first is to convert the continuous data into a discrete form
and then go through the same process that we went through for discrete
distributions of estimating probabilities. For instance, we could take a
variable such as market share and break it down into discrete blocks –
market share between 3% and 3.5%, between 3.5% and 4% and so on – and
consider the likelihood that we will fall into each block. The second is to
find a continuous distribution that best fits the data and to specify the
parameters of the distribution. The rest of the appendix will focus on how to
make these choices.

### How symmetric is the data?

There are some datasets that
exhibit symmetry, i.e., the upside is mirrored by the downside. The symmetric
distribution that most practitioners have familiarity with is the normal
distribution, sown in Figure 6A.6, for a range of parameters:

*Figure 6A.6: Normal Distribution*

if !vml![](statdistns_files/image018.png)endif

The normal distribution has several features that make it
popular. First, it can be fully characterized by just two parameters –
the mean and the standard deviation – and thus reduces estimation pain.
Second, the probability of any value occurring can be obtained simply by
knowing how many standard deviations separate the value from the mean; the probability
that a value will fall 2 standard deviations from the mean is roughly 95%.   The normal distribution is best
suited for data that, at the minimum, meets the following conditions:

1. There
   is a strong tendency for the data to take on a central value.
2. Positive
   and negative deviations from this central value are equally likely
3. The
   frequency of the deviations falls off rapidly as we move further away from
   the central value.

The last two conditions show up when we compute the
parameters of the normal distribution: the symmetry of deviations leads to zero
skewness and the low probabilities of large deviations from the central value
reveal themselves in no kurtosis.

There is a cost we pay, though,
when we use a normal distribution to characterize data that is non-normal since
the probability estimates that we obtain will be misleading and can do more
harm than good. One obvious problem is when the data is asymmetric but another potential
problem is when the probabilities of large deviations from the central value do
not drop off as precipitously as required by the normal distribution. In
statistical language, the actual distribution of the data has fatter tails than
the normal. While all of symmetric distributions in the family are like the
normal in terms of the upside mirroring the downside, they vary in terms of
shape, with some distributions having fatter tails than the normal and the others
more accentuated peaks.  These
distributions are characterized as leptokurtic and you can consider two
examples. One is the logistic distribution, which has longer tails and a higher
kurtosis (1.2, as compared to 0 for the normal distribution) and the other are
Cauchy distributions, which also exhibit symmetry and higher kurtosis and are
characterized by a scale variable that determines how fat the tails are. Figure
6A.7 present a series of Cauchy distributions that exhibit the bias towards
fatter tails or more outliers than the normal distribution.

*Figure 6A.7: Cauchy Distribution*

if !vml![](statdistns_files/image021.png)endif

Either the logistic or the Cauchy distributions can be used
if the data is symmetric but with extreme values that occur more frequently
than you would expect with a normal distribution.

As the probabilities of extreme
values increases relative to the central value, the distribution will flatten
out. At its limit, assuming that the data stays symmetric and we put limits on
the extreme values on both sides, we end up with the uniform distribution,
shown in figure 6A.8:

*Figure 6A.8: Uniform Distribution*

if !vml![](statdistns_files/image024.png)endif

When is it appropriate to assume a uniform distribution for
a variable? One possible scenario is when you have a measure of the highest and
lowest values that a data item can take but no real information about where
within this range the value may fall. In other words, any value within that
range is just as likely as any other value.

Most data does not exhibit symmetry
and instead skews towards either very large positive or very large negative
values. If the data is positively skewed, one common choice is the lognormal
distribution, which is typically characterized by three parameters: a shape (s or sigma),
a scale (m or median) and a shift
parameter (if !vml![](statdistns_files/image027.png)endif). When m=0 and if !vml![](statdistns_files/image029.png)endif=1, you have the standard lognormal distribution and
when if !vml![](statdistns_files/image031.png)endif=0, the distribution requires only scale and sigma
parameters. As the sigma rises, the peak of the distribution shifts to the left
and the skewness in the distribution increases. Figure 6A.9 graphs lognormal
distributions for a range of parameters:

*Figure 6A.9: Lognormal distribution*

if !vml![](statdistns_files/image034.png)endif

The Gamma and Weibull distributions are two distributions
that are closely related to the lognormal distribution; like the lognormal
distribution, changing the parameter levels (shape, shift and scale) can cause
the distributions to change shape and become more or less skewed. In all of
these functions, increasing the shape parameter will push the distribution
towards the left. In fact, at high values of sigma, the left tail disappears entirely
and the outliers are all positive. In this form, these distributions all
resemble the exponential, characterized by a location (m) and scale parameter
(b), as is clear from figure 6A.10.

*Figure
6A.10: Weibull Distribution*

if !vml![](statdistns_files/image037.png)endif

The question of which of these distributions will best fit
the data will depend in large part on how severe the asymmetry in the data is. For
moderate positive skewness, where there are both positive and negative
outliers, but the former and larger and more common, the standard lognormal
distribution will usually suffice. As the skewness becomes more severe, you may
need to shift to a three-parameter lognormal distribution or a Weibull
distribution, and modify the shape parameter till it fits the data. At the
extreme, if there are no negative outliers and the only positive outliers in
the data, you should consider the exponential function, shown in Figure 6a.11:

*Figure
6A.11: Exponential Distribution*

if !vml![](statdistns_files/image040.png)endif

            If
the data exhibits negative slewness, the choices of distributions are more
limited. One possibility is the Beta distribution, which has two shape
parameters (p and q) and upper and lower bounds on the data (a and b). Altering
these parameters can yield distributions that exhibit either positive or
negative skewness, as shown in figure 6A.12:

*Figure
6A.12: Beta Distribution*

if !vml![](statdistns_files/image043.png)endif

Another is an extreme value distribution, which can also be
altered to generate both positive and negative skewness, depending upon whether
the extreme outcomes are the maximum (positive) or minimum (negative) values
(see Figure 6A.13)

*Figure 6A.13:
Extreme Value Distributions*

*if !vml![](statdistns_files/image046.png)endifif !vml![](statdistns_files/image049.png)endif*

### Are there upper or lower limits on data values?

            There
are often natural limits on the values that data can take on. As we noted
earlier, the revenues and the market value of a firm cannot be negative and the
profit margin cannot exceed 100%. Using a distribution that does not constrain
the values to these limits can create problems. For instance, using a normal
distribution to describe profit margins can sometimes result in profit margins
that exceed 100%, since the distribution has no limits on either the downside
or the upside.

            When
data is constrained, the questions that needs to be answered are whether the
constraints apply on one side of the distribution or both, and if so, what the
limits on values are. Once these questions have been answered, there are two
choices. One is to find a continuous distribution that conforms to these
constraints. For instance, the lognormal distribution can be used to model
data, such as revenues and stock prices that are constrained to be never less
than zero. For data that have both upper and lower limits, you could use the
uniform distribution, if the probabilities of the outcomes are even across
outcomes or a triangular distribution (if the data is clustered around a
central value). Figure 6A.14 presents a triangular distribution:

*Figure
6A.14: Triangular Distribution*

if !vml![](statdistns_files/image052.png)endif

An alternative approach is to use a continuous distribution that
normally allows data to take on any value and to put upper and lower limits on
the values that the data can assume. Note that the cost of putting these
constrains is small in distributions like the normal where the probabilities of
extreme values is very small, but increases as the distribution exhibits fatter
tails.

### How likely are you to see extreme values of data, relative to the middle values?

            As
we noted in the earlier section, a key consideration in what distribution to
use to describe the data is the likelihood of extreme values for the data,
relative to the middle value. In the case of the normal distribution, this
likelihood is small and it increases as you move to the logistic and Cauchy
distributions. While it may often be more realistic to use the latter to
describe real world data, the benefits of a better distribution fit have to be
weighed off against the ease with which parameters can be estimated from the
normal distribution. Consequently, it may make sense to stay with the normal
distribution for symmetric data, unless the likelihood of extreme values
increases above a threshold.

            The
same considerations apply for skewed distributions, though the concern will
generally be more acute for the skewed side of the distribution. In other
words, with positively skewed distribution, the question of which distribution
to use will depend upon how much more likely large positive values are than
large negative values, with the fit ranging from the lognormal to the
exponential.

            In
summary, the question of which distribution best fits data cannot be answered
without looking at whether the data is discrete or continuous, symmetric or
asymmetric and where the outliers lie. Figure 6A.15 summarizes the choices in a
chart.

## Tests for Fit

            The
simplest test for distributional fit is visual with a comparison of the
histogram of the actual data to the fitted distribution. Consider figure 6A.16,
where we report the distribution of current price earnings ratios for US stocks
in early 2007, with a normal distribution superimposed on it.

*Figure 6A.16:
Current PE Ratios for US Stocks – January 2007*

if !vml![](statdistns_files/image055.png)endif

The distributions are so clearly divergent that the normal
distribution assumption does not hold up.

            A
slightly more sophisticated test is to compute the moments of the actual data
distribution – the mean, the standard deviation, skewness and kurtosis
– and to examine them for fit to the chosen distribution. With the
price-earnings data above, for instance, the moments of the distribution and
key statistics are summarized  in
table 6A.1:

*Table 6A.1: Current
PE Ratio for US stocks – Key Statistics*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| if !supportEmptyParas endif | | *Current PE* | *Normal Distribution* |if !supportMisalignedRows  |endif
| Mean | | 28.947 | if !supportEmptyParas endif |if !supportMisalignedRows  |endif
| Median | | 20.952 | Median = Mean |if !supportMisalignedRows  |endif
| Standard deviation | | 26.924 | if !supportEmptyParas endif |if !supportMisalignedRows  |endif
| Skewness | | 3.106 | 0 |if !supportMisalignedRows  |endif
| Kurtosis | | 11.936 | 0 |if !supportMisalignedRows  |endif
|  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | ||  | | | |if !supportMisalignedRows  |endif | |if !supportMisalignedColumns|  |  |  |  |  |
endif

Since the normal distribution has no skewness
and zero kurtosis, we can easily reject the hypothesis that price
earnings ratios are normally distributed.  

The typical tests for
goodness of fit compare the actual distribution function of the
data with the cumulative distribution function of the
distribution that is being used to characterize the data, to
either accept the hypothesis that the chosen distribution fits
the data or to reject it. Not surprisingly, given its constant
use, there are more tests for normality than for any other
distribution. The Kolmogorov-Smirnov test is one of the oldest tests
of fit for distributions[if !supportFootnotes[2]endif](#_ftn2),
dating back to 1967. Improved versions of the tests include the
Shapiro-Wilk and Anderson-Darling tests. Applying these tests to
the current PE ratio yields the unsurprising result that the
hypothesis that current PE ratios are drawn from a normal
distribution is roundly rejected:

*Tests of Normality*

if !vml![](statdistns_files/image058.png)endif

There are graphical tests of normality,
where probability plots can be used to assess the hypothesis that
the data is drawn from a normal distribution. Figure 6A.17
illustrates this, using current PE ratios as the data set.

if !vml![](statdistns_files/image061.png)endif

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| if !supportMisalignedRows  |endif || if !supportMisalignedRows  |endif || if !supportMisalignedRows  |endif |

Given that the normal distribution is one of
easiest to work with, it is useful to begin by testing data
for non-normality to see if you can get away with using the normal
distribution. If not, you can extend your search to other and
more complex distributions.

# Conclusion

            Raw
data is almost never as well behaved as we would like it to
be. Consequently, fitting a statistical distribution to data
is part art and part science, requiring compromises along the
way. The key to good data analysis is maintaining a balance
between getting a good distributional fit and preserving ease
of estimation, keeping in mind that the ultimate objective is
that the analysis should lead to better decision. In
particular, you may decide to settle for a distribution that
less completely fits the data over one that more completely
fits it, simply because estimating the parameters may be
easier to do with the former. This may explain the
overwhelming dependence on the normal distribution in
practice, notwithstanding the fact that most data do not meet
the criteria needed for the distribution to fit.

           

if !supportEmptyParas endif

 

# Figure 6A.15: Distributional Choices

# if !vmlendif

if !supportEmptyParas endif

if !supportFootnotes  
 

---

 endif

[if !supportFootnotes[1]endif](#_ftnref1) As the
number of trials increases and the probability of success is close to 0.5, the
binomial distribution converges on the normal distribution.

[if !supportFootnotes[2]endif](#_ftnref2) The
Kolgomorov-Smirnov test can be used to see if the data fits a normal,
lognormal, Weibull, exponential or logistic distribution.
