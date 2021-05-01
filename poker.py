# -*- coding: utf-8 -*-
"""
Created on Sat May  1 15:54:53 2021

@author: 林
"""

from random import choice

def poker():
    a = ['黑桃','紅心','方塊','梅花']
    b =['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    return choice(a) + choice(b)