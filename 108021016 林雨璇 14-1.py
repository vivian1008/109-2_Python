# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#108021016 林雨璇 14-1.py
import urllib.request as ur
url='https://www.asia.edu.tw/' #亞大學校網站
resp=ur.urlopen(url) #打開亞大學校網站，回傳urllib.response物件
print(resp.geturl()) #讀取物件的網址
print(resp.status) #伺服器回傳的網頁狀態碼
print(resp.getheaders()) #讀取網頁表頭
data=resp.read() #要讀取資料，資料會轉為byte
print(data)
print(data.decode()) #用decode轉字串

import requests
url = 'https://www.asia.edu.tw/'
data = requests.get(url) #開啟url指定網頁
print(data.encoding) #網頁編碼
print(data.status_code) #網頁狀態
print(data.headers) #網頁表頭
print(data.text) #網頁內容
