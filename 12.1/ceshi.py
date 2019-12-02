# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/12/1 20:22'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome(executable_path=r'E:\Githubresponsity\notebook\12.1\chromedriver.exe')

driver.set_window_size(1000,30000)

driver.get('https://m.weibo.cn/p/index?containerid=23065700428008635010000000000&luicode=10000011&lfid=100103type%3D1%26q%3D%E7%A6%8F%E5%B7%9E%E5%A4%A7%E9%9B%A8')#https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=selenium%E5%86%85%E5%AE%B9%E5%AE%9A%E4%BD%8D&oq=selenium%25E6%25BB%259A%25E8%25BD%25AE%25E7%25BF%25BB%25E9%25A1%25B5&rsv_pq=f2416189000b8269&rsv_t=89dfRB%2B7pmFqo4Q0QukcuiFWBob5nIQfPCKhk%2BWMUB0eub2dcfG9iFl0bjw&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=2656&rsv_sug3=8&rsv_sug1=3&rsv_sug7=000&rsv_sug2=0&rsv_sug4=4626&rsv_sug=1')
time.sleep(2)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
e_item=driver.find_elements_by_xpath('//*[@class="card-list"]//div[@class="weibo-text"]')
print('\n'.join([e.text for e in e_item[-27:]]))

# print(e)
# print(type(e))



driver.quit()