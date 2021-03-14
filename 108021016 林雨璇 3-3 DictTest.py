# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:57:37 2021

@author: user
"""

# 108021016 林雨璇 3-3 DictTest.py

dic = {'蘋果':'Pomme','香蕉':'banane'} #設定key對應的value
print(dic)
print('蘋果的法文是',dic['蘋果'])
print('香蕉的法文是',dic.get('香蕉'))
print('鳳梨的法文是',dic.get('鳳梨')) #沒有的key就讀不到value
print('鳳梨的法文是',dic.get('鳳梨','沒有寫')) 

dic['番茄'] = 'tomate' #新增key和value
print(dic)

del dic['香蕉'] #刪除指定key和value
print(dic)

dic.clear() #清除全部
print(dic)

dic2={'番茄':'tomate'}
dic.update(dic2) #將新字典和舊字典合併
print(dic)
dic3 = {'番茄':'不想寫'} #如果原本就有會更新
dic.update(dic3)
print(dic)

dic = {'蘋果':'Pomme','香蕉':'banane'}
dic4 = dic #value會一起更改
dic4['蘋果'] = 'apple'
print(dic)
print(dic4)
dic = {'蘋果':'Pomme','香蕉':'banane'}
dic5 = dic.copy() #value不會一起改變
dic5['蘋果'] = 'apple'
print(dic)
print(dic5)

dic = {'蘋果':'Pomme','香蕉':'banane'}
for c,f in dic.items(): #設置c是key，f是value
    print('中文是',c,'法文是',f) #輸出dic的key和value
for c in dic.keys(): 
    print(c) #輸出dic的key
for f in dic.values():
    print(f) #輸出dic的value