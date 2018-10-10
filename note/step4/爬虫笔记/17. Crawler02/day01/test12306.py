# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:37:19 2018

@author: Administrator
"""

import ssl # 安全套接层
import urllib

#自己保证网站证书的安全
context = ssl._create_unverified_context()

url = "https://www.12306.cn/mormhweb/"
ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

req = urllib.request.Request(url, headers=ua_headers)
response = urllib.request.urlopen(req,context=context)

with open("12306.html", "wb") as f:
    f.write(response.read())

