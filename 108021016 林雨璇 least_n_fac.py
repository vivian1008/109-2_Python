# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:35:13 2021

@author: user
"""

# 108021016 林雨璇 least_n_fac.py

M = int(input('輸入一個值'))
f = 2
fac = 1
while fac < M:
    fac = fac*f
    f+=1
    print(fac/f)

    
    