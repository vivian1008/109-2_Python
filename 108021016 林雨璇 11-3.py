# -*- coding: utf-8 -*-
"""
Created on Sat May 29 13:11:02 2021

@author: 林
"""
#108021016 林雨璇 11-3.py
import re 

a = '床前明月光，疑是地上霜，舉頭望明月，低頭思故鄉。' 
c = '012958664、555476'
e = 'I am Ironman'
g = 'xyxyzzz'

b = re.findall('^床前', a) #開頭是否為'床前'
print(b)
b1 = re.findall('思故鄉。$', a) #結尾是否為'思故鄉。'
print(b1)
b2 = re.findall('是地.', a) #接'是地'後面的字元
print(b2)
b3 = re.findall('頭|明', a) #列出含有'頭'、'明'的字元
print(b3)
b4 = re.findall('[故舉低]', a) #按順序列出'舉'、'低'、'故'
print(b4)
b5 = re.findall('[^上明]', a) #列出'上'跟'明'以外的字元
print(b5)
b6 = re.findall('[望上]*', a) #列出'上'和'望'其他字元用''取代
print(b6)
b7 = re.findall('[望上]*?', a) #真不懂在幹嘛
print(b7)
b8 = re.findall('[望上]+', a) #列所有的'望'和'上'，越多越好
print(b8)
d = re.findall('[0-9]+',c) #列出字串的數字
print(d)
f = re.findall('[A-Za-z]+', e) #列出英文，以空格為間隔
print(f)
b9 = re.findall('[望上]+?', a) #也是列出越多'望'跟'上'之類的
print(b9)
h = re.findall('z{3}', g) #列出連續3個z
print(h)
h1 = re.findall('y{1,2}', g) #列1到2個y，越多越好
print(h1)
h2 = re.findall('z{2,3}?', g) #列出連續2-3的z，越少越好
print(h2)
b11 = re.findall('思(?=故鄉)', a) #思右邊是故鄉
print(b11)
b12 = re.findall('思(?!故鄉)', a) #思右邊不是故鄉
print(b12)
b13 = re.findall('(?<=地)上霜', a) #上霜左邊是地
print(b13)
b14 = re.findall('(?<!地)上霜', a) #上霜左邊不是地
print(b14)
