#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/28
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
msg = MIMEText("<html><h1>你好！</h1></html>","html","utf-8")
#发送邮箱
sender = "dashengbrother@126.com"
#接收邮箱
receiver = "1411423885@qq.com"
#发送邮件主题
subject = 'python email test'
msg['From'] = sender
msg['To'] = receiver
# #构建附件
# att = MIMEText(open('D:\\code\\report\\2018_06_28_10_58_04baogao.html','rb').read(),'base64','utf-8')
# #指定文件类型
# att["Content-Type"] = 'application/octet-stream'
# att["Content-Disposition"] = 'attachment;filename="2018_06_28_10_58_04baogao.html"'
# msgRoot.attach(att)

#发送邮箱服务器
smtpserver = "smtp.126.com"
#发送邮箱用户/密码
username = "dashengbrother@126.com"
password = "wds19940108"
#中文需参数”utf-8“，单字节字符不需要
#msg = MIMEText("你好！","text","utf-8")
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
smtp.login(username , password)
smtp.sendmail(sender,[receiver],msg.as_string())
smtp.quit()