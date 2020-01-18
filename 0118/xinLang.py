# coding: utf-8

import urllib.request
import time
import random
from lxml import etree
import logging
import xlrd
from xlutils.copy import copy

# 导入所需模块
import urllib.error
import urllib.request
import urllib.parse
import re
import rsa
import http.cookiejar  # 从前的cookielib
import base64
import json
import urllib
import binascii
import requests

class CollectData():
    """数据收集类
       利用微博高级搜索功能，按关键字搜集一定时间范围内的微博。
    """

    def __init__(self, keyword, area, startTime, interval='50',fileS="weibo.csv",flag=True, begin_url_per="http://s.weibo.com/weibo/"):
        self.begin_url_per = begin_url_per  # 设置固定地址部分
        self.setKeyword(keyword)  # 设置关键字
        self.setArea(area)  # 设置关键字
        self.setStartTimescope(startTime)  # 设置搜索的开始时间
        # self.setRegion(region)  #设置搜索区域
        self.setInterval(interval)  # 设置邻近网页请求之间的基础时间间隔（注意：过于频繁会被认为是机器人）
        self.setFileS(fileS)  # 设置邻近网页请求之间的基础时间间隔（注意：过于频繁会被认为是机器人）
        self.setFlag(flag)

    #设置关键字
    #关键字需解码后编码为utf-8
    def setKeyword(self, keyword):
        self.keyword = keyword.encode("utf-8")

    def setArea(self, area):
        self.area = area

    def setFileS(self, fileS):
        self.fileS = fileS

    def getKeyWord(self):
        return urllib.parse.quote(self.keyword)

    def getArea(self):
        return self.area

        ##设置起始范围，间隔为1天

    #格式为：yyyy-mm-dd
    def setStartTimescope(self, startTime):
        if not (startTime == '-'):
            self.timescope = startTime
        else:
            self.timescope = '-'

    ##设置邻近网页请求之间的基础时间间隔
    def setInterval(self, interval):
        self.interval = int(interval)

        def setInterval(self, interval):
            self.interval = int(interval)

    #设置是否被认为机器人的标志。
    def setFlag(self, flag):
        self.flag = flag

    #构建URL
    def getURL(self):
        #url=self.begin_url_per + "?q=" + self.getKeyWord() + "&region=custom:" + self.getArea() + "&scope=ori&suball=1&timescope=custom:" + self.timescope + "&Refer=g&page="
        #不存在地区的检索
        url = self.begin_url_per + "?q=" + self.getKeyWord() + "&scope=ori&suball=1&timescope=custom:" + self.timescope + "&Refer=g&page="
        print(url)
        return url
        ##爬取一次请求中的所有网页，最多返回50页

    def download(self, url, maxTryNum=3):
        cookie = {
            "Cookie": "_T_WM=93464080046; ALF=1581852238; SSOLoginState=1579265115; SCF=Arnxjp0L_i1cDcGLDQ7dciPttPY2-QiWWf-ofMEjBGtJ9bemFP5t1F3BrxzwqVDGKrrvv3_65W-cKg3zVKJxP2Q.; SUB=_2A25zJdwLDeRhGeNM7loW8C7NzzuIHXVQ6eRDrDV6PUJbktANLWGjkW1NSa5q356jsRQU_fvXD89n0VHB1h4qp_Ji; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW_U-piXhYkoCDoBcSWvGnm5JpX5KzhUgL.Fo-ESKnNeh5pShM2dJLoI0qLxKBLB.BL1-eLxK-LBo5L12qLxK-LB-qL1KzLxK-L1KqLBo-LxK-L1KqLBo-LxK-LB.eLBK5t; SUHB=05iq3V1v0-eHa2; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D20000174"
        }  # 将your cookie替换成自己的cookie
        hasMore = True  # 某次请求可能少于50页，设置标记，判断是否还有下一页
        isCaught = False  # 某次请求被认为是机器人，设置标记，判断是否被抓住。抓住后，需要，进入页面，输入验证码
        #
        i = 1  # 记录本次请求所返回的页数
        while hasMore and i < 99 and (not isCaught):  # 最多返回98页，对每页进行解析，并写入结果文件
            source_url = url + str(i)  # 构建某页的URL
            print('正在抓取{}'.format(source_url))
            data = ''  # 存储该页的网页数据
            goon = True  # 网络中断标记
            ##网络不好的情况，试着尝试请求三次
            for tryNum in range(maxTryNum):
                try:
                    #html = urllib.request.urlopen(source_url, timeout=12, )#cookies=cookie
                    html = requests.get(source_url, cookies=cookie,timeout=12).content

                    #data = html.read().decode()
                    data=html.decode()
                    break
                except:
                    if tryNum < (maxTryNum - 1):
                        time.sleep(10)
                    else:
                        print('Internet Connect Error!')
                        self.flag = False
                        goon = False
                        break
            if goon:
                lines = data.splitlines()
                isCaught = True
                timeList = []
                j = data.replace("\\", "")  # 去掉所有的\
                ## 没有更多结果页面
                if (j.find('<div class="card card-no-result') > 0):
                    hasMore = False
                    break
                    ## 有结果的页面
                else:
                    for line in lines:
                        if (line.__len__() == 36) | (line.__len__() == 41):
                            n = line.find(':')
                            if (n > 0):
                                timeList.append(line)
                        ## 判断是否有微博内容，出现这一行，则说明没有被认为是机器人
                    if (timeList.__len__() > 0):
                        isCaught = False

                    page = etree.HTML(j)
                    ps = page.xpath("//p[@node-type='feed_list_content']")  # 使用xpath解析得到微博内容
                    ti = 0
                    # 获取昵称和微博内容
                    for p in ps:
                        name = p.attrib.get('nick-name')  # 获取昵称
                        txt = p.xpath('string(.)').strip()  # 获取微博内容
                        findPla = txt[-15:-1]
                        if (findPla.find("2") > 0):
                            addr = findPla[findPla.find("2") + 1:len(findPla)]
                            txt = txt[:-len(addr) - 2]
                        else:
                            addr = ""
                        if (name is not None):
                            timeNow = timeList[ti].strip()
                            ti += 1
                            oldWb = xlrd.open_workbook(self.fileS, formatting_info=True)
                            oldWs = oldWb.sheet_by_index(0)
                            rows = int(oldWs.cell(0, 0).value)
                            newWb = copy(oldWb)
                            newWs = newWb.get_sheet(0)
                            newWs.write(rows, 0, str(rows))
                            newWs.write(rows, 1, name)
                            newWs.write(rows, 2, timeNow)
                            newWs.write(rows, 3, addr)
                            newWs.write(rows, 4, txt)
                            newWs.write(0, 0, str(rows + 1))
                            newWb.save(self.fileS)
                            print("save with same name ok")
                lines = None
                ## 处理被认为是机器人的情况
                if isCaught:
                    print('Be Caught!')
                    data = None
                    self.flag = False
                    break
                    ## 没有更多结果，结束该次请求，跳到下一个请求
                if not hasMore:
                    print('No More Results!')
                    if i == 1:
                        time.sleep(random.randint(3, 8))
                    else:
                        time.sleep(10)
                    data = None
                    break
                i += 1
                ## 设置两个邻近URL请求之间的随机休眠时间，防止Be Caught
                sleeptime_one = random.randint(self.interval - 25, self.interval - 15)
                sleeptime_two = random.randint(self.interval - 15, self.interval)
                if i % 2 == 0:
                    sleeptime = sleeptime_two
                else:
                    sleeptime = sleeptime_one
                print('sleeping ' + str(sleeptime) + ' seconds...')
                time.sleep(sleeptime)
            else:
                break


def main():
    # 当前固定为原创微博
    #检索关键字
    keyword = "利奇马"
    # 地区注意格式
    area = "33:1"
    # 起止日期，注意格式
    startTime = "2019-08-08-15:2019-08-08-18"#8-18-24 #8-15-18
    # 随机等待时间初始值
    interval = "26"
    # 文件（及路径） 当前为相对路径，需要存在该文件，并且第一格有个数用来记录数量，初始为0，下次爬取基于该数量附加，不会覆盖
    fileS='weiboData.xls'

    ##实例化收集类，收集指定关键字和起始时间的微博
    cd = CollectData(keyword, area, startTime, interval,fileS)
    url = cd.getURL()
    cd.download(url)


if __name__ == '__main__':
    main()
