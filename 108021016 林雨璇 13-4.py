# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:41:58 2021

@author: 林
"""
#108021016 林雨璇 13-4.py

#18---------------------------------------------------------------------------
import collections
days = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
sport = ['休息', '游泳','跑步', '籃球', '桌球', '羽球', '棒球']
week = zip(days, sport)
d1 = dict(week)
print(d1)
week = zip(days, sport)
d2 = collections.OrderedDict(week) #用items建立有順序性的OrderedDict物件
print(d2)
d = collections.OrderedDict([('Cr', 1),('To', 2)])
print(d)
#19---------------------------------------------------------------------------
from collections import deque
nums = [i for i in range(1,6)]
dq = deque(nums) #用nums建立deque物件
print(dq)
dq.rotate(1) #當括號內的值大於0，deque中所有元素向右旋轉n個元素，超過則依序補到deque左邊，小於0則相反
print(dq)
dq.pop() #從deque刪除最右邊的元素
print(dq)
dq.popleft() #從deque刪除最左邊的元素
print(dq)
dq.append(8) #把8加到deque右邊
print(dq)
dq.appendleft(8) #把8加到deque左邊
print(dq)
print(dq.count(8)) #計算8出現的次數
dq.reverse() #把deque所有元素反轉
print(dq)
#20---------------------------------------------------------------------------
from collections import Counter
c = Counter('Python') #計算每個字母出現的次數
print(c)
x = ['a', 'a', 'b', 'b', 'b']
c = Counter(x)
print(c)
c = Counter({'a':2,'b':3}) #依照元素與出現次數還原原始串列
print(c)
c = Counter(a=2, b=3)
print(c)
#21---------------------------------------------------------------------------
from collections import Counter
c = Counter({'a':2,'b':3,'c':1}) 
print(c)

print(list(c.elements())) #將count物件依照元素與出現次數還原原始串列
print(c.values()) #顯示count物件對應的值
print(c.keys()) #顯示count物件對應的鍵


print(c.most_common()) #顯示count物件最常出現的前n個元素與出現次數，沒有n值則出現所有元素與出現次數
print(c.most_common(1))
print(c.most_common()[::-1]) #由少到多
print(c.most_common()[:-2:-1]) #只列倒數第一
#22---------------------------------------------------------------------------
from collections import Counter
a = Counter(a=2, b=3)
b = Counter(b=2, c=1)
print(a + b) #a和b的元素相加，元素b重複的部分相加
print(a - b) #a的元素和次數減掉b的元素和次數
print(a & b) #a、b都有的元素和次數，次數取較少的那個
print(a | b) #a或b有就納入，次數取較多的那個
