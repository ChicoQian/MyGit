#coding=utf-8
from selenium import webdriver
import time

#访问百度
driver = webdriver.Chrome("C:\Users\K-chico\AppData\Local\Google\Chrome\Application\chromedriver.exe")
driver.get("http://www.baidu.com")

#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

#将页面滚动条拖到底部
js="var q=document.body.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)


#将滚动条移动到页面的顶部
js="var q=document.body.scrollTop=0"
driver.execute_script(js)
time.sleep(3)

driver.quit()


###############################################下拉框-为了选择定位两次#######################################################################

#-*-coding=utf-8

from selenium import webdriver

import os,time

driver= webdriver.Firefox()

file_path =  'file:///' + os.path.abspath('drop_down.html')

driver.get(file_path)

time.sleep(2)

m=driver.find_element_by_id("ShippingMethod")

m.find_element_by_xpath("//option[@value='10.69']").click()

time.sleep(3)

driver.quit()