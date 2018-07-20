#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/28
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os,datetime,time
#发送邮箱
sender = "dashengbrother@126.com"
#接收邮箱
receiver = "1411423885@qq.com"
#发送邮件主题
# subject = 'python email test'

#发送邮箱服务器
smtpserver = "smtp.126.com"
#发送邮箱用户/密码
username = "dashengbrother@126.com"
password = "wds19940108"

msgRoot = MIMEMultipart('related')
#发送邮件主题
msgRoot['Subject'] = 'python email test'

# result_dir = 'D:\\code\\report'
# lists=os.listdir(result_dir)
# lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
# file = os.path.join(result_dir,lists[-1])

#构建附件
att = MIMEText(open(file,'rb').read(),'base64','utf-8')
#指定文件类型
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename=file'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
smtp.login(username , password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()
