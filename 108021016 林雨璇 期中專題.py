# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 21:41:35 2021

@author: 林
"""
#108021016 林雨璇 期中專題
import random

account = input('請輸入要註冊的帳號(4個字元以上，且包含英文字母及數字)') #讓使用者輸入要註冊的帳號
password = input('請輸入要註冊的密碼(6個字元以上，且同時包含1個大寫字母、一個小寫字母及1個數字，可以使用特殊字元)') #讓使用者輸入要註冊的密碼
while len(account) < 4:  #當註冊帳號的長度小於4
    account = input('帳號長度過短，請加長') #輸出長度過短，並且請使用者修改
while len(password) < 6: #當註冊密碼的長度小於6   
    password = input('密碼長度過短，請加長') #輸出長度過短，並且請使用者修改
for i in range('A','Z'+1): #for迴圈從A到Z
    if i not in account: #如果帳號裡不包含A到Z
         account = input('帳號中未包含英文字母，請修改') #輸出未包含字母，請使用者修改
for n in range('a','z'+1): #for迴圈從a到z
    if n not in account: #如果帳號裡不包含a到z
         account = input('帳號中未包含英文字母，請修改') #輸出未包含字母，請使用者修改
for j in range(0,10): #for迴圈從0到9
    if j not in account: #如果帳號裡不包含0到9
         account = input('帳號中未包含數字，請修改') #輸出未包含數字，請使用者修改
for k in range('A','Z'+1): #for迴圈從A到Z
    if k not in password: #如果密碼裡不包含A到Z
         password = input('密碼中未包含大寫字母，請修改') #輸出未包含大寫字母，請使用者修改
for l in range('a','z'+1): #for迴圈從a到z
    if l not in password: #如果密碼裡不包含a到z
         password = input('密碼中未包含小寫字母，請修改') #輸出未包含小寫字母，請使用者修改
for m in range(0,10): #for迴圈從0到9
    if m not in password: #如果密碼裡不包含0到9
         password = input('密碼中未包含數字，請修改') #輸出未包含數字，請使用者修改

s = account #將使用者帳號存入s
ss = password #將使用者密碼存入ss
at = open('account.txt','xt',encoding='utf-8') #打開檔案
at.write(s) #寫入使用者的帳號
at.write(ss) #寫入使用者的密碼
at.close() #關閉檔案    
        
idd = input('請輸入帳號') #請使用者輸入帳號
pd = input('請輸入密碼') #請使用者輸入密碼
    
if idd != account or pd != password: #如果帳號或密碼與註冊的不相同
    print('帳號或密碼錯誤,再輸入一次') #輸出帳號或密碼錯誤
    idd = input('請輸入帳號') #讓使用者再輸入一次帳號
    pd = input('請輸入密碼') #讓使用者再輸入一次密碼
elif idd == account and pd == password: #如果帳號或密碼與註冊的相同
    print('登入成功!') #輸出登入成功
    a = [0,1,2,3,4,5,6,7,8,9] #list儲存數字0到9
    random.shuffle(a) #從a隨機挑數字
for n in range(0,4): 
    
    print(random.choice(a),end='')
    
answer = input('輸入答案') #讓使用者輸入猜的答案
count = 0 #計算使用者猜的次數
if answer == random.choice(a): #如果猜到答案
    count+1 #次數加一
    print('猜中了!猜了',count,'次') #輸出答對了，且輸出答了幾次
elif answer != random.choice(a): #如果猜錯
    
    
    