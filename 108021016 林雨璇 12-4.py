# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:20:57 2021

@author: 林
"""
#108021016 林雨璇 12-4.py
import csv #模組csv

with open('2.csv','wt',newline='') as fout: #寫入內容到2.csv
    writer = csv.writer(fout) #利用csv.writer物件將資料寫入csv檔
    writer.writerows((['56','61','72','53'],['97','69','4','57'],['60','30','49','46'],['18','51','84','51'],['68','18','22','36'],['56','45','95','65'],['23','15','27','22'],['3','73','97','58'],['78','79','72','76'],['59','88','91','79']))

with open('2.csv', 'rt') as fin: #讀取2.csv檔
    reader = csv.DictReader(fin,fieldnames=['程式設計','線性代數','離散數學','平均']) #讀入資料，將每筆資料對應標題
    rows = [row for row in reader]
    print(rows) #輸出檔案的內容
    
    fout = open('3.csv','wt',newline='',encoding='utf-8') #寫入3.csv
    writer = csv.DictWriter(fout,fieldnames=['程式設計','線性代數','離散數學','平均']) #用DictWriter寫入標題
    writer.writeheader()
    writer.writerows(rows)
    fout.close()
    