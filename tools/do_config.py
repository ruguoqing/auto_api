import configparser


class DoConfig:

    @staticmethod
    def get_conf_data(filepath,section,option):
        tt = configparser.ConfigParser()
        tt.read(filepath,encoding='utf-8')
        return tt.get(section, option)


if __name__ == '__main__':
    res = DoConfig.get_conf_data('/Users/meidi/PycharmProjects/AUTO_API_01/configs/run_case.config', 'MODE', 'case_id')
    print(res)
