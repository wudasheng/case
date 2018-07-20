#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/20
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import random
import time
class Page(object):
    url = '192.168.1.102:4200/#/login'
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def _open(self,url):
        self.driver.get(url)
    def open(self):
        self._open(self.url)
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
    def switch_frame(self,loc):
        return self.driver.switch_to_frame(loc)
    def get_screenshot(self):
        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        self.driver.get_screenshot_as_file("D:\\code\\picture\\"+now+".jpg")
    def handle(self,*loc):
        return self.driver.current_window_handle
    def xia(self):
        js = "var q=document.body.scrollTop=10000"
        self.driver.execute_script(js)
    def shang(self):
        js = "var q=document.body.scrollTop=0"
        self.driver.execute_script(js)
    def suiji(self):
        def create_phone():
            # 第二位数字
            second = [3, 4, 5, 7, 8][random.randint(0, 4)]

            # 第三位数字
            third = {
                3: random.randint(0, 9),
                4: [5, 7, 9][random.randint(0, 2)],
                5: [i for i in range(10) if i != 4][random.randint(0, 8)],
                7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
                8: random.randint(0, 9),
            }[second]

            # 最后八位数字
            suffix = random.randint(9999999, 100000000)

            # 拼接手机号
            return "1{}{}{}".format(second, third, suffix)

        # 生成手机号
        phone = create_phone()
        print(phone)
