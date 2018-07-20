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

#++++++++++++++++++邮件发送+++++++++++++++++++++
def mailing(file_new):
    # msg = MIMEText("mail_body", "html", "utf-8")
    msgRoot = MIMEMultipart('related')

    sender = "dashengbrother@126.com"
    # 接收邮箱
    receiver = "1411423885@qq.com"
    # 发送邮件主题
    msgRoot['subject'] = '自动化测试报告'
    # msgRoot['From'] = sender
    # msgRoot['To'] = receiver

    smtpserver = "smtp.126.com"
    # 发送邮箱用户/密码
    username = "dashengbrother@126.com"
    password = "wds19940108"
    # 中文需参数”utf-8“，单字节字符不需要
    # msg = MIMEText("你好！","text","utf-8")
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login(username, password)
    smtp.sendmail(sender, [receiver], msg.as_string())
    smtp.quit()

    # with open(file_new, 'rb') as f:
    #     mail_body = f.read()
    #
    # msg = MIMEText("mail_body", "html", "utf-8")
    # msg['Subject'] = Header("自动化测试报告", 'utf-8')
    # # 发送邮箱
    # sender = "dashengbrother@126.com"
    # # 接收邮箱
    # receiver = "1411423885@qq.com"
    # msg['From'] = sender
    # msg['To'] = receiver
    #
    # # smtp = smtplib.SMTP('smtp.126.com')
    # # smtp.set_debuglevel(1)
    # smtpserver = "smtp.126.com"
    # smtp = smtplib.SMTP()
    # smtp.connect('smtp.126.com')
    # username = "dashengbrother@126.com"
    # password = "wds199418"
    # smtp.login('username', 'password')
    #
    # smtp.sendmail(sender, [receiver], msg.as_string())
    # smtp.quit()
    # print('test report has send out!')
#+++++++++++++++++查找测试报告目录，查找最新的测试报告+++++++++++++
def newReport():
    lists = os.listdir('D:\\code\\report')  # 返回测试报告所在目录下的所有文件列表
    for l in lists:
        print(l)
    lists.sort(key=lambda fn: os.path.getmtime('D:\\code\\report' + "\\" + fn))

    file = os.path.join('D:\\code\\report', lists[-1])

    # lists2 = sorted(lists)  # 获得按升序排序后的测试报告列表
    # file_new = os.path.join(testReport, lists2[-1])  # 获取最后一个即最新的测试报告地址
    print(file)
    return file

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
    fp.close()
    new_report = newReport()  # 获取最新报告文件
    mailing(new_report)  # 发送最新的测试报告



