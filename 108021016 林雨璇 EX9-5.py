# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#108021016 林雨璇 EX9-5.py
class rectangle(): #建立矩形的類別
    def __init__(self,w,h): #宣告矩形的物件:高度和寬度
        self.w = w
        self.h = h
    def area(self): #計算矩形面積的函式
        return self.w * self.h
    def __eq__(self, other): #相等的特殊方法
        return self._area == other.show_area()
    def __gt__(self, other): #大於的特殊方法
        return self._area > other.show_area()
    def __lt__(self, other): #小於的特殊方法
        return self._area < other.show_area()
        
class square(rectangle): #正方形繼承矩形
    def __init__(self,l):
        self.l = l
        super().__init__(self.l,self.l)
    def area(self): #計算正方形面積的函式
        return self.l * self.l


a = rectangle(50,80) #設定矩形高度為50，寬度為80
b = square(90) #設定正方形邊長為90

print(a.area() == b.area()) #輸出矩形面積是否等於正方形面積
print(a.area() < b.area()) #輸出矩形面積是否小於正方形面積
print(a.area() > b.area()) #輸出矩形面積是否大於正方形面積

if a.area() == b.area(): #如果面積相同
    print('兩個面積一樣') #輸出面積一樣
elif a.area() > b.area(): #如果矩形面積大於正方形面積
    print('矩形面積比正方形面積大') #輸出矩形面積比較大   
else: #如果矩形面積小於正方形面積
    print('矩形面積比正方形面積小') #輸出矩形面積比較小
      