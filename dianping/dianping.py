import os
import requests
from bs4 import BeautifulSoup
import re
from test import shops
import json
import time
import random
path = r'C:\Users\dreamer\Desktop\dianping'
os.chdir(path)
header = {
    'cookie':'Cookie:cy=2; cye=beijing; _lxsdk_\
cuid=1666ca7798dc8-0cd2cdcb8de6ec-454c092b-140000-1666ca7798dc8; \
_lxsdk=1666ca7798dc8-0cd2cdcb8de6ec-454c092b-140000-1666ca7798dc8; \
_hc.v=dd2b00f5-acea-a3d1-3e9f-620c1d6f8578.1539421207; \
_dp.ac.v=2999bd5d-8285-4f48-b3f9-401521546945; \
dper=d07bc17dfe9c281633a6384f1dc4ecde47c25b9a393112b37a\
4f578006e7f18d5454023d8c1064d33d4a54cf9765dbbbc048a6bc884b4\
bdebd6851a349ca3d0565785d8feeffbc82cbd8fa4d4c57d7be7119c3682ea\
b74512d899e436e2b5ee6; ll=7fd06e815b796be3df069dec7836c3df; \
ua=dpuser_6949286908; ctu=45410ace5f082793316a221d5bdd91f1daa\
07c14a6887e4ac468c8acfae7426c; uamo=16619864868; aburl=1; \
QRCodeBottomSlide=hasShown; wed_user_path=6698|0; \
_lx_utm=utm_source%3Ddp_pc_wedding; _lxsdk_s=1666d0885bf-b-fb1-7bb%7C%',
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Referer': 'https://www.dianping.com/shoplist/shopRank/pcChannelRankingV2\
?rankId=d5036cf54fcb57e9dceb9fefe3917fff71862f838d1255ea693b953b1d49c7c0',
    'host': 'www.dianping.com'

}


def spider(url):
    scores = []
    page = 1
    while len(scores) <= 100:  # 每一个商家抓取100个用户的评分
        url = url + str(page)  # 构造每一页评论的url
        time.sleep(random.randint(2,15))
        r = requests.get(url, headers=header, timeout=20)
        if r.status_code != 200:
            break
        html = r.text
        print(r.status_code)
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find(name='div', attrs={'class': 'reviews-items'})
        lis = ul.find_all(name='li')
        new_lis = []
        for li in lis:
            if li.find(name='div', attrs={'class': 'review-rank'}):
                new_lis.append(li)
        for li in new_lis:
            div = li.find(name='div', attrs={'class': 'review-rank'})
            span = div.find('span')
            # 提取分数
            score = re.search('sml-str(\w+)', str(span)).group(1)
            scores.append(score)
        page += 1
    if len(scores) == 100:
        return scores


if __name__ == '__main__':
    total_results = []
    base_url = 'http://www.dianping.com/shop/'
    for shop in shops:
        url = base_url + shop['shopId'] + '/review_allp'  # 构造出一个商家的url
        time.sleep(random.randint(2, 15))
        result = spider(url)  # 获取一个店铺的100个用户的评分
        total_results.append(result)
        if len(total_results) == 50:
            break
    with open('results.txt', 'w') as f:
        f.write(json.dumps(total_results))
