#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/29
import unittest, time
import os,datetime
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def sentmail(file_new):
    #发信邮箱
    sender = "dashengbrother@126.com"
    # 接收邮箱
    receiver = "1411423885@qq.com"
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    #定义标题
    msg['subject'] = '自动化测试报告'
    msg['From'] = sender
    msg['To'] = receiver
    # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    # 连接SMTP服务器，此处用的126的SMTP服务器
    smtp.connect('smtp.126.com')

    # 发送邮箱用户/密码
    username = "dashengbrother@126.com"
    password = "wds19940108"
    smtp.login(username, password)
    smtp.sendmail(sender, [receiver], msg.as_string())
    smtp.quit()
    print ('email has send out !')

#查找测试报告，调用发邮件功能
def sendreport():
    #报告所在的目录
    result_dir = 'D:\\code\\report'
    # 获取目录下所有列表
    lists = os.listdir(result_dir)
    lists.sort(
        key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
    print(u'上一次测试生成的报告： ' + lists[-2])

    # lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    # for l in lists:
    #     print(l)
    # print("最新的文件： " + lists[-1])
    # file_new = os.path.join(result_dir, lists[-1])


    # 找到上一次测试生成的文件
    file_new = os.path.join(result_dir, lists[-2])
    print (file_new)
    sentmail(file_new)

if __name__=='__main__':
    test_dir = "D:\\code"
    test_report = 'D:\\code\\report'  # 测试报告所在目录\

    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test*.py',
                                                   top_level_dir=None)

    now = time.strftime("%Y_%m_%d_%H_%M_%S")    #获取当前时间

    filename = 'D:/code/report/' + now + 'baogao.html'

    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='安佳云健康测试报告',
                                           description='用列执行情况： ')

    runner.run(discover)
    sendreport()


