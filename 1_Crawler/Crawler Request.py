#coding=utf-8
#Request获得网页信息的解析方法

'''未解决的问题：
1、需要用户名和登录名的网站爬取
2、多线程的操作方式
3、反爬和反反爬的方式
4、模拟浏览器的方式
5、爬虫时间的设定
6、爬取后数据库存储问题
'''

#///////////////////////////////////////////
#1 静态数据

#1.1 BeautifulSoup解析方法
#BeautifulSoup 中文文档  https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
url='www.baidu.com'

response=requests.get(url,headers=headers)
soup=bs(responds.content,'html.parse')
divs=soup.find_all('div',id='123',class_='321')
Lists=[]
for div in divs:
  List={}
  try:
    List['name']=div.find_all('a', target='_blank')[0].get('title')
    List['country'] = div.find_all('span')[0].get_text()
    Lists.append(List)
  except:
    print('wrong')

totallist=pd.DataFrame(Lists)
print (totallist)
totallist.to_csv('baidu.txt')
print('...............')

#1.2 lxml解析方法
# lxml 官方文档 https://lxml.de/index.html
# lxml 中文教程 https://www.cnblogs.com/ospider/p/5911339.html

import requests
from lxml import tree
import pandas as pd
url='www.baidu.com'

response=requests.get(url)
html = etree.HTML(response.text)    #html=etree.parse('desktop/baidu.html')
divs= html.xpath('//div[@class = "clearfix"]')
Lists=[]
for div in divs:
  List={}
  try:
    List['name']=div.xpath('./div[@class="content"/text()]')[0]
    List['country'] = div.xpath('./td/text()]')[3]
    Lists.append(List)
  except:
    print('wrong')

totallist=pd.DataFrame(Lists)
print (totallist)
totallist.to_csv('baidu.txt')
print('...............')

#2.Ajax数据解析 Json解析
#JsonPath教程 https://blog.csdn.net/luxideyao/article/details/77802389
import requests
import json
import jsonpath
import pandas as pd

url='www.baidu.com'
response=requests.get(url,headers=headers)
dic=json.loads(response.text)
Lists=[]
for j in range(10):
    company = {}
    company['realname']=jsonpath.jsonpath(dic,'$..realname')[j]
    company['title']=jsonpath.jsonpath(dic,'$..title')[j]
    Lists.append(company)

totallist=pd.DataFrame(list)
print (totallist)
totallist.to_csv('baidu.txt')

#3.API数据解析
