---
title: "uValue for iPad/iPhone&amp;iTouch"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/uValue.html
---

uValue for iPad/iPhone&iTouch 
 <!-- body {
font: 100% Verdana, Arial, Helvetica, sans-serif;
background: #666666;
margin: 0; /\* it's good practice to zero the margin and padding of the body element to account for differing browser defaults \*/
padding: 0;
text-align: center; /\* this centers the container in IE 5\* browsers. The text is then set to the left aligned default in the #container selector \*/
color: #000000;
}
.twoColHybRtHdr #container { width: 1000px; /\* this will create a container 80% of the browser width \*/
background: #FFFFFF;
margin: 0 auto; /\* the auto margins (in conjunction with a width) center the page \*/
border: 1px solid #000000;
text-align: left; /\* this overrides the text-align: center on the body element. \*/
} .twoColHybRtHdr #header { background-image: url('uValueImg/topbar.jpg'); background-repeat:repeat-x;background: #DDDDDD; padding: 0 10px; /\* this padding matches the left alignment of the elements in the divs that appear beneath it. If an image is used in the #header instead of text, you may want to remove the padding. \*/
} .twoColHybRtHdr #header h1 {
margin: 0; /\* zeroing the margin of the last element in the #header div will avoid margin collapse - an unexplainable space between divs. If the div has a border around it, this is not necessary as that also avoids the margin collapse \*/
padding: 10px 0; /\* using padding instead of margin will allow you to keep the element away from the edges of the div \*/
}
/\* Tips for sidebar1:
1. Since we are working in relative units, it's best not to use padding on the sidebar. It will be added to the overall width for standards compliant browsers creating an unknown actual width. 2. Since em units are used for the sidebar value, be aware that its width will vary with different default text sizes.
3. Space between the side of the div and the elements within it can be created by placing a left and right margin on those elements as seen in the ".twoColHybRtHdr #sidebar1 p" rule.
\*/
.twoColHybRtHdr #sidebar1 {
float: right; width: 200px; /\* since this element is floated, a width must be given \*/
background: #EBEBEB; /\* the background color will be displayed for the length of the content in the column, but no further \*/
padding: 15px 0; /\* top and bottom padding create visual space within this div \*/
}
.twoColHybRtHdr #sidebar1 h3, .twoColHybRtHdr #sidebar1 p {
margin-left: 10px; /\* the left and right margin should be given to every element that will be placed in the side columns \*/
margin-right: 10px;
}
/\* Tips for mainContent:
1. The space between the mainContent and sidebar1 is created with the right margin on the mainContent div. No matter how much content the sidebar1 div contains, the column space will remain. You can remove this right margin if you want the #mainContent div's text to fill the #sidebar1 space when the content in #sidebar1 ends.
2. Be aware it is possible to cause float drop (the dropping of the non-floated mainContent area below the sidebar) if an element wider than it can contain is placed within the mainContent div. WIth a hybrid layout (percentage-based overall width with em-based sidebar), it may not be possible to calculate the exact width available. If the user's text size is larger than average, you will have a wider sidebar div and thus, less room in the mainContent div. You should be aware of this limitation - especially if the client is adding content with Contribute.
3. In the Internet Explorer Conditional Comment below, the zoom property is used to give the mainContent "hasLayout." This may help avoid several IE-specific bugs.
\*/
.twoColHybRtHdr #mainContent {
margin: 0 210px 0 10px; /\* the left margin's value is equal to the header and footer which creates alignment down the left side of the document. \*/
} .twoColHybRtHdr #footer { padding: 0 10px; /\* this padding matches the left alignment of the elements in the divs that appear above it. \*/
background:#DDDDDD;
} .twoColHybRtHdr #footer p {
margin: 0; /\* zeroing the margins of the first element in the footer will avoid the possibility of margin collapse - a space between divs \*/
padding: 10px 0; /\* padding on this element will create space, just as the the margin would have, without the margin collapse issue \*/
}
/\* Miscellaneous classes for reuse \*/
.fltrt { /\* this class can be used to float an element right in your page. The floated element must precede the element it should be next to on the page. \*/
float: right;
margin-left: 8px;
}
.fltlft { /\* this class can be used to float an element left in your page \*/
float: left;
margin-right: 8px;
}
.clearfloat { /\* this class should be placed on a div or break element and should be the final element before the close of a container that should fully contain a float \*/
clear:both;
height:0;
font-size: 1px;
line-height: 0px;
}
--> 

