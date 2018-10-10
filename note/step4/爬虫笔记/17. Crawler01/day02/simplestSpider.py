# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:11:38 2018

@author: Jun
"""

import requests

# http协议中 request请求，response
headers = {"User-Agent":"Mozilla/5.0(Windows NT 10.0)"}
response = requests.get("http://www.sina.com.cn",headers=headers)
print(response.status_code)