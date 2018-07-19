import time
import os
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType
# from appium.webdriver.webdriver import WebDriver
from utils.config import get_desired_caps, REPORT_PATH

TYPES = {'remote': webdriver.Remote}

class UnSupportTypeError(Exception):
    pass


class WebView(object):
    # def __init__(self):
    def __init__(self, browser_type=None):
        self.url = get_desired_caps()[0]
        self.desired_caps = get_desired_caps()[1]
        self.package = get_desired_caps()[1].pop('appPackage')
        self.apk_file = get_desired_caps()[1].pop('apk_file')
        self.background_time = get_desired_caps()[1].pop('background_time')
        # self.conn_type = get_desired_caps()[1].pop('conn_type')
        # self._type = browser_type.lower()
        self._type = 'remote'
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportTypeError('Only support {}！'.join(TYPES.keys()))
        self.driver = None

    def get(self, implicitly_wait=30, noReset=None):
        if noReset == None or noReset == True:
            self.desired_caps.update({'noReset':True})
        else:
            self.desired_caps.update({'noReset': False})
        # print(self.desired_caps)
        self.driver = webdriver.Remote(self.url, self.desired_caps)
        self.driver.implicitly_wait(implicitly_wait)
        return self

    #driver.get_screenshot_as_file('c:/foo.png')
    def save_screen_shot(self, page_name=None,file_name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\%s_%s' % (page_name, day)
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (file_name, tm))
        return screenshot

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def flickUp(self, x, y1, y2):
        x = int(x * 0.8)
        # y1 = int(y1 * 0.9)
        # y2 = int(y2 * 0.9)
        self.driver.flick(x, y1, x, y2)

    def flickDown(self, x, y1, y2):
        self.driver.flick(x, y2, x, y1)

    def swipeUp(self, x, y1, y2, t=500):
        x = int(x * 0.8)
        # y1 = int(y1 * 0.8)
        # y2 = int(y2 * 0.95)
        self.driver.swipe(x, y1, x, y2, t)

    def swipeDown(self, x, y1, y2, t=5):
        x = int(x * 0.8)
        # y1 = int(y1 * 0.9)
        # y2 = int(y2 * 0.9)
        self.driver.swipe(x, y2, x, y1, t)

    def hideKeyboard(self):
        self.driver.hide_keyboard()

    def pressKeyCode(self, keycode=None):
        self.driver.press_keycode(keycode)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def is_app_installed(self):
        return self.driver.is_app_installed(self.package)

    # def install_app(self):
    #     return self.driver.install_app(APK_PATH + '\{}'.format(self.apk_file))

    def remove_app(self):
        return self.driver.remove_app(self.package)

    def launch_app(self):
        return self.driver.launch_app()

    def close_app(self):
        return self.driver.close_app()

    def background_app(self, background_time=1):
        if background_time:
            return self.driver.background_app(background_time)
        else:
            return self.driver.background_app(self.background_time)

    def set_network_connection(self, conn_type=0):
        conn = {
            '0': 'NO_CONNECTION',
            '1': 'AIRPLANE_MODE',
            '2': 'WIFI_ONLY',
            '4': 'DATA_ONLY',
            '6': 'ALL_NETWORK_ON',
        }

        if str(conn_type) in conn:
            if conn_type == 0:
                self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
            elif conn_type == 1:
                self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
            elif conn_type == 2:
                self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
            elif conn_type == 4:
                self.driver.set_network_connection(ConnectionType.DATA_ONLY)
            elif conn_type == 6:
                self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        else:
            print("None conn type")

    def test_view(self):
        pass


if __name__ == "__main__":
    b = WebView()
    b.get()