# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:48:23 2021

@author: ASIA-H607
"""

#108021016 林雨璇 4-2vision.py

vision = float(input('輸入視力測量值')) #輸入視力的值
if vision < 0.9: #如果視力值小於0.9
    print('近視') #輸出近視
else: #其餘的
    print('視力正常') #輸出視力正常
    