#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/20
from case.public.object import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from case.public.base import Page
from time import sleep
from selenium import webdriver
import unittest,time
class denglu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:4200/#/login"
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()
    #登录账号
    def test_case1(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.denglu()
        sleep(3)
        now_url = driver.current_url
        try:
            assert now_url == 'http://localhost:4200/#/home'
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #用户名为空
    def test_case2(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.username_in(name='')
        po.password_in(password='123456')
        po.button_in()
        username = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                              "form/nz-form-item[1]/nz-form-control/div/nz-form-explain").text
        try:
            assert username == "请输入用户名!"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #密码为空
    def test_case3(self):
        driver = self.driver
        po= login(self.driver,self.url)
        po.open()
        po.username_in(name='wds')
        po.password_in(password='')
        po.button_in()
        password = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                                "form/nz-form-item[2]/nz-form-control/div/nz-form-explain").text
        try:
            assert password == "请输入密码!"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    #用户名不正确
    def test_case4(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.username_in(name='hgklhkas')
        po.password_in(password='123456')
        po.button_in()
        wait = WebDriverWait(driver,10)
        username=wait.until(EC.element_to_be_clickable(
                            (By.XPATH, '//*[@id="cdk-overlay-0"]/nz-message-container/div/nz-message/div/div/div/span'))).text
        try:
            assert username == '无此用户信息或是密码错误'
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #密码不正确
    def test_case5(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.username_in(name='wds')
        po.password_in(password='545532323321')
        po.button_in()
        wait = WebDriverWait(driver, 10)
        password = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="cdk-overlay-0"]/nz-message-container/div/nz-message/div/div/div/span'))).text
        try:
            assert password == '无此用户信息或是密码错误'
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()