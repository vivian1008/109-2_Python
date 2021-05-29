# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#108021016 林雨璇 11-1.py
import re #re模組

s = '哈囉你好嗎?衷心感謝，珍重再見，期待再相逢。' #自訂的string
p = input('輸入想搜尋的字串:') #讓使用者輸入pattern
a = re.search(p, s) #搜尋字串
b = re.match('哈囉', s) #開頭是否為哈囉
b2 = re.match('衷心', s) #開頭是否為衷心
c = re.findall('珍重', s) #找字串裡所有符合'珍重'的字串
d = re.split('，', s) #用逗號進行分割字串
e = re.sub('，','.' , s) #把字串中的逗號用'.'替代
print(b)
print(b2)
print(c)
print(d)
print(e)
count = 0 #設一個數字讓使用者可以重複輸入
while count == 0:
    if a: #如果有找到匹配的字串
        print(a.group()) #輸出找到的字串
        p = input('輸入想搜尋的字串:')
        a = re.search(p, s)
    elif p == '###': #如果使用者輸入###
        count+1 #跳出while
        break #停止
    else: #如果找不到
        print('找不到',p) #輸出找不到這個字串 
        p = input('輸入想搜尋的字串:')
        a = re.search(p, s)
    