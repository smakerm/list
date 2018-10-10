# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:41:06 2018

@author: Administrator
"""

import hashlib

def hashStr(strInfo):
    """
    对字符串进行hash,得到一个16进制的指纹数据
    """
    h = hashlib.md5()
    h.update(strInfo.encode("utf-8"))
    return h.hexdigest()

#print(hashStr("hello"))
#5d41402abc4b2a76b9719d911017c592
#print(hashStr("hello1"))
#203ad5ffa1d7c650ad681fdff3965cd2

CHUCKSIZE = 2048
def hashFile(fileName):
    """
    对文件进行hash,得到一个16进制的指纹数据
    """   
    h = hashlib.sha256()
    with open(fileName, "rb") as f:
        while True:
            chunk = f.read(CHUCKSIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()
    
print(hashFile("Note.txt"))
#a5e30a7feae991c058f55f3bd0277307b9e55f12d295acbb3be3fc9f94d6a6c8

    