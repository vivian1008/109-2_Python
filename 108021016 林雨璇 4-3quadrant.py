# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:04:03 2021

@author: ASIA-H607
"""

#108021016 林雨璇 4-3quadrant.py

x = float(input('輸入x座標')) #使用者輸入x座標
y = float(input('輸入y座標')) #使用者輸入y座標
if x == 0 and y == 0: #如果x座標為0且y座標也為0
    print('原點') #輸出這個點是原點
elif x == 0: #如果x座標為0
    print('該點在y軸上') #輸出這個點在y軸上
elif y == 0: #如果y座標為0
    print('該點在x軸上') #輸出這個點在x軸上
elif x > 0 and y > 0: #如果x座標大於0且y座標大於0
    print('該點在第一象限') #輸出這個點在第一象限
elif x < 0 and  y > 0:  #如果x座標小於0且y座標大於0
    print('該點在第二象限') #輸出這個點在第二象限
elif x < 0 and y < 0: #如果x座標小於0且y座標小於0
    print('該點在第三象限') #輸出這個點在第三象限
else: #其餘的
    print('該點在第四象限') #輸出這個點在第四象限
    