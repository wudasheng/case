#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/21
from case.public.object import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from case.public.base import Page
from time import sleep
from selenium import webdriver
import unittest,time

class zhanghaoleixing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:4200/#/login/"
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()

    #登录账号类型
    def test_case1(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.zhanghaoleixing()
        sleep(2)
        now_url = driver.current_url
        try:
            assert now_url == 'http://localhost:4200/#/basedata/accounttype'
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(1)
    #新建用户
    def test_case2(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.zhanghaoleixing()
        po.handle()
        driver.find_element_by_link_text("新建用户类型").click()
        sleep(1)
        driver.find_element_by_xpath("//div/div[2]/form/nz-form-item/nz-form-control/div/span/input").clear()
        driver.find_element_by_xpath("//div/div[2]/form/nz-form-item/nz-form-control/div/span/input").send_keys("test")
        driver.find_element_by_xpath("//div/div[2]/form/nz-form-item[2]/nz-form-control/div/span/input").clear()
        driver.find_element_by_xpath("//div/div[2]/form/nz-form-item[2]/nz-form-control/div/span/input").send_keys("www.test.com")
        sleep(2)
        driver.find_element_by_xpath("//button[2]").click()
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-account/"
                                         "nz-form-item/nz-form-control/div/span/nz-card[2]/div[2]/nz-table/div/"
                                         "nz-spin/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]/span").text
        try:
            assert a == "test"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #默认点击查询展示用户状态是启用状态
    def test_case3(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.zhanghaoleixing()
        po.handle()
        driver.find_element_by_xpath("//button").click()
        sleep(2)
        a1 = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-account/nz-form-item/"
                                          "nz-form-control/div/span/nz-card[2]/div[2]/nz-table/div/nz-spin/div/div[2]/div"
                                          "/div/div/div/table/tbody/tr[1]/td[3]/span").text
        try:
            assert a1 == "启用"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    #禁用状态查询
    def test_case4(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.zhanghaoleixing()
        po.handle()
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//button").click()
        sleep(2)
        a2 = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-account/nz-form-item/"
                                          "nz-form-control/div/span/nz-card[2]/div[2]/nz-table/div/nz-spin/div/div[2]/div/"
                                          "div/div/div/table/tbody/tr[1]/td[3]/span").text
        try:
            assert a2 == "禁用"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    #类型名称查询
    def test_case5(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.zhanghaoleixing()
        po.handle()
        driver.find_element_by_xpath("//input").send_keys("test")
        driver.find_element_by_xpath("//button").click()
        sleep(2)
        a3 = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-account/"
                                         "nz-form-item/nz-form-control/div/span/nz-card[2]/div[2]/nz-table/div/"
                                         "nz-spin/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]/span").text
        try:
            assert a3 == "test"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    #URL查询
    def test_case6(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.zhanghaoleixing()
        po.handle()
        driver.find_element_by_xpath("//nz-form-item[2]/nz-form-control/div/span/input").send_keys("www.test.com")
        driver.find_element_by_xpath("//button").click()
        sleep(2)
        a4 = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-account/nz-form-item/"
                                          "nz-form-control/div/span/nz-card[2]/div[2]/nz-table/div/nz-spin/div/div[2]/"
                                          "div/div/div/div/table/tbody/tr[1]/td[2]/span").text
        try:
            assert a4 == "www.test.com"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    #编辑修改保存
    def test_case7(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.zhanghaoleixing()
        po.handle()
        driver.find_element_by_xpath("//button").click()
        driver.find_element_by_xpath("//a[contains(text(),'编辑')]").click()
        driver.find_element_by_xpath("//td/span/input").clear()
        driver.find_element_by_xpath("//td/span/input").send_keys("test3")
        driver.find_element_by_xpath("//td[2]/span/input").clear()
        driver.find_element_by_xpath("//td[2]/span/input").send_keys("www.test3.com")
        driver.find_element_by_xpath("//a[contains(text(),'保存')]").click()
        sleep(2)
        a5 = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-account/nz-form-item/"
                                          "nz-form-control/div/span/nz-card[2]/div[2]/nz-table/div/nz-spin/div/div[2]/"
                                          "div/div/div/div/table/tbody/tr[1]/td[1]/span").text
        try:
            assert a5 == "test3"
        except:
            Page.get_screenshot(self)
        sleep(2)
        a7 = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-account/nz-form-item/"
                                          "nz-form-control/div/span/nz-card[2]/div[2]/nz-table/div/nz-spin/div/div[2]/"
                                          "div/div/div/div/table/tbody/tr[1]/td[2]/span").text
        try:
            assert a7 == "www.test3.com"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    #编辑修改不保存
    def test_case8(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.zhanghaoleixing()
        po.handle()
        driver.find_element_by_xpath("//input").send_keys("test3")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'编辑')]").click()
        driver.find_element_by_xpath("//td/span/input").clear()
        driver.find_element_by_xpath("//td/span/input").send_keys("88888888")
        driver.find_element_by_xpath("//a[contains(text(),'取消')]").click()
        sleep(1)
        driver.find_element_by_xpath("//div[2]/button[2]").click()
        sleep(2)
        a9 = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-account/nz-form-item/"
                                          "nz-form-control/div/span/nz-card[2]/div[2]/nz-table/div/nz-spin/div/div[2]/"
                                          "div/div/div/div/table/tbody/tr[1]/td[1]/span").text
        try:
            assert a9 == "test3"
        except:
            Page.get_screenshot(self)
        sleep(2)


    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()
