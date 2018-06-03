# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:18:24 2018

@author: lenovo
"""

import urllib.request as r
city_pinyin=input("请输入城市拼音:")
url="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric"
info=r.urlopen(url.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)
import json
w=json.loads(info)

all_data=[]
for i in range(0,38,4):
    date=w["list"][i]["dt_txt"]
    temp=w["list"][i]["main"]["temp"]
    temp_max=w["list"][i]["main"]["temp_max"]
    temp_min=w["list"][i]["main"]["temp_min"]
    pressure=w["list"][i]["main"]["pressure"]
    test="日期"+str(date),"\n当前温度"+str(temp),"\n最高温度"+str(temp_max),"\n最低温度"+str(temp_min),"\n气压"+str(pressure)
    all_data.append(test)
print(all_data)
