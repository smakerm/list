# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:53:20 2018

@author: Administrator
"""
import urllib
import re

# GET请求的交互方式
ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
url = "http://www.baidu.com/s?"
keyword = input("请输入您需要搜索的信息:")
wd = {"wd":keyword}
wd = urllib.parse.urlencode(wd) #urlencode
fullUrl = url+wd
print(fullUrl) #http://www.baidu.com/s?wd=Python%E7%88%AC%E8%99%AB

# 对百度发起一次get请求
req = urllib.request.Request(fullUrl, headers=ua_headers)
response = urllib.request.urlopen(req)
#with open("baiduSearch.html", "wb") as f:
#    f.write(response.read())
    
# 使用正则来匹配百度的推荐
pattern = re.compile("""<a target="_blank" href='([\s\S]*?)'>([\s\S]*?)</a>""")
items = re.findall(pattern, response.read().decode('utf-8'))
#for it in items:
#    print(it[0], it[1])
with open("baiduSearch.txt", "a") as f:
    for it in items:
        f.write("推荐: "+it[1]+" 链接: "+it[0]+"\n")
    
#/s?wd=python3%E7%88%AC%E8%99%AB%E5%AE%9E%E4%BE%8B%E4%BB%A3%E7%A0%81&ie=utf-8&rsv_rq=2&rsv_cq=Python%E7%88%AC%E8%99%AB python3爬虫实例代码
#/s?wd=python%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&ie=utf-8&rsv_rq=2&rsv_cq=Python%E7%88%AC%E8%99%AB python爬虫基础
#/s?wd=Python%E7%88%AC%E8%99%AB%E5%B7%A5%E4%BD%9C&ie=utf-8&rsv_rq=2&rsv_cq=Python%E7%88%AC%E8%99%AB Python爬虫工作
#/s?wd=Python%E7%88%AC%E8%99%AB%E6%80%8E%E4%B9%88%E5%AD%A6&ie=utf-8&rsv_rq=2&rsv_cq=Python%E7%88%AC%E8%99%AB Python爬虫怎么学
#/s?wd=python%E7%88%AC%E8%99%AB%E7%A8%8B%E5%BA%8F&ie=utf-8&rsv_rq=2&rsv_cq=Python%E7%88%AC%E8%99%AB python爬虫程序
#/s?wd=python3%E7%88%AC%E8%99%AB&ie=utf-8&rsv_rq=2&rsv_cq=Python%E7%88%AC%E8%99%AB python3爬虫