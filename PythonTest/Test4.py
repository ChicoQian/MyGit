# -*- coding: utf-8 -*-

from selenium import webdriver

import os,time

browser = webdriver.Chrome("C:\Users\K-chico\AppData\Local\Google\Chrome\Application\chromedriver.exe")

browser.get("http://www.baidu.com")


#进入搜索设置页

browser.find_element_by_link_text("搜索设置").click()


#设置每页搜索结果为100条

m=browser.find_element_by_name("NR")

m.find_element_by_xpath("//option[@value='100']").click()

time.sleep(2)


#保存设置的信息

browser.find_element_by_xpath("//input[@value='保存设置']").click()

time.sleep(2)

browser.switch_to_alert().accept()



#跳转到百度首页后，进行搜索表（一页应该显示100条结果）

browser.find_element_by_id("kw").send_keys("selenium")

browser.find_element_by_id("su").click()

time.sleep(3)

browser.quit()