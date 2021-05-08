# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:17:14 2021

@author: ASIA-H607
"""

#108021016 林雨璇 EX9-2.py
class rectangle():  #建立矩形的類別
    def __init__(self,name): 
        self.name = name
        
class square(rectangle): #正方形繼承矩形
    def __init__(self,name):
      super().__init__('正方形' + name)

def area(a,b): #計算正方形面積的函式
    return a*b    
    
i = square('邊長') #宣告正方形的物件:邊長
print(i.name,end='')
i = 15 #設定邊長為15
print(i)
print('面積為',area(i,i)) #輸出正方形面積
        