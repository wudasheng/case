#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/7/17
from case.public.object import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from case.public.base import Page
from time import sleep
from selenium import webdriver
import unittest,time
from selenium.webdriver.support.select import Select

class partner(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://192.168.1.102:4200/#/login/"
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()
    def test_case1(self):
        """
    打开合作伙伴管理
    URL验证，抬头验证
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.partner()
        po.shang()
        url = driver.current_url
        try:
            assert url == "http://192.168.1.102:4200/#/partner"
        except:
            Page.get_screenshot(self)
        sleep(1)
        rise = driver.find_element_by_xpath("//app-login/div/div/nz-card/div[1]/div/div").text
        try:
            assert rise == "合作伙伴管理"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case2(self):
        """
    合作伙伴全称查询
    验证查询出来的字段是否正确
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试达人")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        #合作伙伴全称
        full_name_partner = driver.find_element_by_xpath("//table/tbody/tr[1]/td[2]").text
        try:
            assert full_name_partner == "测试达人"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case3(self):
        """
    合作伙伴简称查询
    验证查询的简称名称
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//input[@name='partnerAbbr']").send_keys("测试")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        #合作伙伴简称
        for_shot_partner = driver.find_element_by_xpath("//table/tbody/tr[1]/td[3]").text
        try:
            assert for_shot_partner == "测试"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case4(self):
        """
    查询不存在的合作伙伴名称
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("ADSJKLASDJAHSDJKAHSDKADHAJSDBKAJSDASJDGKJKAD")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        # 合作伙伴全称
        full_name_partner = driver.find_element_by_xpath("//nz-spin/div/div[2]/div/div/div/div[2]/span").text
        try:
            assert full_name_partner == "暂无数据"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case5(self):
        """
    查询不存在的合作伙伴简称
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//input[@name='partnerAbbr']").send_keys("啥打卡机山东矿机啊速度快快乐撒大家看似简单览的")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        # 合作伙伴简称
        for_shot_partner = driver.find_element_by_xpath("//nz-spin/div/div[2]/div/div/div/div[2]/span").text
        try:
            assert for_shot_partner == "暂无数据"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case6(self):
        """
    查询状态为是的查询
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-select/div").click()
        driver.find_element_by_xpath("//div/div/ul/li[1]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        initiate_mode = driver.find_element_by_xpath("//table/tbody/tr[1]/td[8]").text
        try:
            assert initiate_mode == "是"
        except:
            Page.get_screenshot(self)
    def test_case7(self):
        """
    查询否的启用状态
    验证状态展示为否
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-select/div").click()
        driver.find_element_by_xpath("//div/div/ul/li[2]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        initiate_mode = driver.find_element_by_xpath("//table/tbody/tr[1]/td[8]").text
        try:
            assert initiate_mode == "否"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case8(self):
        """
    重置键操作
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-select/div").click()
        driver.find_element_by_xpath("//div/div/ul/li[2]").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/app-root/nz-layout/nz-layout/nz-content/app-login/div/div/nz-card/div[2]/form/div/div[5]/button").click()
        sleep(1)
        state = driver.find_element_by_xpath("//nz-input-group/nz-select/div/div/div").text
        try:
            assert state == "请选择"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case9(self):
        """
    新增页面展示
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        rise = driver.find_element_by_xpath("//app-login/nz-card/div[1]/div/div").text
        try:
            assert rise == "合作伙伴管理编辑"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case10(self):
        """
    合作厂家为空
    验证提示语
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "合作厂家名称必须是30字符以内的汉字、数字、字母"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case11(self):
        """
    合作厂家输入空格
    验证提示语
        """
        driver = self.driver
        po = login(self.driver,self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("        ")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "合作厂家名称必须是30字符以内的汉字、数字、字母"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case12(self):
        """
    合作厂家输入特殊字符
    验证提示语
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("#$%$^&&&^^%&*^%")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "合作厂家名称必须是30字符以内的汉字、数字、字母"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case13(self):
        """
    厂家简称为空
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        #厂家简称
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "厂家简称必须是30字符以内的汉字、数字、字母"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case14(self):
        """
    厂家简称输入空格
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        # 厂家简称
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("           ")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "厂家简称必须是30字符以内的汉字、数字、字母"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case15(self):
        """
    厂家简称输入特殊字符
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        # 厂家简称
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("$%#&^%*(&*(&(&(")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "厂家简称必须是30字符以内的汉字、数字、字母"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case16(self):
        """
    重复输入合作厂家
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试达人")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测"+now)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "新增合作厂商信息成功"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case17(self):
        """
    厂家简称不能重复
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试达人")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测试专用")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "厂家简称不能重复"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case18(self):
        """
    联系人输入一位字符
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测"+now)
        #联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("w")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系人姓名只能输入（2-5位）汉字、字母"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case19(self):
        """
        联系人输入超过五位字符
        :return:
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("健康阿萨德阿萨德撒的")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系人姓名只能输入（2-5位）汉字、字母"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case20(self):
        """
        联系人输入空格
        验证系统提示
        :return:
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("        ")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系人姓名只能输入（2-5位）汉字、字母"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case21(self):
        """
    联系人输入特殊字符
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("#%$")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系人姓名只能输入（2-5位）汉字、字母"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case22(self):
        """
    联系电话输入空格
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        #联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("       ")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系电话只能输入（5-15）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case23(self):
        """
    联系电话输入特殊字符
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("%^$^&%^(&^")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系电话只能输入（5-15）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case24(self):
        """
    联系电话输入中文
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("安水电")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系电话只能输入（5-15）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case25(self):
        """
    联系电话输入英文
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("sdf")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系电话只能输入（5-15）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case26(self):
        """
    联系电话输入少于5位字符
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("123")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系电话只能输入（5-15）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case27(self):
        """
    联系电话输入大于15位字符
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("1529835761011111111")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系电话只能输入（5-15）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case28(self):
        """
    联系QQ输入空格
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("18000000000")
        #联系QQ输入
        driver.find_element_by_xpath("//input[@id='linkerQq']").send_keys("         ")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系QQ只能输入（5-20）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case29(self):
        """
    联系QQ输入英文
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("18000000000")
        # 联系QQ输入
        driver.find_element_by_xpath("//input[@id='linkerQq']").send_keys("sajjh")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系QQ只能输入（5-20）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case30(self):
        """
    联系QQ输入中文
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("18000000000")
        # 联系QQ输入
        driver.find_element_by_xpath("//input[@id='linkerQq']").send_keys("是的是的")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系QQ只能输入（5-20）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case31(self):
        """
    联系QQ输入特殊字符
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("18000000000")
        # 联系QQ输入
        driver.find_element_by_xpath("//input[@id='linkerQq']").send_keys("$^%&*%*&^")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系QQ只能输入（5-20）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case32(self):
        """
    联系QQ输入小于五位字符
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("18000000000")
        # 联系QQ输入
        driver.find_element_by_xpath("//input[@id='linkerQq']").send_keys("1234")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系QQ只能输入（5-20）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case33(self):
        """
    联系QQ输入超过20位字符
    验证系统提示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话输入空格
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("18000000000")
        # 联系QQ输入
        driver.find_element_by_xpath("//input[@id='linkerQq']").send_keys("14114238859724852261411423885")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "联系QQ只能输入（5-20）数字"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case34(self):
        """
    1、新增合作伙伴厂家，验证系统提示
    2、查询新增的合作厂家名，验证查询出的展示
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//nz-card/div/button").click()
        sleep(1)
        now = time.strftime("%Y%m%d%H%M%S")  #获取当前时间
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测" + now)
        # 联系人输入
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试")
        # 联系人电话
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("18000000000")
        # 联系QQ输入
        driver.find_element_by_xpath("//input[@id='linkerQq']").send_keys("1411423885")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "新增合作厂商信息成功"
        except:
            Page.get_screenshot(self)
        sleep(2)
        """
        页面查询添加的合作厂家，病对其进行验证
        """
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        # 合作伙伴全称
        full_name_partner = driver.find_element_by_xpath("//table/tbody/tr[1]/td[2]").text
        try:
            assert full_name_partner == "测试专用"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case35(self):
        """
    1、修改合作厂家名称
    2、验证修改后的合作厂家名称进行查询
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        #合作厂家查询
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td/label/span/input").click()
        #点击修改
        driver.find_element_by_xpath("//button[2]").click()
        sleep(1)
        #跳到修改页面
        driver.find_element_by_xpath("//input[@id='partnerName']").clear()
        driver.find_element_by_xpath("//input[@id='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "修改合作厂商信息成功"
        except:
            Page.get_screenshot(self)
        sleep(2)
        """
        页面查询修改的合作厂家，病对其进行验证
        """
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        # 合作伙伴全称
        full_name_partner = driver.find_element_by_xpath("//table/tbody/tr[1]/td[2]").text
        try:
            assert full_name_partner == "测试专用修改"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case36(self):
        """
    修改厂家简称，验证系统提示
    查询修改后的厂家简称，验证修改的字段
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        # 合作厂家查询
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td/label/span/input").click()
        # 点击修改
        driver.find_element_by_xpath("//button[2]").click()
        sleep(1)
        #清除之前的简称并对它进行修改
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").clear()
        now = time.strftime("%Y%m%d%H%M%S")  # 获取当前时间
        driver.find_element_by_xpath("//input[@id='partnerAbbr']").send_keys("测测测" + now)
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "修改合作厂商信息成功"
        except:
            Page.get_screenshot(self)
        sleep(2)
        """
               页面查询修改的厂家简称，并对其进行验证
               """
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        for_shot_partner = driver.find_element_by_xpath("//table/tbody/tr[1]/td[3]").text
        if "测测测" in for_shot_partner:
            print ("yes")
        else:
            Page.get_screenshot(self)
        sleep(2)
    def test_case37(self):
        """
    修改联系人姓名，验证系统提示
    查询修改后的联系人姓名，并对其进行查询验证
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        # 合作厂家查询
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td/label/span/input").click()
        # 点击修改
        driver.find_element_by_xpath("//button[2]").click()
        sleep(1)
        #清除联系人并对其修改
        driver.find_element_by_xpath("//input[@id='linkerName']").clear()
        driver.find_element_by_xpath("//input[@id='linkerName']").send_keys("测试测试")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "修改合作厂商信息成功"
        except:
            Page.get_screenshot(self)
        sleep(2)
        """
               页面查询修改的联系人姓名，并对其进行验证
               """
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        linkman = driver.find_element_by_xpath("//table/tbody/tr/td[5]").text
        try:
            assert linkman == "测试测试"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case38(self):
        """
    修改联系电话验证系统提示
    查询修改的联系电话进行展示验证
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        # 合作厂家查询
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td/label/span/input").click()
        # 点击修改
        driver.find_element_by_xpath("//button[2]").click()
        sleep(1)
        #清除联系电话并对其进行修改
        driver.find_element_by_xpath("//input[@id='linkerPhone']").clear()
        driver.find_element_by_xpath("//input[@id='linkerPhone']").send_keys("15298357611")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "修改合作厂商信息成功"
        except:
            Page.get_screenshot(self)
        sleep(2)
        """
               页面查询修改的联系人姓名，并对其进行验证
               """
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        contact_number = driver.find_element_by_xpath("//table/tbody/tr/td[6]").text
        try:
            assert contact_number == "15298357611"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case39(self):
        """
    修改联系QQ，并对其系统提示验证
    查询修改的联系QQ进行验证
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        # 合作厂家查询
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td/label/span/input").click()
        # 点击修改
        driver.find_element_by_xpath("//button[2]").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='linkerQq']").clear()
        driver.find_element_by_xpath("//input[@id='linkerQq']").send_keys("972485226")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "修改合作厂商信息成功"
        except:
            Page.get_screenshot(self)
        sleep(2)
        """
               页面查询修改的联系人QQ，并对其进行验证
               """
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        QQ = driver.find_element_by_xpath("//table/tbody/tr/td[7]").text
        try:
            assert QQ == "972485226"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case40(self):
        """
    1、修改状态
    2、验证修改的状态
    3、在将状态修改回来
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        # 合作厂家查询
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td/label/span/input").click()
        # 点击修改
        driver.find_element_by_xpath("//button[2]").click()
        sleep(1)
        #修改状态
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        verity = driver.find_element_by_xpath("//nz-message-container/div/nz-message/div/div/div/span").text
        try:
            assert verity == "修改合作厂商信息成功"
        except:
            Page.get_screenshot(self)
        sleep(2)
        """
               页面查询修改状态，并对其进行验证
               """
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        state = driver.find_element_by_xpath("//table/tbody/tr/td[8]").text
        try:
            assert state == "否"
        except:
            Page.get_screenshot(self)
        sleep(2)
        driver.find_element_by_xpath("//td/label/span/input").click()
        # 点击修改
        driver.find_element_by_xpath("//button[2]").click()
        #将状态修改为启用
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//button").click()
        sleep(2)
    def test_case41(self):
        """
    删除合作伙伴，状态改变
    验证查询修改的状态
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        # 合作厂家查询
        driver.find_element_by_xpath("//input[@name='partnerName']").send_keys("测试专用修改")
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        driver.find_element_by_xpath("//td/label/span/input").click()
        driver.find_element_by_xpath("//button[3]").click()
        sleep(1)
        state = driver.find_element_by_xpath("//table/tbody/tr/td[8]").text
        try:
            assert state == "否"
        except:
            Page.get_screenshot(self)
        sleep(2)
    def test_case42(self):
        """
    分页展示，验证每页展示多少
        """
        driver = self.driver
        po = login(self.driver, self.url)
        po.open()
        po.partner()
        po.shang()
        driver.find_element_by_xpath("//button").click()
        sleep(1)
        po.xia()
        driver.find_element_by_xpath("//div/nz-select/div/span").click()
        driver.find_element_by_xpath("//div[5]/div/div/div/ul/li[2]").click()
        sleep(1)
        po.xia()
        current_page_verity = driver.find_element_by_xpath("//nz-table/div/nz-spin/div/div[2]/div/div/div/div[2]").text
        if "显示第1到第20条记录" in current_page_verity:
            print("yes")
        else:
            Page.get_screenshot(self)
        sleep(2)

        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()









