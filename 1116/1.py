# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:17
# @Author  : yemanzhongting
# @Email   : sggzhang@whu.edu.cn
# @File    : 1.py
# @Software: PyCharm
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib,time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import datetime
import threading
from selenium import webdriver

def getdata():
    driver=webdriver.Chrome(r'D:\GitHubresponsity\notebook\chromedriver.exe')

    driver.get('http://manu52.magtech.com.cn/journalx_gxb/authorLogOn.action')

    driver.find_element_by_xpath('//*[@id="user_name"]').send_keys('yemanzhongting')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('')
    driver.find_element_by_xpath("//input[@onclick='login()']").click()

    #driver.implicitly_wait(3)
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table[1]/tbody/tr[3]/td[3]/table/tbody/tr[1]/td/a').click()

    time.sleep(5)
    #/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table[1]/tbody/tr[3]/td[3]/table/tbody/tr[1]/td/a
    #driver.find_elements_by_css_selector('body > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(3) > td:nth-child(3) > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(3) > table > tbody > tr:nth-child(1) > td > a')
    driver.find_element_by_xpath('//*[@id="_div"]/table[2]/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/a').click()
    time.sleep(8)
    a=driver.find_element_by_xpath('/html/body/center/div[1]/table/tbody/tr[1]/td/table/tbody/tr[4]/td[3]/font')
    tmp=a.text
    driver.quit()
    return tmp



def sendEmail():

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


# def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
#     email_client = smtplib.SMTP(SMTP_host)
#     email_client.login(from_account, from_passwd)
#     # create msg
#     msg = MIMEText(content, 'plain', 'utf-8')
#     msg['Subject'] = Header(subject, 'utf-8')  # subject
#     msg['From'] = from_account
#     msg['To'] = to_account
#     email_client.sendmail(from_account, to_account, msg.as_string())
#
#     email_client.quit()

def all():
    con = getdata()

    sender = 'yemanzhongting@163.com'
    receivers = ['838044557@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # SMTP服务器
    mail_user = "yemanzhongting"  # 用户名
    mail_pass = "whu313"  # 授权密码，非登录密码

    content = con
    title = '人生苦短'  # 邮件主题

    sendEmail()

def sleeptime(hour, min, sec):

    return hour * 3600 + min * 60 + sec;


if __name__ == '__main__':
    second = sleeptime(0, 1, 15);
    while 1 == 1:
        time.sleep(second);
        con = getdata()

        sender = 'yemanzhongting@163.com'
        receivers = ['838044557@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        # 第三方 SMTP 服务
        mail_host = "smtp.163.com"  # SMTP服务器
        mail_user = "yemanzhongting"  # 用户名
        mail_pass = "whu313"  # 授权密码，非登录密码

        content = con
        title = '人生苦短'  # 邮件主题

        sendEmail()



