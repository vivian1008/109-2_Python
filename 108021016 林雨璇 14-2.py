# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 14:03:35 2021

@author: 林
"""
#108021016 林雨璇 14-2.py
import requests
import json

url = 'https://quality.data.gov.tw/dq_download_json.php?nid=9617&md5_url=fc93547438b2106ccec5f9b6b112c0bd'
#上面是高級中等學校科別資料網址    

result = requests.get(url) #讀取網頁資料
data = json.loads(result.text) #轉換為python字典

print(data)


boy1 = 0   # 一年級男學生數 
girl1 = 0  # 一年級女學生數 
boy2 = 0   # 二年級男學生數 
girl2 = 0  # 二年級女學生數 
boy3 = 0   # 三年級男學生數 
girl3 = 0  # 三年級女學生數 

for item in data:  #讀取資料和計算人數
  if item['縣市名稱'] == '臺北市' or item['縣市名稱'] == '臺中市' or item['縣市名稱'] == '臺南市' or item['縣市名稱'] == '高雄市':
      print(item['縣市名稱'])
      boy1 += int(item['一年級男學生數'])
      girl1 += int(item['一年級女學生數'])
      boy2 += int(item['二年級男學生數'])
      girl2 += int(item['二年級女學生數'])
      boy3 += int(item['三年級男學生數'])
      girl3 += int(item['三年級女學生數'])
      
print("4市男生總數=", boy1+boy2+boy3, '4市女生總數=', girl1+girl2+girl3) 
