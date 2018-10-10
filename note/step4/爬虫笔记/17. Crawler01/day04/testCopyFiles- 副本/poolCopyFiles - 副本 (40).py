# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:45:57 2018

@author: Administrator
"""

#把某一个文件夹下面的文件拷贝
#到另一个文件夹下面；文件个数不能少于1000个，
#文件的类型需要有多种，图片，视频，压缩文件，文本文件，
#二进制文件等等；
#使用多进程，多线程，进程池或线程池；
#怎么证明你拷贝的文件没有错误（使用HASH）；
#可以考虑加进度条；
import os

def copyFile(fileName, srcPath, destPath):
    # 如果源路径不存在
    if not os.path.exists(srcPath):
        print("scrPath %s is not exist"%srcPath)
        return False
    
    # 如果目标路径不存在
    if not os.path.exists(destPath):
        try:
            os.mkdir(destPath)
        except:
            print("destPath %s make error"%destPath)
            return False
    
    # 构造源文件路径名和目标文件路径名
    srcFileName = srcPath+'/'+fileName
    destFileName = destPath+'/'+fileName
    
    # 拷贝文件的过程
    with open(srcFileName, 'rb') as fr:
        with open(destFileName, 'wb') as fw:
            for i in fr:
                fw.write(i)
    
    return True

copyFile('baiduSearch.html', "C:/Users/Administrator/Desktop/爬虫/第四天",
         "C:/Users/Administrator/Desktop/爬虫/第四天/testCopyFiles2")
