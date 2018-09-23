import re
import os
os.chdir(r'C:\Users\outao\Desktop\work\爬虫')


#12306存放站点代号的地址需要自己分析出来
#url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9050'

#r = requests.get(url,verify=False)		   #提取网页信息，不判断证书
f=open('stations.txt','r')
text=f.read()
pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)' #正则表达式提取中文以及大写英文字母
result = re.findall(pattern,text)   #进行所需要的信息的提取
stations = dict(result)  #把所获信息设置为一一对应（有点像是c++里的map）
stations_codes=list(stations.values())
stations_names=list(stations.keys())

def get_telecode(d):
    return stations[d]

def get_name(code):
    return stations_names[stations_codes.index(code)]
    





