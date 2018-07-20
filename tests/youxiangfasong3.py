#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/28
import os,datetime,time

#定义文件目录
result_dir = 'D:\\code\\report'
#获取目录下所有列表
lists=os.listdir(result_dir)

for l in lists:
    print (l)
#匿名函数
# 匿名关键字lambda，入参fn（fn就是文件列表内的文件）。fn：这个冒号右边的就是返回的文件路径。getmtime要获取文件的时间
#key 是比较文件名，
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))

# print ("ttttttttttttttt")
# for l in lists:
#     print (l)

print ("ooooooooo")
#获取最新文件
# print ("最新的文件： "+lists[-1])
#获取最新文件路径
file = os.path.join(result_dir,lists[-1])
print (file)

# if not os.path.isdir(result_dir+"\\"+fn) else 0)
# print ('最新的文件为： '+lists[-1]) file = os.path.join(result_dir,lists[-1]) print file