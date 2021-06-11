# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 14:53:14 2021

@author: 林
"""
#108021016 林雨璇 13-2.py
import functools
import itertools
#9----------------------------------------------------------------------------
days = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
p = enumerate(days, start=1) #把days的元素編號，從星期天開始編號1
for c, day in p: 
    print(c, day)
do = ['休息', '游泳','跑步', '籃球', '桌球', '羽球', '棒球', '壘球'] 
week = zip(days, do) #把days跟do依序由前到後組成tuple，然後把tuple組成zip
for day,sport in week:
    print(day,sport)  
#10----------------------------------------------------------------------------
nums = [i for i in range(1,10)] 
nums2 = filter(lambda x:x%2, nums) #用lambda作用到nums的每個元素，結果是true就留下
print(list(nums2)) #奇數
nums3 = filter(lambda x:x%2 == 0, nums)
print(list(nums3)) #偶數
#11----------------------------------------------------------------------------
nums = [i for i in range(1,6)]
def double(x):
    return 2*x
nums2 = map(double, nums) #double作用到一個以上的nums每個元素，最後回傳double作用到nums的結果
print(list(nums2))
a = [i for i in range(1,6)]
b = [i for i in range(6,11)]
c = map(lambda x,y:x*y, a, b) #如果函式接收兩個參數，就要兩個iterable
print(list(c))   
#12----------------------------------------------------------------------------
num = functools.reduce(lambda x, y:x+y, range(1,10)) #函式要能輸入兩個參數，函式作用到iterable由左到右每個元素
print(num)
num = functools.reduce(lambda x, y:x+y, range(1,10),3) #如果有initializer，則初始值為initializer
print(num) 
#13----------------------------------------------------------------------------
def iter_primes(): #產生無窮數列
     numbers = itertools.count(2)
     while True:
         prime = numbers.__next__()
         numbers = filter(prime.__rmod__, numbers) #prime.__rmod__除以prime的餘數不是0才留下
         yield prime #產生prime給主程式，主程式呼叫由原執行狀態繼續執行
for p in iter_primes():
    if p > 1000:
        break
    print(p,' ',end='')
