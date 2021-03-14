# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 14:31:18 2021

@author: ASIA-H607
"""

#108021016 林雨璇 3-2 ListTest.py

list1 = ['麵包','蛋糕','巧克力']
print(list1)
print(list1[1]) #輸出第2個元素
print(len(list1)) #輸出list1的長度

list1[2] = '奶油'
print(list1) #輸出更改後的list1

index = list1.index('麵包')
print(index) #輸出麵包的索引值

list1.append('蜂蜜') #把蜂蜜加入list1
print(list1) 

list1.insert(3,'果醬') #把果醬加到第4個位置
print(list1) 

list1.remove('蛋糕') #刪除指定元素,也可以用pop
print(list1)

del list1[2] #刪除指定元素
print(list1)

list1.sort() #對元素進行排列
print(list1)

for item in list1: #用for迴圈讀取list
    print(item)
    
    list2 = ['雪碧','可樂','七喜']
    list3 =list1+list2 #將list1和list2的元素串接在一起
    print(list3)
    
    list4 = '2077@354@97a'.split('@') #去除"@"的list4
    print(list4)
    
    r = list('456789123')
    print(r[:3]) #輸出r的前三個
    print(r[3:]) #輸出r的第三個之後的元素
    print(r[:-3]) #輸出r的倒數第三個之前的元素
    print(r[-3:]) #輸出r的最後三個
    
    print(r[1:6]) #輸出r[1]到r[6]的前一個元素
    print(r[-4:-1]) #輸出r倒數第4個到倒數第一個之前的元素
    print(r[3:7:2]) #輸出r第三個往後算2個的元素
    print(r[-2:-8:-5]) #輸出r倒數第二個往前算5個的元素
    
    print(r[::-1]) #輸出反轉串列
    
    list5 = list1.copy() #複製list1的內容到list5，也可以用 list5 = list1[:]
    print(list5)