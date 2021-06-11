# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:39:02 2021

@author: 林
"""
#108021016 林雨璇 13-3.py
#14------------------------------------------------------------
from datetime import datetime, date
now = date.today() #回傳現在日期
print(now)
now2 = datetime.now() #回傳現在日期和時間
print(now2)
print(now.year, now.month, now.day) #輸出現在的年、月、日
print(now.hour, now.minute, now.second, now.microsecond) #輸出今天到現在過了幾小時、分鐘、秒
#15------------------------------------------------------------
import time
now = time.time() #累計從1970年1月1日凌晨0點0分0秒到現在的秒數
print(now)
print(time.ctime()) #把累計秒數轉為年月日時分秒，如果括號沒有輸入sec，就預設time.time()的回傳值為輸入
t=time.localtime() #把累計秒數轉為以物件struct_time表示的時間，如果括號沒有輸入sec，就預設time.time()的回傳值為輸入
print(t)
fmt = "%Y-%m-%d(%a) %H %M %S"
print('現在時間為',time.strftime(fmt)) #以format格式顯示
fmt2 = "%Y-%B-%d(%A) %p %I %M %S"
print('現在時間為',time.strftime(fmt2))
#16------------------------------------------------------------
from datetime import datetime,timedelta
birthday = datetime(1995,1,1,21,30,0,0) #起始時間
print(birthday)
day10000 = timedelta(days=10000) #過10000天
someday = birthday + day10000 #從起始時間過10000天是幾年幾月幾日
print(someday)
#17------------------------------------------------------------
import time as t
def count():
    st = t.time() #開始時間
    [x for x in range(10000000)]
    et = t.time() #結束時間
    print ('執行所需時間為',et-st,'秒') #輸出要花幾秒執行
count()
