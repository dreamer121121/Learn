import requests
from bs4 import BeautifulSoup
items = []
# 构造请求
url = 'http://quotes.toscrape.com/'
r = requests.get(url, timeout=60)
soup = BeautifulSoup(r.text, 'lxml')
quotes = soup.find_all(name='div', attrs={'class':"quote"})
# for quote in quotes:
text = quotes[0].span.get_text()
author = quotes[0].find(name='small', attrs={'class': 'author'}).get_text()
tags_label = quotes[0].div.find_all('a')
tags = []
for i in tags_label:
    tags.append(i.get_text())



