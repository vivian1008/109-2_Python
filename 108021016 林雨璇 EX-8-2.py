# -*- coding: utf-8 -*-
"""
Created on Sat May  1 15:33:55 2021

@author: 林
"""

#108021016 林雨璇 EX-8-2.
import sys #匯入sys模組

for path in sys.path: #讀取模組系統的指定路徑
    print(path)
    
P = open('sys-path.txt','wt',encoding='utf-8') #把路徑寫成文字檔，存在sys-path
for line in sys.path:
    print(line,file = P)
P.close()   
