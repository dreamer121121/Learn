#coding:utf-8
import os
import json
import requests
header = {
    'cookie': 'guid=169583271.2006832283541870800.1539452030746.5408; cy=2; cye=beijing; _\
lxsdk_cuid=1666e7e165ac8-01c287ab01595c-454c092b-1fa400-1666e7e165bc8; _lxsdk=1666e7e165ac8-\
01c287ab01595c-454c092b-1fa400-1666e7e165bc8; _hc.v=14d2ce66-7ed0-2d07-0a33-5ce7a8b5e374.\
1539452049; lgtoken=0a6303411-e5ec-4518-819c-1cb21265fa4c; dper=d07bc17dfe9c281633a6384f1dc4ecde1\
8fbe6663dee8dc59c42ff392f2c10b3fb1def21636fe78204fff4a94e30929186df4a86607250ae74e37809d4c33181c3\
7f00c9505848eff3e6741b5200b0a0af6937137659e19c526444bece9351f3; ll=7fd06e815b796be3df069dec7836c\
3df; ua=dpuser_6949286908; ctu=45410ace5f082793316a221d5bdd91f1cde5001aa8b707721b6d01eab8205161; \
uamo=16619864868; _lxsdk_s=1666e7e165b-271-919-b3c%7C%7C55; monitor_count=4',
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/63.0.3239.132 Safari/537.36',
    'Referer': 'https://www.dianping.com/shoplist/shopRank/pcChannelRankingV2\
?rankId=d5036cf54fcb57e9dceb9fefe3917fff71862f838d1255ea693b953b1d49c7c0',
    'host': 'www.dianping.com'

}


url = 'https://www.dianping.com/mylist/ajax/shoprank?rankId=d5036cf54fcb57e9dc\
eb9fefe3917fff71862f838d1255ea693b953b1d49c7c0'

r = requests.get(url, headers=header)
shops = r.json()
shops = shops['shopBeans']
print("成功获取美食店铺的全部信息")