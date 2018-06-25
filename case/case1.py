#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/22
from selenium import webdriver
from time import sleep
#path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
# driver.find_element_by_css_selector("input[placeholder='用户名']").send_keys("wds")
# driver.find_element_by_css_selector("input[type='password']").send_keys("123456")
# driver.find_element_by_css_selector("button[ng-reflect-nz-typ='primary']").click()
sleep(5)