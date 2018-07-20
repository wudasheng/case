#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/7/11
from case.public.object import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from case.public.base import Page
from time import sleep
from selenium import webdriver
import unittest,time
from selenium.webdriver.support.select import Select

class menu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://192.168.1.102:4200/#/login/"
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()
    #登录菜单管理
    def test_case1(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.caidan()
        now_uel = driver.current_url
        try:
            assert now_uel == 'http://192.168.1.102:4200/#/wx/manage'
        except:
            Page.get_screenshot(self)

        driver.quit()
        sleep(2)
    #公众号名称查询
    def test_case2(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.caidan()
        driver.find_element_by_xpath("//input[@name='wxName']").send_keys("睡眠监控")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-spin/div/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]").text
        try:
            assert a == "睡眠监控"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()