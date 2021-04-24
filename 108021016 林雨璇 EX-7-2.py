# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 14:11:06 2021

@author: 林
"""

#108021016 林雨璇 EX-7-2.py
import math

A = {i:int(math.pow(i,2)) for i in range(10)} #從0開始，產生0~9的平方
print(A)

B ={chr(j+97):j+97 for j in range(26)} #從a開始，產生a~z的ascii碼
print(B)
