# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:59:40 2021

@author: 林
"""
#108021016 林雨璇 14-4.py
from bs4 import BeautifulSoup as soup
fin = open('web.htm', encoding='utf-8')
s = fin.read()
htm = soup(s, 'html.parser')

#印出 title 標籤相關內容
print(htm.title.prettify()) #把html轉成容易閱讀的方式
print(htm.title.contents) #找出第一個標籤為title的標籤所對應的值
print(htm.title.contents[0])
print(htm.title.name) #找出第一個對應title的標籤名稱
print(htm.title.string) #找出第一個遇到標籤為title，如果這標籤只有一個值，且是數列或字串，就回傳值

#印出 title 標籤相關內容
print(htm.meta)
print(htm.meta['content'])

#印出 td 標籤相關內容
for item in htm.find_all('td'):
    print(item)
for item in htm.find_all('td',class_='table_head'):
    print(item)
for item in htm.find_all('td',class_='table_siteurl'):
    print(item.a['href'])
    