Title: [How-To][Android] Disable Opening Local File in Browser in custom ROM
Date: 2012-09-25 21:52
Author: kmonsoor
Category: configuration
Slug: how-to-disable-opening-local-file-in-browser-in-custom-rom
Status: draft

<span id="GRmark_2a31fabdfcc49daf26b691bf583a89a8752d2112_open:0"
class="GRcorrect">open</span> .<span
id="GRmark_2a31fabdfcc49daf26b691bf583a89a8752d2112_.:1"
class="GRcorrect">.</span>/.<span
id="GRmark_2a31fabdfcc49daf26b691bf583a89a8752d2112_.:2"
class="GRcorrect">.</span>/<span
id="GRmark_2a31fabdfcc49daf26b691bf583a89a8752d2112_base:3"
class="GRcorrect">base</span>/core/<span
id="GRmark_2a31fabdfcc49daf26b691bf583a89a8752d2112_java:4"
class="GRcorrect">java</span>/<span
id="GRmark_2a31fabdfcc49daf26b691bf583a89a8752d2112_android:5"
class="GRcorrect">android</span>/<span
id="GRmark_2a31fabdfcc49daf26b691bf583a89a8752d2112_webkit:6"
class="GRcorrect">webkit</span>/WebSettings.java file

Set the following values to FALSE:

-   mAllowUniversalAccessFromFileURLs
-   mAllowFileAccessFromFileURLs

