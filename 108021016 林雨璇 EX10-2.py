# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:01:43 2021

@author: 林
"""

#108021016 林雨璇 EX10-2.py
str = '雨' 
cd = str.encode('utf-8') #用utf-8編碼
st = cd.decode('utf-8') #用utf-8解碼
print(cd) #輸出utf-8編碼
print(st) #輸出解碼

cd2 = str.encode('unicode-escape') #用unicode編碼
st2 = cd2.decode('unicode-escape') #用unicode解碼
print(cd2) #輸出unicode編碼
print(st2) #輸出解碼