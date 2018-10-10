# -*- coding: utf-8 -*-
"""
Created on Mon May 28 09:45:27 2018

@author: Administrator
"""

from selenium import webdriver
import time

# 打开浏览器，进入百度指数首页
url = "http://index.baidu.com/?from=pinzhuan#/"
browser = webdriver.Chrome()
browser.get(url)

# 完成登录的过程
browser.find_element_by_class_name('username-text').click()
time.sleep(1)
browser.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('quickzhao3223@hotmail.com')
browser.find_element_by_id('TANGRAM__PSP_4__password').send_keys('1981abc')
browser.find_element_by_id('TANGRAM__PSP_4__submit').click()

# 找到百度指数的搜索框，输入关键词，点击搜索按钮；
# 对图表数据不好抓，可以截图
browser.find_elements_by_class_name('search-input')[0].send_keys("Python爬虫")
#browser.find_elements_by_class_name('search-input-cancle')[0].click()
time.sleep(1)
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(1)
browser.save_screenshot("baiduIndex.png")


