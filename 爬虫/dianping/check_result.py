import os
import json
path=r'C:\Users\dreamer\Desktop\ARGUS\dianping'
os.chdir(path)
f = open('results.txt', 'r')
content = f.read()
content = json.loads(content)
for each in content:
    print(len(each))