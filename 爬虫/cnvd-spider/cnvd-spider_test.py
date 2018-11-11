# -*- coding: utf-8 -*-
import os
import requests
import time
import json
import random
from bs4 import BeautifulSoup
path = r'C:\Users\outao\Desktop\cnvd漏洞信息'
os.chdir(path)
headers = [{
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 \
Safari/537.36'},
    {'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; \
.NET CLR 1.1.4322; .NET CLR 2.0.50727)"},
    {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center \
PC 5.0; .NET CLR 3.0.04506)"},
    {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 \
(KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20"},
    {'User-Agent':  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 \
(KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER"},
    {'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; \
Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; \
.NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)"}]
# index = {0: 'CNVD-ID', 1: '公开日期', 2: '危害级别', 3: '影响产品', 4: 'CVE ID', 5: '漏洞描述', 6: '参考链接', 7: '漏洞解决方案',
# 8: '厂商补丁', 9: '验证信息', 10: '报送时间', 11: '收录时间', 12: '更新时间', 13: '漏洞附件'}  # 需要的信息


def get_page(page):  # 获取一页的html
    header = random.choice(headers)
    vuls = []
    temp = []
    urls = []
    url = "http://ics.cnvd.org.cn/?max=20&offset=" + str(page)  # 构造页面url
    r = requests.get(url, headers=header)
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
        print('正在处理漏洞为：%s' % url)
        time.sleep(random.randint(2, 10))  # 设置每一个漏洞信息的获取间隔
        vul = get_content(url)
        vuls.append(vul)
    save(vuls)  # 保存该页20个漏洞的信息

# 获取一个漏洞的具体信息
def get_content(url):
    header = random.choice(headers)
    vul = {}  # 保存在字典里
    html = requests.get(url, headers=header).text
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('tbody').find_all('tr')
    print(len(trs))
    for i in range(len(trs)):
        tds = trs[i].find_all('td')
        if len(tds) == 2:
            index = tds[0].get_text()
            content = tds[1].get_text().replace('\t', '').replace('\n', '').replace('\r', '')
            if index == '危害级别':
                content = content[0]
            vul[index] = content
        else:
            continue
    return vul


def save(vuls):  # 保存一页共20漏洞信息以列表形式存储在文件中一行
    with open('cnvd-database2.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(vuls, ensure_ascii=False)+'\n')


if __name__ == '__main__':
    base_url = 'http://ics.cnvd.org.cn/?max=20'
    page = 1
    while page <= 88:
        try:
            time.sleep(random.randint(5, 30))  # 设置每一页请求的间隔
            print("-----正在爬取第%d页--------" % page)
            get_page((page - 1) * 20)
            page += 1
        except Exception as e:
            with open('errorinfo.txt', 'a') as error:
                error.write("第%d页出现错误:" % page)
                error.write(str(e)+'\n')
