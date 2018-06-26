import requests
from lxml import etree
import time
import csv
import itchat


localtime = time.localtime(time.time())
now = time.asctime(localtime)
print(now)
r = requests.get('http://www.boc.cn/sourcedb/whpj/')
html = etree.HTML(r.content.decode('utf-8'))
data = html.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/table/tr[27]/td[5]//text()')
itchat.auto_login(enableCmdQR=True)
itchat.send(data[0], toUserName='filehelper')
#f = open('dataset.csv','a')
#writer = csv.writer(f)
#writer.writerow([now,data])
# f.close()
#/body/div[1]/div[5]/div[1]/div[2]/table/tbody/tr[27]/td[5]