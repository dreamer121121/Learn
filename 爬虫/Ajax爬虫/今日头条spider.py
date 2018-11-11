import os
import requests
from urllib.parse import urlencode
import time
import random
import json
root = r'C:\Users\outao\Desktop\图片'
os.chdir(root)


def get_pics(json):
    contents = json.get('data')
    for content in contents:
        if content.get('media_name'):  # 若非空
            if content.get('title'):
                title = content.get('title')
            else:
                title = content.get('content')
            urls = []
            print('----------正在下载'+title+'组图-------------')
            temp = content.get('image_list')
            for i in temp:
                if type(i) == str:
                    urls.append(i)
                else:
                    urls.append(i.get('url'))  # 获取某一个组图的全部url
            os.mkdir(title)
            os.chdir(title)
            i = 0
            for url in urls:
                down_pics(url, i)  # 下载一张图片
                time.sleep(random.randint(1, 15))
                i += 1
            os.chdir(root)



def get_page(offset):
    url_base = 'https://www.toutiao.com/search_content/?'
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    headers = {
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/69.0.3497.100 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    url = url_base + urlencode(params)
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def down_pics(url, i):
    if 'http' not in url:
        url = 'http:'+url
    else:
        pass
    print(url)
    img = requests.get(url).content
    with open(str(i)+'.jpg', 'wb') as f:  # 保存图片必须以为二进制的方式存储
        f.write(img)
        f.close()


if __name__ == '__main__':
    offset = 0
    json1 = get_page(0*20)
    get_pics(json1)
