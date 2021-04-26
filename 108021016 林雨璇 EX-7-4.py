# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 15:42:33 2021

@author: 林
"""

#108021016 林雨璇 EX-7-4.py
import random

A = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(A)
for i in range(4):
  {a : A.count(a) for a in set(A)
  if A.count(a) > 1}
  print(random.choice(A),end='')