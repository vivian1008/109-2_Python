# -*- coding: utf-8 -*-
"""
Created on Sat May 15 16:00:02 2021

@author: 林
"""
#108021016 林雨璇 EX9-6.py
class Score(): #建立分數類別
    def __init__(self,math_score,python_score): #宣告分數的物件:數學分數和python分數
        self.math_score = math_score
        self.python_score = python_score

class Student(): #建立學生類別
        def __init__(self,name,score): #宣告學生的物件:名字和分數
            self.name = name
            self.score = score
        def show_score(self): #輸出名字和分數的函式
            print(self.name,'數學成績為:',self.score.math_score,',python成績為:',self.score.python_score)
            
score = Score(76, 85) #設定數學分數為76，python分數為85
a = Student('xxx', score) #設定名字為xxx
a.show_score() 
           