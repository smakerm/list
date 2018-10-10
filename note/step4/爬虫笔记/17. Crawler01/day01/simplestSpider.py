# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:03:59 2018

@author: Administrator
"""
#import requests
#response = requests.get("http://www.sina.com.cn")
#response.encoding = 'utf-8'
##print(response.text)
#with open('sina.html', 'wb') as f:
#    f.write(response.text.encode('utf-8'))

from urllib import request
req = request.Request("http://www.sina.com.cn") # 构造request请求
response = request.urlopen(req)                 # 得到了response响应信息
#print(type(response.read()))                    #<class 'bytes'>
print(response.read().decode("utf-8"))


