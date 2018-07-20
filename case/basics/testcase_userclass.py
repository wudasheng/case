#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/7/13
from case.public.object import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from case.public.base import Page
from time import sleep
from selenium import webdriver
import unittest,time
from selenium.webdriver.support.select import Select

class userclass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://192.168.1.102:4200/#/login/"
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()
    def test_case1(self):
        """
    打开用户等级管理，并对其进行URL验证，标签验证
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        sleep(1)
        url = driver.current_url
        try:
            assert url == "http://192.168.1.102:4200/#/user/level"
        except:
            Page.get_screenshot(self)
        po.shang()
        look_up = driver.find_element_by_xpath("//nz-card/div[1]/div/div").text
        try:
            assert look_up == "用户等级管理"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case2(self):
        """
    健康助理查询。
    级别上查询出来后验证健康助理字段
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        sleep(1)
        po.shang()
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div[7]/div/div/div/ul/li[2]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verify = driver.find_element_by_xpath("//table/tbody/tr[1]/td[2]/span").text
        try:
            assert verify == "健康助理"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case3(self):
        """
    健康管理师查询。
    级别上查询出来后验证健康管理师字段
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        sleep(1)
        po.shang()
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div[7]/div/div/div/ul/li[3]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verify = driver.find_element_by_xpath("//table/tbody/tr[1]/td[2]/span").text
        try:
            assert verify == "健康管理师"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case4(self):
        """
    组别号查询
    验证组别号是1的字段
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//div[2]/nz-input-group/span/nz-select/div/div/div").click()
        sleep(1)
        driver.find_element_by_xpath("//li[contains(text(),'1')]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verify = driver.find_element_by_xpath("//table/tbody/tr[1]/td[3]").text
        try:
            assert verify == "1"
        except:
            Page.get_screenshot(self)
    def test_case5(self):
        """
    启用状态查询
    状态栏验证用用字段
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//div[3]/nz-input-group/span/nz-select/div/span").click()
        driver.find_element_by_xpath("//li[contains(text(),'启用')]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verify = driver.find_element_by_xpath("//table/tbody/tr[1]/td[6]/span").text
        try:
            assert verify == "启用"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case6(self):
        """
    禁用状态查询
    状态验证禁用字段
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//div[3]/nz-input-group/span/nz-select/div/span").click()
        driver.find_element_by_xpath("//li[contains(text(),'禁用')]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verify = driver.find_element_by_xpath("//table/tbody/tr[1]/td[6]/span").text
        try:
            assert verify == "禁用"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case7(self):
        """
    用户名查询
    用户名栏验证吴大胜字段
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("吴大胜")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verify = driver.find_element_by_xpath("//table/tbody/tr[1]/td[4]/span").text
        try:
            assert verify == "吴大胜"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case8(self):
        """
    查询不能在的用户
    字段验证
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("lalalallalaal的吗下雨")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verify = driver.find_element_by_xpath("//nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]/span").text
        try:
            assert verify == "暂无数据"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case9(self):
        """
    重置键操作
    级别和状态验证默认字符
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div[7]/div/div/div/ul/li[3]").click()
        driver.find_element_by_xpath("//div[3]/nz-input-group/span/nz-select/div/span").click()
        driver.find_element_by_xpath("//li[contains(text(),'启用')]").click()
        driver.find_element_by_xpath("//button[2]").click()
        sleep(1)
        verify = driver.find_element_by_xpath("//nz-select/div/div/div").text
        try:
            assert verify == "请选择"
        except:
            Page.get_screenshot(self)
        sleep(1)
        verify1 = driver.find_element_by_xpath("//nz-input-group/span/nz-select/div/div/div").text
        try:
            assert verify1 == "请选择"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case10(self):
        """
    新增页面跳转
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//div[2]/button").click()
        sleep(1)
        verify = driver.find_element_by_xpath("//app-user-level-save-or-update/nz-card/div[1]/div/div").text
        try:
            assert verify == "用户等级新增"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case11(self):
        """
    级别为空提交
    验证提示语
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//div[2]/button").click()
        sleep(1)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert verity == "级别不能为空！"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case12(self):
        """
    组别号为空
    验证系统提示语
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//div[2]/button").click()
        sleep(1)
        driver.find_element_by_xpath("//nz-select/div/div").click()
        driver.find_element_by_xpath("//div[7]/div/div/div/ul/li").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert verity == "组别号不能为空！"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case13(self):
        """
    等级为健康助理师，组别号为1（组别已存在管理师），未分配等级客服为空
    验证系统提示是否与预期的一致
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//div[2]/button").click()
        sleep(1)
        driver.find_element_by_xpath("//nz-select/div/div").click()
        driver.find_element_by_xpath("//div[7]/div/div/div/ul/li").click()
        sleep(1)
        driver.find_element_by_xpath("//div[contains(text(),'请输入组别')]").click()
        driver.find_element_by_xpath("/html/body/div/div[7]/div/div/div/ul/li").click()
        sleep(1)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert verity == "除了管理师，其他级别客服不能为空！"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(2)
    def test_case14(self):
        """
    级别选择健康管理师，组别为1（组别已存在管理师），未分配等级客服为空
    验证系统提示是否与预期的一致
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//div[2]/button").click()
        sleep(1)
        driver.find_element_by_xpath("//nz-select/div/div").click()
        driver.find_element_by_xpath("//div[7]/div/div/div/ul/li[2]").click()
        sleep(2)
        driver.find_element_by_xpath("//div[contains(text(),'请输入组别')]").click()
        driver.find_element_by_xpath("/html/body/div/div[7]/div/div/div/ul/li").click()
        sleep(1)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        if "此组别已存在管理师" in verity:
            print("yes")
        else:
            Page.get_screenshot(self)
        sleep(2)
    def test_case15(self):
        """
    将健康助理级别改成将康管理师，此组别号已存在管理师
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("赵剑")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td[7]/button").click()
        sleep(1)
        driver.find_element_by_xpath("//nz-select/div/div").click()
        driver.find_element_by_xpath("//div[7]/div/div/div/ul/li[2]").click()
        sleep(1)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        if "此组别已存在管理师" in verity:
            print("yes")
        else:
            Page.get_screenshot(self)
        sleep(2)
    def test_case16(self):
        """
    修改状态
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("赵剑")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td[7]/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert verity == "禁用情况下，上面的任何操作都不会做修改！"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case17(self):
        """
    禁用状态下修改级别
    提示语言验证
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.userclass()
        po.shang()
        sleep(1)
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("赵剑")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td[7]/button").click()
        sleep(1)
        driver.find_element_by_xpath("//nz-select/div/div").click()
        driver.find_element_by_xpath("//div[7]/div/div/div/ul/li[2]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert verity == "禁用情况下，上面的任何操作都不会做修改！"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div[2]/button").click()
        sleep(2)
    def test_case18(self):
        """
    禁用状态下修改组别号
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("赵剑")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td[7]/button").click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-user-level-save-or-update/nz-card/div[2]/form/nz-form-item[2]/div/nz-select/div/span").click()
        driver.find_element_by_xpath("/html/body/div/div[7]/div/div/div/ul/li[1]").click()
        sleep(1)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert verity == "禁用情况下，上面的任何操作都不会做修改！"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div[2]/button").click()
        sleep(2)
    def test_case19(self):
        """
    禁用状态下修改当前客服
    验证提示语
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("赵剑")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td[7]/button").click()
        sleep(2)
        driver.find_element_by_xpath("//nz-form-item[3]/div/nz-select/div/div").click()
        driver.find_element_by_xpath("//div[7]/div/div/div/ul/li").click()
        sleep(1)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert verity == "除了管理师，其他级别客服不能为空！"
        except:
            Page.get_screenshot(self)
        driver.find_element_by_xpath("//div/div[2]/button").click()
        sleep(2)
    def test_case20(self):
        """
    状态修改成启用状态
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("赵剑")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td[7]/button").click()
        sleep(2)
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert verity == "更新菜单信息成功"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case21(self):
        """
    启用状态下修改最别号，系统提示语言验证，页面展示验证
    验证完后再修改回来
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("赵剑")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td[7]/button").click()
        sleep(2)
        driver.find_element_by_xpath(
            "/html/body/app-root/nz-layout/nz-layout/nz-content/app-user-level-save-or-update/nz-card/div[2]/form/nz-form-item[2]/div/nz-select/div/span").click()
        driver.find_element_by_xpath("/html/body/div/div[7]/div/div/div/ul/li[4]").click()
        sleep(1)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-modal/div/div[2]/div[1]/div/div/div/div[1]/div/div").text
        try:
            assert verity == "更新菜单信息成功"
        except:
            Page.get_screenshot(self)
        sleep(1)
        driver.find_element_by_xpath("//div/div[2]/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("赵剑")
        sleep(2)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        group_verity = driver.find_element_by_xpath("//table/tbody/tr/td[3]/span").text
        try:
            assert group_verity == "4"
        except:
            Page.get_screenshot(self)
        sleep(1)
        driver.find_element_by_xpath("//td[7]/button").click()
        sleep(2)
        driver.find_element_by_xpath(
            "/html/body/app-root/nz-layout/nz-layout/nz-content/app-user-level-save-or-update/nz-card/div[2]/form/nz-form-item[2]/div/nz-select/div/span").click()
        driver.find_element_by_xpath("/html/body/div/div[7]/div/div/div/ul/li[1]").click()
        sleep(1)
        driver.find_element_by_xpath("//button").click()
        sleep(2)
    def test_case22(self):
        """
    每页展示20条数据，验证显示当前页面展示多少条
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.userclass()
        po.shang()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        po.xia()
        driver.find_element_by_xpath("//div/nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div[9]/div/div/div/ul/li[2]").click()
        sleep(1)
        po.xia()
        current_page_verity = driver.find_element_by_xpath("//nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]").text
        if "显示第1到第20条记录" in current_page_verity:
            print ("yes")
        else:
            Page.get_screenshot(self)
        sleep(2)

        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()

