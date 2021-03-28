# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:26:31 2021

@author: user
"""
#108021016 林雨璇 5-Prime.py

n = int(input('輸入一個數')) #讓使用者輸入一個數
i = 2

while i < n: #當i小於n
    if(n % i == 0): #如果n可以整除i
        print('不是質數') #就不是質數
        break #中斷迴圈
    i+=1 #i遞增1
else: #如果沒有可以整除的數
    print('是質數') #就是質數
    
        