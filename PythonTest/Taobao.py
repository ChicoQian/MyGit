# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome("C:\Users\K-chico\AppData\Local\Google\Chrome\Application\chromedriver.exe")
browser.get("https://www.taobao.com/")
browser.maximize_window()
elem = browser.find_element_by_id("q")
elem.send_keys(u"7 plus保护套" + Keys.RETURN)
time.sleep(2)
browser.find_element_by_id("J_Itemlist_TLink_538511644500").click()
time.sleep(2)
browser.get("https://login.taobao.com/member/login.jhtml?from=taobaoindex&f=top&style=&sub=true&redirect_url=https%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm")
browser.find_element_by_id("J_Quick2Static").click()
time.sleep(2)
#browser.get("https://auth.alipay.com/login/index.htm?loginScene=7&goto=https%3A%2F%2Fauth.alipay.com%2Flogin%2Ftaobao_trust_login.htm%3Ftarget%3Dhttps%253A%252F%252Flogin.taobao.com%252Fmember%252Falipay_sign_dispatcher.jhtml%253Ftg%253Dhttps%25253A%25252F%25252Fi.taobao.com%25252Fmy_taobao.htm%25253Fspm%25253Da230r.1.1997525045.1.1sinIX&params=VFBMX3JlZGlyZWN0X3VybD1odHRwcyUzQSUyRiUyRmkudGFvYmFvLmNvbSUyRm15X3Rhb2Jhby5odG0lM0ZzcG0lM0RhMjMwci4xLjE5OTc1MjUwNDUuMS4xc2luSVg%3D")

elem1 = browser.find_element_by_id("TPL_username_1")
elem1.send_keys(u"子羽睿敏")
time.sleep(2)
elem2 = browser.find_element_by_id("TPL_password_1")
time.sleep(2)
elem2.send_keys("z123456")
time.sleep(2)
browser.find_element_by_id("J_SubmitStatic").click()
#try:
#    browser.find_element_by_xpath("//li[contains(title(),'黑色')]").click()
#except NoSuchElementException:
#    assert 0, "can't find seleniumhq"
#finally:
 #   browser.close()