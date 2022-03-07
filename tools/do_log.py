'''
longging 日志 默认是warning级别，默认输出渠道为控制台
五个级别从轻到重 debug，info，waring,error,critical
'''

import logging
from configs.get_path import log_file_path


class RunLog:

    def set_log(self, level, msg):
        # 收集日志
        my_logger = logging.getLogger('mylog')
        my_logger.setLevel(level)

        # 设置日志输出格式
        formater = logging.Formatter('%(name)s-%(asctime)s-%(filename)s-日志信息: %(message)s')

        # 日志输出渠道，到控制台，级别设置为INFO
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formater)

        # 日志输出渠道，文件，级别设置为WARNING
        fh = logging.FileHandler(log_file_path)
        fh.setLevel('DEBUG')
        fh.setFormatter(formater)

        # 将收集器和输出渠道关联
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'INFO':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        # 关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.set_log('DEBUG', msg)

    def info(self, msg):
        self.set_log('INFO', msg)

    def warning(self, msg):
        self.set_log('WARNING', msg)

    def error(self, msg):
        self.set_log('ERROR', msg)

    def critical(self, msg):
        self.set_log('CRITICAL', msg)


if __name__ == '__main__':
    RunLog().error('你已经出错了，赶紧排查问题')
    RunLog().info('注意观察事态的发展')