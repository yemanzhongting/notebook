# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/12/1 19:42'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 两种方法任选其一，都是指向同一个文件
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

import time,random
driver=webdriver.Chrome(executable_path=r'E:\Githubresponsity\notebook\12.1\chromedriver.exe')

driver.set_window_size(1000,30000)

driver.get('https://weibo.cn/pub/')

driver.find_element_by_xpath('/html/body/div[2]/div/a[1]').click()


name_xpath='//*[@id="loginname"]'
pass_xpath='//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input'

name='838044557@qq.com'
pass_='whu3.13'

time.sleep(3)
login_xpath='//*[@id="pl_login_form"]/div/div[3]/div[6]/a'

# try:
#     element=WebDriverWait(driver,5).until(
#         EC.presence_of_element_located((By.ID,'loginname'))
#     )
# except:
#     driver.quit()

#driver.implicitly_wait(1)

#ALF=1577794254; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW_U-piXhYkoCDoBcSWvGnm5JpX5K-hUgL.Fo-ESKnNeh5pShM2dJLoI0qLxKBLB.BL1-eLxK-LBo5L12qLxK-LB-qL1KzLxK-L1KqLBo-LxK-L1KqLBo-LxK-LB.eLBK5t; _T_WM=96218712805; SCF=Arnxjp0L_i1cDcGLDQ7dciPttPY2-QiWWf-ofMEjBGtJ0cRPPJAo6ERVXWpX-TpaE0wlBTRH9sXr78_KFXUtwzw.; SUB=_2A25w594CDeRhGeNM7loW8C7NzzuIHXVQK-JKrDV6PUJbktAKLRTukW1NSa5q35Ob8J8S-NOdwP1CCdiU4tAQz-om; SUHB=0U1Zn80fIE2ZbA

# for cookie in bdcookie:
#     driver.add_cookie({
#             "domain":".baidu.com",
#             "name":cookie,
#             "value":bdcookie[cookie],
#             "path":'/',
#             "expires":None
#         })

# lists = cookie.split(';')
# bdcookie = {}
# for i in lists:
#     j = i.strip()
#     j = j.split('=')
#     bdcookie[j[0]] = j[1]

#driver.find_element_by_xpath('//*[@id="loginName"]').click()

driver.find_element_by_xpath('//*[@id="loginName"]').send_keys(name)
driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys(pass_)
driver.find_element_by_xpath('//*[@id="loginAction"]').click()

time.sleep(2)
driver.save_screenshot('a.png')

driver.get('https://weibo.com/')
driver.find_element_by_xpath('//*[@id="plc_top"]/div/div/div[2]/a').click()

driver.get('https://m.weibo.cn/p/index?containerid=23065700428008635010000000000&luicode=10000011&lfid=100103type%3D1%26q%3D%E7%A6%8F%E5%B7%9E%E5%A4%A7%E9%9B%A8')

for cookie in driver.get_cookies():
    print("%s=%s;"%(cookie['name'],cookie['value']))

driver.get('https://s.weibo.com/weibo?q=%E7%A6%8F%E5%B7%9E&Refer=index')

driver.find_element_by_xpath('//*[@id="pl_feedtop_top"]/div[3]/a').click()

#执行js
js = 'document.querySelector("body > div.m-layer > div.inner > div > div:nth-child(1) > dl.time.clearfix > dd > input[type=text]:nth-child(1)").removeAttribute("readonly")'#"$('input:eq(0)').removeAttr('readonly')"  # jQuery，移除属性
# js = "$('input:eq(0)').attr('readonly',false)"  # jQuery，设置为false
#document.querySelector("body > div.m-layer > div.inner > div > div:nth-child(1) > dl.time.clearfix > dd > select:nth-child(2)").removeAttribute('readonly')
driver.execute_script(js)

#执行js
js = 'document.querySelector("body > div.m-layer > div.inner > div > div:nth-child(1) > dl.time.clearfix > dd > input[type=text]:nth-child(3)").removeAttribute("readonly")'#"$('input:eq(0)').removeAttr('readonly')"  # jQuery，移除属性
# js = "$('input:eq(0)').attr('readonly',false)"  # jQuery，设置为false
#document.querySelector("body > div.m-layer > div.inner > div > div:nth-child(1) > dl.time.clearfix > dd > select:nth-child(2)").removeAttribute('readonly')
driver.execute_script(js)

# selector = Select(driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/dl[2]/dd/label[3]'))#find_element_by_id("selectdemo"))
#
# # 下面三种方法用于选择"篮球运动员"
# #selector.select_by_index("2")  # 通过index进行选择,index从0开始
# #selector.select_by_value("210103")  # 通过value属性值进行选择
# selector.select_by_visible_text("原创")  # 通过标签显示的text进行选择

driver.find_element_by_xpath('//*[@id="radio03"]').click()

driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/dl[4]/dd/input[1]').clear()
driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/dl[4]/dd/input[1]').send_keys('2019-12-01')

driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/dl[4]/dd/input[2]').clear()
driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/dl[4]/dd/input[2]').send_keys('2019-12-02')

sel=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/dl[5]/dd/select[1]')
#driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/dl[4]/dd/input[1]').clear()
Select(sel).select_by_visible_text('福建')
sel=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/dl[5]/dd/select[2]')
#driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/dl[4]/dd/input[2]').clear()
Select(sel).select_by_visible_text('福州')

#/html/body/div[7]/div[2]/div/div[1]/dl[4]/dd/select[1]
sel=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/dl[4]/dd/select[1]')
Select(sel).select_by_visible_text('8时')
sel=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/dl[4]/dd/select[2]')
Select(sel).select_by_visible_text('8时')

driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[2]/a[1]').click()

# count=0
# for i in range(20):
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#
#     e_item = driver.find_elements_by_xpath('//*[@class="card-list"]//div[@class="weibo-text"]')
#     #e_item = driver.find_elements_by_xpath('//*[@class="card-list"]//div[@class="weibo-text"]')
#
#     if i !=0:
#         print('\n'.join([e.text for e in e_item[-27:]]))
#         count =count+10
#     else:
#         print('\n'.join([e.text for e in e_item]))
#         count = count + 27
#     time.sleep(random.uniform(3,5))
#
#
#
# #e_item = driver.find_elements_by_xpath('//div[@class="result c-container "]')
#
# #    test=driver.find_element_by_xpath('//*[@class="weibo-text"]/text()')#('//*[@class="weibo-text"]')
#     #print(test)
#
# driver.quit()



