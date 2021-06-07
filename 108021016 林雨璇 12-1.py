# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 13:40:05 2021

@author: 林
"""
#108021016 林雨璇 12-1.py
import os #模組os

print(os.getcwd()) #輸出現在所在的資料夾
os.chdir('c:\\Program Files') #更改路徑到C槽的Program Files資料夾
print(os.getcwd()) #確認有更改到
print(os.listdir('c:\\Program Files')) #輸出這個資料夾裡的資料夾和檔案
a = 0 #用來計算檔案數量
b = 0 #用來計算資料夾數量
cs = os.listdir('c:\\Program Files') #取得C槽的Program Files資料夾裡的所有東西
for c in cs:
    if os.path.isdir(c): #是資料夾的話，b就加一
        b+=1        
    else: #檔案的話，a加一
        a+=1      
print('資料夾有',b,'個') #輸出有幾個資料夾
print('檔案有',a,'個') #輸出有幾個檔案
