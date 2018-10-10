# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:04:05 2018

@author: Administrator
"""

import urllib
import re


#思考一下：怎么快速的判断一个代理服务器是可用的？
# 封装一个方法，来检测当前的这个代理服务器是否可用
def chechProxy(proxy_addr):
    data = ""
    url = "http://www.baidu.com"
    proxy = urllib.request.ProxyHandler({"http":proxy_addr})
    # 替换handler，以实现可以处理Proxy
    opener = urllib.request.build_opener(proxy)
    # 把opener装载进urllib库中，准备使用
    urllib.request.install_opener(opener)
    try:
        response = urllib.request.urlopen(url, timeout=10)   
        data = response.read().decode('utf-8')
    except:
        pass
    
    pattern = re.compile("<title>百度一下，你就知道</title>")
    title = re.findall(pattern, data)
    print(title)
    if len(title) == 0:#list的长度为0，说明没有获取到信息
        return False
    else:
        return True
    
print(chechProxy("185.106.121.98:1080"))
                 #"name:password@ip:port"    





