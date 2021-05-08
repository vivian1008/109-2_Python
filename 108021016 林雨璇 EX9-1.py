# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#108021016 林雨璇 EX9-1.py
class rectangle():  #建立矩形的類別
    def __init__(self,name): 
        self.name = name
def area(a,b): #計算矩形面積的函式
    return a*b

w = rectangle('寬度') #宣告矩形的物件:寬度
h = rectangle('高度') #宣告矩形的物件:高度
print(w.name)
print(h.name)
w = 6  #設定寬度為6
h = 8 #高度為8
print(w) #輸出寬度
print(h) #和高度
print('面積為',area(h,w)) #最後輸出面積
        