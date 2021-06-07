# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:10:17 2021

@author: 林
"""
#108021016 林雨璇 12-2.py
import os,glob #模組os跟glob

a = 'C:\\Users\林\Desktop\py' #要計算的資料夾路徑

def find (dir): #遞迴函式列出資料夾和py檔
    d = 0 #計算資料夾的數量
    e = 0 #計算py檔的數量
    bs = os.listdir(dir) #取得指定路徑資料夾的內容
    for b in bs:
        c = os.path.join(dir, b)
        if os.path.isdir(c): #是資料夾的話，d加一
            print('資料夾:',c)
            d+=1
            print('有',d,'個資料夾') #輸出有幾個資料夾

    for g in glob.glob("*.py"): #是py檔的話，e加一
            print('py檔:',g)
            e+=1
            print('有',e,'個py檔') #輸出有幾個py檔
find(a)
