# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:05:18 2021

@author: user
"""

#108021016 林雨璇 3-4 SetTest.py

f = set(('r',5,'j',6)) #set排序
print(f)
f = set(['安安','你好','安安']) #set中的重複只會輸出1次
print(f)
f = set({'蘋果':'Pomme','香蕉':'banane'})
print(f)
f = set('08000985742') #set中的重複只會輸出1次
print(f)

f.add('g') #把g加進f裡面
print(f)
f.remove('0') #把0從f移除
print(f)

a = set('1234')
b = set('3456')
print(a|b) #輸出a和b的聯集
print(a&b) #輸出a和b的交集
print(a-b) #輸出a和b的差集
print(a^b) #輸出a和b的互斥

c = set('iphone')
d = set('iphone X')
print(c <= d) #輸出是否c的元素都存在於d中
print(c < d) #輸出是否c的元素都存在於d中，而且d有超過1個以上c沒有的元素
print(c >= d) #輸出是否d的元素都存在c於中
print(c > d) #輸出是否d的元素都存在於c中，而且c有超過1個以上d沒有的元素