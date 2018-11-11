# coding : utf-8
import os
import json
import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', db='argus')
cur = conn.cursor()

# 读取文件
path = r'C:\Users\outao\Desktop\cnvd漏洞信息'
os.chdir(path)
f = open('cnvd.txt', 'r', encoding='utf-8')
contents = f.readlines()
i = 1
for content in contents:
    print("-----插入第%d页-----" % i)
    if content.startswith(u'\ufeff'):
        content = content.encode('utf-8')[3:].decode('utf-8')  # 去除bom
    vuls = json.loads(content)  # 转换为列表了
    j = 1
    for vul in vuls:
        print(vul)
        print("正在插入第%d个漏洞" % j)
        # 将漏洞信息补充为16个字段
        if 'BUGTRAQ ID' not in vul:
            vul['BUGTRAQ ID'] = ''
        if '其他 ID' not in vul:
            vul['其他 ID'] = ''
        if 'CVE ID' not in vul:
            vul['CVE ID'] = ''
        data = (vul['CNVD-ID'], vul['公开日期'], vul['危害级别'], vul['影响产品'], vul['BUGTRAQ ID'], vul['其他 ID'],
                vul['CVE ID'], vul['漏洞描述'], vul['参考链接'], vul['漏洞解决方案'], vul['厂商补丁'],
                vul['验证信息'], vul['报送时间'], vul['收录时间'], vul['更新时间'], vul['漏洞附件'])
        cur.execute('insert IGNORE into vul_cnvd (CNVD_ID, Open_date, Level, Vender, BUGTRAQ_ID, Other_ID, CVE_ID, Vul_desc, \
Reference_URL, Vul_mitigation, Vender_patch, Ver_info,Submit_time,Reserved_time,Update_time,Vul_attachment) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',data)
        cur.connection.commit()  # 执行commit操作，插入语句才能生效
        j += 1
    i += 1
    # if i == 8:
    #     break
