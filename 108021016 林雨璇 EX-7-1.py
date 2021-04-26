# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#108021016 林雨璇 EX-7-1.py
import math

A = [(i+2)*5 for i in range(10)] #i從2開始累加1，每次乘以5
print(A) 

B = [int(3*math.pow(2,j)) for j in range(9)] #從3開始，每次乘以2的0次方、1次方、2次方...
print(B)

C = [k for k in range(6) for l in range(k)] #0就輸出0個，1就輸出1個，2就輸出2個...
print(C)

D=[chr(m+96) for m in range(7) for n in range(m)] #a輸出1個，b輸出2個，c輸出3個
print(D)

E=[o for o in range(11) for p in range(o)]
print(E)
