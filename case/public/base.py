#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/20
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
class Page(object):
    url = 'localhost:4200/#/login'
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