# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:18:50 2018

@author: outao
"""
from elasticsearch import Elasticsearch
import pymysql
import datetime
db = pymysql.connect(host='localhost', user='root', db='ics_scan', password='123456')
cursor = db.cursor()  # 获取游标
sql = 'select * from knowledgebase_vulnerability '
es = Elasticsearch('localhost:9200')
cursor.execute(sql)
results = cursor.fetchall()
starttime = datetime.datetime.now()
doc = []
for row in results:
    ###########插入一条数据
    doc.append({'index': {'_index': 'xt', '_type': 'vulnerability'}})  # 定义方法(操作信息头）
    doc.append(
        {'ssvid': '', 'CVE-ID': '', 'CNVD-ID': '', 'CNNVD-ID': '', 'Vul_open_date': row[7],
         'Vul_discovery_date': '', 'Vul_level': row[2], 'Vul_title': row[0], 'Vul_desc': row[3],
        'Vul_vender':  row[1], 'Vul_mitigation': row[5], 'Vul_provider': row[6], 'patch_name': '', 'patch_url': ''})  # 定义数据
    ###########
es.bulk(index='test', doc_type='xt', body=doc)
endtime = datetime.datetime.now()
time = endtime - starttime
print("耗时：" + str(time))
