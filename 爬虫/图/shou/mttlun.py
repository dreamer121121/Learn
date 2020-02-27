import os
import requests
from bs4 import BeautifulSoup
import random
import time
def main(html_f):
    print("Processing :"+html_f)
    f = open(html_f,'r')
    html = f.read()
    f.close()
    save_path = html_f.split('.')[0]
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    os.chdir(save_path)
    img_urls = []
    soup = BeautifulSoup(html, 'lxml')
    ignore_js_list = soup.find_all('ignore_js_op')
    for item in ignore_js_list:
        img_obj = item.find('img')
        img_url = img_obj.get('file')
        if img_url:
            img_urls.append(img_url)
    print("total img_url num:",len(img_urls))
    for url in img_urls:
        time.sleep(random.randint(5,10))
        try:
            print(url)
            r = requests.get(url,timeout=30)
            img = r.content
            f = open(url[-10:-4]+'.gif','wb')
            f.write(img)
            f.close()
            print("success")
        except Exception as e:
            print('Error url:',url)
if __name__ == '__main__':
    """get one img"""
    # url = 'https://www.wifi599.com/forum/201901/28/165135wvrtfie66hr6y8wh.gif'
    # r = requests.get(url, timeout=30)
    # img = r.content
    # f = open(url[-10:-4] + '.gif', 'wb')
    # f.write(img)
    # f.close()
    """get one img"""
    html_f_list = [f for f in os.listdir('./') if f.endswith('.txt')]
    for f in html_f_list:
        os.chdir('C:\\Users\\dreamer\\Desktop\\repositories\\learn\\learn\\爬虫\\图\\shou')
        if f != 'Error.txt' and f != 'kind_html.txt'and f != '0.txt' and f!='1.txt' and f != '10.txt' and f!= '11.txt' and f!= '12.txt':
            main(f)
        else:
            continue





