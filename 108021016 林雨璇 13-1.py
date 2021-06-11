# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:09:31 2021

@author: 林
"""
#108021016 林雨璇 13-1.py
import os
import pprint
import itertools
#1-----------------------------------------------------------
os.system('dir') #讓系統執行cmd指令，windows用dir
print(os.getenv('COMPUTERNAME')) #輸出電腦名稱
print(os.getenv('HOMEDRIVE')) #輸出家目錄所在資料夾
print(os.getenv('HOMEPATH')) #輸出家目錄路徑
print(os.getenv('USERNAME')) #輸出使用者名稱
#2-----------------------------------------------------------
print('在函式外，顯示全域變數', globals()) #用字典儲存全域變數
print('在函式外，顯示區域變數', locals()) #用字典儲存區域變數
def add(x, y):
    sum = x+y
    print('在函式內，顯示全域變數')
    pprint.pprint(globals()) #將全域變數顯示在螢幕
    print('在函式內，顯示區域變數')
    pprint.pprint(locals()) #將區域變數顯示在螢幕
    return sum
ans = add(1,2)
#3-----------------------------------------------------------
nums = itertools.count(1,2) #產生資料列，從1開始，每次遞增2
for i in range(5): 
    num = nums.__next__() #取得num的下一個元素
    print(num)
#4-----------------------------------------------------------  
nums1 = [1, 2, 3]
cyclenums = itertools.cycle(nums1) #不斷循環產生資料列
for i in range(6): 
    num1 = cyclenums.__next__()
    print(num1)
#5-----------------------------------------------------------
nums2 = [1, 2, 3]
repeatnums = itertools.repeat(nums2, 3) #用nums2重複3次，也就是產生3個nums2
for i in range(3):
    num2 = repeatnums.__next__()
    print(num2)
#6-----------------------------------------------------------
nums3 = [i for i in range(1, 6)] #1到5
sums = itertools.accumulate(nums3) #nums3累加
print(list(sums))
sums = itertools.accumulate(nums3, lambda x,y:x*y) #nums3前項乘後項
print(list(sums))
#7-----------------------------------------------------------
s = itertools.chain('Py','thon')  #將括號內多個物件依序取出所有元素，串接成新數列
print(list(s))
#8-----------------------------------------------------------
perm = itertools.permutations('ABC', 2) #把ABC取2個元素的所有排列，如果2是none的話，排列所有元素
print(list(perm))
comb = itertools.combinations('ABC', 2) #把ABC取2個元素的所有組合
print(list(comb))    
