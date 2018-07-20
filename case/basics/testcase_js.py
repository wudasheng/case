#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/7/12
from case.public.object import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from case.public.base import Page
from time import sleep
from selenium import webdriver
import unittest,time
from selenium.webdriver.support.select import Select

class js(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://192.168.1.102/#/login/"
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()
    #登录角色管理页面
    def test_case1(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.js()
        sleep(1)
        now_url = driver.current_url
        try:
            assert now_url == 'http://192.168.1.102:4200/#/role'
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    #查询默认展示安佳组别
    def test_case2(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.js()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//table/tbody/tr[1]/td[1]").text
        try:
            assert a == "安佳"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #默认安佳组别下角色名称查询
    def test_case3(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.js()
        driver.find_element_by_xpath("//span/input").send_keys("测试专用")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//table/tbody/tr/td[2]").text
        try:
            assert a == "测试专用"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #修改角色名称
    def test_case4(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.js()
        driver.find_element_by_xpath("//span/input").send_keys("测试专用")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'编辑角色')]").click()
        driver.find_element_by_xpath("//td[2]/span/input").clear()
        driver.find_element_by_xpath("//td[2]/span/input").send_keys("享佳测试")
        driver.find_element_by_xpath("//a[contains(text(),'保存')]").click()
        sleep(1)
        a = driver.find_element_by_xpath("//table/tbody/tr/td[2]").text
        try:
            assert a == "享佳测试"
        except:
            Page.get_screenshot(self)
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'编辑角色')]").click()
        driver.find_element_by_xpath("//td[2]/span/input").clear()
        driver.find_element_by_xpath("//td[2]/span/input").send_keys("测试专用")
        driver.find_element_by_xpath("//a[contains(text(),'保存')]").click()
        sleep(3)
    #修改角色名称不保存
    def test_case5(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.js()
        driver.find_element_by_xpath("//span/input").send_keys("测试专用")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'编辑角色')]").click()
        driver.find_element_by_xpath("//td[2]/span/input").clear()
        driver.find_element_by_xpath("//td[2]/span/input").send_keys("享佳测试")
        driver.find_element_by_xpath("//a[contains(text(),'取消')]").click()
        driver.find_element_by_xpath("//div[2]/button[2]").click()
        sleep(1)
        a = driver.find_element_by_xpath("//table/tbody/tr/td[2]").text
        try:
            assert a == "测试专用"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #默认安佳组别下禁用状态查询
    def test_case6(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.js()
        sleep(3)
        driver.find_element_by_xpath("//nz-form-item[3]/nz-form-control/div/span/nz-select").click()
        driver.find_element_by_xpath("//div/ul/li[3]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//table/tbody/tr/td[3]").text
        try:
            assert a == "禁用"
        except:
            Page.get_screenshot(self)
        sleep(3)
    #不存在的角色名称查询
    def test_case7(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.js()
        driver.find_element_by_xpath("//span/input").send_keys("askjdlasdkjasd")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]/span").text
        try:
            assert a == "暂无数据"
        except:
            Page.get_screenshot(self)
        sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()