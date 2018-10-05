import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User - Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 \
Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.json()  # 把返回的响应转换为json
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = BeautifulSoup(item.get('text'), 'lxml').get_text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['reposts'] = item.get('comments_count')
            yield weibo  # 返回生成器

if __name__ == '__main__':
    json = get_page(3)
    items = json1.get('data').get('cards')
    # results = parse_page(json)
    # print(type(results))
    # for result in results:
    # print(result)
