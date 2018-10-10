# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:05:13 2018

@author: Administrator
"""

# POST请求的交互方式
from urllib import request,parse

youdaoUrl = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
           "X-Requested-With":"XMLHttpRequest", # 可以处理Ajax
           "Accept":"application/json, text/javascript, */*; q=0.01",# 可以接收json数据
           }
while True:
    key = input("请输入您要翻译的英文,输入CloseMe则退出:")
    if key == "CloseMe": # 输入CloseMe，则直接退出
        break
    
    formdata = {"i":key,
                "from":"AUTO",
                "to":"AUTO",
                "smartresult":"dict",
                "client":"fanyideskweb",
                "salt":"1527148862626",
                "sign":"547b8ff87043e3eecbc2d5446238fb4a",
                "doctype":"json",
                "version":"2.1",
                "keyfrom":"fanyi.web",
                "action":"FY_BY_REALTIME",
                "typoResult":"false"
            }
    # 做urlencode
    data = bytes(parse.urlencode(formdata), encoding="utf-8") # 由于post
    # 需要发送bytes类型的数据，所以这个地方需要转换成bytes
    req = request.Request(youdaoUrl, data, headers, method="POST")
    repsonse = request.urlopen(req)
    info = repsonse.read().decode("utf-8") # bytes -> json str
    print(info)# {"type":"EN2ZH_CN","errorCode":0,"elapsedTime":0,"translateResult":[[{"src":"hi","tgt":"嗨"}]]}
#i=hi&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=1527148862626&sign=547b8ff87043e3eecbc2d5446238fb4a&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTIME&typoResult=false
    