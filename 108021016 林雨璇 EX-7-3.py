# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 14:49:04 2021

@author: 林
"""

#108021016 林雨璇 EX-7-3.py

import math

def prime (a,b): #先寫一個判對質數的函式
  b = 2  
  while b < a: 
      if(a % b == 0): #如果可以整除
          break #就不是質數
      b+=1 #b+1，繼續測試
  else: #如果不能
      return True 

A = (i for i in range(2,100)  #從2到100
     if (prime(i,math.sqrt(i) == True))) #如果是質數
for j in A:
    print(j,',',end='') #輸出質數，用end=''不換行
