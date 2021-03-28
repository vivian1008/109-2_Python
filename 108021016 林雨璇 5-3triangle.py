# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:56:46 2021

@author: user
"""

# 108021016 林雨璇 5-3triangle.py

n = int(input('三角形的高度?'))
for i in range(1,n+1):
    for j in range(1,i*2): 
        print(' ',end='')
        print('*',end='')
    print()