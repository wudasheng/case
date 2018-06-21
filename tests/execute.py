#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wudasheng time:2018/6/21
import unittest, time
import HTMLTestRunner
def together():
    testunit = unittest.TestSuite()

    test_dir = "D:\\code"

    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test*.py',
                                                   top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            print(testunit)

    return testunit

if __name__=='__main__':

    testunit = unittest.TestSuite()

    testunit.addTest(together())
    now = time.strftime("%Y_%m_%d_%H_%M_%S")

    filename ='D:/code/report/'+now+'baogao.html'
    fp = open(filename, 'wb')

    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title='安佳云健康测试报告',
                                         description='用列执行情况： ')
    runner.run(testunit)
    fp.close()
    # runner=unittest.TextTestRunner()
    # runner.run(together())