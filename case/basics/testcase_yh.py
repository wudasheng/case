#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/7/6
from case.public.object import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from case.public.base import Page
from time import sleep
from selenium import webdriver
import unittest,time

class user(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://192.168.1.102:4200/#/login/"
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()

    #用户管理登录
    def test_case1(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        sleep(1)
        now_url = driver.current_url
        try:
            assert now_url == "http://192.168.1.102:4200/#/user"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #登录名查询
    def test_case2(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("wds")
        driver.find_element_by_xpath("//button").click()
        sleep(2)
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                         "nz-card/div/div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[1]/"
                                         "table/tbody/tr/td[3]").text
        try:
            assert a == "wds"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #用户名查询
    def test_case3(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//input[@name='realName']").send_keys("吴大胜")
        driver.find_element_by_xpath("//button").click()
        sleep(2)
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/"
                                         "nz-card/div/div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[1]/table/"
                                         "tbody/tr/td[4]").text
        try:
            assert a == "吴大胜"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #组别查询
    def test_case4(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-cascader/div/div/span").click()
        driver.find_element_by_xpath("//div[5]/div/div/ul/li").click()
        sleep(2)
        driver.find_element_by_xpath("//button").click()
        sleep(2)
        a = driver.find_element_by_xpath("//table/tbody/tr[1]/td[2]").text
        try:
            assert a == "安佳"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #启用状态查询
    def test_case5(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//button").click()
        sleep(2)
        a = driver.find_element_by_xpath("//table/tbody/tr[1]/td[6]").text
        try:
            assert a == "是"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #未启用状态查询
    def test_case6(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        sleep(1)
        driver.find_element_by_xpath("//button").click()
        sleep(2)
        a = driver.find_element_by_xpath("//table/tbody/tr[1]/td[6]").text
        try:
            assert a == "否"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #重置键操作
    def test_case7(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        sleep(1)
        driver.find_element_by_xpath("//div[6]/button").click()
        sleep(1)
        a2 = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/div/div/nz-card/"
                                          "div[2]/form/div/div[4]/nz-input-group/nz-select/div/div/div").text
        try:
            assert a2 == "请选择"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #查询不存在的登录名
    def test_case8(self):
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("ashdklaskldadasd")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div/div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]/span").text
        try:
            assert a == "暂无数据"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #查询不存在的用户名
    def test_case9(self):
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//input[@name='realName']").send_keys("kasjdhjasdjkahsf")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/nz-card/"
                                     "div/div/div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]/span").text
        try:
            assert a == "暂无数据"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #新增输入已存在的登录名
    def test_case10(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("wds")
        sleep(2)
        a = driver.find_element_by_xpath("//div/nz-form-explain/div/div").text
        try:
            assert a == "登录名已经存在"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #输入已存在的用户名
    def test_case11(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("吴大胜")
        sleep(2)
        a = driver.find_element_by_xpath("//nz-form-control/div/nz-form-explain/div/div").text
        try:
            assert a == "用户姓名已经存在"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #登录名为空
    def test_case12(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("dfg456546dfgasdg")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "登陆名不能为空"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #登录名输入特殊字符
    def test_case13(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("@#$%^&*(")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("漫画546电饭锅")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "登陆名只能输入汉字字母数字！"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #用户名为空
    def test_case14(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("第三方士大夫84654")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "用户名不能为空"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #用户名输入特殊字符/空格
    def test_case15(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("8625sdfsfs")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("&^$   &^%")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "用户名只能输入汉字字母数字！"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #密码为空提交
    def test_case16(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("asasd654")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("kdl78559")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "密码不能为空"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #密码输入特殊字符
    def test_case17(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("78952856365")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("156586358")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("#$^%&*&%^^$^^*&")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "密码只能输入6-20位字母数字！"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #密码输入空格
    def test_case18(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("489658966")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("鸡蛋大声道23")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("                 ")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "密码只能输入6-20位字母数字！"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #密码输入小于6位字符
    def test_case19(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("546526525565")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("265665625225")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("1234")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "密码只能输入6-20位字母数字"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #密码输入大于20位字符
    def test_case20(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("sdfasdsdf")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("jhdgsdfas阿萨德")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("1234567890123456789012345")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "密码只能输入6-20位字母数字"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #重新输入密码不一致
    def test_case21(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("沃尔特与欧普")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("破已一头热千万")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("12345678")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        driver.find_element_by_xpath("//input[@id='job']").send_keys("测试")
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("17080000900")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "密码不一致"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #性别不选
    def test_case22(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("UI让他认为")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("只需补充不能更换")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        #此处为性别选择
        # driver.find_element_by_xpath("//nz-select/div/div/div").click()
        # driver.find_element_by_xpath("//div/ul/li[2]").click()
        driver.find_element_by_xpath("//input[@id='job']").send_keys("测试")
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("17200000040")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "性别不能为空"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #岗位为空
    def test_case23(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("发挥大幅度")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("开奖号开始到")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("")
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("17004000600")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "职位不能为空"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #岗位输入特殊字符
    def test_case24(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("水电费是的个人")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("健康交给你")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("#$%^&*&*^%")
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("17080500000")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "职位只能输入1-20位汉字字母数字"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #岗位输入空格
    def test_case25(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("斯蒂芬世纪东方")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("水电费是否")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("           ")
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("17050080001")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "职位只能输入1-20位汉字字母数字"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #岗位输入大于20位字符
    def test_case26(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("分开蓝色654款")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("撒旦789个啊实多")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("一二三啊大大金卡收到货实打实卡上大街上安吉斯柯达阖家安康啊数据库的哈加快速度啊就是看到阿三五六")
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("17000051019")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        sleep(2)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "职位只能输入1-20位汉字字母数字"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #联系方式输入已注册的手机号码
    def test_case27(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("15298357610")
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "该手机号已经被注册"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #联系方式输入特殊字符
    def test_case28(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("#￥……%……%……（（%……￥……%￥%……%……&")
        sleep(1)
        a = driver.find_element_by_xpath("//nz-form-explain/div/div").text
        try:
            assert a == "号码格式不合法"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #联系方式为空
    def test_case29(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("斯蒂芬世纪东方")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("水电费是否")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("柯兰多")
        #此处为联系方式操作
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "联系方式不能为空"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #联系方式输入空格
    def test_case30(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("斯蒂芬世纪东方")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("水电费是否")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("柯兰多")
        #此处为联系方式操作
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("                          ")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "联系方式必须是11位数字！"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #联系方式输入中文
    def test_case31(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("斯蒂芬世纪东方")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("水电费是否")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("柯兰多")
        #此处为联系方式操作
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("圣诞节疯狂的设计费")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "联系方式必须是11位数字！"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #联系方式输入小于11位数字
    def test_case32(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("斯蒂芬世纪东方")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("水电费是否")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("柯兰多")
        #此处为联系方式操作
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("152983576")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "联系方式必须是11位数字！"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #联系方式输入大于11位数字
    def test_case33(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("斯蒂芬世纪东方")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("水电费是否")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("柯兰多")
        #此处为联系方式操作
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("152983578562552456")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "联系方式必须是11位数字！"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #岗位输入大于20位字母
    def test_case34(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("分开蓝色654款")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("撒旦789个啊实多")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("sadklasfasdgdfasdasdasdasdasdasfasdasdasdfasdaasd")
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("17000051019")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        sleep(2)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "职位只能输入1-20位汉字字母数字"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #登录名输入大于20位字母
    def test_case35(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("sajkdhasjkdajkshdasdasdafdfasdafsdfasdasdasdasdasd")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("撒旦789个啊实多")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("就是阿三五六")
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("17000051019")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        sleep(2)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "登陆名只能输入1-20位汉字字母数字"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #登录名输入大于20位汉字
    def test_case36(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("安徽省打卡的萨科技等哈说简单化科技萨达哈就开始对奥斯卡级大号的阿萨德会卡家收到货啊数据库")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("撒旦789个啊实多")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("就是阿三五六")
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("17000051019")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        sleep(2)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "登陆名只能输入1-20位汉字字母数字"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #用户名输入大于20位字母
    def test_case37(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("收到货啊数据库")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("fsdfkkldjasdasdasdasfgasdasdasdasdasdasdasdaasdasdasdadadasd")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("就是阿三五六")
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("17000051019")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        sleep(2)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "用户名只能输入1-20位汉字字母数字"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #用户名输入大于20位汉字
    def test_case38(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("收到货啊数据库")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("是的恢复健康审单复核阿斯加德哈就开始对啊数据库的哈卡时间段阿卡丽时点击拉克丝卡萨丁十九大十九大氨基酸的空间")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("就是阿三五六")
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("17000051019")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("18000000000")
        sleep(2)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "用户名只能输入1-20位汉字字母数字"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #联系方式与紧急联系电话一致
    def test_case39(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("斯蒂芬世纪东方")
        driver.find_element_by_xpath("//input[@id='realName']").send_keys("水电费是否")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@id='passwordSecond']").send_keys("123456")
        driver.find_element_by_xpath("//nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div/ul/li[2]").click()
        #此处为岗位操作
        driver.find_element_by_xpath("//input[@id='job']").send_keys("柯兰多")
        #此处为联系方式操作
        driver.find_element_by_xpath("//input[@id='phone']").send_keys("13000021000")
        driver.find_element_by_xpath("//input[@id='urgentPhone']").send_keys("13000021000")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        a = driver.find_element_by_xpath("//nz-message/div/div/div/span").text
        try:
            assert a == "紧急联系电话应与联系方式不相同"
        except:
            Page.get_screenshot(self)
        driver.quit()
        sleep(3)
    #分页展示
    def test_case40(self):
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.user()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        po.xia()
        driver.find_element_by_xpath("//div/nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div[5]/div/div/div/ul/li[2]").click()
        sleep(2)
        po.xia()
        a = driver.find_element_by_xpath("//div/nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]").text
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





