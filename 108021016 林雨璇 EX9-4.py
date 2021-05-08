# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:09:26 2021

@author: ASIA-H607
"""

#108021016 林雨璇 EX9-4.py
class rectangle():  #建立矩形的類別
    def __init__(self,w,h):  #宣告矩形的物件:高度和寬度
        self.width = w
        self.hight = h
    def area(self): #計算矩形面積的函式
        return self.width * self.hight
class square(rectangle): #正方形繼承矩形
    def __init__(self,l): #宣告正方形的物件:邊長
        self.len = l
        super().__init__(self.len,self.len)
    def area(self): #正方形的類別重新定義面積函式
        return self.len * self.len
    def perimeter(self): #新增方法計算正方形週長
        return 4 * self.len

i = square(33) #設定邊長為33
print('正方形週長為',i.perimeter()) #輸出正方形週長
