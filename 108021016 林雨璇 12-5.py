# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:20:58 2021

@author: 林
"""
#108021016 林雨璇 12-5.py
import pickle #模組pickle

a = open('poem.txt','rt',encoding='utf-8') #讀取poem文字檔
b = a.read()
print(b) #輸出內容
a.close()

c = '昔人已乘黃鶴去，此地空余黃鶴樓。黃鶴一去不復返，白雲千載空悠悠'
with open('poem.bin','wb') as fout: #開poem為二進位模式
    pickle.dump(c,fout) #把詩寫進二進位檔
with open('poem.bin','rb') as fin:
    d = pickle.load(fin) #把二進位檔讀出 
    print(d)
    