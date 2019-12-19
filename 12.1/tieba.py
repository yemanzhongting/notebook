# -*- coding: UTF-8 -*-
import os
import pickle

__author__ = 'zy'
__time__ = '2019/12/5 14:13'
from selenium import webdriver
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 两种方法任选其一，都是指向同一个文件
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

import time,random,json

cookie='TIEBA_USERTYPE=744b29c1c38a9afa821f4b98; bdshare_firstime=1552222831079; BAIDUID=DCB87A3A6A7D1E0B39AE49D75624928D:FG=1; BIDUPSID=DCB87A3A6A7D1E0B39AE49D75624928D; PSTM=1550837224; MCITY=-218%3A; BDUSS=TFNeUlBfm8tZ3R0VUtpNVRiQ2NqTDRtMEFOS3lubDlkSUc5SlZuaWVUREZoUGhkRVFBQUFBJCQAAAAAAAAAAAEAAACv0aBWemhhbmc5OTllAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMX30F3F99BdM; TIEBAUID=b202ce2227d77bae26f7e6de; STOKEN=c45d6d04de4ecd92d7f5dff7c853402cb0b34c310d79494641c88ec914816543; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1573538842,1574132882,1574133360,1575011399; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=6285279232; delPer=0; PSINO=6; H_PS_PSSID=1425_21112_30211_18560_30192_22159; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1574132881,1574133359,1575011399,1575526396; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1575526396'
lists = cookie.split(';')
bdcookie = {}
for i in lists:
    j = i.strip()
    j = j.split('=')
    bdcookie[j[0]] = j[1]

driver=webdriver.Chrome(executable_path=r'E:\Githubresponsity\notebook\12.1\chromedriver.exe')

driver.get('https://tieba.baidu.com')

for cookie in bdcookie:
    driver.add_cookie({
            "domain":".baidu.com",
            "name":cookie,
            "value":bdcookie[cookie],
            "path":'/',
            "expires":None
        })

driver.get('https://tieba.baidu.com/')

driver.find_element_by_xpath('//*[@id="onekey_sign"]/a').click()

driver.find_element_by_xpath('//*[@id="dialogJbody"]/div/div/div[1]/a').click()
driver.quit()

# req=requests.get('http://tieba.baidu.com/i/i/forum?&pn=1',cookie=cookie)
# print(req.content)

# wait = WebDriverWait(driver, 10)
#
# def getBDCookies():
#     # get login taobao cookies
#     url = "https://tieba.baidu.com/"
#     driver.get("https://passport.baidu.com/v2/?login")
#     driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__footerULoginBtn"]').click()
#     driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__userName"]').clear()
#     driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__userName"]').send_keys('15518288378')
#     driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__password"]').clear()
#     driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__password"]').send_keys('bdwp3.13')
#
#     driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__submit"]').click()
#
#     while True:
#         print("Please login in com!")
#         time.sleep(1)
#         # if login in successfully, url  jump to www.taobao.com
#         while driver.current_url ==  url:
#             tbCookies  = driver.get_cookies()
#             driver.quit()
#             cookies = {}
#             for item in tbCookies:
#                 cookies[item['name']] = item['value']
#                 outputPath = open('BDCookies.pickle','wb')
#             pickle.dump(cookies,outputPath)
#             outputPath.close()
#             return cookies
# def readbdCookies():
#     # if hava cookies file ,use it
#     # if not , getTaobaoCookies()
#     if os.path.exists('BDCookies.pickle'):
#         readPath = open('BDCookies.pickle','rb')
#         tbCookies = pickle.load(readPath)
#     else:
#         tbCookies = getBDCookies()
#     return tbCookies
#
# tbCookies = readbdCookies()
#
# driver.get("https://tieba.baidu.com/")
# for cookie in tbCookies:
#     driver.add_cookie({
#         "domain":".baidu.com",
#         "name":cookie,
#         "value":tbCookies[cookie],
#         "path":'/',
#         "expires":None
#     })
# driver.get("https://tieba.baidu.com/")




#cookies = json.dumps(cookies)

# 1 from selenium import webdriver
#  2 import time
#  3
#  4 #driver1登录网站，获得cookie并保存
#  5 driver1 = webdriver.Chrome()
#  6 driver1.get("https://www.ketangpai.com/User/login.html")
#  7 driver1.maximize_window()
#  8 time.sleep(2)
#  9
# 10 #第一次通过send_keys向输入框发送用户名密码登录
# 11 driver1.find_element_by_xpath("//input[@name='account']").send_keys("your username")
# 12 driver1.find_element_by_xpath("//input[@name='pass']").send_keys("your password")
# 13 time.sleep(2)
# 14 driver1.find_element_by_xpath("//div[@class='padding-cont pt-login']//a[@class='auto-login fl']").click()
# 15 time.sleep(3)
# 16 driver1.find_element_by_xpath("//div[@class='padding-cont pt-login']//a[@class='btn-btn']").click()
# 17 time.sleep(6)
# 18 #用get_cookies的方法得到登录后的cookie，这个cookie是个列表，列表中两个元素都是字典，第一个是登录前的cookie，第二个是登录后的cookie
# 19 #将cookie保存在变量savedCookies中
# 20 savedCookies = driver1.get_cookies()
# 21 print(savedCookies)
# 22
# 23 #driver2得到driver1的cookie,先删除自己的所有cookie,再将driver1的cookie添加进来
# 24 driver2 = webdriver.Chrome()
# 25 #必须首先加载网站，这样selenium才知道cookie是属于哪个网站的
# 26 driver2.get("https://www.ketangpai.com/User/login.html")
# 27 #一旦加载网站，即使没登录，也会产生一个cookie，所以这个cookie被删除了
# 28 driver2.delete_all_cookies()
# 29 #遍历savedCookies中的两个元素
# 30 for cookie in savedCookies:
# 31     #k代表着add_cookie的参数cookie_dict中的键名，这次我们要传入这5个键
# 32     for k in {'name', 'value', 'domain', 'path', 'expiry'}:
# 33         #cookie.keys()属于'dict_keys'类，通过list将它转化为列表
# 34         if k not in list(cookie.keys()):
# 35             #saveCookies中的第一个元素，由于记录的是登录前的状态，所以它没有'expiry'的键名，我们给它增加
# 36             if k == 'expiry':
# 37                 t = time.time()
# 38                 cookie[k] = int(t)    #时间戳s
# 39     #将每一次遍历的cookie中的这五个键名和键值添加到cookie
# 40     driver2.add_cookie({k: cookie[k] for k in {'name', 'value', 'domain', 'path', 'expiry'}})
# 41
# 42 #加载我们想要看到的页面的url
# 43 driver2.get("https://www.ketangpai.com/Main/index.html")
# 44 #再次打印driver2的cookie
# 45 print(driver2.get_cookies())