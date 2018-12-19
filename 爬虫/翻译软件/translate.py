# # -*- coding: utf-8 -*-
# # filename:GoogleTranslation1.2.py
# import requests
# import urllib.parse
# import urllib.request
# import time
# import pyperclip
# from tkinter import *
# import re
#
#
# def translate(text, f='zh-cn', t='en'):
#     url_google = 'http://translate.google.cn/translate_t'
#     reg_text = re.compile(r'(?<=TRANSLATED_TEXT=).*?;')
#     user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
#                  r'Chrome/44.0.2403.157 Safari/537.36'
#     '''user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)'''''
#     values = {'hl': 'zh-cn', 'ie': 'utf-8', 'text': text, 'langpair': '%s|%s' % (t, f)}
#     value = urllib.parse.urlencode(values)#将json编写成url
#     print(url_google+'?'+value)
#     req = urllib.request.Request(url_google + '?' + value)
#
#     req.add_header('User-Agent', user_agent)
#     response = urllib.request.urlopen(req)
#     content = response.read().decode('utf-8')
#     f=open('results.txt','w',encoding='utf-8')
#     f.write(content)
#     f.close()
#     print(content)
#     data = re.search(reg_text,content)
#     print('--data--',data)
#     result = data.group(0).strip(';').strip('\'')
#     return result
#
#
# def getcopytext(copyBuff):
#     copyedText = pyperclip.paste()
#     if copyBuff != copyedText:
#         copyBuff = copyedText
#         normalizedText = copyBuff.replace('\r', '\\r').replace('\n', '\\n').replace('-\\r\\n', '').replace("\\r\\n",
#                                                                                                            " ")
#     else:
#         print('no change')
#     return normalizedText
#
#
# def showtxt(inputtxt):
#     root = Tk()
#
#     root.title('DayDayUp')  # 定义窗体标题
#     root.geometry('400x200')  # 定义窗体的大小，是400X200像素
#     label = Label(root, text=inputtxt, wraplength=400, justify='left', font=12)
#     # label['text'] = inputtxt
#     label.pack()
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     copyBuff = ' '
#     # text_1 原文
#     # text_1=open('c:\\text.txt','r').read()
#     # while True:
#     time.sleep(0.003)
#     copyedText = 'china'
#     if copyBuff != copyedText:
#         copyBuff = copyedText
#         text_1 = copyBuff.replace('\r', '\\r').replace('\n', '\\n').replace('-\\r\\n', '').replace("\\r\\n", " ")
#         text_2 = translate(text_1)  # .strip("'")
#         showtxt(text_2)
# import requests
# import json
# import sys
# import urllib
# from bs4 import BeautifulSoup
# import re
# import execjs
# import os
#
#
# class Translate:
#     def __init__(self, query_string):
#         self.api_url = "https://translate.google.cn"
#         self.query_string = query_string
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0"
#         }
#
#     def get_url_param_data(self):
#         url_param_part = self.api_url + "/translate_a/single?"
#         url_param = url_param_part + "client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=btn&ssel=3&tsel=3&kc=0&"
#         url_get = url_param + "tk=" + str(self.get_tk()) + "&q=" + str(self.get_query_string())
#         print(url_get)
#         return url_get
#
#     def get_query_string(self):
#         query_url_trans = urllib.parse.quote(self.query_string)  # 汉字url编码
#         return query_url_trans
#
#     def get_tkk(self):
#         part_jscode_2 = "\n" + "return TKK;"
#         tkk_page = requests.get(self.api_url, headers=self.headers)
#         tkk_code = BeautifulSoup(tkk_page.content, 'lxml')
#         patter = re.compile(r'(TKK.*?\);)', re.I | re.M)
#         part_jscode = re.findall(patter, str(tkk_code))
#         print(part_jscode[0])
#         js_code = part_jscode[0] + part_jscode_2
#         with open("D:/googletranslate.js", "w")  as  f:
#             f.write(js_code)
#             f.close
#         tkk_value = execjs.compile(open(r"D:/googletranslate.js").read()).call('eval')
#         print(tkk_value)
#         return tkk_value
#
#     def get_tk(self):
#         tk_value = execjs.compile(open(r"D:/googletranslate_1.js").read()).call('tk', self.query_string, self.get_tkk())
#         print(tk_value)
#         return tk_value
#
#     def parse_url(self):
#         response = requests.get(self.get_url_param_data(), headers=self.headers)
#         return response.content.decode()
#
#     def get_trans_ret(self, json_response):
#         dict_response = json.loads(json_response)
#         ret = dict_response[0][0][0]
#         print(ret)
#
#     def run(self):
#         json_response = self.parse_url()
#         self.get_trans_ret(json_response)
#
#
# if __name__ == "__main__":
#     query_string = "Google 翻译是谷歌公司提供一项免费的翻译服务，可提供 80 种语言之间的即时翻译，支持任意两种语言之间的字词、句子和网页翻译"
#     google = Translate(query_string)
#     google.run()
# import requests
# base_url = 'http://www.liuyanlin.cn/google_translate?sl=en&tl=zh-Ch&wd='
# wd='china'
# url = base_url + wd
# print(url)
# r = requests.get(url).text
# print(r)
# 导入需要的库
import urllib.request

import urllib.parse
import json
import time
import random
import hashlib
import re
import pandas as pd
import random
def translate(content):
    # content = input('请输入需要翻译的句子：')
    print(type(content))
    print('content',content)

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    data = {}

    # u = 'fanyideskweb'
    # d = content
    # f = str(int(time.time() * 1000) + random.randint(1, 10))
    # c = 'rY0D^0\'nM0}g5Mm1z%1G4'
    #
    # sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1517053104119'
    data['sign'] = 'e253254497b96c2c1c8e31ce8d6c13d1'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CL1CKBUTTON'
    data['typoResult'] = 'true'

    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=url, data=data, method='POST')
    response = urllib.request.urlopen(request)
    content =response.read().decode('utf-8')
    regular = re.compile('tgt":"(.*)"')
    result = re.search(regular,content)
    translate = result.group(1)
    # translate = json.loads(content[translateResult][0][0])['tgt']
    return translate
if __name__ == '__main__':
    countries = pd.read_csv('country.csv')
    countries = countries.values
    countries = countries.tolist()
    f = open('results.txt','w',encoding='utf8')
    unsolved_country = []
    i=0
    for country in countries:
        try:
            country = country[0]
            print('开始处理'+country)
            time.sleep(random.randint(0,15))
            result = translate(country)
            str = country+':'+result+'\n'
            f.write(str)
            i+=1
            print('处理完成' + country)
        except:
            unsolved_country.append(country)
    f.write(json.dumps(unsolved_country))
    f.close()

