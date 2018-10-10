# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:36:36 2018

@author: Administrator
"""

from http import cookiejar
from urllib import request
from urllib import parse

# 创建一个Cookiejar对象
cookie = cookiejar.CookieJar()

# 通过HTTPCookieProcessor处理cookiejar
cookie_handler = request.HTTPCookieProcessor(cookie)

# 构建一个opener
opener = request.build_opener(cookie_handler)
opener.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36")]

# 使用post的方式发送数据包,用来进行登录
url = "http://www.renren.com/SysHome.do"
data = {"email":"XXXX","password":"YYYY"}

data = bytes(parse.urlencode(data),encoding="utf-8")
req = request.Request(url, data=data, method="POST")
response = opener.open(req)

# 登录之后，打开自己的主页
responseMyrenren = opener.open("http://www.renren.com/961482489/profile")
with open("myRenrenWithCookiejar.html", "wb") as f:
    f.write(responseMyrenren.read())







