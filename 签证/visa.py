import requests
import re
import time
n=0
while True:
	my_file = open('my_file.txt','a')
	n+=1
	headers = {
		'Cookie':'BrowserId=W10rUO5uQXWw5ZVny_N8nQ; __utmz=1.1528463384.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); oinfo=c3RhdHVzPUFDVElWRSZ0eXBlPTYmb2lkPTAwREMwMDAwMDAwUGh1UA==; autocomplete=1; lloopch_loid=00DC0000000PhuP; lloopch_lpid=060C0000000QwL9; oid=00DC0000000PhuP; apex__aa-time=IS6fakgA7Fxko2mnu4GJSQ_3D_3D; __utma=1.1949805318.1528463384.1528536389.1528560604.3; __utmc=1; __utmt=1; __utmb=1.1.10.1528560604; sid=00DC0000000PhuP!ARwAQP2HkygAZEHf83ivDJA8Ax1.dQ9nPPLvDllsz4IATVcPbZ6rCHCtLApr4Hwd15jBHPS7S85gMH_oWTH0juGjkG8zGxV8; sid_Client=h00000FHOI80000000PhuP; clientSrc=221.6.40.200; inst=APP_0h',
		'Host':'cgifederal.secure.force.com',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
	} 
	r = requests.get('https://cgifederal.secure.force.com/applicanthome', headers = headers)
	date = re.search('<div.*?leftPanelText.*?&#20026;(.*?)</div>',r.text,re.S)
	localtime = time.localtime(time.time())
	now = time.asctime(localtime)
	print('for the %s time'%n)
	my_file.write('\n%s____%s'%(now,date.group(1)))
	my_file.close()
	time.sleep(30)