# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:11:55 2021

@author: 林
"""

def f(n): #函式f(n)
    for i in range(1,n+1): #從1到n
        print(i) #輸出i  
 
if __name__ == '__main__': #讓這個檔案當腳本的時候不會執行本身的主程式
  print(f(5)) 
        