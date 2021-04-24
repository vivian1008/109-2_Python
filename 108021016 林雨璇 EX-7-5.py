# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 15:43:06 2021

@author: 林
"""

#108021016 林雨璇 EX-7-5.py
t = ['Tell me and I forget. Teach me and I remember.' 'Involve me and I learn.','A pessimist is one who makes difficulties of his opportunities and an optimist is one who makes opportunities of his difficulties.','Always remember that you are absolutely unique.',' Just like everyone else.']
#t是題目的文字內容
A = open('motto1.txt','wt',encoding='utf-8') #打開文字檔，寫入文字檔
for line in t: #取文字內容
  print(line,file=A)  #用print寫入檔案
A.close() #close把資料完全寫入檔案

A = open('motto1.txt','rt',encoding='utf-8') #打開文字檔，讀出文字檔
a = A.read() #讀取整個文字檔
print(a)  #輸出
A.close() #關檔

B = open('motto2.txt','wt',encoding='utf-8') #打開文字檔，寫入文字檔
for line in t: #取文字內容
        print(str.upper(line),file=B) #用print寫入檔案，且用upper改成全部大寫
B.close() #close把資料完全寫入檔案      

B = open('motto2.txt','rt',encoding='utf-8') #打開文字檔，讀出文字檔
b = B.read() #讀取整個文字檔
print(b)  #輸出
B.close() #關檔
