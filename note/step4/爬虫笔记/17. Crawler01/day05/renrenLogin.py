# -*- coding: utf-8 -*-
"""
Created on Fri May 25 15:58:50 2018

@author: Administrator
"""

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.renren.com/")
driver.find_element_by_id('email').send_keys('yyyy')        # 用户名
driver.find_element_by_id('password').send_keys('xxxxxxxx') # 密码
driver.find_element_by_id('login').click()
#driver.find_element_by_id('sb_form_go').click()