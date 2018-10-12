import os
import json
path = r'C:\Users\outao\Desktop\cnvd漏洞信息'
os.chdir(path)
f = open('cnvd.txt', 'r', encoding='utf-8')
contents = f.readlines()
i=1
for content in contents:
    print("第%i页" % i)
    if content.startswith(u'\ufeff'):
        content = content.encode('utf-8')[3:].decode('utf-8')  # 去除bom
    vuls = json.loads(content)  # 转换为列表了
    for vul in vuls:
        print(len(vul))
        if len(vul) == 15 or len(vul) == 16:
            print(vul)
    i+=1


