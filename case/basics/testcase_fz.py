#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/29
from case.public.object import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from case.public.base import Page
from time import sleep
from selenium import webdriver
import unittest,time
from selenium.webdriver.support.select import Select

class fenzu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://192.168.1.102:4200/#/login/"
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()

    #登录分组管理
    def test_case1(self):
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.fenzu()
        sleep(2)
        now_uel = driver.current_url
        try:
            assert now_uel == 'http://192.168.1.102:4200/#/group'
        except:
            Page.get_screenshot(self)

        driver.quit()
        sleep(2)
    #新建分组
    def test_case2(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.fenzu()
        sleep(1)
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/button[1]").click()
        driver.find_element_by_css_selector("input[name='groupName']").clear()
        driver.find_element_by_css_selector("input[name='groupName']").send_keys('享佳测试')
        driver.find_element_by_css_selector("div[unselectable='unselectable']").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                     "nz-card/div[2]/div[1]/button").click()
        sleep(3)
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div[2]/form/div/div[1]/nz-input-group/span/input").send_keys("享佳测试")
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                     "nz-card/div[2]/form/div/div[3]/button").click()
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                         "div[2]/div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[1]/table/"
                                         "tbody/tr/td[3]").text
        try:
            assert a == "享佳测试"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(4)
   #新建分组默认状态查询是启用状态
    def test_case3(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.fenzu()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div[2]/form/div/div[1]/nz-input-group/span/input").send_keys("享佳测试")
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                     "nz-card/div[2]/form/div/div[3]/button").click()
        sleep(2)
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                         "div[2]/div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[1]/table/"
                                         "tbody/tr/td[4]").text
        try:
            assert a == "是"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #重置建验证
    def test_case4(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.fenzu()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div[2]/form/div/div[1]/nz-input-group/span/input").send_keys("享佳测试")
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/"
                                     "form/div/div[2]/nz-input-group/nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[1]").click()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/"
                                     "form/div/div[4]/button").click()
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/"
                                     "form/div/div[2]/nz-input-group/nz-select/div/div/div").text
        try:
            assert a == "请选择"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(4)
    #修改父组别
    def test_case5(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.fenzu()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div[2]/form/div/div[1]/nz-input-group/span/input").send_keys("享佳测试")
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                     "nz-card/div[2]/form/div/div[3]/button").click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/"
                                     "div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/"
                                     "label/span[1]/input").click()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/"
                                     "button[2]").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/form/"
                                     "div[1]/div/app-group-picker/form/nz-cascader/div/div/span").click()
        driver.find_element_by_xpath("//div[7]/div/ul/li[2]").click()
        driver.find_element_by_xpath("//ul[2]/li").click()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/div[1]/button").click()
        sleep(3)
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div[2]/form/div/div[1]/nz-input-group/span/input").send_keys("享佳测试")
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                     "nz-card/div[2]/form/div/div[3]/button").click()
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/"
                                     "div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[1]/table/tbody/tr/td[2]").text
        try:
            assert a == "领导"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(4)
    #修改组别名称
    def test_case6(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.fenzu()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div[2]/form/div/div[1]/nz-input-group/span/input").send_keys("享佳测试")
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                     "nz-card/div[2]/form/div/div[3]/button").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/"
                                     "div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/"
                                     "label/span[1]/input").click()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/"
                                     "button[2]").click()
        sleep(2)
        driver.find_element_by_xpath("//input[@name='groupName']").clear()
        driver.find_element_by_xpath("//input[@name='groupName']").send_keys("测试享佳")
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/div[1]/button").click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div[2]/form/div/div[1]/nz-input-group/span/input").send_keys("测试享佳")
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                     "nz-card/div[2]/form/div/div[3]/button").click()
        sleep(1)
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                         "div[2]/div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[1]/table/"
                                         "tbody/tr/td[3]").text
        try:
            assert a == "测试享佳"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #修改页面，关闭键操作
    def test_case7(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.fenzu()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div[2]/form/div/div[1]/nz-input-group/span/input").send_keys("测试享佳")
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                     "nz-card/div[2]/form/div/div[3]/button").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/"
                                     "div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/"
                                     "label/span[1]/input").click()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/"
                                     "button[2]").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/div[1]/button").click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div[2]/form/div/div[1]/nz-input-group/span/input").send_keys("测试享佳")
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                     "nz-card/div[2]/form/div/div[3]/button").click()
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                         "div[2]/div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[1]/table/"
                                         "tbody/tr/td[4]").text
        try:
            assert a == "否"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #查询不存在的分组名
    def test_case8(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.fenzu()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div[2]/form/div/div[1]/nz-input-group/span/input").send_keys("死死死死死")
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                      "nz-card/div[2]/form/div/div[3]/button").click()
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/div[2]/"
                                         "div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]/span").text
        try:
            assert a == "暂无数据"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(5)
    #分页展示
    def test_case9(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.fenzu()
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                     "nz-card/div[2]/form/div/div[3]/button").click()
        po.xia()
        driver.find_element_by_xpath("//div/nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div[6]/div/div/div/ul/li[2]").click()
        po.xia()
        sleep(2)
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                         "div[2]/div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]").text
        if "显示第1到第20条记录" in a:
            print ("yes")
        else:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()












