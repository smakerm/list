# -*- coding: utf-8 -*-
"""
Created on Mon May 28 17:25:39 2018

@author: Administrator
"""

import basicSpider

url = "http://www.sina.com.cn/"
headers = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36")]
proxy = {"http":"182.129.243.84:9000"}

with open("sina.html", "wb") as f:
    f.write(basicSpider.downloadHtml(url, headers, proxy).encode("utf-8"))
