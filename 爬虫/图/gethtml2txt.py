import requests
from bs4 import BeautifulSoup
import os
dirname = 'xia/'
path = './'+dirname
os.chdir(path)

"""获取某一类img的页面"""
if not os.path.exists('kind_html.txt'):
    url = 'https://mtlluntan2.com/forum.php?mod=forumdisplay&fid=54&filter=typeid&typeid=15'
    r = requests.get(url)
    kind_html = r.text
    f = open('kind_html.txt','w',encoding='utf8')
    f.write(kind_html)
    f.close()
"""获取某一类img的页面"""

f = open('kind_html.txt','r',encoding='utf8')
kind_html = f.read()
soup = BeautifulSoup(kind_html,'lxml')
subpage_ul = soup.find('ul',attrs={'id':'waterfall'})
subpage_a_list = subpage_ul.find_all('a')
all_hrefs = []
for a in subpage_a_list:
    all_hrefs.append("https://mtlluntan2.com/"+a.attrs["href"])
err_f = open('Error.txt','a')
i = 0
for href in all_hrefs:
    try:
        print("processing：",href)
        r = requests.get(href,timeout=30)
        html = r.text
        f = open(str(i)+'.txt','w')
        f.write(html)
        f.close()
        i+=1
    except Exception as e:
        print("ERROR:",href)
        err_f.write(href+'\n')
err_f.close()

# print(all_subpage_herf)
# f = open('./tuiche/2.txt','w')
# f.write(html)
# f.close()
