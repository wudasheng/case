#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/20
from case.public.base import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
class login(Page):
    url = '192.168.1.102:4200/#/login'
    def __init__(self,driver,url):
        Page.__init__(self,driver,url)

    input_username = (By.CSS_SELECTOR, "input[placeholder='用户名']")
    input_password = (By.CSS_SELECTOR, "input[type='password']")
    input_button = (By.CSS_SELECTOR, "button[ng-reflect-nz-type='primary']")

    def open_url(self):
        self.open()
    def username_in(self,name):
        self.find_element(*self.input_username).clear()
        self.find_element(*self.input_username).send_keys(name)
    def password_in(self,password):
        self.find_element(*self.input_password).clear()
        self.find_element(*self.input_password).send_keys(password)
    def button_in(self):
        self.find_element(*self.input_button).click()
    #登录
    def denglu(self):
        self.find_element(*self.input_username).send_keys('wds')
        self.find_element(*self.input_password).send_keys('123456')
        self.find_element(*self.input_button).click()
    #账号类型
    def zhanghaoleixing(self):
        self.find_element(*self.input_username).send_keys('wds')
        self.find_element(*self.input_password).send_keys('123456')
        self.find_element(*self.input_button).click()
        WebDriverWait(self.driver,30).until(
            EC.element_to_be_clickable((By.XPATH, '//li[12]/div'))
        ).click()
        sleep(3)
        self.driver.find_element_by_xpath("//li[contains(text(),'账号类型')]").click()
    #分组管理
    def fenzu(self):
        self.find_element(*self.input_username).send_keys('wds')
        self.find_element(*self.input_password).send_keys('123456')
        self.find_element(*self.input_button).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//li[12]/div'))
        ).click()
        sleep(3)
        self.driver.find_element_by_xpath("//li[contains(text(),'分组管理')]").click()
    #用户管理
    def user(self):
        self.find_element(*self.input_username).send_keys('wds')
        self.find_element(*self.input_password).send_keys('123456')
        self.find_element(*self.input_button).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//li[12]/div'))
        ).click()
        sleep(3)
        self.driver.find_element_by_xpath("//li[contains(text(),'用户管理')]").click()
    #公众号菜单管理
    def caidan(self):
        self.find_element(*self.input_username).send_keys('wds')
        self.find_element(*self.input_password).send_keys('123456')
        self.find_element(*self.input_button).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//li[12]/div'))
        ).click()
        sleep(3)
        self.driver.find_element_by_xpath("//li[contains(text(),'公众号菜单')]").click()
    #角色管理
    def js(self):
        self.find_element(*self.input_username).send_keys('wds')
        self.find_element(*self.input_password).send_keys('123456')
        self.find_element(*self.input_button).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//li[12]/div'))
        ).click()
        sleep(3)
        self.driver.find_element_by_xpath("//li[contains(text(),'角色管理')]").click()
    #菜单管理
    def menu(self):
        self.find_element(*self.input_username).send_keys('wds')
        self.find_element(*self.input_password).send_keys('123456')
        self.find_element(*self.input_button).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//li[12]/div'))
        ).click()
        sleep(3)
        self.driver.find_element_by_xpath("//li[contains(text(),'菜单管理')]").click()
    def userclass(self):
        """
    用户等级管理
        """
        self.find_element(*self.input_username).send_keys('wds')
        self.find_element(*self.input_password).send_keys('123456')
        self.find_element(*self.input_button).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//li[12]/div'))
        ).click()
        sleep(3)
        self.driver.find_element_by_xpath("//li[contains(text(),'用户等级')]").click()
    def partner(self):
        """
    合作伙伴管理
        """
        self.find_element(*self.input_username).send_keys('wds')
        self.find_element(*self.input_password).send_keys('123456')
        self.find_element(*self.input_button).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//li[12]/div'))
        ).click()
        sleep(3)
        self.driver.find_element_by_xpath("//li[contains(text(),'合作伙伴')]").click()
    def customer(self):
        """
    客户管理
        """
        self.find_element(*self.input_username).send_keys('wds')
        self.find_element(*self.input_password).send_keys('123456')
        self.find_element(*self.input_button).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//li[11]/div'))
        ).click()
        sleep(3)
        self.driver.find_element_by_xpath("//li[contains(text(),'客户管理')]").click()