# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:55:02 2021

@author: 林
"""

#108021016 林雨璇 EX9-7.py

class Stick_man(): #新增類別:火柴人
    count = 0   #count是Stick_man的共用物件
    def __init__(self): #新增一個火柴人
        Stick_man.count+=1
    def kill(self): #減少一個火柴人
        Stick_man.count-=1
    @classmethod  #類別方法  
    def show_count(cls):
        print('有',cls.count,'個火柴人') #cls.count就是count
 
x = Stick_man() #新增一個火柴人
Stick_man.show_count() #顯示火柴人數量
y = Stick_man()
Stick_man.show_count()
x.kill() #減少
Stick_man.show_count()


class Talk(): #新增類別:Talk
    @staticmethod #靜態方法的修飾器
    def puipui(): #輸出puipui的方法
        print('puipui')

Talk.puipui()        