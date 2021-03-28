# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 108021016 林雨璇 5-1 alphabet.py


for i in range(ord('A'),ord('Z')+1): #用ord找出字母的ASCII碼，然後用迴圈讓它跑出大寫的26個字母
    print(chr(i),end='') #印出大寫字母，用end=''讓它不要換行
for i in range(ord('a'),ord('z')+1):#用ord找出字母的ASCII碼，然後用迴圈讓它跑出小寫的26個字母
    print(chr(i),end='') #印出小寫字母，用end=''讓它不要換行
    