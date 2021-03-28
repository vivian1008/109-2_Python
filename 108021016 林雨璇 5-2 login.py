# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:59:54 2021

@author: ASIA-H607
"""

#108021016 林雨璇 5-2 login.py

ad = input('輸入帳號') #讓使用者輸入帳號註冊
pd = input('輸入密碼') #讓使用者輸入密碼註冊
t = 0 #等下用來計算使用者輸入的次數

en1 = input('輸入你的帳號') #讓使用者輸入帳號登入
en2 = input('輸入你的密碼') #讓使用者輸入密碼登入

while t < 2 : #當輸入次數沒超過3次
    if en1 == ad and en2 == pd: #如果帳號密碼輸入正確
        print('登入成功') #輸出登入成功
        break #結束程式
    elif en1 != ad or en2 != pd: #如果帳號或密碼輸入不正確
        print('帳號或密碼錯誤,再輸入一次') #讓使用者再輸入一次
        en1 = input('輸入你的帳號')
        en2 = input('輸入你的密碼')
        t = t + 1 #輸入次數加1
else: #輸入三次
        print('連續三次錯誤，系統暫停使用') #三次就不能再輸入了
        
 
    
    
    