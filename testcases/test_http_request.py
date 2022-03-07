# coding:utf-8
'''
用unittest框架 编写HttpRequest类的测试用例
使用ddt 数据驱动
ddt 装饰类，data装饰方法
'''

import unittest
from ddt import ddt, data
from libs.http_request import HttpRequest
from tools.do_excel import get_case, write_result
from configs.get_path import test_data_path
from tools.do_log import RunLog

test_data = get_case(test_data_path)


@ddt
class TestHttpRequest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('开始执行用例')

    @classmethod
    def tearDownClass(cls) -> None:
        print('所有用例执行完成')

    @data(*test_data)  # 脱外套
    def test_http_request(self, case):
        # print(int(case['case_id']),(case['method'], case['url'], eval(case['header']), eval(case['data'])))
        res = HttpRequest(case['method'], case['url'], eval(case['header']), eval(case['data'])).http_request()
        status = res.json()['status']
        try:
            self.assertEqual(status, case['except'])
            test_result = 'pass'
            RunLog().debug('用例执行通过')
            print(case['case_id'], case['module'],'用例执行通过')
        except AssertionError as e:
            test_result = 'failed'
            RunLog().info('******用例执行失败********')
            print(case['case_id'],case['module'],'******用例执行失败********')
            raise e
        finally:
            #  请求结果和测试结果写入Excel
            write_result(test_data_path, case['sheet'], case['case_id']+1, str(res.json()), test_result)


if __name__ == '__main__':
    unittest.main('-s')