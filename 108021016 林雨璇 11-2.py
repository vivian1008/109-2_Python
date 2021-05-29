# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:41:07 2021

@author: 林
"""

#108021016 林雨璇 11-2.py
import string #模組string
import re #模組re

a = string.printable #a為string能印出的所有字元

print(re.findall('\d', a)) #只印出數字
print(re.findall('\D', a)) #數字以外的字元
print(re.findall('\s', a)) #空白字玩
print(re.findall('\S', a)) #非空白字元
print(re.findall('\w', a)) #英文、數字或底線字元，或中文字元
print(re.findall('\W', a)) #非英文、數字或底線字元，也可以是中文的標點符號
print(re.findall('\b', a)) #\w跟\W的邊界
print(re.findall('\B', a)) #不在\w跟\W的邊界
