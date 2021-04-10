# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
#108021016 林雨璇 6-1-PrimeTest.py
import math

def divisiible(a,b):
   b=2
   while b < a:
       if(a % b == 0):
           print('不是質數')
           break
       b+=1
   else:
       print('是質數')
            
n = int(input('輸入一個數'))
divisiible(n,math.sqrt(n))    
