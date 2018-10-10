# -*- coding: utf-8 -*-
"""
Created on Mon May 28 10:46:42 2018

@author: Administrator
"""

# 日志
import logging
import sys

# 创建日志的实例
logger = logging.getLogger("testLogger")

# 定制Logger的输出格式
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

# 创建日志:文件日志，终端日志
file_handler = logging.FileHandler('testLogger.log')
file_handler.setFormatter(formatter)

consle_handler = logging.StreamHandler(sys.stdout)
consle_handler.setFormatter(formatter)

# 设置默认的日志级别
logger.setLevel(logging.INFO)

# 把文件日志和终端日志添加到日志处理器中
logger.addHandler(file_handler)
logger.addHandler(consle_handler)

logger.critical("Test Critical log")
logger.error("Test Error log")
logger.warning("Test Warning log")
logger.info("Test Info log")
logger.debug("Test Debug log")

# 当不再使用这个日志Handler时，记得要remove
logger.removeHandler(file_handler)
logger.removeHandler(consle_handler)



