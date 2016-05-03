# coding:utf-8
import urllib
import urllib2

url = "http://127.0.0.1:5000/set_gps"
lat = 123
lng = 456
params = {"lat":lat,"lng":lng}
params = urllib.urlencode(params)

reqest = urllib2.Request(url)

print reqest

reqest.add_data(params)

res = urllib2.urlopen(reqest)
r = res.lead(reqest)
print res
