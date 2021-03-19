# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:43:06 2021

@author: ASIA-H607
"""

#108021016 林雨璇 4-5star_sign.py

mon = int(input('你的生日月份?')) #使用者輸入月份
day = int(input('你的生日日期?')) #使用者輸入日期

if (mon == 3 and day > 20) or (mon == 4 and day < 20): #如果生日在3/21~4/19之間
    print('牡羊座') #輸出牡羊座
elif(mon == 4 and day > 19) or (mon == 5 and day < 21): #如果生日在4/20~5/20之間
    print('金牛座') #輸出金牛座
elif(mon == 5 and day > 20) or (mon == 6 and day < 22): #如果生日在5/21~6/21之間
    print('雙子座') #輸出雙子座
elif(mon == 6 and day > 21) or (mon == 7 and day < 23): #如果生日在6/22~7/22之間
    print('巨蟹座') #輸出巨蟹座
elif(mon == 7 and day > 22) or (mon == 8 and day < 23): #如果生日在7/23~8/22之間
    print('獅子座') #輸出獅子座
elif(mon == 8 and day > 22) or (mon == 9 and day < 23): #如果生日在8/23~9/22之間
    print('處女座') #輸出處女座
elif(mon == 9 and day > 22) or (mon == 10 and day < 24): #如果生日在9/23~10/23之間
    print('天秤座') #輸出天秤座
elif(mon == 10 and day > 23) or (mon == 11 and day < 22): #如果生日在10/24~11/21之間
    print('天蠍座') #輸出天蠍座
elif(mon == 11 and day > 21) or (mon == 12 and day < 21): #如果生日在11/22~12/20之間
    print('射手座') #輸出射手座   
elif(mon == 12 and day > 20) or (mon == 1 and day < 21): #如果生日在12/21~1/20之間
    print('魔羯座') #輸出摩羯座
elif(mon == 1 and day > 20) or (mon == 2 and day < 20): #如果生日在1/21~2/19之間
    print('水瓶座') #輸出水瓶座
else: #剩下的天數
    print('雙魚座') #輸出雙魚座
    