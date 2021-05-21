# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:43:09 2021

@author: 林
"""

#108021016 林雨璇 EX9-8.py

try:
    x = int(input('輸入一個整數'))
    y = int(input('輸入一個整數'))
    print(x/y)
except ValueError as e: #輸入的值不是整數的話
    print('輸入的不是整數',e)
except ZeroDivisionError as e: #分母為零的話
    print('不能除以0啦',e)    
except Exception as e: 
    print('發生其他種類的錯誤',e)
else: #程式執行正確的話
    print('沒錯')
finally: #程式不管對不對都會執行
    print('不管怎樣都會執行這裡，puipui')    