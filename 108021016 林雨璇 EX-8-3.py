# -*- coding: utf-8 -*-
"""
Created on Sat May  1 15:50:13 2021

@author: 林
"""

#108021016 林雨璇 EX-8-3.py
import dice,poker #匯入dice跟poker的模組

print('丟兩次骰子得到是',dice.dice(),'與',dice.dice())
if dice.dice() + dice.dice() > 7: #如果骰子點數和大於7
    print('兩次骰子的點數和大於7')
    print('抽一張牌',poker.poker(),'再丟一次骰子',dice.dice())
else:
    print('兩次骰子的點數和小於等於7')
    print('抽兩張牌得到是',poker.poker(),'與',poker.poker())   
