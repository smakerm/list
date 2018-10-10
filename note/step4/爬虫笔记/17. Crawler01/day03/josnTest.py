# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:41:37 2018

@author: Administrator
"""

import json

jsonDict = {'One':'1','Two':'2'}
# json encode
# dict --> json str
jsonDumps = json.dumps(jsonDict)
#print(type(jsonDumps))
#print(jsonDumps)
#<class 'str'>
#{"One": "1", "Two": "2"}

# json decode
# json str -> dict
jsonLoads = json.loads(jsonDumps)
#print(type(jsonLoads)) #<class 'dict'>
#for key,value in jsonLoads.items():
#    print(key,value)
#One 1
#Two 2
    
#strJson = '{"translateResult":[[{"tgt":"嗨","src":"hi"}]],"errorCode":0,"type":"en2zh-CHS","smartResult":{"entries":["","int. 嗨！（表示问候或用以唤起注意）\r\n","n. (Hi)人名；(柬)希\r\n"],"type":1}}'
#print(strJson)    
strJson1 = '{"translateResult":[[{"tgt":"你好","src":"hi"}]]}'   
jsonLoads = json.loads(strJson1)
#print(strJson1["translateResult"][0][0]["tgt"])
#print(strJson1["translateResult"][0][0]["src"])
#jsonLoads1 = json.loads(strJson)
#for key,value in jsonLoads1.item():
#    if key =="translateResult":
#        print(value[0][0]["tgt"])

print(type(jsonLoads))
print(jsonLoads["translateResult"][0][0]["tgt"])
