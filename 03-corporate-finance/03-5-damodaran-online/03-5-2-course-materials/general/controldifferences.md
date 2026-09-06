---
title: "Controlling for differences in relative valuation"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook/controldifferences.htm
---

if !supportAnnotations <!-- --> <!--
function msoCommentShow(anchor\_id, com\_id)
{
if(msoBrowserCheck())
{
c = document.all(com\_id);
if (null != c)
{
a = document.all(anchor\_id);
var cw = c.offsetWidth;
var ch = c.offsetHeight;
var aw = a.offsetWidth;
var ah = a.offsetHeight;
var x = a.offsetLeft;
var y = a.offsetTop;
var el = a;
while (el.tagName != "BODY")
{
el = el.offsetParent;
x = x + el.offsetLeft;
y = y + el.offsetTop;
}
var bw = document.body.clientWidth;
var bh = document.body.clientHeight;
var bsl = document.body.scrollLeft;
var bst = document.body.scrollTop;
if (x + cw + ah / 2 > bw + bsl && x + aw - ah / 2 - cw >= bsl )
{ c.style.left = x + aw - ah / 2 - cw; }
else
{ c.style.left = x + ah / 2; }
if (y + ch + ah / 2 > bh + bst && y + ah / 2 - ch >= bst )
{ c.style.top = y + ah / 2 - ch; }
else
{ c.style.top = y + ah / 2; }
c.style.visibility = "visible";
} } }
function msoCommentHide(com\_id)
{
if(msoBrowserCheck())
{
c = document.all(com\_id);
if (null != c)
{
c.style.visibility = "hidden";
c.style.left = -1000;
c.style.top = -1000;
} }
}
function msoBrowserCheck()
{
ms = navigator.appVersion.indexOf("MSIE");
vers = navigator.appVersion.substring(ms + 5, ms + 6);
ie4 = (ms > 0) && (parseInt(vers) >= 4);
return ie4;
}
if (msoBrowserCheck())
{
document.styleSheets.dynCom.addRule(".msocomanchor","background: infobackground");
document.styleSheets.dynCom.addRule(".msocomoff","display: none");
document.styleSheets.dynCom.addRule(".msocomtxt","visibility: hidden");
document.styleSheets.dynCom.addRule(".msocomtxt","position: absolute");
document.styleSheets.dynCom.addRule(".msocomtxt","top: -1000");
document.styleSheets.dynCom.addRule(".msocomtxt","left: -1000");
document.styleSheets.dynCom.addRule(".msocomtxt","width: 33%");
document.styleSheets.dynCom.addRule(".msocomtxt","background: infobackground");
document.styleSheets.dynCom.addRule(".msocomtxt","color: infotext");
document.styleSheets.dynCom.addRule(".msocomtxt","border-top: 1pt solid threedlightshadow");
document.styleSheets.dynCom.addRule(".msocomtxt","border-right: 2pt solid threedshadow");
document.styleSheets.dynCom.addRule(".msocomtxt","border-bottom: 2pt solid threedshadow");
document.styleSheets.dynCom.addRule(".msocomtxt","border-left: 1pt solid threedlightshadow");
document.styleSheets.dynCom.addRule(".msocomtxt","padding: 3pt 3pt 3pt 3pt");
}
// --> endif 
<!--
/\* Font Definitions \*/
@font-face
{font-family:"Courier New";
panose-1:2 7 3 9 2 2 5 2 4 4;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:-536859905 -1073711037 9 0 511 0;}
@font-face
{font-family:Times;
panose-1:2 0 5 0 0 0 0 0 0 0;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:3 0 0 0 1 0;}
@font-face
{font-family:"New York";
panose-1:0 0 0 0 0 0 0 0 0 0;
mso-font-alt:"Times New Roman";
mso-font-charset:77;
mso-generic-font-family:roman;
mso-font-format:other;
mso-font-pitch:variable;
mso-font-signature:3 0 0 0 1 0;}
@font-face
{font-family:Wingdings;
panose-1:5 0 0 0 0 0 0 0 0 0;
mso-font-charset:2;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:0 268435456 0 0 -2147483648 0;}
@font-face
{font-family:"\FF2D\FF33 \30B4\30B7\30C3\30AF";
mso-font-charset:78;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:-536870145 1791491579 18 0 131231 0;}
@font-face
{font-family:"\FF2D\FF33 \30B4\30B7\30C3\30AF";
mso-font-charset:78;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:-536870145 1791491579 18 0 131231 0;}
@font-face
{font-family:Calibri;
panose-1:2 15 5 2 2 2 4 3 2 4;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:-1610611985 1073750139 0 0 159 0;}
@font-face
{font-family:"Lucida Grande";
panose-1:2 11 6 0 4 5 2 2 2 4;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:-520090897 1342218751 0 0 447 0;}
/\* Style Definitions \*/
p.MsoNormal, li.MsoNormal, div.MsoNormal
{mso-style-unhide:no;
mso-style-qformat:yes;
mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-justify:inter-ideograph;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-bidi-font-family:"Times New Roman";}
h1
{mso-style-priority:9;
mso-style-unhide:no;
mso-style-qformat:yes;
mso-style-link:"Heading 1 Char";
mso-style-next:Normal;
margin-top:24.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
text-justify:inter-ideograph;
line-height:150%;
mso-pagination:widow-orphan lines-together;
page-break-after:avoid;
mso-outline-level:1;
font-size:16.0pt;
font-family:Calibri;
mso-ascii-font-family:Calibri;
mso-ascii-theme-font:major-latin;
mso-fareast-font-family:"\FF2D\FF33 \30B4\30B7\30C3\30AF";
mso-fareast-theme-font:major-fareast;
mso-hansi-font-family:Calibri;
mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi;
color:#345A8A;
mso-themecolor:accent1;
mso-themeshade:181;
mso-font-kerning:0pt;}
h2
{mso-style-priority:9;
mso-style-qformat:yes;
mso-style-link:"Heading 2 Char";
mso-style-next:Normal;
margin-top:10.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
text-justify:inter-ideograph;
line-height:150%;
mso-pagination:widow-orphan lines-together;
page-break-after:avoid;
mso-outline-level:2;
font-size:13.0pt;
font-family:Calibri;
mso-ascii-font-family:Calibri;
mso-ascii-theme-font:major-latin;
mso-fareast-font-family:"\FF2D\FF33 \30B4\30B7\30C3\30AF";
mso-fareast-theme-font:major-fareast;
mso-hansi-font-family:Calibri;
mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi;
color:#4F81BD;
mso-themecolor:accent1;}
h3
{mso-style-unhide:no;
mso-style-qformat:yes;
mso-style-link:"Heading 3 Char";
mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
text-justify:inter-ideograph;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:3;
tab-stops:346.5pt;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-bidi-font-family:"Times New Roman";
font-weight:normal;
font-style:italic;
mso-bidi-font-style:normal;}
h4
{mso-style-unhide:no;
mso-style-qformat:yes;
mso-style-link:"Heading 4 Char";
mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
text-justify:inter-ideograph;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:4;
tab-stops:.5in 5.0in;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-fareast-font-family:"Times New Roman";
font-weight:normal;
font-style:italic;
mso-bidi-font-style:normal;}
h5
{mso-style-unhide:no;
mso-style-qformat:yes;
mso-style-link:"Heading 5 Char";
mso-style-next:Normal;
margin-top:6.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
text-justify:inter-ideograph;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:5;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-bidi-font-family:"Times New Roman";
font-weight:normal;
font-style:italic;
mso-bidi-font-style:normal;}
h6
{mso-style-unhide:no;
mso-style-qformat:yes;
mso-style-link:"Heading 6 Char";
mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:6;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-bidi-font-family:"Times New Roman";
font-weight:normal;
text-decoration:underline;
text-underline:single;}
p.MsoHeading9, li.MsoHeading9, div.MsoHeading9
{mso-style-unhide:no;
mso-style-qformat:yes;
mso-style-link:"Heading 9 Char";
mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:9;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-bidi-font-family:"Times New Roman";
font-style:italic;
mso-bidi-font-style:normal;}
p.MsoFootnoteText, li.MsoFootnoteText, div.MsoFootnoteText
{mso-style-unhide:no;
mso-style-link:"Footnote Text Char";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-justify:inter-ideograph;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-bidi-font-family:"Times New Roman";}
p.MsoCommentText, li.MsoCommentText, div.MsoCommentText
{mso-style-noshow:yes;
mso-style-unhide:no;
mso-style-link:"Comment Text Char";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-justify:inter-ideograph;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-bidi-font-family:"Times New Roman";}
p.MsoFooter, li.MsoFooter, div.MsoFooter
{mso-style-unhide:no;
mso-style-link:"Footer Char";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-justify:inter-ideograph;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:center 3.0in right 6.0in;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-bidi-font-family:"Times New Roman";}
span.MsoFootnoteReference
{mso-style-unhide:no;
mso-ansi-font-size:8.0pt;
position:relative;
top:-3.0pt;
mso-text-raise:3.0pt;}
span.MsoCommentReference
{mso-style-noshow:yes;
mso-style-unhide:no;
mso-ansi-font-size:9.0pt;}
p.MsoAcetate, li.MsoAcetate, div.MsoAcetate
{mso-style-noshow:yes;
mso-style-priority:99;
mso-style-link:"Balloon Text Char";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-justify:inter-ideograph;
mso-pagination:widow-orphan;
font-size:9.0pt;
font-family:"Lucida Grande";
mso-fareast-font-family:"Times New Roman";}
span.MsoSubtleEmphasis
{mso-style-priority:19;
mso-style-unhide:no;
mso-style-qformat:yes;
color:gray;
mso-themecolor:text1;
mso-themetint:127;
font-style:italic;}
span.Heading3Char
{mso-style-name:"Heading 3 Char";
mso-style-unhide:no;
mso-style-locked:yes;
mso-style-link:"Heading 3";
mso-ansi-font-size:12.0pt;
font-family:Times;
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";
mso-fareast-language:EN-US;
font-style:italic;
mso-bidi-font-style:normal;}
span.Heading4Char
{mso-style-name:"Heading 4 Char";
mso-style-unhide:no;
mso-style-locked:yes;
mso-style-link:"Heading 4";
mso-ansi-font-size:12.0pt;
font-family:"Times New Roman";
mso-ascii-font-family:"Times New Roman";
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:"Times New Roman";
mso-bidi-font-family:"Times New Roman";
mso-fareast-language:EN-US;
font-style:italic;
mso-bidi-font-style:normal;}
span.Heading5Char
{mso-style-name:"Heading 5 Char";
mso-style-unhide:no;
mso-style-locked:yes;
mso-style-link:"Heading 5";
mso-ansi-font-size:12.0pt;
font-family:Times;
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";
mso-fareast-language:EN-US;
font-style:italic;
mso-bidi-font-style:normal;}
span.Heading6Char
{mso-style-name:"Heading 6 Char";
mso-style-unhide:no;
mso-style-locked:yes;
mso-style-link:"Heading 6";
mso-ansi-font-size:12.0pt;
font-family:Times;
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";
mso-fareast-language:EN-US;
text-decoration:underline;
text-underline:single;}
span.Heading9Char
{mso-style-name:"Heading 9 Char";
mso-style-unhide:no;
mso-style-locked:yes;
mso-style-link:"Heading 9";
mso-ansi-font-size:12.0pt;
font-family:Times;
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";
mso-fareast-language:EN-US;
font-style:italic;
mso-bidi-font-style:normal;}
span.FooterChar
{mso-style-name:"Footer Char";
mso-style-unhide:no;
mso-style-locked:yes;
mso-style-link:Footer;
mso-ansi-font-size:12.0pt;
font-family:Times;
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";
mso-fareast-language:EN-US;}
span.FootnoteTextChar
{mso-style-name:"Footnote Text Char";
mso-style-unhide:no;
mso-style-locked:yes;
mso-style-link:"Footnote Text";
font-family:Times;
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";
mso-fareast-language:EN-US;}
span.CommentTextChar
{mso-style-name:"Comment Text Char";
mso-style-noshow:yes;
mso-style-unhide:no;
mso-style-locked:yes;
mso-style-link:"Comment Text";
mso-ansi-font-size:12.0pt;
mso-bidi-font-size:12.0pt;
font-family:Times;
mso-ascii-font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:Times;
mso-bidi-font-family:"Times New Roman";
mso-fareast-language:EN-US;}
p.IllustrationHeading, li.IllustrationHeading, div.IllustrationHeading
{mso-style-name:"Illustration Heading";
mso-style-unhide:no;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
text-justify:inter-ideograph;
line-height:200%;
mso-pagination:widow-orphan;
border:none;
mso-border-alt:solid windowtext .75pt;
padding:0in;
mso-padding-alt:1.0pt 1.0pt 1.0pt 1.0pt;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:Times;
mso-fareast-font-family:"Times New Roman";
mso-bidi-font-family:"Times New Roman";
font-style:italic;
mso-bidi-font-style:normal;}
span.BalloonTextChar
{mso-style-name:"Balloon Text Char";
mso-style-noshow:yes;
mso-style-priority:99;
mso-style-unhide:no;
mso-style-locked:yes;
mso-style-link:"Balloon Text";
mso-ansi-font-size:9.0pt;
mso-bidi-font-size:9.0pt;
font-family:"Lucida Grande";
mso-ascii-font-family:"Lucida Grande";
mso-fareast-font-family:"Times New Roman";
mso-hansi-font-family:"Lucida Grande";
mso-bidi-font-family:"Lucida Grande";
mso-fareast-language:EN-US;}
span.Heading1Char
{mso-style-name:"Heading 1 Char";
mso-style-priority:9;
mso-style-unhide:no;
mso-style-locked:yes;
mso-style-link:"Heading 1";
mso-ansi-font-size:16.0pt;
mso-bidi-font-size:16.0pt;
font-family:Calibri;
mso-ascii-font-family:Calibri;
mso-ascii-theme-font:major-latin;
mso-fareast-font-family:"\FF2D\FF33 \30B4\30B7\30C3\30AF";
mso-fareast-theme-font:major-fareast;
mso-hansi-font-family:Calibri;
mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi;
color:#345A8A;
mso-themecolor:accent1;
mso-themeshade:181;
mso-fareast-language:EN-US;
font-weight:bold;}
span.Heading2Char
{mso-style-name:"Heading 2 Char";
mso-style-priority:9;
mso-style-unhide:no;
mso-style-locked:yes;
mso-style-link:"Heading 2";
mso-ansi-font-size:13.0pt;
mso-bidi-font-size:13.0pt;
font-family:Calibri;
mso-ascii-font-family:Calibri;
mso-ascii-theme-font:major-latin;
mso-fareast-font-family:"\FF2D\FF33 \30B4\30B7\30C3\30AF";
mso-fareast-theme-font:major-fareast;
mso-hansi-font-family:Calibri;
mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi;
color:#4F81BD;
mso-themecolor:accent1;
mso-fareast-language:EN-US;
font-weight:bold;}
span.SpellE
{mso-style-name:"";
mso-spl-e:yes;}
span.GramE
{mso-style-name:"";
mso-gram-e:yes;}
.MsoChpDefault
{mso-style-type:export-only;
mso-default-props:yes;
font-size:10.0pt;
mso-ansi-font-size:10.0pt;
mso-bidi-font-size:10.0pt;
font-family:Cambria;
mso-ascii-font-family:Cambria;
mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:"\FF2D\FF33 \660E\671D";
mso-fareast-theme-font:minor-fareast;
mso-hansi-font-family:Cambria;
mso-hansi-theme-font:minor-latin;
mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:minor-bidi;
mso-fareast-language:JA;}
.MsoPapDefault
{mso-style-type:export-only;
margin-bottom:10.0pt;}
/\* Page Definitions \*/
@page
{mso-footnote-separator:url(":controldifferences\_files:header.htm") fs;
mso-footnote-continuation-separator:url(":controldifferences\_files:header.htm") fcs;
mso-endnote-separator:url(":controldifferences\_files:header.htm") es;
mso-endnote-continuation-separator:url(":controldifferences\_files:header.htm") ecs;}
@page WordSection1
{size:8.5in 11.0in;
margin:1.0in 1.25in 1.0in 1.25in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-paper-source:0;}
div.WordSection1
{page:WordSection1;}
/\* List Definitions \*/
@list l0
{mso-list-id:818810608;
mso-list-type:hybrid;
mso-list-template-ids:1522823860 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l0:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l0:level2
{mso-level-number-format:bullet;
mso-level-text:o;
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.25in;
font-family:"Courier New";
mso-bidi-font-family:"Times New Roman";}
@list l0:level3
{mso-level-number-format:bullet;
mso-level-text:\F0A7;
mso-level-tab-stop:1.25in;
mso-level-number-position:left;
margin-left:1.25in;
text-indent:-.25in;
font-family:Wingdings;}
@list l0:level4
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:1.75in;
mso-level-number-position:left;
margin-left:1.75in;
text-indent:-.25in;
font-family:Symbol;}
@list l0:level5
{mso-level-number-format:bullet;
mso-level-text:o;
mso-level-tab-stop:2.25in;
mso-level-number-position:left;
margin-left:2.25in;
text-indent:-.25in;
font-family:"Courier New";
mso-bidi-font-family:"Times New Roman";}
@list l0:level6
{mso-level-number-format:bullet;
mso-level-text:\F0A7;
mso-level-tab-stop:2.75in;
mso-level-number-position:left;
margin-left:2.75in;
text-indent:-.25in;
font-family:Wingdings;}
@list l0:level7
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:3.25in;
mso-level-number-position:left;
margin-left:3.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l0:level8
{mso-level-number-format:bullet;
mso-level-text:o;
mso-level-tab-stop:3.75in;
mso-level-number-position:left;
margin-left:3.75in;
text-indent:-.25in;
font-family:"Courier New";
mso-bidi-font-family:"Times New Roman";}
@list l0:level9
{mso-level-number-format:bullet;
mso-level-text:\F0A7;
mso-level-tab-stop:4.25in;
mso-level-number-position:left;
margin-left:4.25in;
text-indent:-.25in;
font-family:Wingdings;}
@list l1
{mso-list-id:1811635676;
mso-list-type:hybrid;
mso-list-template-ids:-146355696 67698689 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l1:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l1:level2
{mso-level-number-format:bullet;
mso-level-text:o;
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:"Courier New";
mso-bidi-font-family:"Times New Roman";}
@list l1:level3
{mso-level-number-format:bullet;
mso-level-text:\F0A7;
mso-level-tab-stop:1.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Wingdings;}
@list l1:level4
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:2.0in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l1:level5
{mso-level-number-format:bullet;
mso-level-text:o;
mso-level-tab-stop:2.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:"Courier New";
mso-bidi-font-family:"Times New Roman";}
@list l1:level6
{mso-level-number-format:bullet;
mso-level-text:\F0A7;
mso-level-tab-stop:3.0in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Wingdings;}
@list l1:level7
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:3.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l1:level8
{mso-level-number-format:bullet;
mso-level-text:o;
mso-level-tab-stop:4.0in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:"Courier New";
mso-bidi-font-family:"Times New Roman";}
@list l1:level9
{mso-level-number-format:bullet;
mso-level-text:\F0A7;
mso-level-tab-stop:4.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Wingdings;}
@list l2
{mso-list-id:1907762458;
mso-list-type:hybrid;
mso-list-template-ids:344383840 67698689 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l2:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l2:level2
{mso-level-number-format:bullet;
mso-level-text:o;
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:"Courier New";
mso-bidi-font-family:"Times New Roman";}
@list l2:level3
{mso-level-number-format:bullet;
mso-level-text:\F0A7;
mso-level-tab-stop:1.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Wingdings;}
@list l2:level4
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:2.0in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l2:level5
{mso-level-number-format:bullet;
mso-level-text:o;
mso-level-tab-stop:2.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:"Courier New";
mso-bidi-font-family:"Times New Roman";}
@list l2:level6
{mso-level-number-format:bullet;
mso-level-text:\F0A7;
mso-level-tab-stop:3.0in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Wingdings;}
@list l2:level7
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:3.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l2:level8
{mso-level-number-format:bullet;
mso-level-text:o;
mso-level-tab-stop:4.0in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:"Courier New";
mso-bidi-font-family:"Times New Roman";}
@list l2:level9
{mso-level-number-format:bullet;
mso-level-text:\F0A7;
mso-level-tab-stop:4.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Wingdings;}
ol
{margin-bottom:0in;}
ul
{margin-bottom:0in;}
-->
  Controlling for differences in relative valuation 

# [littlebook](../littlebook.htm) The Little Book of Valuation

# Controlling for Differences across Firms

            No
matter how carefully we construct our list of comparable firms, we will end up
with firms that are different from the firm we are valuing. The differences may
be small on some variables and large on others and we will have to control for
these differences in a relative valuation. There are three ways of controlling
for these differences:

## 1. Subjective Adjustments

Relative
valuation begins with two choices - the multiple used in the analysis and the
group of firms that comprises the comparable firms. In many
relative valuation, the multiple is calculated for each of the
comparable firms and the average is computed. To evaluate an individual firm, the
analyst then compare the multiple it trades at to the average computed; if it is significantly different, the analyst can make a
subjective judgment about whether the firm�s individual characteristics
(growth, risk or cash flows) may explain the difference. Thus, a firm may have
a PE ratio of 22 in a sector where the average PE is only 15, but the analyst
may conclude that this difference can be justified because the firm has higher
growth potential than the average firm in the industry. If, in the judgment of
the analyst, the difference on the multiple cannot be explained by the
fundamentals, the firm will be viewed as over valued (if its multiple is higher
than the average) or undervalued (if its multiple is lower than the average).

The
weakness in this approach is not that analysts are called upon to make
subjective judgments, but that the judgments are often based upon little more
than guesswork. All too often, these judgments confirm their biases about
companies.

## 2. Modified Multiples

            In
this approach, we modify the multiple to take into account the most important
variable determining it – the companion variable. To provide an
illustration, analysts who compare PE ratios across companies with very
different growth rates often divide the PE ratio by the expected growth rate in
EPS to determine a growth-adjusted PE ratio or the PEG ratio. This ratio is
then compared across companies with different growth rates to find under and
over valued companies.

There
are two implicit assumptions that we make when using these modified multiples.
The first is that these firms are comparable on all the other measures of
value, other than the one being controlled for. In other words, when comparing
PEG ratios across companies, we are assuming that they are all of equivalent
risk. The other assumption generally made is that that the relationship between
the multiples and fundamentals is linear. Again, using PEG ratios to illustrate
the point, we are assuming that as growth doubles, the PE ratio will double; if
this assumption does not hold up and PE ratios do not increase proportional to
growth, companies with high growth rates will look cheap on a PEG ratio basis.

## 3. Statistical Techniques

            Subjective
adjustments and modified multiples are difficult to use when the relationship
between multiples and the fundamental variables that determine them becomes
complex. There are statistical techniques that offer promise, when this
happens. In this section, we will consider the advantages of these approaches
and potential concerns.

### Sector Regressions

In a regression, we attempt to explain a
dependent variable by using independent variables that we believe influence the
dependent variable. This mirrors what we are attempting to do in relative
valuation, where we try to explain differences across firms on a multiple (PE
ratio, EV/EBITDA) using fundamental variables (such as risk, growth and cash
flows). Regressions offer three advantages over the subjective approach:

if !supportListsa.     endifThe output from the regression gives us a
measure of how strong the relationship is between the multiple and the variable
being used. Thus, if we are contending that higher growth companies have higher
PE ratios, the regression should yield clues to both how growth and PE ratios
are related (through the coefficient on growth as an independent variable) and
how strong the relationship is (through the t statistics and R squared).

if !supportListsb.     endifIf the relationship between a multiple
and the fundamental we are using to explain it is non-linear, the regression
can be modified to allow for the relationship.

if !supportListsc.     endifUnlike the modified multiple approach,
where we were able to control for differences on only one variable, a
regression can be extended to allow for more than one variable and even for
cross effects across these variables.

In general, regressions seem particularly
suited to our task in relative valuation, which is to make sense of voluminous
and sometimes contradictory data. There are two key questions that we face when
running sector regressions:

if !supportLists�     
endifThe
first relates to how we define the sector. If we define sectors too narrowly,
we run the risk of having small sample sizes, which undercut the usefulness of
the regression. Defining sectors broadly entails fewer risks. While there may be
large differences across firms when we do this, we can control for those
differences in the regression.

if !supportLists�     
endifThe
second involves the independent variables that we use in the regression. While
the focus in statistics classes is increasing the explanatory power of the
regression (through the R-squared) and including any variables that accomplish
this, the focus of regressions in relative valuations is narrower. Since our
objective is not to explain away all differences in pricing across firms but
only those differences that are explained by fundamentals, we will use only those
variables that are related to those fundamentals. The last section where we
analyzed multiples using DCF models should yield valuable clues. As an example,
consider the PE ratio. Since it is determined by the payout ratio, expected
growth and risk, we will include only those variables in the regression. We
will not add other variables to this regression, even if doing so increases the
explanatory power, if there is no fundamental reason why these variables should
be related to PE ratios.

### Market Regression

            Searching
for comparable firms within the sector in which a firm operates is fairly
restrictive, especially when there are relatively few firms in the sector or
when a firm operates in more than one sector. Since the definition of a
comparable firm is not one that is in the same business but one that has the
same growth, risk and cash flow characteristics as the firm being analyzed, we
need not restrict our choice of comparable firms to those in the same industry.
The regression introduced in the previous section controls for differences on
those variables that we believe cause multiples to vary across firms. Based
upon the variables that determine each multiple, we should be able to regress
PE, PBV and PS ratios against the variables that should affect them. As shown in
the last section the fundamentals that determine each multiple are summarized in
table 7.5:

*Table 7.5: Fundamentals
Determining Equity Multiples*

|  |  |
| --- | --- |
| *Multiple* | *Fundamental Determinants* |

|  |  |
| --- | --- |
| Price Earnings Ratio | Expected Growth, Payout, Risk |
| Price to Book Equity Ratio | Expected Growth, Payout, Risk, ROE |
| Price to Sales Ratio | Expected Growth, Payout, Risk, Net Margin |

It is, however,
possible that the proxies that we use for risk (beta), growth (expected growth
rate in earnings per share), and cash flow (payout) may be imperfect and that
the relationship may not be linear. To deal with these limitations, we can add
more variables to the regression - e.g., the size of the firm may operate as a
good proxy for risk.

            The
first advantage of this market-wide approach over the �subjective� comparison
across firms in the same sector, described in the previous section, is that it
does quantify, based upon actual market data, the degree to which higher growth
or risk should affect the multiples. It is true that these estimates can contain
errors, but those errors are a reflection of the reality that many analysts
choose not to face when they make subjective judgments. Second, by looking at
all firms in the market, this approach allows us to make more meaningful
comparisons of firms that operate in industries with relatively few firms.
Third, it allows us to examine whether all firms in an industry are under- or
overvalued, by estimating their values relative to other firms in the market.

### Limitations of Statistical Techniques

            Statistical
techniques are not a panacea for research or for qualitative analysis. They are
tools that every analyst should have access to, but they should remain tools. In
particular, when applying regression techniques to multiples, we need to be
aware of both the distributional properties of multiples that we talked about
earlier in the chapter and the relationship among and with the independent
variables used in the regression.

if !supportLists�     
endifThe fact that multiples are not normally
distributed can pose problems when using standard regression techniques. These
problems are accentuated with small samples, where the asymmetry in the
distribution can be magnified by the existences of a few large outliers.

if !supportLists�     
endifIn a multiple regression, the independent
variables are themselves supposed to be independent of each other. Consider, however,
the independent variables that we have used to explain valuation multiples –
cash flow potential or payout ratio, expected growth and risk. Across a sector
and over the market, it is quite clear that high growth companies will tend to
be risky and have low payout. This correlation across independent variables
creates �multicollinearity� which can undercut the
explanatory power of the regression.

if !supportLists�     
endifEarlier in the chapter, we noted how much the
distributions for multiples changed over time, making comparisons of PE ratios
or EV/EBITDA multiples across time problematic. By the same token, a multiple regression
where we explain differences in a multiple across companies at a point in time
will itself lose predictive power as it ages. A regression of PE ratios against
growth rates in early 2005 may therefore not be very useful in valuing stocks
in early 2006.

if !supportLists�     
endifAs a final note of caution, the R-squared on
relative valuation regressions will almost never be higher than 70% and it is
common to see them drop to 30 or 35%. Rather than ask the question of how high
an R-squared has to be to be meaningful, we would focus on the predictive power
of the regression. When the R-squared decreases, the ranges on the forecasts
from the regression will increase. As an example, the beverage sector
regression (from illustration 7.3) yields a forecasted PE of 32.97 but the
R-squared of 51% generates a range of 27.11 to 38.83 for the forecast with 95%
accuracy; if the R-squared had been higher the range would have been tighter.

if !supportAnnotations 

---

 endif
