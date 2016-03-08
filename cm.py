#!/usr/bin/python
import urllib2
import base64
import json
import datetime
import math

## Edit lines 11 & 12
## Find your ChartMogul API Token and Secret key at https://app.chartmogul.com/#admin/api
###################################
username="CHARTMOGUL_API_TOKEN"
password="CHARTMOGUL_SECRET_KEY"
###################################


today=datetime.date.today().strftime("%Y-%m-%d")
yesterday=datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime("%Y-%m-%d")

base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

headers = {"Authorization" : "Basic %s" % base64string}
url = "https://api.chartmogul.com/v1/metrics/all?start-date="+yesterday+"&interval=day&end-date="+today

request = urllib2.Request(url, headers=headers)

contents = urllib2.urlopen(request).read()

jsonData = json.loads(contents)

for item in jsonData["entries"]:
    mrr = item.get("mrr")
    arpa = item.get("arpa")
    ltv = item.get("ltv")
    customers = item.get("customers")
    arr = item.get("arr")
    asp = item.get("asp")

def monetize( data ):
	if data:
		a = str(data)
		if "." in a:
			b = math.modf(data)
			c = str(b[1]).replace(" ", "")[:-4].upper()
			d = '${:,.2f}'.format(int(c)).replace(' ', '')[:-3].upper()
			return d
		else:
			b = a.replace(' ', '')[:-2].upper()
			c = '${:,.2f}'.format(int(b)).replace(' ', '')[:-3].upper()
			return c
	else:
		return data

print "ChartMogul"
print "---"
print "MRR: ", monetize(mrr)
print "LTV: ", monetize(ltv)
print "Customers: ", customers
print "ARR: ", monetize(arr)
print "ARPA: ", monetize(arpa)