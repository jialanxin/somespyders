import requests
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
import time


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'lanxin_jia@163.com'
password = '520693SYo'
to_addr = '171541975@qq.com'
smtp_server = 'smtp.163.com'
n = 1
try:
    while True:
        time.sleep(5)
        print('searching ' + '%s' % n + ' time')
        n = n + 1
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-18&leftTicketDTO.from_station=YLH&leftTicketDTO.to_station=NJH&purpose_codes=ADULT'
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url, verify=False)
        raw_trains = r.json()['data']['result']
        D5538 = raw_trains[-6]
        D5534 = raw_trains[-7]
        D5528 = raw_trains[-9]
        D5538_seat = D5538.split('|')
        D5534_seat = D5534.split('|')
        D5528_seat = D5528.split('|')
        D5538_order = D5538_seat[1]
        D5534_order = D5534_seat[1]
        D5528_order = D5528_seat[1]
        if D5538_order == '预定':
            msg = MIMEText('D5538有票了', 'plain', 'utf-8')

            msg['From'] = _format_addr('D5538有票了<%s>' % from_addr)
            msg['Subject'] = Header('D5538有票了', 'utf-8').encode()

            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, password)
            server.sendmail(from_addr, [to_addr], msg.as_string())
            server.quit()
            break
        if D5534_order == '预定':
            msg = MIMEText('D5534有票了', 'plain', 'utf-8')

            msg['From'] = _format_addr('D5534有票了<%s>' % from_addr)
            msg['Subject'] = Header('D5534有票了', 'utf-8').encode()

            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, password)
            server.sendmail(from_addr, [to_addr], msg.as_string())
            server.quit()
            break
        if D5528_order == '预定':
            msg = MIMEText('D5528有票了', 'plain', 'utf-8')

            msg['From'] = _format_addr('D5528有票了<%s>' % from_addr)
            msg['Subject'] = Header('D5528有票了', 'utf-8').encode()

            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, password)
            server.sendmail(from_addr, [to_addr], msg.as_string())
            server.quit()
            break
except ConnectionError as c:
    msg = MIMEText('Error', 'plain', 'utf-8')
    msg['From'] = _format_addr('Error<%s>' % from_addr)
    msg['Subject'] = Header('Error', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()