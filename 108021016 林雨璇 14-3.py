# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:06:33 2021

@author: 林
"""

#108021016 林雨璇 14-3.py
import xml.etree.ElementTree as xmltree
tree = xmltree.ElementTree(file='my.xml')
root = tree.getroot()
print(root.tag) #顯示root的屬性tag

for a in root: #顯示root下兩層的標籤、屬性、值
    print('a標籤', a.tag, '，屬性', a.attrib, '，值', a.text)

    for b in a:
        print('b標籤', b.tag, '，屬性', b.attrib, '，值', b.text)
      
for item in root.iter('item'): #找出標籤為item的屬性和值
    print('item',item.attrib , item.text)

for item in root.iter('morning'):
    print('morning',item.attrib , item.text)


for item in root.findall('./morning/item/hw'): #找出 root 下一層標籤為 morning 的下一層標籤為 item 的所有標籤的屬性與值
    print('標籤為', item.tag, '，屬性', item.attrib, '，值', item.text) 
        