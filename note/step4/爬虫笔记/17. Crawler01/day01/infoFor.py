# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 09:40:23 2018

@author: Jun
"""

# 0 and 'a' or 'b'
# 'b'
# 1 and 'a' or 'b'
# 'a'

import requests

def info(object, spacing=20, collapse=1):
    """
    按照一定的格式打印出模块及方法的详细意思
    """
    
    # 遍历一次object对象，把里面可以调用的方法提取出来
    methodList = [method for method in dir(object) 
    if callable(getattr(object, method))]
    
    #print(methodList)
    # collpase = 1,并行
    # collpase = 0,保持原来的格式
    processFunc = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
    
    # 打印出：左端是方法名，右端是说明文档
    print('\n'.join(["%s %s"%(method.ljust(spacing), processFunc(str(getattr(object, method).__doc__))) 
         for method in methodList]))

info(requests)