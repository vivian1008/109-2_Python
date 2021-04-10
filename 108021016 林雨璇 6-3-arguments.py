# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 12:52:25 2021

@author: 林
"""

#108021016 林雨璇 6-3-arguments.py
def arg(*args,**kwargs): #函式輸入位置引數跟關鍵字引數
    print('位置引數是:',args) #輸出位置引數
    print('關鍵字引數是:',kwargs) #輸出關鍵字引數
    
arg(1,2,3,4,a=17,r=35) #主程式使用函式
