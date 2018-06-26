import requests
from lxml import etree
import time


while True:
    localtime = time.localtime(time.time())
    now = time.asctime(localtime)
    print(now)
    r = requests.get('http://www.boc.cn/sourcedb/whpj/')
    html = etree.HTML(r.content.decode('utf-8'))
    data = html.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/table//text()')
    try : 
        position = data.index('美元')
        print(data[position+6])
        time.sleep(10)
    except :
        pass 
