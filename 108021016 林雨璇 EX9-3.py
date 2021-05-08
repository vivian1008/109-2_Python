# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:42:08 2021

@author: ASIA-H607
"""

#108021016 林雨璇 EX9-3.py
class rectangle():  #建立矩形的類別
    def __init__(self,name): 
        self.name = name
    def area(self):
        pass
class square(rectangle): #正方形繼承矩形
    def __init__(self,name):    
        super().__init__('正方形' + name)
    def area(self): #正方形的類別重新定義面積函式
        return '361'

I = square('邊長')  #宣告正方形的物件:邊長  
print(I.name,end='')
i = 19 #設定邊長為19
print(i)
print('面積為',I.area()) #輸出正方形面積
