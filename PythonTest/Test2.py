# -*- coding: utf-8 -*-

from selenium import webdriver
import time  #调入time函数

browser = webdriver.Chrome("C:\Users\K-chico\AppData\Local\Google\Chrome\Application\chromedriver.exe")

url= 'http://www.baidu.com'
browser.get(url)
print browser.title  # 把页面title 打印出来
browser.maximize_window()  #将浏览器最大化显示
print "设置浏览器宽480、高800显示"
browser.set_window_size(480, 800)  #参数数字为像素点
time.sleep(0.3)  #休眠0.3秒
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)  # 休眠3秒
browser.quit()
################################################控制前进，后退########################################################################
#coding=utf-8

from selenium import webdriver
import time

browser = webdriver.Chrome("C:\Users\K-chico\AppData\Local\Google\Chrome\Application\chromedriver.exe")

#访问百度首页
first_url= 'http://www.baidu.com'
print "now access %s" %(first_url)
browser.get(first_url)
time.sleep(2)

#访问新闻页面
second_url='http://news.baidu.com'
print "now access %s" %(second_url)
browser.get(second_url)
time.sleep(2)

#返回（后退）到百度首页
print "back to  %s "%(first_url)
browser.back()
time.sleep(1)

#前进到新闻页
print "forward to  %s"%(second_url)
browser.forward()
time.sleep(2)

browser.quit()
################################################控制前进，后退########################################################################