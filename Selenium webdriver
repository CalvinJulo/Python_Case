# coding=utf-8
# selenium 操作百度
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(executable_path ='/Users/zcglook/Documents/selenium/chromedriver')
driver.get('https://www.baidu.com')

print ('before search=========')

title=driver.title
print(title)

now_url=driver.current_url
print (now_url)

driver.find_element_by_id('kw').send_keys('陈荣杰')
driver.find_element_by_id('su').click()
sleep(5)

print ('After search========')

title =driver.title
print(title)

now_url=driver.current_url
print(now_url)

user=driver.find_element_by_class_name('nums_text').text
print(user)
driver.quit()
