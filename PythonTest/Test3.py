###############################################定位方式########################################################################
from selenium import webdriver

import os,time  #调入time函数

browser = webdriver.Chrome("C:\Users\K-chico\AppData\Local\Google\Chrome\Application\chromebrowser.exe")

browser.get("http://www.baidu.com")

#file_path =  'file:///' + os.path.abspath('checkbox.html')
#dr.get(file_path)
time.sleep(2)

#########百度输入框的定位方式##########

#通过id方式定位
browser.find_element_by_id("kw").send_keys("selenium")

#通过name方式定位
browser.find_element_by_name("wd").send_keys("selenium")

#通过tag name方式定位
browser.find_element_by_tag_name("input").send_keys("selenium")

#通过class name 方式定位
browser.find_element_by_class_name("s_ipt").send_keys("selenium")

#通过CSS方式定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")

#通过xphan方式定位
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

############################################

browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()

###############################################定位方式########################################################################


#xpath:attributer （属性）

browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

#input标签下id =kw的元素

 

#xpath:idRelative （id相关性）

browser.find_element_by_xpath("//div[@id='fm']/form/span/input").send_keys("selenium")

#在/form/span/input 层级标签下有个div标签的id=fm的元素

browser.find_element_by_xpath("//tr[@id='check']/td[2]").click() 

# id为'check' 的tr ，定闪他里面的第2个td

 

#xpath:position （位置）

browser.find_element_by_xpath("//input").send_keys("selenium") 

browser.find_element_by_xpath("//tr[7]/td[2]").click()

#第7个tr 里面的第2个td

 

#xpath: href （水平参考）

browser.find_element_by_xpath("//a[contains(text(),'网页')]").click()

#在a标签下有个文本（text）包含（contains）'网页' 的元素

 

#xpath:link

browser.find_element_by_xpath("//a[@href='http://www.baidu.com/']").click()

#有个叫a的标签，他有个链接href='http://www.baidu.com/ 的元素


browser.find_element_by_link_text("贴 吧").click()

#link 定位

browser.find_element_by_partial_link_text("贴").click()

#通过find_element_by_partial_link_text() 函数，我只用了“贴”字，脚本一样找到了"贴 吧" 的链接

# 选择页面上所有的input，然后从中过滤出所有的checkbox并勾选之
inputs = browser.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
time.sleep(2)

# 选择所有的checkbox并全部勾上
checkboxes = browser.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(2)

# 打印当前页面上有多少个checkbox
print len(browser.find_elements_by_css_selector('input[type=checkbox]'))
time.sleep(2)
# 把页面上最后1个checkbox的勾给去掉
browser.find_elements_by_css_selector('input[type=checkbox]').pop().click()
###############################################层及定位#######################################################################
#点击Link1链接（弹出下拉列表）
browser.find_element_by_link_text('Link1').click()
from selenium.webdriver.support.ui import WebDriverWait
#找到id 为dropdown1的父元素
WebDriverWait(browser, 10).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())#在父亲元件下找到link为Action的子元素
menu = browser.find_element_by_id('dropdown1').find_element_by_link_text('Action')

#鼠标定位到子元素上
webdriver.ActionChains(browser).move_to_element(menu).perform()

time.sleep(2)

browser.quit()
################################################上传文件########################################################################
#脚本要与upload_file.html同一目录
file_path =  'file:///' + os.path.abspath('upload_file.html')
webdriver.get(file_path)

#定位上传按钮，添加本地文件
webdriver.find_element_by_name("file").send_keys('D:\\selenium_use_case\upload_file.txt')
time.sleep(2)

webdriver.quit()