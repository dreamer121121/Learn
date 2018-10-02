import requests,re,datetime,time,json
from tkinter import*
from tkinter import messagebox
from datetime import timedelta,date
from prettytable import PrettyTable
from stationsInfo import stations_codes,stations_names
 
def getHtmltext(url,headers):
    r=requests.get(url,headers=headers)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r.text
 
def Show(html):
        html = json.loads(html)
        table = PrettyTable(
            ["车次", "出发/到达车站", "出发/到达时间", "历时", "商务座", "一等座", "二等座", "高级软卧", "软卧", "动卧", "硬卧", "软座", "硬座", "无座", "其他",
             "备注"])
        tickets = []
        for i in html['data']['result']:
            name = [
                "station_train_code",
                "from_station_name",
                'start_time',
                "lishi",
                "swz_num",
                "zy_num",
                "ze_num",
                "gr_num",
                "rw_num",
                "dw_num",
                "yw_num",
                "rz_num",
                "yz_num",
                "wz_num",
                "qt_num",
                "note_num"
            ]
            data = {
                "station_train_code": '',
                "from_station_name": '',
                "to_station_name": '',
                'start_time': '',
                'end': '',
                "lishi": '',
                "swz_num": '',
                "zy_num": '',
                "ze_num": '',
                "dw_num": '',
                "gr_num": '',
                "rw_num": '',
                "yw_num": '',
                "rz_num": '',
                "yz_num": '',
                "wz_num": '',
                "qt_num": '',
                "note_num": ''
            }
            item = i.split('|')  # 用"|"进行分割
            data['station_train_code'] = item[3]  # 车次在3号位置
            data['from_station_name'] = item[6]  # 始发站信息在6号位置
            data['to_station_name'] = item[7]  # 终点站信息在7号位置
            data['start_time'] = item[8]  # 出发时间信息在8号位置
            data['arrive_time'] = item[9]  # 抵达时间在9号位置
            data['lishi'] = item[10]  # 经历时间在10号位置
            data['swz_num'] = item[32] or item[25]  # 特别注意：商务座在32或25位置
            data['zy_num'] = item[31]  # 一等座信息在31号位置
            data['ze_num'] = item[30]  # 二等座信息在30号位置
            data['gr_num'] = item[21]  # 高级软卧信息在31号位置
            data['rw_num'] = item[23]  # 软卧信息在23号位置
            data['dw_num'] = item[27]  # 动卧信息在27号位置
            data['yw_num'] = item[28]  # 硬卧信息在28号位置
            data['rz_num'] = item[24]  # 软座信息在24号位置
            data['yz_num'] = item[29]  # 硬座信息在29号位置
            data['wz_num'] = item[26]  # 无座信息在26号位置
            data['qt_num'] = item[22]  # 其他信息在22号位置
            data['note_num'] = item[1]  # 备注在1号位置
            # 如果没有信息用'-'代替
            for pos in name:
                if data[pos] == '':
                    data[pos] = '-'
            cont = []
            cont.append(data)
            for x in cont:
                tmp = []
                for y in name:
                    if y == "from_station_name":
                        s = stations_names[stations_codes.index(data['from_station_name'])] + '--' +stations_names[stations_codes.index(data["to_station_name"])]
                        tmp.append(s)
                    elif y == "start_time":
                        s =data['start_time']+ '--' +data["arrive_time"]
                        tmp.append(s)
                    elif y == "station_train_code":
                        s =data['station_train_code']
                        tmp.append(s)
                    else:
                        tmp.append(data[y])
                tickets.append(tmp)
            """
            for ticket in tickets:
                table.add_row(ticket)
        print(table)
        """
        return tickets
def ShowTicket(from_station,to_station,date):
    time = str(date)
    from_station = from_station
    to_station = to_station
    url = "https://kyfw.12306.cn/otn/leftTicket/queryA?"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400"
    }
    # time=entry_time.get()
    # start=entry_start.get()
    # end=entry_end.get()
    url = url + 'leftTicketDTO.train_date=' + time + '&leftTicketDTO.from_station=' + from_station + '&leftTicketDTO.to_station=' + to_station + '&purpose_codes=ADULT'
    html = getHtmltext(url, headers)
    tickets=Show(html)
    return  tickets


