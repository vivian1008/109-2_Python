# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:36:24 2021

@author: ASIA-H607
"""

#108021016 林雨璇 4-4leap_year.py

year = int(input('輸入西元年')) #使用者輸入西元年

if year % 400 == 0: #如果是400的倍數
    print('是閏年') #輸出是閏年
elif year % 100 == 0: #如果是100的倍數
    print('不是閏年') #輸出不是閏年
elif year % 4 == 0: #如果是4的倍數
    print('是閏年') #輸出是閏年
else: #剩下的
    print('不是閏年')#輸出不是閏年
    