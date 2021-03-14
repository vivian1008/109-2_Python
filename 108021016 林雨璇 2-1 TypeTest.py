# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 108021016 林雨璇 2-1 TypeTest.py

name = input('你叫什麼名字?') #輸入姓名到name
print('哦,你叫',name) #輸出姓名

str = "Hi"
a = True
b = 16
c = 6.24
print(str,type(str)) #顯示str的類別
print(a,type(a)) #顯示a的類別
print(b,type(b)) #顯示b的類別
print(c,type(c)) #顯示c的類別

print(int(20)) #顯示整數數值
print(int(20.5)) #顯示整數數值
print(int('1000',2)) #1000為2進位,轉換為十進位是8

print(float(45)) #顯示浮點數
print(float(43.45)) #顯示浮點數
print(float('43.4567')) #顯示浮點數

print(bool(1)) #顯示布林值
print(bool(0)) #顯示布林值

dd = 10**456 #10的456次方
print(dd)