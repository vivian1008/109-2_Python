# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:39:53 2021

@author: 林
"""

#108021016 林雨璇 EX-8-1.py
import guess as gs #匯入guess的模組

for i in range(10): #進行10次猜拳
    a = input('出拳:') #玩家輸入要出的拳
    print('電腦出:',gs.figure_guess()) #輸出電腦隨機選出的拳
    if (a == '石頭' and gs.figure_guess() == '剪刀') or (a == '布' and gs.figure_guess() == '石頭' ) or (a == '剪刀' and gs.figure_guess() == '布'):
        print('你贏了')
    elif (a == '布' and gs.figure_guess() == '剪刀') or (a == '剪刀' and gs.figure_guess() == '石頭') or (a == '石頭' and gs.figure_guess() == '布'):  
        print('你輸了')  
    elif (a == '剪刀' and gs.figure_guess() == '剪刀') or (a == '石頭' and gs.figure_guess() == '石頭') or (a == '布' and gs.figure_guess() == '布'):
        print('平手喔')
        