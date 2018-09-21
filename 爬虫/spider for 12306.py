
import requests
import stations1
from prettytable import PrettyTable
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
def cli():
    str = input("请输入出发站: ");
    str1 = input("请输入到达站: ");
    date = input("请输入出发日期(格式xxxx-xx-xx): ");
    options = input("请输入列车类型（格式g、d、t、k、z）: ");
    from_station = stations1.get_telecode(str)#查找相应站点的代号
    to_station = stations1.get_telecode(str1)
    url = ('https://kyfw.12306.cn/otn/leftTicket/queryO?'
          'leftTicketDTO.train_date={}&'
          'leftTicketDTO.from_station={}&'
          'leftTicketDTO.to_station={}&'
          'purpose_codes=ADULT').format(date,from_station,to_station)
    r = requests.get(url, verify=False)
    raw_trains = r.json()['data']['result']
    pt = PrettyTable()
    pt._set_field_names('车次 车站 时间 历时 商务座 一等座 二等座 动卧 软卧 硬卧 硬座 无座'.split())
    for raw_train in raw_trains:
        data_list = raw_train.split('|')
        train_no = data_list[3]
        initial = train_no[0].lower()
        if not options or initial in options:
            from_station_code = data_list[6]
            to_station_code = data_list[7]
            from_station_name = ''
            to_station_name = ''
            start_time = data_list[8]
            arrive_time = data_list[9]
            time_duration = data_list[10]
            business_seat = data_list[32] or '--'
            first_class_seat = data_list[31] or '--'
            second_class_seat = data_list[30] or '--'
            pneumatic_sleep = data_list[33] or '--'
            soft_sleep = data_list[23] or '--'
            hard_sleep = data_list[28] or '--'
            hard_seat = data_list[29] or '--'
            no_seat = data_list[26] or '--'
            pt.add_row([train_no,
                    '\n'.join([stations1.get_name(from_station_code), stations1.get_name(to_station_code)]),
                    '\n'.join([start_time, arrive_time]),
                    time_duration,
                    business_seat,
                    first_class_seat,
                    second_class_seat,
                    pneumatic_sleep,
                    soft_sleep,
                    hard_sleep,
                    hard_seat,
                    no_seat
            ])
    print(pt)
 
if __name__ == '__main__':
    cli()

