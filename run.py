# coding:utf-8
'''
添加用例到测试套件，执行用例
'''


import unittest
from tools import HTMLTestRunner
from testcases.test_http_request import TestHttpRequest

suite = unittest.TestSuite()
loader = unittest.TestLoader()  # 用例加载
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))  # 添加用例

# 1 TextTestRunner 生成简单的TXT 报告
# with open('reports/http_test_report.txt', 'w+', encoding='utf-8') as ff:
    # runner = unittest.TextTestRunner(stream=ff, verbosity=2)
    # runner.run(suite)  # 执行用例

#  2.HTMLTestRunner 生成简单的HTML报告
with open('reports/test.html', 'wb') as ff:
    runner = HTMLTestRunner.HTMLTestRunner(ff, title='202203report', description='this is a api test')
    runner.run(suite)  # 运行用例（用例集合)


