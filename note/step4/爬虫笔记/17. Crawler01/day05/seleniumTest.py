# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:51:53 2018

@author: Administrator
"""

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.bing.com")
time.sleep(2)
driver.find_element_by_id('sb_form_q').send_keys('区块链')
driver.find_element_by_id('sb_form_go').click()
with open("bingSearch.html", "wb") as f:
    f.write(driver.page_source.encode("utf-8"))
time.sleep(5)



#driver.quit()
#driver.close()
