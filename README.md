# ChartMogul Menu Bar
Get your ChartMogul metrics in your Mac OS X Menu Bar.
-------------------

![](http://i.imgur.com/kvdQKWF.png)

## Installation instructions

1. Download
	
	BitBar is the app we'll use to add your metrics to your Menu Bar
	
	a) [Download BitBar](https://github.com/matryer/bitbar/releases/download/v1.5.0-beta2/BitBar.v1.5-beta2.zip)
	
	b) [Download ChartMogul plugin](https://github.com/bilbof/chartmogul-menu/archive/master.zip)

2. Add ChartMogul API keys

	You can find your ChartMogul API Token and Secret Key at https://app.chartmogul.com/#admin/api (admin permissions required).

	a) Open the chartmogul-menu Zip file downloaded in step 1b, open the cm.py file in the chartmogul-menu folder with a text editor (e.g. TextEdit, Sublime Text 2, Atom).

	b) Add your ChartMogul API Token and Secret Key to lines 6 & 7 of cm.py.

3. Run the app

	a) Open the Zip file downloaded in step 1a, then open the BitBar app.

	b) In your Mac OS X Menu Bar, click *BitBar > Preferences > Change Plugin folder...*, then select the 'chartmogul-menu' folder. This should start the app. If this doesn't start the app restart BitBar.