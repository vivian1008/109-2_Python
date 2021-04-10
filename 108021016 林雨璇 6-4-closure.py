# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:11:47 2021

@author: 林
"""

#108021016 林雨璇 6-4-closure.py
def fun(name): #寫第一個函式
    def fun2(money): #內部函式
        return name+money #回傳name跟money
    return fun2 #回傳fun2
x = fun('Jack') #name為Jack
y = fun('Rose') #name為Rose
print(x(',存款有500元')) #輸出name和money
print(y(',存款有1000萬元')) #輸出name和money
