# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome("C:\Users\K-chico\AppData\Local\Google\Chrome\Application\chromedriver.exe")
browser.get("http://www.yahoo.com")
assert "Yahoo!" in browser.title
elem = browser.find_element_by_name("p")
elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(0.2)
try:
    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
finally:
    browser.close()