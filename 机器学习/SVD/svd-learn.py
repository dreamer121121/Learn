import os
import json
path=r'C:\Users\outao\Desktop\work\dianping'
os.chdir(path)
f = open('results.txt', 'r')
content = f.read()
content = json.loads(content)
print(len(content))
print(len(content[-1]))