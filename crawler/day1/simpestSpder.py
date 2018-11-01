# from urllib import request
#
# req = request.Request("http://www.sina.com.cn")
#
# response = request.urlopen(req)
#
# print(response.read().decode())
#

import requests

response = requests.get('http://www.sina.com.cn')
response.encoding = 'utf-8'
print(response.text)