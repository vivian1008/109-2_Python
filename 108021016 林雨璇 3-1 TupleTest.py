# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#108021016 林雨璇 3-1 TupleTest.py

t1 = (5,1,3)
t2 = (t1,4,7,8)
a,b,c = t1
print(a,b,c) #輸出t1結果
a,b,c = c,a,b
print(a,b,c) #輸出交換的結果
print(t2) #輸出t2結果
print(len(t1)) #輸出結果長度
print(t1[0]) #輸出結果第一位

t3 = (9,)
print(t3)
