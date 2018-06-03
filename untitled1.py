# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:48:49 2018

@author: lenovo
"""
import urllib.request as r
url="http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996"
info=r.urlopen(url.format("chengdou")).read().decode("utf-8","ignor")
print(url)
import json
w=json.loads(info)
w["weather"][0]["description"]
w["main"]["temp"]