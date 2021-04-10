# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:27:00 2021

@author: 林
"""

#108021016 林雨璇 6-5-gcd.py
def gcd(a,b): #判斷最大公因數的函式
    if a % b == 0: #如果a能被b整除
        print('最大公因數是:',b) #最大公因數就是b
    else: #否則
        return gcd(b, a % b) #把比較小的數跟a除以b的餘數再做一次判斷
    
m = int(input('輸入比較大的那個數')) #讓使用者輸入比較大的那個數
n = int(input('輸入比較小的那個數')) #讓使用者輸入比較小的那個數
gcd(m,n)   #套入函式
