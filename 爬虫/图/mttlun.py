import requests
from bs4 import BeautifulSoup
def main():
    f = open('2.txt','r')
    html = f.read()
    f.close()
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
    # url = 'https://www.wifi599.com/forum/201901/28/165135wvrtfie66hr6y8wh.gif'
    # r = requests.get(url, timeout=30)
    # img = r.content
    # f = open(url[-10:-4] + '.gif', 'wb')
    # f.write(img)
    # f.close()
    main()





