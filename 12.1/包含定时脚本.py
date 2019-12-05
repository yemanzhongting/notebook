# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/12/5 15:11'
# encoding: utf-8
'''
@LstmPython3.6    @tieba 
@Administrator    @2019/12/5  @15:02 
@PyCharm
'''
from selenium import webdriver
import os
import pickle
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 两种方法任选其一，都是指向同一个文件
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import smtplib,time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import datetime
import threading
from selenium import webdriver
import time,random,json

def sleeptime(hour, min, sec):

    return hour * 3600 + min * 60 + sec;

def check():
    cookie = ' '
    lists = cookie.split(';')
    bdcookie = {}
    for i in lists:
        j = i.strip()
        j = j.split('=')
        bdcookie[j[0]] = j[1]

    #driver = webdriver.Chrome(executable_path=r'E:\Githubresponsity\notebook\12.1\chromedriver.exe')
    driver = webdriver.Chrome(r'D:\arcgisserver\chromedriver.exe')
    driver.get('https://tieba.baidu.com')

    for cookie in bdcookie:
        driver.add_cookie({
            "domain": ".baidu.com",
            "name": cookie,
            "value": bdcookie[cookie],
            "path": '/',
            "expires": None
        })

    driver.get('https://tieba.baidu.com/')

    driver.find_element_by_xpath('//*[@id="onekey_sign"]/a').click()

    driver.find_element_by_xpath('//*[@id="dialogJbody"]/div/div/div[1]/a').click()
    driver.quit()

def sendEmail():
    sender = 'yemanzhongting@163.com'
    receivers = ['838044557@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # SMTP服务器
    mail_user = "yemanzhongting"  # 用户名
    mail_pass = ""  # 授权密码，非登录密码

    content = '签到成功'
    title = '签到成功'  # 邮件主题

    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

if __name__ == '__main__':
    while 1 == 1:
        time.sleep(sleeptime(24,0,0));
        try:
            check()
            sendEmail()
        except:
            pass