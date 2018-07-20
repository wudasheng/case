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

class menu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://192.168.1.102:4200/#/login/"
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()
    #菜单管理登录
    def test_case1(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        url = driver.current_url
        try:
            assert url == "http://192.168.1.102:4200/#/menumanage"
        except:
            Page.get_screenshot(self)
        sleep(2)
        a = driver.find_element_by_xpath("//app-menu-manage/nz-card[1]/div[1]/div/div").text
        try:
            assert a == "菜单管理"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #菜单名查询
    def test_case2(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        driver.find_element_by_xpath("//input[@name='menuName']").send_keys("测试专用")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//tbody/tr/td[2]/span").text
        try:
            assert a == "测试专用"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #不存在的菜单名查询
    def test_case3(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        driver.find_element_by_xpath("//input[@name='menuName']").send_keys("sajdashdkasjhdahsdkjsahdahsdhkajs")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]/span").text
        try:
            assert a == "暂无数据"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    #新增菜单名
    def test_case4(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//nz-card[2]/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//div/div/i").click()
        sleep(2)
        driver.find_element_by_xpath("//div/ul/li").click()
        driver.find_element_by_xpath("//ul[2]/li").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='menuName']").send_keys("测试专用1")
        driver.find_element_by_xpath("//input[@id='menuSort']").send_keys("2")
        driver.find_element_by_xpath("//input[@id='menuUrl']").send_keys("www.ceshi.com")
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert a == "添加菜单信息成功"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div/div/div[2]/button").click()
        driver.quit()
        sleep(3)
    #菜单名称为空
    def test_case5(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//nz-card[2]/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert a == "菜单名称不能为空！"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div/div/div[2]/button").click()
        driver.quit()
        sleep(3)
    #序号为空
    def test_case6(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//nz-card[2]/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='menuName']").send_keys("测试专用2")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert a == "菜单序号不能为空！"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div/div/div[2]/button").click()
        driver.quit()
        sleep(3)
    #序号输入特殊字符
    def test_case7(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//nz-card[2]/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='menuName']").send_keys("测试专用3")
        driver.find_element_by_xpath("//input[@id='menuSort']").send_keys("$%#^&%&")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert a == "菜单序号格式不正确，只能是数字！"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div/div/div[2]/button").click()
        driver.quit()
        sleep(3)
    #序号输入空格
    def test_case8(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//nz-card[2]/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='menuName']").send_keys("测试专用3")
        driver.find_element_by_xpath("//input[@id='menuSort']").send_keys("                  ")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert a == "菜单序号格式不正确，只能是数字！"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div/div/div[2]/button").click()
        driver.quit()
        sleep(3)
    #序号输入汉字
    def test_case9(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//nz-card[2]/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='menuName']").send_keys("测试专用3")
        driver.find_element_by_xpath("//input[@id='menuSort']").send_keys("束带结发")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert a == "菜单序号格式不正确，只能是数字！"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div/div/div[2]/button").click()
        driver.quit()
        sleep(3)
    #序号输入字母
    def test_case10(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//nz-card[2]/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='menuName']").send_keys("测试专用3")
        driver.find_element_by_xpath("//input[@id='menuSort']").send_keys("sdfkhdkjasd")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert a == "菜单序号格式不正确，只能是数字！"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div/div/div[2]/button").click()
        driver.quit()
        sleep(3)
    #修改菜单名称
    def test_case11(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//input[@name='menuName']").send_keys("测试专用1")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td[5]/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='menuName']").clear()
        driver.find_element_by_xpath("//input[@id='menuName']").send_keys("测试专用2")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert a == "更新菜单信息成功"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div/div/div[2]/button").click()
        sleep(2)
        driver.find_element_by_xpath("//input[@name='menuName']").send_keys("测试专用2")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//tbody/tr/td[2]/span").text
        try:
            assert a == "测试专用2"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #修改菜单地址
    def test_case12(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//input[@name='menuName']").send_keys("测试专用2")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td[5]/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='menuUrl']").clear()
        driver.find_element_by_xpath("//input[@id='menuUrl']").send_keys("www.ceshi2.com")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert a == "更新菜单信息成功"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div/div/div[2]/button").click()
        sleep(2)
        driver.find_element_by_xpath("//input[@name='menuName']").send_keys("测试专用2")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//table/tbody/tr[1]/td[3]/span").text
        try:
            assert a == "www.ceshi2.com"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #分页展示
    def test_cae13(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        po.xia()
        driver.find_element_by_xpath("//div/nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div[5]/div/div/div/ul/li[2]").click()
        sleep(1)
        po.xia()
        a = driver.find_element_by_xpath("//nz-spin/div/div[2]/div/div/div/div[2]").text
        if "显示第1到第20条记录" in a:
            print ("yes")
        else:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    def test_case14(self):
        """
    新增菜单名称输入特殊字符，验证系统提示
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//nz-card[2]/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='menuName']").send_keys("%$^$&^%")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert a == "菜单名称格式不正确，只能是汉字字母数字！"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div/div/div[2]/button").click()
        driver.quit()
        sleep(3)
    def test_case15(self):
        """
    菜单名称输入空格验证提示语
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//nz-card[2]/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='menuName']").send_keys("              ")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert a == "菜单名称不能为空！"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div/div/div[2]/button").click()
        driver.quit()
        sleep(3)
    def test_case16(self):
        """
    启用状态查询，验证状态栏展示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//nz-select/div/span").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        state_verity = driver.find_element_by_xpath("//table/tbody/tr[1]/td[4]").text
        try:
            assert state_verity == "启用"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case17(self):
        """
    禁用状态查询并验证页面展示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.menu()
        po.shang()
        driver.find_element_by_xpath("//nz-select/div/span").click()
        driver.find_element_by_xpath("//div/ul/li[3]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        state_verity = driver.find_element_by_xpath("//table/tbody/tr[1]/td[4]").text
        try:
            assert state_verity == "禁用"
        except:
            Page.get_screenshot(self)
        sleep(2)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
