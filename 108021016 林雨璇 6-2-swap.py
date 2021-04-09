# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:49:36 2021

@author: ASIA-H607
"""

#108021016 林雨璇 6-2-swap.py
def swap(a,b): #函式
    if a > b: #如果a大於b
        c = a #先用c把a的值存起來
        a = b #b的質移到a
        b = c #把原本a的值移到b
        print(a,b) #先輸出小的，再輸出大的
    else:
        print(a,b) #本來就比較小的話就直接輸出
        
m = int(input('輸入一個數')) #讓使用者輸入第一個數
n = int(input('輸入一個數')) #讓使用者輸入第二個數
swap(m,n) #套入函式
