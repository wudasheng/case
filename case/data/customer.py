#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/7/18
from case.public.object import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from case.public.base import Page
from time import sleep
from selenium import webdriver
import unittest,time

class customer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://192.168.1.102:4200/#/login/"
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()
    def test_case1(self):
        """
    登录客户管理
    验证URL地址
    验证抬头
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.customer()
        sleep(1)
        url = driver.current_url
        try:
            assert url == "http://192.168.1.102:4200/#/customer"
        except:
            Page.get_screenshot(self)
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-card/div/div[1]/span").text
        try:
            assert verity == "客户管理"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case2(self):
        """
    组别查询
    验证查询出来的组别名
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.customer()
        driver.find_element_by_xpath("//div/div/i").click()
        driver.find_element_by_xpath("//div[14]/div/div/ul/li[5]").click()
        driver.find_element_by_xpath("//ul[2]/li[2]").click()
        sleep(2)
        driver.find_element_by_xpath("//button[1]").click()
        sleep(2)
        verify = driver.find_element_by_xpath("//table/tbody/tr[1]/td[4]").text
        try:
            assert verify == "James-卡特"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case3(self):
        """
    客户名称查询
    验证查询的客户名称是否一致
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.customer()
        driver.find_element_by_xpath("//input[@name='custName']").send_keys("测试1")
        driver.find_element_by_xpath("//button[1]").click()
        sleep(2)
        verity = driver.find_element_by_xpath("//table/tbody/tr[1]/td[2]").text
        try:
            assert verity == "测试1"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case4(self):
        """
    查询设备号
    验证查询的设备号是否与查询的一致
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.customer()
        driver.find_element_by_xpath("//input[@name='devCode']").send_keys("867967025947526")
        driver.find_element_by_xpath("//button[1]").click()
        sleep(2)
        verity = driver.find_element_by_xpath("//table/tbody/tr[1]/td[3]").text
        try:
            assert verity == "867967025947526"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case5(self):
        """
    查询不存在的客户名称，验证结果
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.customer()
        driver.find_element_by_xpath("//input[@name='custName']").send_keys("askjdsjdhnasjkdkasdnajkshdkasndjasdbasdkjakjd")
        driver.find_element_by_xpath("//button[1]").click()
        sleep(2)
        verity = driver.find_element_by_xpath("//app-custtable/div[2]/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]/span").text
        try:
            assert verity == "暂无数据"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case6(self):
        """
    查询不存在的设备编号，验证返回的结果
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.customer()
        driver.find_element_by_xpath("//input[@name='devCode']").send_keys("8679670259475263325323565")
        driver.find_element_by_xpath("//button[1]").click()
        sleep(2)
        verity = driver.find_element_by_xpath(
            "//app-custtable/div[2]/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]/span").text
        try:
            assert verity == "暂无数据"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case7(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.customer()
        #查询test用户
        driver.find_element_by_xpath("//input[@name='custName']").send_keys("test")
        driver.find_element_by_xpath("//button[1]").click()
        sleep(2)

