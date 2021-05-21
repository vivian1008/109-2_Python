# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:40:34 2021

@author: 林
"""

#108021016 林雨璇 EX10-1.py
import string #模組string
import random #模組random

mpwd = string.digits #產生一組由數字組成的字串
lpwd = string.ascii_letters #產生一組由字母組成的字串
pwd = '' 
for i in range(6): #產生共12位數的字串
    pwd = pwd + random.choice(lpwd) + random.choice(mpwd)
print(pwd) #輸出密碼
