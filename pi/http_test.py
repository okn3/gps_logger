#coding:utf-8
import requests
url = "http://127.0.0.1:5000/api/set/gps"
lat = 888
lng = 888
data = {'lat':lat,'lng':lng}
r = requests.post(url, data=data)
print r
