'''
参数格式约定采用   ${参数名}  格式
利用正则 对该种类型数据进行处理，替换成实际的参数
'''

import re
from get_data import GetData


class DoRegx:

    @staticmethod
    def get_param(s):

        while re.search('\$\{(.*?)\}',s):
            value = re.search('\$\{(.*?)\}',s).group(0)
            key = re.search('\$\{(.*?)\}',s).group(1)
            s = s.replace(value, getattr(GetData, key))
        return s


if __name__ == '__main__':
    s = '{"mobilephone":"${normal_tel}","pwd":"${pwd}"}'
    print(DoRegx.get_param(s))