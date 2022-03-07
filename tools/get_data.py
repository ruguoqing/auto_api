'''
初始化数据存储
反射用法
a = getattr(GetData, 'admin_tel') 获取值
setattr(GetData, 'admin_tel','123456')
'''


class GetData:

    Cookie = None
    admin_tel = '18766663333'
    normal_tel = '18566668888'
    pwd = '666666'