import os
from utils.file_reader import YamlReader

'''
    List all dirs
'''
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
DATA_PATH = os.path.join(BASE_PATH, 'data')
APK_PATH = os.path.join(BASE_PATH, 'apk')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
TEST_PATH = os.path.join(BASE_PATH, 'testcase\case')


class Config(object):
    def __init__(self, config=CONFIG_PATH + "\config.yml"):
        self.configs = YamlReader(config).data

    def get(self, element):
        # return self.configs[index].get(element)
        for config in self.configs:
            for i in range(len(config)):
                if element in config[i]:
                    yield config[i].get(element)

def get_desired_caps():
    cfg_info = Config()
    desired_caps = {}
    appium_url = cfg_info.get('appium_url')
    for url in appium_url:
        url = url
    content = cfg_info.get('desired_caps_info')
    for info in content:
        desired_caps.update(info)
    return(url, desired_caps)

if __name__ == "__main__":
    result = get_desired_caps()
    print(result[0].pop('appPackage'))
    print(result[1])

