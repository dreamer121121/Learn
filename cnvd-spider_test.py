# -*- coding: utf-8 -*-
import requests
import re
import xlwt
import time
import time
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 \
Safari/537.36'
}
index = {0: 'CNVD-ID', 1: '公开日期', 2: '危害级别', 3: '影响产品', 4: 'CVE ID', 5: '漏洞描述', 6: '参考链接', 7: '漏洞解决方案',
8: '厂商补丁', 9: '验证信息', 10: '报送时间', 11: '收录时间', 12: '更新时间', 13: '漏洞附件'}  # 需要的信息

def get_page(page):
    vuls=[]
    temp=[]
    urls=[]
    url = "http://ics.cnvd.org.cn/?max=20&offset=" + str(page)  # 构造页面url
    r = requests.get(url, headers=headers)
    print(r.status_code)
    while r.status_code != 200:
        r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    tags = soup.find_all('a')
    for tag in tags:
        temp.append(tag.attrs['href'])
    for each in temp:
        if 'http' in each:
            urls.append(each)
    # 获取内容
    for url in urls:
        vul = get_content(url)
        vuls.append(vul)


# 获取一个漏洞的具体信息
def get_content(url):
    vul = {}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find_all('tr')
    for i in range(len(trs)):
        if i not in index:
            continue
        td = trs[i].find_all('td')[1]
        vul[index[i]] = td.get_text()
    return vul

def save():
    pass

if __name__ == '__main__':
    page = 0
    get_page(page)
