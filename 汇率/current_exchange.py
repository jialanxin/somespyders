import requests
import re
import time
from bs4 import BeautifulSoup
import csv

while True:
	localtime = time.localtime(time.time())
	now = time.asctime(localtime)
	print(now)
	r = requests.get('http://www.boc.cn/sourcedb/whpj/')
	soup = BeautifulSoup(r.content.decode('utf-8'),features='lxml')
	data = soup.body.contents[1].contents[13].contents[1].contents[-2].contents[-1].contents[-4].contents[7].string
	f = open('dataset.csv','a')
	writer = csv.writer(f)
	writer.writerow([now,data])
	f.close()
	time.sleep(300)
