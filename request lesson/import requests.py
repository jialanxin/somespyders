import requests
param = {'wd': '莫凡Python'}
r = requests.get('http://www.baidu.com/s', params=param)

data = {'firstname':'莫烦', 'lastname':'周'}
r = requests.post('http://pythonscraping.com/files/processing.php',data=data)
print(r.text)