# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:35:13 2021

@author: user
"""

# 108021016 林雨璇 least_n_fac.py

M = int(input('輸入一個值')) #讓使用者輸入一個數
f = 1
N = 1
while N < M: #當N!沒超過M
    N = N*f #N!就繼續往上乘
    f+=1  #f遞增
    if N > M: #如果N!大於M
     print(N) #輸出N!
    