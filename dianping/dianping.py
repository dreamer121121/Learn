
import requests
from bs4 import BeautifulSoup
import re
from get_shops import shops
import json
import time
import random
User_agent = [
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
    'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/63.0.3239.132 Safari/537.36'
    ]

header = {
    'cookie': '__guid=169583271.2006832283541870800.1539452030746.5408; cy=2; cye=beijing; _\
lxsdk_cuid=1666e7e165ac8-01c287ab01595c-454c092b-1fa400-1666e7e165bc8; _lxsdk=1666e7e165ac8-01c\
287ab01595c-454c092b-1fa400-1666e7e165bc8; _hc.v=14d2ce66-7ed0-2d07-0a33-5ce7a8b5e374.1539452049; \
dper=d07bc17dfe9c281633a6384f1dc4ecde18fbe6663dee8dc59c42ff392f2c10b3fb1def21636fe78204fff4a94e309\
29186df4a86607250ae74e37809d4c33181c37f00c9505848eff3e6741b5200b0a0af6937137659e19c526444bece9351\
f3; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_6949286908; ctu=45410ace5f082793316a221d5bdd91f\
1cde5001aa8b707721b6d01eab8205161; uamo=16619864868; s_ViewType=10; _lxsdk_s=16670690c48-f7a-a88\
-92f%7C%7C682; monitor_count=25',
    'User-agent': random.choice(User_agent),
    'Referer': 'https://www.dianping.com/shoplist/shopRank/pcChannelRankingV2\
?rankId=d5036cf54fcb57e9dceb9fefe3917fff71862f838d1255ea693b953b1d49c7c0',
    'host': 'www.dianping.com'
}

def spider(shop_url):
    scores = []
    page = 1
    while len(scores) < 100:  # 每一个商家抓取100个用户的评分
        url = shop_url + str(page)  # 构造每一页评论的url
        print(url)
        print("正在爬第：%d页" % page)
        time.sleep(random.randint(5, 15))
        r = requests.get(url, headers=header)
        print(r.status_code)
        if r.status_code != 200:
            break
        html = r.text
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
            if len(scores) == 100:  # 避免超出100
                break
            score = re.search('sml-str(\w+)', str(span)).group(1)
            scores.append(score)
        page += 1
    if len(scores) == 100:
        return scores


if __name__ == '__main__':
    f = open('results.txt', 'r')
    total_results = f.read()
    f.close()
    total_results = json.loads(total_results)
    base_url = 'http://www.dianping.com/shop/'
    i = 50
    trace = []
    try:
        while i <= 50:
            shop = shops[i-1]
            trace.append(i)
            print("---------------正在爬第%d个商家-----------------"%i)
            url = base_url + shop['shopId'] + '/review_all/p'  # 构造出一个商家的url
            time.sleep(random.randint(5, 15))
            result = spider(url)  # 获取一个店铺的100个用户的评分
            if not result:  # 若返回为NONE则跳过继续爬取下一商家
                continue
            total_results.append(result)
            if len(total_results) == 50:
                break
            i += 1
    except Exception as e:
        f1 = open('error.txt', 'w')
        f1.write(str(e))
        f1.write(json.dumps(trace))
    f = open('results.txt', 'w')
    f.write(json.dumps(total_results))
    f.close()
