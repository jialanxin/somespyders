# coding: utf-8
"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets beijing shanghai 2016-08-25
"""

import requests
from docopt import docopt
from stations import stations
from prettytable import PrettyTable
from  colorama import Fore


def cli():
    arguments = docopt(__doc__, version='Tickets 1.0')
    from_station = stations.get(arguments.get('<from>'), None)
    to_station = stations.get(arguments.get('<to>'), None)
    date = arguments.get('<date>')
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, from_station, to_station)
    r = requests.get(url, verify=False)
    pt = PrettyTable()
    pt._set_field_names('车次 车站 时间 历时 一等座 二等座 软卧 硬卧 硬座 无座'.split())
    raw_trains = r.json()['data']['result']
    for raw_train in raw_trains:
        data_list = raw_train.split('|')
        train_na = data_list[3]
        from_station_code = data_list[6]
        to_station_code = data_list[7]
        from_station_name = ''
        to_station_name = ''
        start_time = data_list[8]
        arrive_time = data_list[9]
        time_duration = data_list[10]
        first_class_seat = data_list[31] or '--'
        second_class_seat = data_list[30] or '--'
        soft_sleep = data_list[23] or '--'
        hard_sleep = data_list[28] or '--'
        hard_seat = data_list[29] or '--'
        no_seat = data_list[26] or '--'
        pt.add_row([train_na, '\n'.join([Fore.GREEN+from_station_code+Fore.RESET, Fore.RED+to_station_code+Fore.RESET]), '\n'.join([Fore.GREEN+start_time+Fore.RESET, Fore.RED+arrive_time+Fore.RESET]), time_duration,
                    first_class_seat, second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat])
    print(pt)

if __name__ == '__main__':
    cli()
