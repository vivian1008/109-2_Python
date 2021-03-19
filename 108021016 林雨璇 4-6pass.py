# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:07:46 2021

@author: ASIA-H607
"""

# 108021016 林雨璇 4-6pass.py


num = input('輸入學號') #使用者輸入學號
ProgramPass = ('s01,s02,s08') #程式及格的集合
MathPass = ('s01,s05,s07') #數學及格的集合

if num in ProgramPass and num in MathPass: #如果輸入的學號在兩個集合都有
    print('程式、數學兩科都及格') #輸出兩科都及格
elif num in ProgramPass: #如果輸入的學號在程式及格的集合
    print('程式及格但數學不及格')  #輸出程式及格但數學不及格
elif num in MathPass: #如果輸入的學號在數學及格的集合
    print('數學及格但程式不及格') #輸出數學及格但程式不及格
else: #都沒有的
    print('程式、數學兩科都不及格') #輸出兩科都不及格
    
    