|  |  |  |
| --- | --- | --- |
| [uValue](http://itunes.apple.com/us/app/uvalue/id440046276) | (function() { var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true; po.src = 'https://apis.google.com/js/plusone.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s); })(); |  |

 uValue | uValue | [uValue](http://itunes.apple.com/us/app/uvalue-mobile/id492586911) |

  

# uValue: The Corporate Valuation App

### About its creators

[Aswath
Damodaran](http://www.stern.nyu.edu/faculty/bio/aswath-damodaran) is a professor
of
Finance at the Stern School of Business, New York University.

[Anant
Sundaram](http://faculty.tuck.dartmouth.edu/anant-sundaram/) is a professor
of
Finance at the Tuck School of Business at Dartmouth.

Anant
and Aswath teach
valuation and corporate finance classes to MBAs and executives.

Ally Mahmoud(D’20), a Computer Science major from Dartmouth College, provided outstanding software development services. The original software development was done by Xiandong Ren, Jianfeng Huo, and Yuting Cheng, all graduates of the Computer Science programs at Dartmouth.

 ©
2011 - 2020 Damodaran & Sundaram. All Rights Reserved

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

# About this app

**uValue**
is a corporate
valuation
app
for the iPad and the iPhone. The
app helps you value
businesses
using
conceptually rigorous,
yet practical, widely-used
tools. You can value firms
using  the ‘weighted
average cost of capital’ (WACC, or 'cost of capital')
approach,
the ‘adjusted present value’ (APV)
approach, the ‘dividend
growth
model’ (DGM), or
real option
valuation (ROV) techniques. The app also includes a set of handy
calculators to value bonds, annuities and perpetuities, as well as to
calculate the cost of capital, to forecast exchange rates, to
lever/unlever betas, and so forth.

The
app
is free. We want anyone
who is keen to do a good valuation, anywhere, to have access to
self-contained, fully-functional tools to do so. Time and again, we see
that poor investment decisions start with poor valuations.
Consequently, **uValue**
is fundamentally educational in its intent — it comes with
three important features: pop-up boxes that define and explain every
input or concept, a *uValue
Companion*
that is a mini-textbook on valuation, and links to a data set that give
you industry data benchmarks.

**uValue**
presumes basic familiarity with financial statements. With the WACC and
the APV models, you can also choose between 'Detailed' or 'Simple'
versions. (There is a section that walks you through how to make
choices if you're not sure.) You do have to agree to a disclaimer
within the app before you can use it.

We
hope you have fun with **uValue**,
and enjoy using it!

# iPad App details

1. *Latest
   version*: uValue 4.0.2, last updated June 2020 (now iOS 13 compatible).
2. Rating:
   4+
3. Price:
   Free
4. Primary category:
   Finance
5. Secondary category:
   Business
6. Support email: [uValueapp@gmail.com](mailto:uValueapp@gmail.com)

# iPhone/iPod Touch App details

1. *Latest
   version*: uValueMobile 4.0.2, last uploaded June 2020 (now iOS 13 compatible).
2. Rating:
   4+
3. Price:
   Free
4. Primary category:
   Finance
5. Secondary category:
   Business
6. Support email: [uValueapp@gmail.com](mailto:uValueapp@gmail.com)

# Errata and corrections

Much
as we have tried to dot every 'i' and cross every 't', it is possible
that glitches remain. (Do let us know if/as/when you find them. Thanks
in advance!). 

Since
we will offer app updates every once in a while, when we do find
errors, we will post suggested corrections (as well as ways to work
around them) in the section [Errata
& Corrections](errata.html) (see tab
above).

  
  
  

uValue
